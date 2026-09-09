#!/usr/bin/env python3
"""Check existing mathematics, actual Mermaid diagrams and the isolated WebGL page."""
from __future__ import annotations
import functools
import json
import subprocess
import threading
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'site-review'; OUT.mkdir(exist_ok=True)
# Record the inherited dependency audit without applying unreviewed major upgrades.
audit = subprocess.run(['npm','audit','--json'],cwd=ROOT,capture_output=True,text=True,timeout=60)
try:
    audit_data = json.loads(audit.stdout)
    (OUT/'dependency-audit.json').write_text(json.dumps(audit_data,ensure_ascii=False,indent=2))
except json.JSONDecodeError:
    (OUT/'dependency-audit.json').write_text(json.dumps({'status':'unavailable','returncode':audit.returncode}))
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args): pass
server = ThreadingHTTPServer(('127.0.0.1',4174), functools.partial(QuietHandler, directory=str(ROOT/'dist')))
threading.Thread(target=server.serve_forever,daemon=True).start()
BASE = 'http://127.0.0.1:4174'
results = {}
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--enable-unsafe-swiftshader'])
        context = browser.new_context(viewport={'width':1440,'height':1000},color_scheme='light')
        page = context.new_page()
        errors = []
        page.on('pageerror',lambda err: errors.append(str(err)))
        page.goto(BASE+'/blog/dipole-to-ecg/',wait_until='domcontentloaded')
        page.wait_for_selector('mjx-container',timeout=45000)
        results['mathjax_rendered_equations'] = page.locator('mjx-container').count()
        assert results['mathjax_rendered_equations'] > 0
        assert page.locator('.toc [href^="#"]').count() > 0
        page.locator('.article-body h2').first.scroll_into_view_if_needed()
        page.screenshot(path=str(OUT/'legacy-ecg-math-desktop.png'))
        # This article contains real <pre class="mermaid"> blocks; Z-Image uses native SVG.
        page.goto(BASE+'/blog/ai-science-paradigm/',wait_until='domcontentloaded')
        page.wait_for_selector('.mermaid svg',timeout=45000)
        results['mermaid_rendered_diagrams'] = page.locator('.mermaid svg').count()
        assert results['mermaid_rendered_diagrams'] > 0
        assert page.locator('.mermaid .error-icon, .mermaid .error-text').count() == 0
        page.locator('.mermaid').first.scroll_into_view_if_needed()
        page.screenshot(path=str(OUT/'legacy-mermaid-desktop.png'))
        page.goto(BASE+'/blog/z-image/',wait_until='domcontentloaded')
        assert page.evaluate('typeof window.mermaid.initialize') == 'function'
        results['legacy_mermaid_global_available'] = True
        page.goto(BASE+'/blog/guanghua-building-3d/',wait_until='domcontentloaded')
        iframe = page.locator('iframe[src="/interactive/guanghua-building.html"]')
        assert iframe.count() == 1
        iframe.scroll_into_view_if_needed()
        canvas = page.frame_locator('iframe[src="/interactive/guanghua-building.html"]').locator('canvas').first
        canvas.wait_for(state='visible',timeout=45000)
        results['webgl_iframe_canvas'] = canvas.evaluate('(el) => ({width: el.width, height: el.height})')
        assert results['webgl_iframe_canvas']['width'] > 0
        page.wait_for_timeout(2500)
        page.screenshot(path=str(OUT/'legacy-webgl-desktop.png'))
        nojs = browser.new_context(java_script_enabled=False,viewport={'width':1440,'height':1000})
        plain = nojs.new_page(); plain.goto(BASE+'/blog/dipole-to-ecg/',wait_until='domcontentloaded')
        assert plain.locator('.article-body').bounding_box()['width'] >= 650
        results['raw_html_nojs_width'] = plain.locator('.article-body').bounding_box()['width']
        results['browser_errors'] = errors
        (OUT/'legacy-check.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
        assert not errors, errors
        results['checks'] = 'passed'
        browser.close()
    (OUT/'legacy-check.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
    print(json.dumps(results,ensure_ascii=False,indent=2))
finally:
    server.shutdown()

#!/usr/bin/env python3
"""Optional browser smoke test. Install Playwright and Chromium to run locally."""
from __future__ import annotations
import functools
import json
import threading
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'site-review'; OUT.mkdir(exist_ok=True)
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args): pass
server = ThreadingHTTPServer(('127.0.0.1', 4173), functools.partial(QuietHandler, directory=str(ROOT/'dist')))
threading.Thread(target=server.serve_forever, daemon=True).start()
BASE = 'http://127.0.0.1:4173'
ROUTES = {'home':'/', 'home-zh':'/zh/', 'archive':'/blog/', 'profile':'/about/', 'profile-zh':'/about/zh/', 'subscribe':'/subscribe/', 'article':'/blog/compressed-modernity-medical-training/'}
results = []
try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width, label in [(1440, 'desktop'), (390, 'mobile')]:
            context = browser.new_context(viewport={'width':width,'height':1000 if width > 720 else 844}, device_scale_factor=1, color_scheme='light')
            # All shell resources must work without external font/script CDNs.
            context.route('**/*', lambda route: route.continue_() if route.request.url.startswith(BASE) or route.request.url.startswith('data:') else route.abort())
            page = context.new_page(); errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            for name, route in ROUTES.items():
                response = page.goto(BASE+route, wait_until='load')
                assert response and response.status == 200, (name, response.status if response else None)
                page.wait_for_timeout(150)
                assert page.locator('h1').first.is_visible(), name
                overflow = page.evaluate('document.documentElement.scrollWidth > innerWidth + 2')
                assert not overflow, f'Horizontal overflow: {name} at {width}px'
                page.screenshot(path=str(OUT/f'{name}-{label}.png'), full_page=name in ['home','home-zh','archive','subscribe'])
                if name == 'home':
                    assert page.locator('.hero-portrait img').evaluate('(img) => img.complete && img.naturalWidth > 0')
                    assert not page.locator('script[src*="mathjax"], script[src*="mermaid"]').count()
                    page.locator('#theme-toggle').click()
                    assert page.locator('html').evaluate('(el) => el.classList.contains("dark")')
                    assert page.locator('#theme-toggle').get_attribute('aria-pressed') == 'true'
                    page.screenshot(path=str(OUT/f'home-dark-{label}.png'), full_page=True)
                    page.locator('#theme-toggle').click()
                if name == 'archive':
                    search = page.locator('#post-query'); assert search.is_visible()
                    search.fill('压缩现代性'); assert page.locator('[data-post-row]:visible').count() >= 1
                    page.locator('#post-language').select_option('zh-CN')
                    assert page.locator('[data-post-row]:visible').count() >= 1
                    assert page.locator('[data-post-row][data-language="en"]:visible').count() == 0
                    search.fill('no-match-39b0d2ea'); assert page.locator('#empty-results').is_visible()
                    search.fill(''); page.locator('#post-language').select_option('all')
                if name == 'article' and width < 720:
                    page.locator('.toc-mobile summary').click(); assert page.locator('.toc-mobile .toc-list').is_visible()
                    page.screenshot(path=str(OUT/'article-mobile-toc.png'))
                results.append({'page':route,'width':width,'overflow':overflow})
            assert not errors, errors
            context.close()
        nojs = browser.new_context(java_script_enabled=False)
        page = nojs.new_page()
        for route in ['/', '/zh/', '/blog/', '/blog/compressed-modernity-medical-training/']:
            page.goto(BASE+route, wait_until='domcontentloaded')
            assert page.locator('main').inner_text().strip(), f'Content missing without JavaScript: {route}'
        assert page.locator('.article-body').inner_text().find('医院') >= 0
        browser.close()
    (OUT/'ui-check.json').write_text(json.dumps({'checks':'passed','browsers':'Chromium','external_requests':'blocked for shell checks','pages':results,'javascript_disabled':'passed'}, ensure_ascii=False,indent=2))
finally:
    server.shutdown()

"""Optional local visual QA: pip install playwright; playwright install chromium.
Run after npm run build. Outputs screenshots outside the repository by default.
"""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from threading import Thread
import json, os
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(os.environ.get('QA_OUTPUT','/tmp/jay-blog-visual'));OUT.mkdir(parents=True,exist_ok=True)
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(ROOT/'dist')))
Thread(target=server.serve_forever,daemon=True).start();base=f'http://127.0.0.1:{server.server_port}'
results=[]
with sync_playwright() as p:
    browser=p.chromium.launch()
    for width in [390,1440]:
      for dark in [False,True]:
        context=browser.new_context(viewport={'width':width,'height':1000},color_scheme='dark' if dark else 'light',reduced_motion='reduce')
        for name,path in [('home','/'),('archive','/blog/'),('subscribe','/subscribe/'),('article','/blog/compressed-modernity-medical-training/')]:
          page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
          page.goto(base+path,wait_until='networkidle')
          page.locator('img').evaluate_all('(imgs)=>imgs.forEach(i=>i.loading="eager")')
          page.wait_for_function('Array.from(document.images).every(i=>i.complete)',timeout=30000)
          assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth+1'),(name,width,'overflow')
          if name=='article':
            assert page.locator('img[src*="/photos/"]').count()==5
            assert page.locator('img[src*="/photos/"]').evaluate_all('(imgs)=>imgs.every(i=>i.naturalWidth>0)')
            page.locator('img[src*="hospital-corridor.webp"]').scroll_into_view_if_needed()
            page.screenshot(path=str(OUT/f'{name}-photos-{width}-{dark}.png'))
            page.evaluate('scrollTo(0,0)')
          page.screenshot(path=str(OUT/f'{name}-{width}-{dark}.png'),full_page=name=='home')
          if name=='archive':
            page.locator('#article-search').fill('压缩现代性');assert page.locator('.archive-card:visible').count()==1
            page.locator('#article-search').fill('unlikely-no-result-293845');assert page.locator('#archive-empty').is_visible()
          if name=='home':
            before=page.locator('html').get_attribute('class') or '';page.locator('#theme-toggle').click();after=page.locator('html').get_attribute('class') or '';assert ('dark' in before)!=('dark' in after)
            if width==390:page.locator('.site-menu summary').click();assert page.locator('.site-menu a[href="/about/"]').is_visible()
          assert not errors,(name,errors)
          results.append({'page':name,'width':width,'dark':dark,'status':'passed'});page.close()
        context.close()
    context=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':844})
    for path in ['/','/blog/','/blog/compressed-modernity-medical-training/']:
      page=context.new_page();page.goto(base+path);assert page.locator('main a').count()>3;assert page.locator('h1').count()==1;page.close()
    browser.close()
server.shutdown();(OUT/'results.json').write_text(json.dumps(results,indent=2))
print(f'Passed {len(results)} browser configurations and 3 no-JavaScript pages')

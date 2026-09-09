"""Optional visual QA: pip install playwright Pillow; playwright install chromium.
Run after npm run build. Output lives outside the repository by default.
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
results=[];probes=[]
with sync_playwright() as p:
    browser=p.chromium.launch()
    for width in [390,1440]:
      for dark in [False,True]:
        context=browser.new_context(viewport={'width':width,'height':1000},color_scheme='dark' if dark else 'light',reduced_motion='reduce')
        context.add_init_script(f"localStorage.setItem('color-theme', '{'dark' if dark else 'light'}')")
        for name,path in [('home','/'),('archive','/blog/'),('subscribe','/subscribe/'),('article','/blog/compressed-modernity-medical-training/')]:
          page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
          page.goto(base+path,wait_until='networkidle')
          page.locator('img').evaluate_all('(imgs)=>imgs.forEach(i=>i.loading="eager")')
          page.locator('img').evaluate_all('(imgs)=>Promise.all(imgs.map(i=>i.decode().catch(()=>{})))')
          assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth+1'),(name,width,'overflow')
          if name=='article':
            photos=page.locator('img[src*="/photos/"]');assert photos.count()==5
            assert photos.evaluate_all('(imgs)=>imgs.every(i=>i.naturalWidth>0)')
            photo=page.locator('img[src*="hospital-corridor.webp"]')
            photo.scroll_into_view_if_needed();photo.evaluate('(i)=>i.decode()')
            page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
            page.wait_for_timeout(300)
            probes.append({'width':width,'dark':dark,'computed':photo.evaluate('(i)=>({src:i.currentSrc,width:i.naturalWidth,opacity:getComputedStyle(i).opacity,visibility:getComputedStyle(i).visibility,display:getComputedStyle(i).display,filter:getComputedStyle(i).filter,clip:getComputedStyle(i).clipPath,ancestors:[i.parentElement,i.parentElement.parentElement].map(p=>({tag:p.tagName,opacity:getComputedStyle(p).opacity,filter:getComputedStyle(p).filter,visibility:getComputedStyle(p).visibility}))})')})
            photo.screenshot(path=str(OUT/f'photo-only-{width}-{dark}.png'))
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
server.shutdown()
(OUT/'results.json').write_text(json.dumps(results,indent=2));(OUT/'photo-rendering.json').write_text(json.dumps(probes,indent=2))
from PIL import Image,ImageStat
for shot in OUT.glob('photo-only-*.png'):
    im=Image.open(shot).convert('RGB');cx,cy=im.width//2,im.height//2
    crop=im.crop((cx-im.width//4,cy-im.height//4,cx+im.width//4,cy+im.height//4))
    assert max(ImageStat.Stat(crop).stddev)>25,(shot,'Photo painted as a blank box')
print(f'Passed {len(results)} browser configurations, 3 no-JavaScript pages and painted-image checks')

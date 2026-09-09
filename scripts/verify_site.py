"""Dependency-free checks against the actual Astro build output."""
from pathlib import Path
from html.parser import HTMLParser
import json, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];DIST=ROOT/'dist'
class Page(HTMLParser):
    def __init__(self,text):super().__init__();self.tags=[];self.feed(text)
    def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
    def attrs(self,tag):return [a for t,a in self.tags if t==tag]

def check(path):
    f=DIST/path;assert f.is_file(),f'Missing {path}'
    text=f.read_text();page=Page(text)
    canonical=[x for x in page.attrs('link') if x.get('rel')=='canonical'];assert len(canonical)==1,path
    assert canonical[0]['href'].startswith('https://jiahaoblog.com/'),path
    assert len([x for x in page.attrs('link') if x.get('type')=='application/rss+xml'])==3,path
    assert len(page.attrs('h1'))==1,(path,'h1')
    return text,page

for f in ['index.html','blog/index.html','subscribe/index.html','about/index.html','about/zh/index.html']:
    text,page=check(f)
    assert not any('mathjax' in s.get('src','').lower() or 'mermaid.min.js' in s.get('src','') for s in page.attrs('script')),f

sets={}
for f in ['rss.xml','rss/zh.xml','rss/en.xml']:
    root=ET.parse(DIST/f).getroot();assert root.tag=='rss'
    channel=root.find('channel');items=channel.findall('item');assert items
    guids=[i.findtext('guid') for i in items];assert len(guids)==len(set(guids))
    assert all(g.startswith('https://jiahaoblog.com/blog/') and 'hello-world' not in g for g in guids)
    sets[f]=set(guids)
assert sets['rss/zh.xml'].isdisjoint(sets['rss/en.xml'])
assert sets['rss/zh.xml']|sets['rss/en.xml']==sets['rss.xml']
assert 'Sitemap: https://jiahaoblog.com/sitemap-index.xml' in (DIST/'robots.txt').read_text()
sitemap=''.join(p.read_text() for p in DIST.glob('sitemap*.xml'))
assert 'hello-world' not in sitemap
for suffix,language in [('', 'zh-CN'),('-en','en')]:
    text,page=check(f'blog/compressed-modernity-medical-training{suffix}/index.html')
    assert page.attrs('html')[0]['lang']==language
    photos=[a for a in page.attrs('img') if '/photos/' in a.get('src','')]
    assert len(photos)==5,(suffix,len(photos))
    for photo in photos:
        assert all(photo.get(k) for k in ['alt','width','height','srcset','sizes'])
        assert photo.get('loading')=='lazy'
        assert (DIST/photo['src'].lstrip('/')).is_file()
    assert len([a for a in page.attrs('link') if 'hreflang' in a])==2
    assert 'BlogPosting' in text and 'dateModified' in text
    ids=[a.get('id') for _,a in page.tags if a.get('id')]
    assert len(ids)==len(set(ids)),('duplicate ids',suffix)
    for i in range(1,29):assert f'ref-{i}' in ids
_,sample=check('blog/hello-world/index.html')
assert any(m.get('name')=='robots' and 'noindex' in m.get('content','') for m in sample.attrs('meta'))
assert not (ROOT/'.github/workflows/wechat-draft.yml').exists()
assert not (ROOT/'scripts/wechat/publish.py').exists()
print(json.dumps({'status':'passed','rss_items':{k:len(v) for k,v in sets.items()},'photo_count_per_article':5,'checked':'canonical, feeds, language pairs, sources, sample exclusion, conditional runtimes'},indent=2))

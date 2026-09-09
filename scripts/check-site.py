#!/usr/bin/env python3
"""Build-output checks; Python standard library only. Run after `npm run build`."""
from __future__ import annotations
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
from xml.etree import ElementTree as ET
from email.utils import parsedate_to_datetime

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
ORIGIN = 'https://jiahaoblog.com'
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

class Page(HTMLParser):
    def __init__(self, source: str):
        super().__init__(convert_charrefs=True)
        self.lang = ''; self.head = False; self.first_head = True
        self.links = []; self.meta = {}; self.alternates = []; self.canonicals = []
        self.scripts = []; self.jsonld = []; self.images = []; self.post = False
        self.ids = set(); self.in_json = False; self.buffer = ''; self.main = False
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html' and not self.lang: self.lang = a.get('lang', '')
        if tag == 'head' and self.first_head: self.head = True
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'main' and a.get('id') == 'main-content': self.main = True
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag == 'img': self.images.append(a)
        if tag == 'article' and 'data-post' in a: self.post = True
        if tag == 'script':
            if a.get('src'): self.scripts.append(a['src'])
            if self.head and a.get('type') == 'application/ld+json': self.in_json = True; self.buffer = ''
        if self.head and tag == 'meta': self.meta[a.get('name') or a.get('property')] = a.get('content', '')
        if self.head and tag == 'link':
            if a.get('rel') == 'canonical': self.canonicals.append(a.get('href'))
            if a.get('rel') == 'alternate': self.alternates.append(a)
    def handle_endtag(self, tag):
        if tag == 'head': self.head = False; self.first_head = False
        if tag == 'script' and self.in_json:
            self.jsonld.append(json.loads(self.buffer)); self.in_json = False
    def handle_data(self, data):
        if self.in_json: self.buffer += data

def local_path(url: str) -> Path:
    path = unquote(urlparse(url).path).lstrip('/')
    target = DIST / path
    if not target.suffix: target /= 'index.html'
    return target

def require(condition: bool, message: str) -> None:
    if not condition: raise AssertionError(message)

def main() -> None:
    require(DIST.is_dir(), 'Build output missing: run npm run build first')
    pages = {}
    for path in DIST.rglob('*.html'):
        source = path.read_text(encoding='utf-8')
        if 'class="site-header"' not in source: continue  # Standalone demos retain their own documents.
        page = Page(source)
        require(page.lang in ('en', 'zh-CN'), f'Incorrect page language: {path}')
        require(page.main, f'Missing main landmark: {path}')
        require(len(page.canonicals) == 1, f'Canonical count: {path}')
        canonical = page.canonicals[0]
        require(canonical.startswith(ORIGIN + '/'), f'Canonical origin: {path}')
        require(not urlparse(canonical).query, f'Canonical contains query: {path}')
        require(page.meta.get('description'), f'Missing description: {path}')
        require(page.meta.get('og:url') == canonical, f'OG URL differs from canonical: {path}')
        require(len([a for a in page.alternates if a.get('type') == 'application/rss+xml']) == 3, f'RSS autodiscovery missing: {path}')
        require(page.jsonld, f'Missing structured data: {path}')
        if path.name != '404.html': require('noindex' not in page.meta.get('robots', ''), f'Unexpected noindex: {path}')
        if page.post:
            require(page.meta.get('og:type') == 'article', f'Incorrect article OG type: {path}')
            graph = page.jsonld[0].get('@graph', [])
            require(any(n.get('@type') == 'BlogPosting' for n in graph), f'Missing BlogPosting schema: {path}')
        pages[canonical] = page
    require(len(pages) >= 8, 'Unexpectedly few generated pages')
    for canonical, page in pages.items():
        for alt in page.alternates:
            if alt.get('hreflang') and alt['hreflang'] != 'x-default':
                target = pages.get(alt['href'])
                require(target is not None, f'Missing translated page: {alt}')
                require(target.lang == alt['hreflang'], f'hreflang mismatch: {alt}')
                require(any(a.get('href') == canonical for a in target.alternates), f'Non-reciprocal language link: {canonical}')
    feed_counts = {}; feed_urls = {}
    for name, language in [('rss.xml', None), ('rss/zh.xml', 'zh-CN'), ('rss/en.xml', 'en')]:
        doc = ET.parse(DIST / name).getroot(); require(doc.tag == 'rss', f'Not RSS 2.0: {name}')
        channel = doc.find('channel'); require(channel is not None, f'Missing channel: {name}')
        require(channel.find('{http://www.w3.org/2005/Atom}link').get('href') == f'{ORIGIN}/{name}', f'Wrong feed self link: {name}')
        items = channel.findall('item'); urls = []; dates = []
        for item in items:
            url = item.findtext('link'); urls.append(url)
            require(item.findtext('guid') == url, f'Unstable feed GUID: {name}')
            require(url in pages and pages[url].post, f'RSS item not a built article: {url}')
            require(item.findtext('title') and item.findtext('description'), f'RSS metadata missing: {url}')
            dates.append(parsedate_to_datetime(item.findtext('pubDate')))
            if language: require(pages[url].lang == language, f'Wrong language in feed: {url}')
        require(len(set(urls)) == len(urls), f'Duplicate RSS items: {name}')
        require(dates == sorted(dates, reverse=True), f'RSS dates out of order: {name}')
        feed_counts[name] = len(items); feed_urls[name] = set(urls)
    require(feed_counts['rss.xml'] > 0, 'All-article feed is empty')
    index = ET.parse(DIST / 'sitemap-index.xml').getroot(); sitemap_urls = set()
    for location in index.findall('.//s:loc', NS):
        child = ET.parse(local_path(location.text)).getroot()
        sitemap_urls.update(loc.text for loc in child.findall('.//s:url/s:loc', NS))
    for canonical, page in pages.items():
        if 'noindex' not in page.meta.get('robots', ''):
            require(canonical in sitemap_urls, f'Page absent from sitemap: {canonical}')
    require(not any('/404' in url for url in sitemap_urls), '404 must not be in sitemap')
    require(f'Sitemap: {ORIGIN}/sitemap-index.xml' in (DIST/'robots.txt').read_text(), 'Robots sitemap pointer missing')
    for route in ['/', '/zh/', '/blog/', '/about/', '/about/zh/', '/subscribe/']:
        page = pages[ORIGIN + route]
        require(not any('mathjax' in src.lower() or 'mermaid' in src.lower() for src in page.scripts), f'Heavy script on non-technical page: {route}')
        for link in page.links:
            parsed = urlparse(link)
            if link.startswith('/') or parsed.netloc == 'jiahaoblog.com':
                require(local_path(link).is_file(), f'Broken internal page/asset: {route} -> {link}')
    for path in ['.github/workflows/wechat-draft.yml', 'scripts/wechat/publish.py', 'scripts/wechat/requirements.txt']:
        require(not (ROOT/path).exists(), f'Obsolete uploader remains: {path}')
    archive = pages[ORIGIN + '/blog/']
    for canonical, page in pages.items():
        if page.post: require(urlparse(canonical).path in archive.links, f'Article absent from server-rendered archive: {canonical}')
    report = {'pages_checked':len(pages), 'article_pages':sum(p.post for p in pages.values()), 'rss_items':feed_counts, 'sitemap_urls':len(sitemap_urls), 'checks':'passed'}
    out = ROOT/'site-review'; out.mkdir(exist_ok=True)
    (out/'site-check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__': main()

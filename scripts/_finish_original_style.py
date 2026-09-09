"""One-time, branch-only migration. Removed before merging the verified result."""
from pathlib import Path
from io import BytesIO
import hashlib, html, json, re, time
import requests
from PIL import Image, ImageOps

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/images/compressed-modernity/photos'
OUT.mkdir(parents=True,exist_ok=True)
COMMONS='https://commons.wikimedia.org/wiki/File:'
items=[
 {'id':'hospital-corridor','file':'Hospital_corridor_2.jpg','hash':'2/2e','author':'tanakawho','license':'CC BY 2.0','licenseUrl':'https://creativecommons.org/licenses/by/2.0/','zh':'医院走廊，2007年。环境资料图，非本文受访者所在病区。','en':'Hospital corridor, 2007. An illustrative setting, not the ward of an interviewee in this article.'},
 {'id':'hopkins-interns-1889','file':'First_group_of_interns_at_Johns_Hopkins_Hospital,_April_1889.jpg','hash':'9/92','author':'Unknown photographer / U.S. National Library of Medicine','license':'Public domain','licenseUrl':'https://creativecommons.org/publicdomain/mark/1.0/','zh':'1889年4月，约翰斯·霍普金斯医院第一批实习医师合影。美国国家医学图书馆藏，摄影者未详。','en':'The first group of interns at Johns Hopkins Hospital, April 1889. U.S. National Library of Medicine; photographer unknown.'},
 {'id':'shanghai-housing','file':'Wanbang_Garden_Pudong_Shanghai_2007.jpg','hash':'9/91','author':'Ssarkarhyd','license':'CC BY-SA 3.0','licenseUrl':'https://creativecommons.org/licenses/by-sa/3.0/','zh':'上海浦东万邦都市花园住宅楼。住房改革段落的城市环境资料图。','en':'Apartment buildings at Wanbang Garden in Pudong, Shanghai. Urban context for the discussion of housing reform.'},
 {'id':'osler-bedside','file':'William_Osler_at_bedside_of_patients._Wellcome_L0004900.jpg','hash':'7/76','author':'Wellcome Library, London / Wellcome Collection','license':'CC BY 4.0','licenseUrl':'https://creativecommons.org/licenses/by/4.0/','zh':'床旁诊查史料图。Wellcome藏品L0004900；具体拍摄年份未标。','en':'Historical bedside photographs, Wellcome collection L0004900. Exact photographic dates are not specified.'},
 {'id':'pumch-old-building','file':'Old_building_of_Peking_Union_Medical_College_Hospital_(20180821142741).jpg','hash':'3/30','author':'N509FZ','license':'CC BY-SA 4.0','licenseUrl':'https://creativecommons.org/licenses/by-sa/4.0/','zh':'北京协和医院老楼，2018年8月21日。建筑资料照片。','en':'The old PUMCH building, photographed on 21 August 2018. Architectural reference photograph.'},
]
session=requests.Session()
session.headers['User-Agent']='JayBlogEditorial/1.0 (https://jiahaoblog.com/about/; attributed educational photo use)'
for item in items:
    name=requests.utils.quote(item['file'],safe='')
    original=f"https://upload.wikimedia.org/wikipedia/commons/{item['hash']}/{name}"
    thumb=f"https://upload.wikimedia.org/wikipedia/commons/thumb/{item['hash']}/{name}/1280px-{name}"
    urls=[original] if item['id'] in ['hospital-corridor','shanghai-housing'] else [thumb,original]
    error=None
    for url in urls:
        for attempt in range(3):
            try:
                response=session.get(url,timeout=(15,90))
                response.raise_for_status()
                if len(response.content)>40_000_000: raise ValueError('Image exceeds size limit')
                image=ImageOps.exif_transpose(Image.open(BytesIO(response.content))).convert('RGB')
                image.load()
                raw_digest=hashlib.sha256(response.content).hexdigest()
                break
            except Exception as exc:
                error=exc
                time.sleep(2*(attempt+1))
        else: continue
        break
    else: raise RuntimeError(f"Unable to retrieve {item['file']}: {error}")
    image.thumbnail((1280,1800),Image.Resampling.LANCZOS)
    dest=OUT/f"{item['id']}.webp"
    image.save(dest,'WEBP',quality=84,method=6)
    item.update(width=image.width,height=image.height,source=COMMONS+name,original=original,sourceSha256=raw_digest,bytes=dest.stat().st_size)
    small=image.copy();small.thumbnail((640,1000),Image.Resampling.LANCZOS)
    small.save(OUT/f"{item['id']}-640.webp",'WEBP',quality=82,method=6)
    print(item['id'],item['width'],item['height'],item['bytes'])

by_id={item['id']:item for item in items}
def figure(key,language):
    a=by_id[key];e=html.escape
    base='/images/compressed-modernity/photos/'+key
    change='按比例缩放并转为WebP，未裁切。' if language=='zh' else 'Resized proportionally and converted to WebP; not cropped.'
    return f'''<figure class="cm-figure cm-photo"><a href="{e(a['source'],quote=True)}" target="_blank" rel="noopener noreferrer"><img src="{base}.webp" srcset="{base}-640.webp 640w, {base}.webp {a['width']}w" sizes="(max-width: 700px) 100vw, 850px" width="{a['width']}" height="{a['height']}" loading="lazy" decoding="async" alt="{e(a[language],quote=True)}" /></a><figcaption>{e(a[language])} {e(a['author'])} / Wikimedia Commons · <a href="{a['licenseUrl']}">{a['license']}</a>。{change} <a href="{e(a['source'],quote=True)}">{'来源' if language=='zh' else 'Source'}</a></figcaption></figure>'''

for language,suffix in [('zh',''),('en','-en')]:
    path=ROOT/f'src/content/blog/compressed-modernity-medical-training{suffix}.md'
    text=path.read_text()
    before=text
    header,body=text.split('---',2)[1:]
    header=re.sub(r'(?m)^wechat:\n(?:[ \t].*(?:\n|$))*','',header)
    for old,key in [('William_Osler_at_bedside','osler-bedside'),('Old_building_of_Peking','pumch-old-building')]:
        found=[m for m in re.finditer(r'<figure\b[^>]*>[\s\S]*?</figure>',body) if old in m.group()]
        assert len(found)==1,(path,old,len(found))
        body=body.replace(found[0].group(),figure(key,language),1)
    heading='## 消失的后勤与被借用的传统' if language=='zh' else '## The support that disappeared, and the tradition that survived'
    assert body.count(heading)==1
    body=body.replace(heading,figure('hospital-corridor',language)+'\n\n'+heading,1)
    needle='这种教学革新有着充分的专业理由' if language=='zh' else 'The educational rationale was substantial.'
    assert body.count(needle)==1
    body=body.replace(needle,figure('hopkins-interns-1889',language)+'\n\n'+needle,1)
    needle='与此同时，培养制度的调整又会改写个人已经排好的人生计划。' if language=='zh' else 'Changes to training could meanwhile overturn plans already made.'
    assert body.count(needle)==1
    body=body.replace(needle,figure('shanghai-housing',language)+'\n\n'+needle,1)
    # The user's prose must survive byte-for-byte after removing figure markup and whitespace.
    strip=lambda s:re.sub(r'\s+','',re.sub(r'<figure\b[^>]*>[\s\S]*?</figure>','',s))
    assert strip(before.split('---',2)[2])==strip(body),'Unexpected prose change'
    path.write_text('---'+header+'---'+body)

profile=ROOT/'public/images/profile';profile.mkdir(parents=True,exist_ok=True)
avatar=ImageOps.exif_transpose(Image.open(ROOT/'public/avatar.jpg')).convert('RGB')
for size in (192,384):
    picture=ImageOps.fit(avatar,(size,size),Image.Resampling.LANCZOS)
    picture.save(profile/f'avatar-{size}.webp','WEBP',quality=86,method=6)

path=ROOT/'src/pages/index.astro';text=path.read_text()
text=text.replace('import { getCollection } from "astro:content";','import { getCollection } from "astro:content";\nimport { publicPosts, distinctPosts } from "../lib/site.mjs";')
text,n=re.subn(r'const posts = \(await getCollection\("blog"\)\)\.sort\([\s\S]*?\);','const posts = distinctPosts(publicPosts(await getCollection("blog")));',text,count=1);assert n==1
text=text.replace('const otherPosts = posts.slice(1);','const otherPosts = posts.slice(1, 7);')
text=text.replace('src="/avatar.jpg"','src="/images/profile/avatar-192.webp" width="192" height="192" loading="lazy" decoding="async"')
needle='>Latest Paper ↗</a>';assert needle in text
text=text.replace(needle,needle+'\n        <a href="/subscribe/" class="rounded-lg border border-indigo-200 bg-white/80 px-5 py-3 text-sm font-semibold text-indigo-700 transition hover:bg-indigo-50 dark:border-indigo-800 dark:bg-gray-900/70 dark:text-indigo-300">RSS · 订阅更新</a>',1)
assert text.count('</aside>')==1
text=text.replace('</aside>','''<section class="site-subscribe"><h3 class="text-lg font-bold">Follow the writing</h3><p class="mt-3 text-sm leading-relaxed text-gray-600 dark:text-gray-300">Research notes and essays, delivered to your RSS reader. No account required.</p><a href="/rss/zh.xml">中文 RSS</a><a href="/rss/en.xml">English RSS</a><a href="/subscribe/">All subscriptions →</a></section>\n      </aside>''',1)
path.write_text(text)

# Correct old language metadata at its source, not only in templates.
for path in (ROOT/'src/content/blog').glob('*.md'):
    text=path.read_text();parts=text.split('---',2)
    if len(parts)!=3: continue
    header=parts[1]
    title=re.search(r'(?m)^title:\s*(.+)$',header)
    if title and re.search('[\u3400-\u9fff]',title.group(1)) and not path.stem.endswith('-en'):
        if re.search(r'(?m)^lang:',header):header=re.sub(r'(?m)^lang:.*$','lang: zh-CN',header)
        else:header+='lang: zh-CN\n'
    header=re.sub(r'(?m)^wechat:\n(?:[ \t].*(?:\n|$))*','',header)
    parts[1]=header;path.write_text('---'.join(parts))

manifest={'note':'Publicly sourced photographs, resized proportionally to WebP without cropping. Credits do not imply endorsement.','photos':items}
(ROOT/'docs/medical-training-photo-sources.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')

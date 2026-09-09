export const SITE = 'https://jiahaoblog.com';
export const AUTHOR = { '@type': 'Person', '@id': `${SITE}/#author`, name: 'Jia-Hao Ji', alternateName: 'Jay', url: `${SITE}/about/`, sameAs: ['https://github.com/Biogod2020'] };
export const postPath = (post) => `/blog/${post.slug}/`;
export function languageOf(post) {
  if (post.slug.endsWith('-en')) return 'en';
  if (/[\u3400-\u9fff]/u.test(post.data.title)) return 'zh-CN';
  return post.data.lang || 'en';
}
export function publicPosts(posts) {
  return posts.filter(p => p.slug !== 'hello-world' && !p.data.draft).sort((a,b) => b.data.pubDate.valueOf()-a.data.pubDate.valueOf() || a.slug.localeCompare(b.slug));
}
export function distinctPosts(posts) {
  const slugs = new Set(posts.map(p => p.slug));
  return posts.filter(p => !(p.slug.endsWith('-en') && slugs.has(p.slug.slice(0,-3))));
}
export function translations(post, posts) {
  const base = post.slug.replace(/-en$/, '');
  const pair = posts.filter(p => p.slug === base || p.slug === `${base}-en`);
  if (pair.length !== 2 || new Set(pair.map(languageOf)).size !== 2) return [];
  return pair.map(p => ({ lang: languageOf(p), href: postPath(p) }));
}
export function readingMinutes(body) {
  const text = body.replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi,'').replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi,'').replace(/<[^>]*>/g,'').replace(/https?:\/\/\S+/g,'');
  const cjk = (text.match(/[\u3400-\u9fff]/gu)||[]).length;
  const words = (text.replace(/[\u3400-\u9fff]/gu,' ').match(/\b[\w'-]+\b/g)||[]).length;
  return Math.max(1,Math.ceil(cjk/350 + words/220));
}
export const xml = value => String(value).replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g,'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&apos;');
export function feed(posts, language) {
  const chosen = publicPosts(posts).filter(p => !language || languageOf(p) === (language === 'zh' ? 'zh-CN' : 'en'));
  const path = language ? `/rss/${language}.xml` : '/rss.xml';
  const title = language === 'zh' ? 'Jay’s Blog · 中文' : language === 'en' ? 'Jay’s Blog · English' : 'Jay’s Blog';
  const dates = chosen.flatMap(p => [p.data.pubDate,p.data.updatedDate].filter(Boolean).map(d=>new Date(d).valueOf()));
  const modified = dates.length ? `<lastBuildDate>${new Date(Math.max(...dates)).toUTCString()}</lastBuildDate>` : '';
  return `<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/"><channel><title>${xml(title)}</title><link>${SITE}/</link><description>Medicine, artificial intelligence, research and society · 医学、人工智能与社会观察</description>${language ? `<language>${language === 'zh' ? 'zh-CN':'en'}</language>`:''}<atom:link href="${SITE}${path}" rel="self" type="application/rss+xml"/>${modified}${chosen.map(p => `<item><title>${xml(p.data.title)}</title><link>${SITE}${xml(postPath(p))}</link><guid isPermaLink="true">${SITE}${xml(postPath(p))}</guid><description>${xml(p.data.description)}</description><pubDate>${p.data.pubDate.toUTCString()}</pubDate><dc:creator>Jia-Hao Ji</dc:creator><dc:language>${languageOf(p)}</dc:language></item>`).join('')}</channel></rss>`;
}

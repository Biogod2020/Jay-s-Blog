import { SITE, absoluteURL, type Language } from './site';
import { getPosts, postLanguage, postPath } from './posts';
// RSS 2.0, with stable canonical GUIDs. Deliberately summary-only: interactive posts stay on the site.
export function escapeXML(value: string): string {
  return value.replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&apos;');
}
export async function buildFeed(language?: Language): Promise<Response> {
  const all = await getPosts();
  const posts = all.filter(post => !language || postLanguage(post) === language).slice(0, 50);
  const feedPath = language === 'en' ? '/rss/en.xml' : language === 'zh-CN' ? '/rss/zh.xml' : '/rss.xml';
  const suffix = language === 'en' ? 'English' : language === 'zh-CN' ? '中文' : 'All writing';
  const modified = posts.length ? new Date(Math.max(...posts.map(post => (post.data.updatedDate ?? post.data.pubDate).valueOf()))).toUTCString() : undefined;
  const items = posts.map(post => {
    const url = escapeXML(absoluteURL(postPath(post)));
    return `<item><title>${escapeXML(post.data.title)}</title><link>${url}</link><guid isPermaLink="true">${url}</guid><pubDate>${post.data.pubDate.toUTCString()}</pubDate><dc:creator>${escapeXML(SITE.author)}</dc:creator><description>${escapeXML(post.data.description)}</description>${post.data.tags.map(tag => `<category>${escapeXML(tag)}</category>`).join('')}</item>`;
  }).join('\n');
  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/"><channel><title>Jay’s Blog — ${suffix}</title><link>${SITE.url}/</link><description>${escapeXML(language === 'zh-CN' ? SITE.descriptionZh : SITE.description)}</description><atom:link href="${absoluteURL(feedPath)}" rel="self" type="application/rss+xml"/>${language ? `<language>${language === 'zh-CN' ? 'zh-cn' : 'en'}</language>` : ''}${modified ? `<lastBuildDate>${modified}</lastBuildDate>` : ''}${items}</channel></rss>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' } });
}

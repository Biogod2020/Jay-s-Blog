import { getCollection, type CollectionEntry } from 'astro:content';
import { SITE, type Alternate, type Language } from './site';
export type Post = CollectionEntry<'blog'>;

export async function getPosts(): Promise<Post[]> {
  const today = new Date().toISOString().slice(0, 10);
  return (await getCollection('blog'))
    .filter(post => !post.data.draft && post.data.pubDate.toISOString().slice(0, 10) <= today)
    .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf() || a.slug.localeCompare(b.slug));
}
export function postPath(post: Post): string {
  return new URL(`/blog/${post.slug}/`, SITE.url).pathname;
}
export function postLanguage(post: Post): Language {
  return post.data.lang ?? (/\p{Script=Han}/u.test(post.data.title) ? 'zh-CN' : 'en');
}
export function readingMinutes(post: Post): number {
  const text = post.body.replace(/<(script|style)\b[^>]*>[\s\S]*?<\/\1>/gi, '')
    .replace(/data:[^\s"')]+/g, '').replace(/<[^>]+>/g, '').replace(/https?:\/\/\S+/g, '');
  const chinese = (text.match(/\p{Script=Han}/gu) ?? []).length;
  const words = (text.match(/[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*/g) ?? []).length;
  return Math.max(1, Math.ceil(chinese / 400 + words / 220));
}
export function postAlternates(post: Post, all: Post[]): Alternate[] {
  const counterpart = post.slug.endsWith('-en') ? post.slug.slice(0, -3) : `${post.slug}-en`;
  const matches = all.filter(other => other.slug === post.slug ||
    (post.data.translationKey ? other.data.translationKey === post.data.translationKey : other.slug === counterpart));
  const seen = new Set<string>();
  return matches.flatMap(other => {
    const lang = postLanguage(other);
    if (seen.has(lang)) return [];
    seen.add(lang);
    return [{ lang, href: postPath(other) }];
  });
}
export function homepagePosts(all: Post[], lang: Language): Post[] {
  return all.filter(post => {
    const alternatives = postAlternates(post, all);
    return alternatives.length < 2 || postLanguage(post) === lang || !alternatives.some(a => a.lang === lang);
  }).slice(0, 4);
}
export function postFeatures(post: Post) {
  const body = post.body;
  return {
    math: post.data.math ?? /\$\$|\\\(|\\\[|\$[^\s$][^$\n]*\$/.test(body),
    mermaid: post.data.mermaid ?? /```mermaid|class=["'][^"']*mermaid/.test(body),
    icons: post.data.icons ?? /\bfa[srb]?\s+fa-|\bfa-solid\b|\bfa-brands\b/.test(body),
  };
}

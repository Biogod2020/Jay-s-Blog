import { getCollection } from 'astro:content';
import { feed } from '../lib/site.mjs';
export const prerender = true;
export async function GET() {
  return new Response(feed(await getCollection('blog')), { headers: { 'Content-Type':'application/rss+xml; charset=utf-8' } });
}

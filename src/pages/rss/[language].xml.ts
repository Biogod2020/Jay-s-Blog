import { getCollection } from 'astro:content';
import type { APIRoute } from 'astro';
import { feed } from '../../lib/site.mjs';
export const prerender = true;
export function getStaticPaths() { return ['zh','en'].map(language => ({params:{language}})); }
export const GET: APIRoute = async ({params}) => new Response(feed(await getCollection('blog'),params.language), {headers:{'Content-Type':'application/rss+xml; charset=utf-8'}});

import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import lazyMarkdownImages from './src/lib/remark-images.mjs';

export default defineConfig({
  site: 'https://jiahaoblog.com',
  base: '/',
  trailingSlash: 'always',
  output: 'static',
  compressHTML: true,
  integrations: [tailwind(), sitemap({
    filter: page => !/\/404\/?$/.test(new URL(page).pathname),
  })],
  markdown: { remarkPlugins: [lazyMarkdownImages] },
});

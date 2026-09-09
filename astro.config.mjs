import {defineConfig} from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
export default defineConfig({
  site:'https://jiahaoblog.com',base:'/',
  integrations:[tailwind(),sitemap({filter:(page)=>!['/blog/hello-world/','/404/','/zh/'].includes(new URL(page).pathname)})],
});

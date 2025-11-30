import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  site: 'https://biogod2020.github.io',
  base: '/Jay-s-Blog',
  integrations: [tailwind(), sitemap()],
  markdown: {
    smartypants: false,
  },
});

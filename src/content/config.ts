import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    lang: z.enum(['en', 'zh-CN']).optional(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    translationKey: z.string().optional(),
    math: z.boolean().optional(),
    mermaid: z.boolean().optional(),
    icons: z.boolean().optional(),
    externalScripts: z.array(z.string()).optional(),
    localScripts: z.array(z.string()).optional(),
    localStyles: z.array(z.string()).optional(),
  }),
});

export const collections = { blog };

import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
	type: 'content',
	// Type-check frontmatter using a schema
	schema: z.object({
		title: z.string(),
		description: z.string(),
		lang: z.enum(['en', 'zh-CN']).optional(),
		// Transform string to Date object
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		heroImage: z.string().optional(),
		externalScripts: z.array(z.string()).optional(),
		localScripts: z.array(z.string()).optional(),
		localStyles: z.array(z.string()).optional(),
		wechat: z.object({
			draft: z.boolean().optional(),
			title: z.string().optional(),
			author: z.string().optional(),
			digest: z.string().optional(),
			cover: z.string().optional(),
			sourceUrl: z.string().url().optional(),
			openComment: z.boolean().optional(),
			onlyFansCanComment: z.boolean().optional(),
		}).optional(),
	}),
});

export const collections = { blog };

# GEMINI.md - Jay's Blog ("Thinking in Algorithms")

## Project Overview
This is a personal blog and digital garden built with **Astro 4.x**, **Tailwind CSS**, and **TypeScript**. It serves as a platform for documenting research in Artificial Intelligence, Data Visualization, and Web Development. The project emphasizes high-quality technical content and sophisticated visualizations.

## Tech Stack
- **Framework:** [Astro](https://astro.build/) (v4.0.0+)
- **Styling:** [Tailwind CSS](https://tailwindcss.com/) with `@tailwindcss/typography`
- **Language:** [TypeScript](https://www.typescriptlang.org/)
- **Integrations:** `@astrojs/sitemap`, `@astrojs/tailwind`
- **Content:** Markdown-based using Astro Content Collections

## Key Directory Structure
- `/src/content/blog/`: Contains the Markdown files for blog posts.
- `/src/pages/`: Astro routing and page templates (e.g., `index.astro`, `blog/[...slug].astro`).
- `/src/components/`: Reusable Astro components.
- `/src/layouts/`: Layout components (e.g., `Layout.astro`).
- `/public/`: Static assets including images, icons, and specialized CSS for specific posts.
- `/raw/`: Source HTML files and raw assets used for importing content.
- `/wechat_version/`: WeChat-specific versions of blog articles.
- `/.memory/`: ASSA (Autonomous Self-Sovereign Agent) project-specific memory and patterns.
- `/scripts/`: Project-specific automation scripts.

## Content Workflow & Automation
The project includes several Python scripts for processing and importing content:
- `html_to_blog.py`: Converts raw HTML documents to Astro-compatible Markdown.
- `fix_symbols.py` & `fix_bold_tags.py`: Utility scripts for cleaning up content formatting.
- `src/content/config.ts`: Defines the schema for blog post metadata (title, description, pubDate, heroImage, etc.).

## ASSA System Integration
This project is an **ASSA-enabled** workspace. It utilizes the Autonomous Self-Sovereign Agent (v3.5 Weaver) architecture for continuous learning and architectural evolution.
- **Patterns:** Project-specific conventions are distilled into `.memory/patterns.md`.
- **Ledger:** Raw interaction signals are tracked in `.memory/evolution_ledger.json`.
- **Knowledge Graph:** The "Weaver" automatically rebuilds the hierarchical knowledge graph (G0-G3 tiers).

## Key Commands
- `npm run dev` / `npm start`: Start the local development server at `http://localhost:4321`.
- `npm run build`: Build the static site for production (output in `/dist`).
- `npm run preview`: Locally preview the production build.
- `python3 html_to_blog.py`: Script for converting HTML source files to blog posts.

## Development Conventions
- **TypeScript:** Prioritize using `interface` over `type` for defining object shapes.
- **Styling:** Prefer Vanilla CSS or Tailwind classes. Avoid complex runtime CSS-in-JS.
- **Verification:** After modifying frontend components or blog layouts, verify the changes using browser automation or manual visual checks.
- **Context7:** Use the `context7` extension to fetch up-to-date documentation for Astro or any third-party libraries.

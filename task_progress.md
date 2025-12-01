# Task Progress Snapshot
**Date:** Monday, December 1, 2025
**Current Working Directory:** `/Users/jay/LocalProjects/Jay-s-Blog`

## Overall Goal
Standardize blog post layouts by refactoring legacy posts to use the global `Layout.astro` and `[...slug].astro` mechanisms (specifically for TOC generation and script management).

## Current Focus
Refactoring `src/content/blog/ai-visualization.md`.

## Status: Paused / Interrupted
The workflow was interrupted just before applying changes to `src/content/blog/ai-visualization.md`.

### Completed Actions
1.  **Script Migration:** 
    *   Created `public/scripts/ai-visualization.js`.
    *   Populated it with all necessary logic (`renderDashboardDemo`, `callGemini`, `renderMermaid`, `activateSignal`, etc.) extracted from the original Markdown file.
2.  **Layout Verification:**
    *   Verified `src/layouts/Layout.astro` handles `localScripts` and `externalScripts` correctly.
    *   Verified `src/pages/blog/[...slug].astro` correctly generates a Table of Contents (TOC) from Markdown headings.
3.  **Reference Check:**
    *   Reviewed `src/content/blog/ai-science-paradigm.md` as a successful example of the new format.

### Next Steps (Immediate To-Do)
1.  **Refactor `src/content/blog/ai-visualization.md`:**
    *   Update Frontmatter: Add `localScripts: ["/scripts/ai-visualization.js"]`.
    *   Remove HTML Wrappers: Delete outer `<html>`, `<head>`, `<body>`, `<header>`, and `<main>` tags. The layout handles these.
    *   Remove Inline Scripts: Delete all `<script>` tags (logic is now in the external file).
    *   Standardize Headings: Convert HTML `<section><h2>Title</h2>...</section>` structures to standard Markdown (`## Title`) to ensure the automatic TOC works.
    *   Clean up styling: Remove hardcoded tailwind classes that conflict with the prose typography where possible, or ensure they sit inside `<div>` wrappers if specific styling is needed.

2.  **Verification:**
    *   Check if the "AI Visualization" post renders correctly in the browser.
    *   Verify the TOC appears in the sidebar.
    *   Verify interactive elements (Mermaid, Charts, Gemini Mock) still function.

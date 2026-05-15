# About Me Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a standalone, narrative-driven "About Me" page using a sticky two-column layout, fetching its content from a Markdown file to maximize maintainability.

**Architecture:** Use Astro components for the layout (ProfileSidebar and a custom main page), fetch Markdown for the narrative text, and update the global Layout for navigation.

**Tech Stack:** Astro, Tailwind CSS, `@tailwindcss/typography`.

---

### Task 1: Asset Management

**Files:**
- Modify: `public/resume_long.pdf` (Create by copying)
- Modify: `public/avatar.jpg` (Create by copying)

- [ ] **Step 1: Create assets directory and copy files**
```bash
cp /Users/jay/LocalProjects/Jay-s-Blog/personal_profile/resume_long.pdf public/resume_long.pdf
cp /Users/jay/LocalProjects/Jay-s-Blog/personal_profile/avatar.jpg public/avatar.jpg
```

- [ ] **Step 2: Verify assets are in place**
Run: `ls public/resume_long.pdf public/avatar.jpg`
Expected: PASS (files should be listed)

### Task 2: Create the Sidebar Component

**Files:**
- Create: `src/components/ProfileSidebar.astro`

- [ ] **Step 1: Write the sidebar component**
```astro
---
---
<div class="bg-gray-100 dark:bg-gray-800 rounded-2xl p-6 shadow-sm sticky top-24">
  <div class="flex justify-center mb-6">
    <img src="/avatar.jpg" alt="Jiahao Ji" class="w-48 h-48 rounded-full object-cover border-4 border-gray-800 dark:border-gray-200" />
  </div>
  
  <h2 class="text-xl font-bold text-center text-gray-900 dark:text-white mb-2">Jiahao Ji</h2>
  <p class="text-center text-sm text-gray-600 dark:text-gray-400 mb-6">MD Candidate, Fudan University<br/>Clinical Neuroscience & AI</p>
  
  <div class="space-y-3 mb-8">
    <div>
      <p class="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Email</p>
      <p class="text-sm font-medium text-indigo-600 dark:text-indigo-400">Jhji19@fudan.edu.cn</p>
    </div>
    <div>
      <p class="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Phone</p>
      <p class="text-sm font-medium text-gray-800 dark:text-gray-200">+86 18516701383</p>
    </div>
  </div>
  
  <div class="flex justify-center">
    <a href="/resume_long.pdf" target="_blank" class="w-full text-center px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-medium rounded-lg transition-colors duration-200">
      Download Resume (PDF)
    </a>
  </div>
</div>
```

- [ ] **Step 2: Commit**
```bash
git add src/components/ProfileSidebar.astro
git commit -m "feat: add ProfileSidebar component"
```

### Task 3: Create the Narrative Markdown Content

**Files:**
- Create: `src/content/about/narrative.md`

- [ ] **Step 1: Create directory and content file**
```bash
mkdir -p src/content/about
```

- [ ] **Step 2: Write the narrative content**
```markdown
## The Intersection of Medicine & AI
I am an MD candidate in the 8-year program at Fudan University. My journey began at the bedside, observing the devastating impacts of neurodegenerative diseases. This clinical exposure ignited my passion for understanding the pathological mechanisms of brain disorders. To achieve this, I pivoted toward computational biology and machine learning, specifically working within the MSRA AI and the Brain group. I believe that integrating multi-modal foundation models with clinical neuroscience is the key to uncovering the next generation of biomarkers and therapeutic targets.

## Engineering for Biology: Spatial Omics
At the Fudan Data-Driven Future Lab and the Institute of Medical Genetics, my research is heavily focused on Spatial Transcriptomics and Bioinformatics. 

To solve the data scarcity and curation bottlenecks in spatial omics, I independently developed **SpatialDataAgent**—an autonomous framework utilizing an Autoresearch-style iterative ReAct loop. This system successfully recovered 769 H&E-ST paired datasets from GEO (+141% over manual methods), leading to the generation of HESRT, a massive datalake containing 29.2 million spots of histological data.

Additionally, I engineered **ASSA (Autonomous Self-Sovereign Agent)**, a robust agentic framework featuring hierarchical memory systems for autonomous adaptation, and **Spatial-CLIP**, fine-tuning vision-language encoders to align histopathology images with spatial transcriptomics data.

## Future Outlook
Looking ahead, my goal is to bridge the gap between high-dimensional spatial data and actionable clinical insights. I am actively researching Neural Networks (Transformers, GNNs) and Multi-GPU Training paradigms to push the boundaries of what is possible in Alzheimer's Spatial Intelligence. Ultimately, I strive to translate these complex data-driven methodologies into precise, personalized medicine for patients suffering from cognitive decline.
```

- [ ] **Step 3: Commit**
```bash
git add src/content/about/narrative.md
git commit -m "feat: add narrative markdown content"
```

### Task 4: Create the About Page Route

**Files:**
- Create: `src/pages/about.astro`

- [ ] **Step 1: Write the main page wrapper**
```astro
---
import Layout from "../layouts/Layout.astro";
import ProfileSidebar from "../components/ProfileSidebar.astro";
import * as Narrative from "../content/about/narrative.md";

// We use max-w-6xl for this page to accommodate the two-column layout
---

<Layout title="About Me - Jiahao Ji" maxWidth="max-w-6xl">
  <div class="grid grid-cols-1 md:grid-cols-12 gap-8 mt-4">
    <!-- Left Column: Sticky Sidebar -->
    <div class="md:col-span-4 lg:col-span-3">
      <ProfileSidebar />
    </div>
    
    <!-- Right Column: Scrolling Narrative -->
    <div class="md:col-span-8 lg:col-span-9 bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-sm">
      <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-8 border-b pb-4 dark:border-gray-700">About Me</h1>
      <article class="prose prose-indigo dark:prose-invert max-w-none">
        <Narrative.Content />
      </article>
    </div>
  </div>
</Layout>
```

- [ ] **Step 2: Commit**
```bash
git add src/pages/about.astro
git commit -m "feat: build about me layout page"
```

### Task 5: Add Navigation Link to Header

**Files:**
- Modify: `src/layouts/Layout.astro`

- [ ] **Step 1: Add "About" link to Layout navigation**
```bash
# We will use sed to insert the link before the ThemeToggle in src/layouts/Layout.astro
# We insert it around line 143 where the other nav links are.
```
*Wait, sed is not recommended. I will use the `replace_file_content` tool when executing.*

For the plan, I will show the manual edit.

```astro
// Locate in src/layouts/Layout.astro:
          <a
            href="/blog"
            class="hover:text-indigo-600 dark:hover:text-indigo-400 transition"
            >Blog</a
          >
// Add this right below it:
          <a
            href="/about"
            class="hover:text-indigo-600 dark:hover:text-indigo-400 transition"
            >About</a
          >
```

- [ ] **Step 2: Install tailwindcss typography plugin if missing**
Run: `npm install -D @tailwindcss/typography`
(It's needed for the `prose` class we used in Task 4).

- [ ] **Step 3: Update tailwind.config.mjs to include typography**
Modify `tailwind.config.mjs` to add the plugin.
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
```

- [ ] **Step 4: Commit**
```bash
git add src/layouts/Layout.astro tailwind.config.mjs package.json package-lock.json
git commit -m "feat: add about page to nav and configure typography plugin"
```

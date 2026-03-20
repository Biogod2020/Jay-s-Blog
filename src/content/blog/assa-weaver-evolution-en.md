---
title: "Weaver: An AI Self-Evolving System Grown from Practice"
description: "Documenting the real journey of the ASSA project from a few lines of scripts to a V3.5 hierarchical knowledge graph. This is not just a technological leap, but a deep reflection on 'Human-AI Collaborative Sovereignty'."
pubDate: 2026-03-20
heroImage: "/images/assa-evolution/cover.png"
---

<div class="mb-12">
    <div class="inline-block px-4 py-1.5 mb-6 rounded-full bg-indigo-50 text-indigo-600 text-sm font-semibold border border-indigo-100 dark:bg-indigo-900/30 dark:text-indigo-300">
        <span class="flex items-center">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
            ASSA V3.5 Evolution Report
        </span>
    </div>
</div>

<figure class="mb-12 rounded-2xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-xl bg-gray-900 flex justify-center p-4">
    <img src="/images/assa-evolution/extension-preview.png" alt="ASSA Extension Preview in Gemini CLI" class="max-w-full h-auto object-contain rounded-lg border border-gray-700" style="max-height: 500px;" />
</figure>

As a "poor student" who has heavily relied on `geminicli` for three months, while I am constantly amazed by Gemini's intelligence, I am also frequently troubled by its **forgetfulness** and **hallucinations**.

The pain is visceral: you're wrestling with complex generic logic in a large project. You clearly stated in the first turn, "*All type definitions must use interface*," yet by the 30th turn, it's casually writing `type` everywhere. Or it confidently reports, "<span class="text-green-600 dark:text-green-400 font-mono">Code modified successfully</span>," but when you open the file, **the physical content remains untouched**. Repeatedly correcting the same mistakes, or watching it mess up code in a large project while ignoring the facts—it’s a real headache.

Recently, openclaw went viral. I gave it a spin—it’s fun, but it didn’t quite feel like a reliable tool for research or development yet. However, the wisdom of the crowd is infinite. Browsing clawhub, I saw many brilliant `skills`. Inspired by the **self-evolment** approach, I looked through the `geminicli` extension library, found no similar plugins, and decided to build one myself. This was my first attempt at a <u class="decoration-indigo-500 decoration-2 underline-offset-4">ReAct system (Reasoning and Acting loop)</u>. My personal experience has been decent—memory has definitely improved—though long-term effects remain to be seen.

Looking back, I realized that only through **daily practice** can one uncover technical nuances and devise solutions. All progress is built on constant trial and error. As Marx said, all human knowledge comes from productive practice. Only by doing can we progress.

I asked the AI to summarize the process below. Feel free to read or try the plugin I developed (*even if it only has one star from me right now*).

### 🚀 Plugin Quick Start

> **Install Command**:
> ```bash
> gemini extensions install https://github.com/Biogod2020/ASSA
> ```

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/Biogod2020/ASSA)

> [!IMPORTANT]
> **Current Limitations**: The extension isn't perfect. When used alongside other tools, the memory function sometimes fails to trigger automatically. Additionally, as the context grows longer, the hook injection seems to weaken.
> 
> In the future, I might consider more low-level logic to ensure memory is submitted consistently. But for now, with limited dev time, manually triggering it in long contexts works fine. I’m also waiting for Google to update and provide more robust, lower-level hooks. Feedback is always welcome!

---

## 01. Evolution Timeline: Eight Days of Fire

In just over a week, we underwent "**compressed evolution**"—from building vertical memory to restructuring horizontal order.

<div class="my-10">
    <div class="relative border-l-2 border-indigo-200 dark:border-indigo-800 ml-4 space-y-8">
        <!-- Day 1-2 -->
        <div class="relative pl-8">
            <div class="absolute w-4 h-4 bg-indigo-500 rounded-full -left-[9px] top-1 border-4 border-white dark:border-gray-900"></div>
            <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-1">Day 1-2: Clueless Exploration</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400">Trial and error with <code class="bg-gray-100 dark:bg-gray-800 px-1 py-0.5 rounded text-xs">Python</code> scripts, eventually migrating to the <code class="bg-gray-100 dark:bg-gray-800 px-1 py-0.5 rounded text-xs">JS/TS</code> ecosystem.</p>
        </div>
        <!-- Day 3-4 -->
        <div class="relative pl-8">
            <div class="absolute w-4 h-4 bg-indigo-500 rounded-full -left-[9px] top-1 border-4 border-white dark:border-gray-900"></div>
            <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-1">Day 3-4: Embracing MCP & Hooks</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400">Solving instruction drift and execution black boxes; establishing the <strong>L1-L2-L3</strong> distillation path.</p>
        </div>
        <!-- Day 4 -->
        <div class="relative pl-8">
            <div class="absolute w-4 h-4 bg-indigo-500 rounded-full -left-[9px] top-1 border-4 border-white dark:border-gray-900"></div>
            <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-1">Day 4: Solving the "Freshness" Problem</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400">Introducing <code class="text-orange-500 text-xs">PENDING</code> / <code class="text-green-500 text-xs">PROCESSED</code> status filtering to prevent historical amnesia.</p>
        </div>
        <!-- Day 5 -->
        <div class="relative pl-8">
            <div class="absolute w-4 h-4 bg-indigo-500 rounded-full -left-[9px] top-1 border-4 border-white dark:border-gray-900"></div>
            <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-1">Day 5: Architectural Foresight</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400">Introducing **Graph** organization and categorizing knowledge into **G0-G3** tiers.</p>
        </div>
        <!-- Day 6 -->
        <div class="relative pl-8">
            <div class="absolute w-4 h-4 bg-indigo-500 rounded-full -left-[9px] top-1 border-4 border-white dark:border-gray-900"></div>
            <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-1">Day 6: Embracing Subagents</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400">Offloading main process pressure; decoupling <em>Distiller</em> and <em>Promoter</em> logic.</p>
        </div>
        <!-- Day 6-8 -->
        <div class="relative pl-8">
            <div class="absolute w-4 h-4 bg-indigo-500 rounded-full -left-[9px] top-1 border-4 border-white dark:border-gray-900"></div>
            <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-1">Day 6-8: Peak Performance & Governance</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400">Implementing the <u class="decoration-indigo-500 decoration-2 underline-offset-2">Index-First Strategy</u> and establishing main process sovereignty.</p>
        </div>
    </div>
</div>

---

## 02. Clueless Exploration (Day 1-2)

When development first began, I was truly wandering in the dark.

I initially asked the AI to write a version in Python, trying to intercept and record conversations with simple scripts. This immediately hit a wall: Python scripts required extra dependencies (like running `pip install` constantly), and they felt out of place within Gemini CLI’s native `TypeScript/Node.js` architecture. In practice, these cross-language calls made the environment unstable, leading to frequent freezes.

After two days of struggle, I abandoned Python and decided to follow Gemini CLI’s native ecosystem, switching entirely to **JS/TS**. This was the first step toward professional engineering—painful as it was to start over, it laid the foundation for the high-performance Hook mechanism that followed.

---

## 03. Embracing MCP & Hooks, Establishing the Evolution Path (Day 3-4)

After switching to JS, I began to study the tools Gemini CLI provides for developers.

I learned what "Hooks" are—they act as **"undercover agents"** inserted before AI reasoning (`BeforeAgent`) and after tool execution (`AfterTool`). I started using MCP (Model Context Protocol) tools to distill daily errors and corrections.

Through continuous discussion and experimentation, the AI and I co-summarized a highly effective concept: the <u class="decoration-indigo-500 decoration-2 underline-offset-4">**L1-L2-L3 Knowledge Distillation Path**</u>.

- **L1 (Ledger)**: Records **raw correction signals** and error messages like a ledger.
- **L2 (Local)**: Distills these into **development habits** and patterns specific to the current project.
- **L3 (Global)**: Promotes them to **global guidelines** across projects.

This hierarchical approach mirrors how human developers summarize their own experiences—knowledge is no longer a tangled mess, but a clear path for promotion.

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-12">
    <div class="glass-card p-6 rounded-2xl border border-gray-100 dark:border-gray-800">
        <h3 class="text-indigo-600 dark:text-indigo-400 font-bold mb-3 flex items-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"></path></svg>
            Physical Metadata
        </h3>
        <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
            We no longer rely solely on the AI's semantic memory. Instead, we use Hooks to forcefully inject physical identifiers into every tool output. This establishes objective coordinates, ensuring reported successes are based on actual file changes.
        </p>
    </div>
    <div class="glass-card p-6 rounded-2xl border border-gray-100 dark:border-gray-800">
        <h3 class="text-purple-600 dark:text-purple-400 font-bold mb-3 flex items-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
            Semantic Reflex Sensor
        </h3>
        <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
            Leveraging the AI's understanding of interaction sentiment. When I correct an error or offer praise (e.g., "<em>Perfect</em>," "<em>That's wrong</em>"), the system automatically captures these signals and triggers a feedback loop to record the lesson immediately.
        </p>
    </div>
</div>

---

## 04. Solving the Knowledge "Freshness" Problem (Day 4)

As interactions increased, it became clear that simply accumulating facts wouldn't work. Log files grew longer, and if every distillation required reading the entire history, **Token consumption and response times would skyrocket**.

The AI suggested vector search or summary compression, but both felt too complex and prone to losing detail.

Instead, I came up with a "brute force" solution: classifying knowledge as either "Expired/Processed" or "Fresh." I added status flags to every signal in the Ledger. This way, during distillation, the AI only processes "Fresh" knowledge marked as `<span class="text-orange-500 font-bold text-sm">PENDING</span>`, tagging it as `<span class="text-green-500 font-bold text-sm">PROCESSED</span>` once done. Efficiency surged, and the AI's attention became laser-focused.

---

## 05. Architectural Foresight: Graph & G0-G3 Tiers (Day 5)

Even with efficient distillation, the rules in the files continued to pile up. Without a solid architecture from the start, organizing them would eventually become impossible.

Drawing on my experience with tools like Obsidian, I realized that a <u class="decoration-indigo-500 decoration-2 underline-offset-4">**Graph**</u> structure would be ideal. I moved away from flat Markdown lists toward an interconnected knowledge graph.

I also felt that knowledge shouldn't just be a flat graph—rules have different weights. For instance, *not deleting code recklessly has higher priority than following a specific naming convention*. This led to the **G0-G3 tiered system**:

<figure class="my-16 relative">
<div class="flex justify-center bg-slate-50/50 dark:bg-slate-900/30 rounded-2xl p-8 border border-slate-200 dark:border-slate-800 overflow-hidden">
<svg class="w-full max-w-2xl h-auto" viewBox="0 0 600 350" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="tier-grad" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#4f46e5" stop-opacity="0.1" /><stop offset="100%" stop-color="#7c3aed" stop-opacity="0.05" /></linearGradient></defs><path d="M 50 300 L 550 300 L 450 50 L 150 50 Z" fill="url(#tier-grad)" stroke="#4f46e5" stroke-width="2" opacity="0.6" /><line x1="125" y1="112.5" x2="475" y2="112.5" stroke="#4f46e5" stroke-width="1" stroke-dasharray="5,5" /><line x1="100" y1="175" x2="500" y2="175" stroke="#4f46e5" stroke-width="1" stroke-dasharray="5,5" /><line x1="75" y1="237.5" x2="525" y2="237.5" stroke="#4f46e5" stroke-width="1" stroke-dasharray="5,5" /><g font-family="sans-serif" font-weight="bold" text-anchor="middle"><text x="300" y="90" fill="#4f46e5" font-size="16">G0: Core Mandates (Hard Red Lines)</text><text x="300" y="152.5" fill="#6366f1" font-size="16">G1: Foundation (Engineering Standards)</text><text x="300" y="215" fill="#8b5cf6" font-size="16">G2: Domain (Specific Domain Knowledge)</text><text x="300" y="277.5" fill="#a855f7" font-size="16">G3: Fragments (Technical Snippets)</text></g></svg>
</div>
<figcaption class="text-center text-sm text-gray-500 mt-4 italic">
    Fig 5.1: Weaver G0-G3 Knowledge Tiers. This system ensures both clarity and precise indexing across different contexts.
</figcaption>
</figure>

---

## 06. Embracing Subagents (Day 6)

While the Graph worked well, asking the main process Agent to both write code and maintain a sophisticated knowledge graph system was a massive engineering load—**context would blow up easily**.

Looking for optimizations, I saw `Subagent` implementations in the Superpowers extension and realized Gemini CLI supports them natively.

I decided to embrace Subagents, offloading background distillation (`Distiller`) and global rule synchronization (`Promoter`) into independent sub-tools. This was like giving the main Agent two secretarial assistants, drastically reducing its workload while boosting overall system performance.

<div class="my-12 p-1 rounded-3xl bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 shadow-xl shadow-indigo-500/20">
    <div class="bg-white dark:bg-gray-900 rounded-[22px] p-8 md:p-10">
        <h3 class="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-10 flex items-center justify-center">
            <svg class="w-8 h-8 mr-4 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
            Division of Labor: Main Process vs. Subagents
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-16">
            <div class="space-y-6">
                <div class="inline-flex items-center px-5 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/50 text-indigo-700 dark:text-indigo-300 text-sm font-bold uppercase tracking-widest border border-indigo-200 dark:border-indigo-800">
                    Main Agent
                </div>
                <p class="text-xl md:text-2xl text-gray-800 dark:text-gray-200 leading-relaxed font-semibold">
                    Focuses on executing user tasks, writing core code, and making final <span class="text-indigo-600 dark:text-indigo-400">Architectural Governance</span> decisions.
                </p>
            </div>
            <div class="space-y-6">
                <div class="inline-flex items-center px-5 py-1.5 rounded-full bg-green-100 dark:bg-green-900/50 text-green-700 dark:text-green-300 text-sm font-bold uppercase tracking-widest border border-green-200 dark:border-green-800">
                    Subagents
                </div>
                <p class="text-xl md:text-2xl text-gray-800 dark:text-gray-200 leading-relaxed font-semibold">
                    Perform heavy-lifting in the background: transforming raw signals into Patterns and promoting them to the global library.
                </p>
            </div>
        </div>
    </div>
</div>

---

## 07. Extreme Optimization & Testing (Day 6 - Present)

Real-world testing and optimization are always the most tedious parts. To handle context bloat caused by injecting too many rules (which once hit 25KB+), I implemented an aggressive <u class="decoration-indigo-500 decoration-2 underline-offset-4">**"Index-First"**</u> strategy, also known as **Skeleton-First** parsing.

The system no longer crams in the full text of every rule. Instead, it injects only the index skeleton, fostering a "pre-reading instinct" in the Agent so it can `read_file` on its own when it needs to make changes.

Furthermore, to prevent Subagents from making messy logical choices during organization, I established **"Main Process Sovereignty"**: Subagents handle the distillation and conflict detection, but the final decision on merging must be queried through the main process to the user.

After countless iterations, we arrived at version 3.5—finally, a system that’s truly a joy to use.

### The System Codex: Unshakable Principles

During testing, I realized the system needed explicit "ground rules" to prevent the AI from getting lazy. I categorized these as **G1 Engineering Standards** and hardcoded them into its system prompt:

<aside class="glass-card p-8 rounded-2xl border border-indigo-100 dark:border-indigo-900/50 my-12 relative overflow-hidden">
    <div class="absolute top-0 right-0 p-4 opacity-10">
        <svg class="w-24 h-24 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path></svg>
    </div>
    <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-6 flex items-center">
        <span class="w-2 h-8 bg-indigo-500 rounded mr-3"></span> Selected Codex Rules
    </h3>
    <ul class="space-y-8 relative z-10">
        <li class="relative pl-8">
            <span class="absolute left-0 top-1 text-indigo-500 font-mono font-bold">01.</span>
            <strong class="text-gray-900 dark:text-white block mb-2">Reflex Sovereignty</strong>
            <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
                The Agent must realize it is not just an executor of instructions, but a guardian of system integrity. Mandatory incremental distillation at the end of every turn (the <code>Mandatory Heartbeat</code>) ensures it is actively thinking.
            </p>
        </li>
        <li class="relative pl-8">
            <span class="absolute left-0 top-1 text-indigo-500 font-mono font-bold">02.</span>
            <strong class="text-gray-900 dark:text-white block mb-2">Empirical Truth</strong>
            <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
                [Rule: <code>G1-EMPIRICAL-TRUTH</code>] prohibits semantic guessing of execution results. Before reporting success, physical audits (e.g., file reads, running tests, VLM audits) are mandatory to verify the state of the physical world.
            </p>
        </li>
        <li class="relative pl-8">
            <span class="absolute left-0 top-1 text-indigo-500 font-mono font-bold">03.</span>
            <strong class="text-gray-900 dark:text-white block mb-2">Surgical Edit</strong>
            <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
                Gone are the days when the AI would lazily rewrite entire files, losing critical details. Now, blind full-file overwrites are forbidden. Deep reading to identify specific subsections and precise use of <code>replace</code> are required.
            </p>
        </li>
    </ul>
</aside>

---

## Conclusion: Knowledge Grown from Practice

Marx once said that all human knowledge comes from productive practice. Every functional node of ASSA wasn't a pre-designed blueprint; it was "forged" by the AI and me through constant trial, anxiety, and correction.

The truth of engineering often hides within the most mundane failures. When you start taking every "historical misread" by the AI seriously, and when you start worrying that your knowledge base will become "messy," the seeds of evolution are sown. **The Weaver architecture isn't a pre-set blueprint; it is a physical response to the pains of evolution.**

<div class="glass-card p-6 rounded-2xl border border-indigo-100 dark:border-indigo-900/50 my-12 bg-indigo-50/30 dark:bg-indigo-900/10">
    <h3 class="text-indigo-600 dark:text-indigo-400 font-bold mb-3 flex items-center">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
        The Philosophy of "Growing"
    </h3>
    <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
        Initially, I wanted to design a perfect architecture from scratch, like a comprehensive Python framework. But experience proved that <strong>design decoupled from actual usage scenarios is just a fantasy</strong>. Structures that seem brilliant in theory collapse instantly when they hit real-world code errors, Token limits, or tool timeouts.
    </p>
    <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed">
        True iteration happens during every painful copy-paste, and every exasperated "Why did you forget again?!" It forces you to write a Hook, add a status flag, or split off a Subagent. This is the essence of "<strong>practice leads to true knowledge</strong>." Don't be afraid of messy code at the start. As long as you are writing, using, and feeling the pain, it will eventually grow into what it needs to be.
    </p>
</div>

Through these three months of experimentation, I haven’t just built a better tool; I’ve deeply experienced the joy of moving forward through practice. While this plugin is still in its infancy, the process of watching it grow from nothing has been my greatest reward.

---
<footer class="mt-20 pt-8 border-t border-gray-100 dark:border-gray-800 text-sm text-gray-500 flex items-center justify-center space-x-2">
    <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
    <p>This article was co-written with ASSA V3.5. Core evolution data based on practice records from Commit <code>71bcf21</code> to <code>5231114</code>.</p>
</footer>

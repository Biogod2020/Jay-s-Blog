---
title: "Lecture Notes: Rethinking Research Visualization in the AI Era"
description: "From passive reading to interactive, end-to-end reconstruction: building a visualization mindset of AI logic + HTML presentation"
pubDate: 2025-12-01
localScripts:
  - "/scripts/ai-visualization.js"
lang: en
---

<div class="not-prose mb-12 space-y-8">
  <div class="relative text-center space-y-3">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-32 h-32 bg-primary-50 dark:bg-primary-900/20 rounded-full blur-3xl -z-10"></div>
    <div class="inline-flex items-center justify-center px-3 py-1 text-xs font-medium text-primary-700 bg-primary-50 dark:bg-primary-900/30 rounded-full ring-1 ring-inset ring-primary-600/20">
      <i class="fas fa-university mr-2"></i> Shanghai Medical College, Fudan University
    </div>
    <div class="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 dark:text-slate-100 leading-tight">
      Lecture Notes: <span class="gradient-text block md:inline">Research Visualization in the AI Era</span>
    </div>
    <p class="text-xl text-slate-500 dark:text-slate-400 font-light tracking-wide">From passive reading to interactive, end-to-end reconstruction</p>
  </div>

  <div class="glass-card rounded-2xl p-8 relative overflow-hidden group hover:shadow-lg transition-shadow duration-300">
    <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
      <i class="fas fa-layer-group text-8xl text-primary-500"></i>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 relative z-10 text-left">
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-400 font-bold mb-1">Audience</div>
        <div class="text-slate-700 dark:text-slate-300 font-medium">Senior undergraduates / master's and PhD students</div>
      </div>
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-400 font-bold mb-1">Length</div>
        <div class="text-slate-700 dark:text-slate-300 font-medium">About 90 minutes</div>
      </div>
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-400 font-bold mb-1">Goal</div>
        <div class="text-slate-700 dark:text-slate-300 font-medium">Learn to think in terms of "AI logic + HTML presentation", and pick up tools that make a real difference at every stage of research.</div>
      </div>
    </div>
  </div>
</div>

## Introduction: Cognitive Friction and the Bridge Between Us

In the previous chapter we looked at how AI drives scientific discovery as a "fourth paradigm". The more practical bottleneck is this: **how can our human brains read and understand what AI produces, efficiently?**

We face a degree of **cognitive friction** we have not had before. It comes from the large gap between how humans and machines fundamentally process information.

<div class="not-prose grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
  <div class="glass-card p-6 rounded-xl border-l-4 border-l-slate-400">
    <div class="flex items-center gap-3 mb-3">
      <i class="fas fa-microchip text-slate-500 dark:text-slate-400 text-xl"></i>
      <span class="text-lg font-bold text-slate-900 dark:text-slate-100">Where AI is comfortable</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400 mb-3"><strong>Structured logic and linear streams</strong></p>
    <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
      AI (especially a large language model) is a probabilistic prediction engine, and its output is forced into a linear stream of text. It is best at producing <strong>structured languages</strong> (JSON, Python, HTML, XML), and nested brackets or deep hierarchies do not bother it.
    </p>
  </div>
  <div class="glass-card p-6 rounded-xl border-l-4 border-l-primary-500">
    <div class="flex items-center gap-3 mb-3">
      <i class="fas fa-eye text-primary-500 text-xl"></i>
      <span class="text-lg font-bold text-slate-900 dark:text-slate-100">Where humans are comfortable</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400 mb-3"><strong>Visual perception and pattern recognition</strong></p>
    <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
      Humans are visual animals. We process images, colour, spatial layout and interaction far faster than plain text.
    </p>
    <ul class="list-none space-y-2 mt-4 text-sm text-slate-500 dark:text-slate-400">
      <li class="flex items-start gap-2">
        <i class="fas fa-exclamation-circle text-amber-500 mt-1"></i>
        <span>Reading long stretches of plain text takes a lot of effort, especially unformatted data or code.</span>
      </li>
      <li class="flex items-start gap-2">
        <i class="fas fa-arrow-down text-red-500 mt-1"></i>
        <span>That effort slows research down and makes it easy to miss insights.</span>
      </li>
    </ul>
  </div>
</div>

> The core mismatch: AI produces "dense code and text", while humans want "high-bandwidth visuals and interaction".

The way out is to translate the structured code AI is good at, in real time, into a visual experience that people grasp more easily. That bridge is **HTML + the browser**.

## The Internet's Gift to Science

To see why HTML makes sense as the core medium for research visualization, it helps to look at where it came from: **Web technology was created in the first place to serve scientific communication.**

<div class="not-prose relative border-l-4 border-slate-200 dark:border-slate-700 ml-4 my-10 space-y-12">
  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-slate-100 border-4 border-slate-400 rounded-full"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-2xl text-slate-800">1989</span>
      <span class="font-bold text-primary-600">The Web is born at CERN (European Organization for Nuclear Research)</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400">Physicist <strong>Tim Berners-Lee</strong> invented HTML to fix a real problem: papers came in incompatible formats and information could not be shared.
      <span class="bg-primary-50 dark:bg-primary-900/30 text-primary-700 px-2 py-0.5 rounded text-xs ml-1">Origin: built for scientific communication</span>
    </p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://baike.baidu.com/item/%E8%92%82%E5%A7%86%C2%B7%E4%BC%AF%E7%BA%B3%E6%96%AF-%E6%9D%8E" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/LS3_4919_%28cropped%29.jpg/330px-LS3_4919_%28cropped%29.jpg" alt="Tim Berners-Lee" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>Tim Berners-Lee · Baidu Baike</span>
      </a>
      <a href="https://en.wikipedia.org/wiki/Tim_Berners-Lee" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 hover:text-primary-600">
        <i class="fas fa-globe text-[11px]"></i>
        <span>Wikipedia</span>
      </a>
    </div>
    <div class="mt-3 flex items-center gap-3 text-xs text-slate-500 dark:text-slate-400">
      <a href="https://www.w3.org/People/Berners-Lee/" target="_blank" class="inline-flex items-center gap-2 hover:text-primary-600">
        <span class="w-8 h-8 rounded-full overflow-hidden bg-slate-200 flex items-center justify-center">
          <i class="fas fa-user text-slate-500 dark:text-slate-400 text-xs"></i>
        </span>
        <span>Tim Berners-Lee's homepage (W3C)</span>
      </a>
      <a href="https://home.cern/" target="_blank" class="inline-flex items-center gap-2 hover:text-primary-600">
        <span class="w-8 h-8 rounded-full overflow-hidden bg-slate-200 flex items-center justify-center">
          <i class="fas fa-atom text-slate-500 dark:text-slate-400 text-xs"></i>
        </span>
        <span>CERN website</span>
      </a>
    </div>
  </div>

  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-slate-100 border-4 border-slate-300 rounded-full"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-xl text-slate-500 dark:text-slate-400">2004</span>
      <span class="font-medium text-slate-700 dark:text-slate-300">Markdown is released</span>
    </div>
    <p class="text-sm text-slate-500 dark:text-slate-400">John Gruber created Markdown to make writing HTML simpler. It has become the default format for AI output.</p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://baike.baidu.com/item/%E7%BA%A6%E7%BF%B0%C2%B7%E6%A0%BC%E9%B2%81%E4%BC%AF" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/64/John_Gruber%2C_2009_%28cropped%29.jpg" alt="John Gruber" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>John Gruber · Baidu Baike</span>
      </a>
      <a href="https://en.wikipedia.org/wiki/John_Gruber" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 hover:text-primary-600">
        <i class="fas fa-globe text-[11px]"></i>
        <span>Wikipedia</span>
      </a>
    </div>
    <div class="mt-3 text-xs">
      <a href="https://daringfireball.net/projects/markdown/" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-500 dark:text-slate-400 hover:text-primary-600 hover:bg-primary-50 dark:bg-primary-900/30 border border-slate-100">
        <i class="fas fa-link text-xs"></i>
        <span>Original Markdown spec (Daring Fireball)</span>
      </a>
    </div>
  </div>

  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-white dark:bg-gray-800 border-4 border-blue-500 rounded-full"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-2xl text-slate-800">2008</span>
      <span class="font-bold text-blue-600">Chrome and the V8 engine</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400">Google released the very fast V8 engine, and the browser grew into something close to an operating system.</p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://baike.baidu.com/item/%E6%8B%89%E6%96%AF%C2%B7%E5%B7%B4%E5%85%8B" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Lars_Bak.png" alt="Lars Bak" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>Lars Bak · Baidu Baike</span>
      </a>
      <a href="https://en.wikipedia.org/wiki/Lars_Bak_(computer_programmer)" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 hover:text-blue-600">
        <i class="fas fa-globe text-[11px]"></i>
        <span>Wikipedia</span>
      </a>
    </div>
    <div class="mt-3 flex items-center gap-4">
      <a href="https://www.google.com/" target="_blank" class="inline-flex items-center gap-2 hover:opacity-80">
        <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google Logo" class="h-4 object-contain">
        <span class="text-xs text-slate-500 dark:text-slate-400">Google</span>
      </a>
      <a href="https://www.google.com/chrome/" target="_blank" class="inline-flex items-center gap-2 hover:opacity-80">
        <img src="https://www.google.com/chrome/static/images/chrome-logo.svg" alt="Chrome Logo" class="h-5 object-contain">
        <span class="text-xs text-slate-500 dark:text-slate-400">Chrome browser</span>
      </a>
      <a href="https://v8.dev/" target="_blank" class="inline-flex items-center gap-2 hover:text-blue-600 text-xs text-slate-500 dark:text-slate-400">
        <i class="fas fa-bolt text-blue-500 text-xs"></i>
        <span>Official V8 blog</span>
      </a>
    </div>
  </div>

  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-slate-100 border-4 border-slate-300 rounded-full"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-xl text-slate-500 dark:text-slate-400">2011-2014</span>
      <span class="font-medium text-slate-700 dark:text-slate-300">Visualization libraries and front-end frameworks take off</span>
    </div>
    <p class="text-sm text-slate-500 dark:text-slate-400">
      <strong>D3.js (2011)</strong> made data move on web pages;<br>
      <strong>Vue.js (2014)</strong> let developers assemble complex applications from building blocks.
    </p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://en.wikipedia.org/wiki/Mike_Bostock" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://avatars.githubusercontent.com/u/230541?v=4" alt="Mike Bostock" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>Mike Bostock · Wikipedia</span>
      </a>
      <a href="https://baike.baidu.com/item/%E5%B0%A4%E9%9B%A8%E6%BA%AA" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://avatars.githubusercontent.com/u/499550?v=4" alt="Evan You" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>Evan You · Baidu Baike</span>
      </a>
      <a href="https://en.wikipedia.org/wiki/Evan_You" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 hover:text-primary-600">
        <i class="fas fa-globe text-[11px]"></i>
        <span>Evan You · Wikipedia</span>
      </a>
    </div>
    <div class="mt-3 flex items-center gap-4">
      <a href="https://d3js.org/" target="_blank" class="inline-flex items-center gap-2 hover:opacity-80">
        <img src="https://d3js.org/logo.svg" alt="D3.js Logo" class="h-5 object-contain">
        <span class="text-xs text-slate-500 dark:text-slate-400">D3.js website</span>
      </a>
      <a href="https://vuejs.org/" target="_blank" class="inline-flex items-center gap-2 hover:opacity-80">
        <img src="https://vuejs.org/images/logo.png" alt="Vue.js Logo" class="h-5 object-contain">
        <span class="text-xs text-slate-500 dark:text-slate-400">Vue.js website</span>
      </a>
    </div>
  </div>

  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-white dark:bg-gray-800 border-4 border-purple-500 rounded-full animate-pulse"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-2xl text-slate-800">Now</span>
      <span class="font-bold text-purple-600">The AI coding era</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400">You no longer need to write V8-level JavaScript or Vue syntax by hand. A natural-language prompt is enough to draw on all of this history and generate research tools.</p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://baike.baidu.com/item/%E8%90%A8%E5%A7%86%C2%B7%E9%98%BF%E7%89%B9%E6%9B%BC" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Sam_Altman_TechCrunch_SF_2019_Day_2_Oct_3_%28cropped%29.jpg/330px-Sam_Altman_TechCrunch_SF_2019_Day_2_Oct_3_%28cropped%29.jpg" alt="Sam Altman" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>Sam Altman · Baidu Baike</span>
      </a>
      <a href="https://en.wikipedia.org/wiki/Sam_Altman" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 hover:text-purple-600">
        <i class="fas fa-globe text-[11px]"></i>
        <span>Wikipedia</span>
      </a>
    </div>
  </div>
</div>

### 1.2 Markdown vs. HTML: What's the Difference?

<div class="not-prose grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="glass-card p-6 rounded-xl flex flex-col h-full">
    <div class="mb-4">
      <span class="bg-slate-100 text-slate-600 dark:text-slate-400 px-2 py-1 rounded text-xs font-bold uppercase tracking-wider">Markdown</span>
      <div class="text-lg font-bold text-slate-900 dark:text-slate-100 mt-1">2004 minimalism</div>
    </div>
    <div class="flex-grow space-y-4 text-sm text-slate-600 dark:text-slate-400">
      <p><strong>You have seen it before</strong>: asterisks in <code>**key point**</code> and hashes in <code># Heading</code> are markup. It is the default format every AI model uses for text output.</p>
      <div class="bg-red-50 text-red-700 p-3 rounded text-xs border border-red-100">
        <strong>Limitation</strong>: it is "digital paper". Sortable tables, zoomable images and interactive buttons are all out of reach.
      </div>
    </div>
  </div>

  <div class="glass-card p-6 rounded-xl flex flex-col h-full border border-primary-100 shadow-lg shadow-primary-500/5">
    <div class="mb-4">
      <span class="bg-primary-100 text-primary-600 px-2 py-1 rounded text-xs font-bold uppercase tracking-wider">HTML</span>
      <div class="text-lg font-bold text-slate-900 dark:text-slate-100 mt-1">A full-featured digital container</div>
    </div>
    <div class="flex-grow space-y-4 text-sm text-slate-600 dark:text-slate-400">
      <p><strong>What it is</strong>: a combination of structure, presentation and behavior. AI can generate HTML easily, and the browser turns it straight into interactive software.</p>
      <div class="bg-green-50 text-green-800 p-3 rounded text-xs border border-green-100">
        <strong>Advantage</strong>: information moves from a flat page to something you can interact with, which suits how humans see.
      </div>
    </div>
  </div>
</div>

<div class="not-prose mt-6 p-4 bg-slate-800 text-slate-200 rounded-lg text-center text-sm font-medium">
  Takeaway: <span class="text-white">Markdown</span> is for talking to AI (input); <span class="text-white">HTML</span> is for receiving what AI produces (output).
</div>

## The Spectrum of Visualization Tools: Finding the Middle Ground

Research visualization has a whole spectrum of tools. Knowing where each one stops is the first step to choosing the right one.

### 2.1 Base layer: Markdown (the scratch pad)

<div class="not-prose relative pl-8 border-l-2 border-slate-200 dark:border-slate-700">
  <div class="absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-slate-300 border-2 border-white"></div>
  <p class="text-sm text-slate-500 dark:text-slate-400 mb-2">The format you see most often when chatting with ChatGPT, and the default output of today's AI.</p>
  <div class="flex flex-wrap gap-2 text-sm">
    <span class="px-2 py-1 bg-slate-100 text-slate-600 dark:text-slate-400 rounded">Plain text</span>
    <span class="px-2 py-1 bg-slate-100 text-slate-600 dark:text-slate-400 rounded">Simple formatting</span>
    <span class="px-2 py-1 bg-red-50 text-red-600 rounded">Limitation: static and linear</span>
  </div>
  <div class="mt-4 grid md:grid-cols-2 gap-4 text-xs">
    <div class="bg-slate-900 text-slate-100 rounded-lg p-3 font-mono">
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">Source (Markdown)</div>
      <pre><code># Introduction to immune checkpoint blockade

**PD-1 inhibitors** can reactivate
exhausted T cells.

- nivolumab
- pembrolizumab</code></pre>
    </div>
    <div class="bg-white dark:bg-gray-800 rounded-lg p-3 border border-slate-200 dark:border-slate-700 text-[13px] leading-relaxed">
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">Rendered (in a paper / web page)</div>
      <div class="text-sm font-bold text-slate-900 dark:text-slate-100 mb-1">Introduction to immune checkpoint blockade</div>
      <p class="mb-1"><strong>PD-1 inhibitors</strong> can reactivate exhausted T cells.</p>
      <ul class="list-disc pl-5 text-slate-600 dark:text-slate-400">
        <li>nivolumab</li>
        <li>pembrolizumab</li>
      </ul>
    </div>
  </div>
</div>

### 2.2 Rigor layer: Python / R (the printing press)

<div class="not-prose relative pl-8 border-l-2 border-slate-200 dark:border-slate-700">
  <div class="absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-slate-300 border-2 border-white"></div>
  <p class="text-sm text-slate-500 dark:text-slate-400 mb-2">The plotting tools most often used for journal figures (Matplotlib, ggplot2).</p>
  <div class="mb-2 text-sm text-slate-600 dark:text-slate-400 bg-slate-50 dark:bg-slate-900 p-2 rounded inline-block">
    <strong>Background</strong>: John Hunter (Matplotlib, 2003) / Hadley Wickham (ggplot2, 2005)
  </div>
  <div class="flex flex-wrap gap-2 text-sm mt-1">
    <span class="px-2 py-1 bg-slate-100 text-slate-600 dark:text-slate-400 rounded">Static, high resolution</span>
    <span class="px-2 py-1 bg-slate-100 text-slate-600 dark:text-slate-400 rounded">Precise control</span>
    <span class="px-2 py-1 bg-red-50 text-red-600 rounded">Limitation: heavy and slow</span>
  </div>
  <div class="mt-4 grid md:grid-cols-2 gap-4 text-xs">
    <div class="bg-slate-900 text-slate-100 rounded-lg p-3 font-mono overflow-x-auto">
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">Source (Python / Matplotlib)</div>
      <pre><code>import matplotlib.pyplot as plt

groups = ["CR", "PR", "SD", "PD"]
values = [12, 25, 18, 9]

plt.bar(groups, values, color="#3b82f6")
plt.ylabel("Patients")
plt.title("Response to PD-1 Blockade")
plt.tight_layout()
plt.show()</code></pre>
    </div>
    <div class="bg-white dark:bg-gray-800 rounded-lg p-3 border border-slate-200 dark:border-slate-700 text-[13px] leading-relaxed flex flex-col">
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">Rendered (static figure in a paper)</div>
      <div class="flex-1 flex items-center justify-center">
        <div class="w-full max-w-xs h-32 border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 rounded-lg flex items-end justify-around px-4 py-3">
          <div class="flex flex-col items-center text-[11px] text-slate-600 dark:text-slate-400">
            <div class="w-6 bg-blue-500 rounded-t h-16 mb-1"></div>
            <span>CR</span>
          </div>
          <div class="flex flex-col items-center text-[11px] text-slate-600 dark:text-slate-400">
            <div class="w-6 bg-blue-500 rounded-t h-24 mb-1"></div>
            <span>PR</span>
          </div>
          <div class="flex flex-col items-center text-[11px] text-slate-600 dark:text-slate-400">
            <div class="w-6 bg-blue-500 rounded-t h-14 mb-1"></div>
            <span>SD</span>
          </div>
          <div class="flex flex-col items-center text-[11px] text-slate-600 dark:text-slate-400">
            <div class="w-6 bg-blue-500 rounded-t h-8 mb-1"></div>
            <span>PD</span>
          </div>
        </div>
      </div>
      <p class="mt-2 text-[11px] text-slate-500 dark:text-slate-400 text-center">A static PNG / PDF embedded in the article.</p>
    </div>
  </div>
</div>

### 2.3 Core layer: HTML + JS (the dashboard)

<div class="not-prose relative pl-8 border-l-2 border-primary-500">
  <div class="absolute -left-[11px] top-0 w-5 h-5 rounded-full bg-primary-50 dark:bg-primary-900/30 border-4 border-primary-100 shadow-sm"></div>
  <p class="text-sm text-slate-500 dark:text-slate-400 mb-2">The focus of this course, and the often-overlooked "middle ground".</p>
  <div class="mb-2 text-sm text-slate-600 dark:text-slate-400 bg-primary-50 dark:bg-primary-900/30 p-2 rounded inline-block border border-primary-100">
    <strong>Background</strong>: Mike Bostock (D3.js, 2011) opened the era of "data-driven documents".
  </div>
  <ul class="list-none space-y-2 mt-2">
    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-slate-300">
      <i class="fas fa-chevron-down text-primary-500 text-xs"></i> <strong>Collapse</strong>: keep the main view clean.
    </li>
    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-slate-300">
      <i class="fas fa-filter text-primary-500 text-xs"></i> <strong>Filter</strong>: find the data you care about instantly.
    </li>
    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-slate-300">
      <i class="fas fa-mouse-pointer text-primary-500 text-xs"></i> <strong>Respond</strong>: show values on hover, zoom by box-selecting.
    </li>
  </ul>
  <p class="text-sm font-bold text-primary-700 mt-2">Why it matters: it is a container for thinking, and gives the best experience for exploratory data analysis (EDA).</p>
  <div class="mt-4 grid md:grid-cols-2 gap-4 text-xs">
    <div class="bg-slate-900 text-slate-100 rounded-lg p-3 font-mono overflow-x-auto">
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">Source (HTML + JS dashboard snippet)</div>
      <pre><code>&lt;div id="response-dashboard"&gt;
  &lt;select id="group-filter"&gt;
    &lt;option value="all"&gt;All patients&lt;/option&gt;
    &lt;option value="responder"&gt;Responders (CR+PR)&lt;/option&gt;
  &lt;/select&gt;
  &lt;div class="bar" data-type="CR"&gt;CR: 12&lt;/div&gt;
  &lt;div class="bar" data-type="PR"&gt;PR: 25&lt;/div&gt;
  &lt;div class="bar" data-type="SD"&gt;SD: 18&lt;/div&gt;
  &lt;div class="bar" data-type="PD"&gt;PD: 9&lt;/div&gt;
&lt;/div&gt;</code></pre>
    </div>
    <div class="bg-white dark:bg-gray-800 rounded-lg p-3 border border-slate-200 dark:border-slate-700 text-[13px] leading-relaxed">
      <div class="flex items-center justify-between">
        <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">Rendered (colourful interactive dashboard)</div>
        <div class="flex gap-2">
          <button class="px-2 py-1 text-[11px] rounded bg-gradient-to-r from-indigo-500 to-cyan-400 text-white shadow" onclick="renderDashboardDemo(true)">Refresh mock data</button>
          <select id="group-filter-demo" class="p-1.5 border border-slate-200 dark:border-slate-700 rounded text-[11px]" onchange="filterResponseBarsDemo()">
            <option value="all">All patients</option>
            <option value="responder">Responders</option>
          </select>
        </div>
      </div>
      <div id="response-dashboard-demo" class="mt-2 space-y-3">
        <div class="grid grid-cols-4 gap-2 h-28 items-end">
          <div class="flex flex-col items-center text-[11px] text-slate-600 dark:text-slate-400">
            <div class="w-full rounded-t response-bar-demo transition-all duration-500 shadow-sm" data-type="CR"></div>
            <span class="mt-1 font-semibold text-slate-700 dark:text-slate-300">CR</span>
          </div>
          <div class="flex flex-col items-center text-[11px] text-slate-600 dark:text-slate-400">
            <div class="w-full rounded-t response-bar-demo transition-all duration-500 shadow-sm" data-type="PR"></div>
            <span class="mt-1 font-semibold text-slate-700 dark:text-slate-300">PR</span>
          </div>
          <div class="flex flex-col items-center text-[11px] text-slate-600 dark:text-slate-400">
            <div class="w-full rounded-t response-bar-demo transition-all duration-500 shadow-sm" data-type="SD"></div>
            <span class="mt-1 text-slate-500 dark:text-slate-400">SD</span>
          </div>
          <div class="flex flex-col items-center text-[11px] text-slate-600 dark:text-slate-400">
            <div class="w-full rounded-t response-bar-demo transition-all duration-500 shadow-sm" data-type="PD"></div>
            <span class="mt-1 text-slate-500 dark:text-slate-400">PD</span>
          </div>
        </div>
        <div class="text-[11px] text-slate-500 dark:text-slate-400 flex items-center gap-2">
          <span class="inline-flex items-center gap-1 text-indigo-600"><i class="fas fa-magic text-xs"></i> Gradient highlight</span>
          <span class="inline-flex items-center gap-1 text-emerald-600"><i class="fas fa-filter text-xs"></i> Filter to highlight CR/PR</span>
        </div>
      </div>
    </div>
  </div>
</div>

## In Practice: Interactive Reconstruction Across the Whole Workflow

Theory has to serve practice. Below are 5 scenarios you can use right away, each with **steps** and a **prompt you can copy directly**.

<div class="not-prose space-y-16">
### 3.1 Rethinking reading: from linear text to an interactive app

<div class="glass-card p-8 rounded-2xl relative overflow-hidden">
<div class="absolute top-0 right-0 w-24 h-24 bg-blue-50 rounded-bl-full -z-10"></div>

<div class="bg-primary-50 dark:bg-primary-900/30 rounded-lg p-5 mb-6 text-sm text-primary-800 leading-relaxed">
<strong>The idea</strong>: most papers we read are PDFs with tight line spacing and crowded pages. Figures often land on a different page, so we keep flipping back and forth. It is hard on the eyes and hard on concentration.<br>
Rather than accept the layout as given, <strong>take the paper apart and reassemble it</strong>: if there is a web version, right-click and choose <strong>View Page Source</strong>, hand that HTML to an AI, and ask it to rebuild the content as an HTML reader that suits the way you read.<br>
The source already contains the image URLs, heading structure and so on, so one conversion gives you a reading page with <strong>larger type, more white space, and figures next to the text that discusses them</strong>.<br>
Even without the web source, or if you simply prefer copying text from the PDF, you can ask the AI to re-lay it out as "key points as a list + wider line spacing + important sentences in bold". Lower information density and clearer emphasis make long papers much more comfortable and faster to read.
</div>

<div class="mb-6 text-xs text-slate-500 dark:text-slate-400 flex flex-wrap gap-3 items-center">
<span class="font-semibold text-slate-600 dark:text-slate-400 flex items-center gap-1"><i class="fas fa-compass text-primary-500"></i> State-of-the-art examples:</span>
<a href="https://distill.pub/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-primary-100 hover:bg-primary-50 dark:bg-primary-900/30 hover:text-primary-700">
<i class="fas fa-file-alt text-[10px]"></i><span>Distill.pub (interactive papers)</span>
</a>
<a href="https://observablehq.com/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-primary-100 hover:bg-primary-50 dark:bg-primary-900/30 hover:text-primary-700">
<i class="fas fa-chart-line text-[10px]"></i><span>Observable (interactive data notebooks)</span>
</a>
</div>

<div class="grid md:grid-cols-2 gap-8 mb-8">
<div>
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide">Steps</h4>
<ol class="space-y-3 text-sm text-slate-600 dark:text-slate-400">
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">1</span>
<span>Open the paper's web (HTML) version, right-click on an empty area and choose <strong>View Page Source</strong>.</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">2</span>
<span>Press <code>Ctrl+A</code> to select all and <code>Ctrl+C</code> to copy.</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">3</span>
<span>Open Gemini/ChatGPT and enter the prompt on the right.</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">4</span>
<span>When the AI replies "please paste the code", paste the source you copied.</span>
</li>
</ol>
</div>
<div class="flex flex-col">
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide flex justify-between items-center">
AI Prompt (copy as is)
<button class="text-primary-600 hover:text-primary-800 text-xs font-normal" onclick="copyToClipboard('prompt-3-1')"><i class="fas fa-copy mr-1"></i> Copy</button>
</h4>
<div class="bg-slate-800 p-4 rounded-lg text-xs font-mono text-green-400 overflow-x-auto flex-grow leading-relaxed" id="prompt-3-1">
You are a senior front-end engineer and a biomedical expert.
Task: rebuild the paper HTML source I provide as a single-file HTML page.
Requirements:
1. **Layout**: use Tailwind CSS, a minimal academic style, large type and an easy-on-the-eyes background colour.
2. **Interactive contents**: generate a floating table of contents (TOC) on the left; clicking an entry jumps to it.
3. **Figures beside text**: find the `&lt;img&gt;` tags in the source and keep the original image links. Move each figure next to the place in the text that cites it (e.g. "Fig 1"), so text and figures sit side by side.
4. **Term explanations**: identify 5 key medical abbreviations in the text (e.g. tumour markers, gene names) and add a hover tooltip explaining each one.
First reply "Ready, please paste the HTML source", and then I will send the code.
</div>
</div>
</div>

<!-- Live Demo 3.1 -->
<div class="mt-6 demo-browser-mockup bg-white dark:bg-gray-800 shadow-lg border border-slate-200 dark:border-slate-700">
<div class="p-6 border-b border-slate-100">
<div class="flex items-center gap-2 text-xs text-slate-400 font-bold uppercase tracking-widest mb-2">
<span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span> Preview
</div>
<h4 class="font-serif text-xl text-slate-800 font-bold mb-2">Immune checkpoint blockade (example)</h4>
<p class="font-serif text-lg leading-relaxed text-slate-600 dark:text-slate-400">
Recent studies show that <span class="cursor-help border-b-2 border-dotted border-primary-500 relative group text-primary-700 font-medium">
PD-1
<span class="invisible group-hover:visible opacity-0 group-hover:opacity-100 transition-all duration-200 absolute bottom-full left-1/2 -translate-x-1/2 bg-slate-800 text-white text-xs p-3 rounded-lg w-64 mb-2 z-10 shadow-xl text-left leading-snug">
<strong>Programmed cell death protein 1</strong><br>
Tumour cells evade attack by the immune system by binding PD-1 on T cells.
<svg class="absolute text-slate-800 h-2 w-full left-0 top-full" x="0px" y="0px" viewBox="0 0 255 255"><polygon class="fill-current" points="0,0 127.5,127.5 255,0"/></svg>
</span>
</span> inhibitors can reactivate exhausted T cells and markedly improve outcomes in metastatic melanoma. Click 
<button onclick="toggleModal()" class="text-primary-600 font-bold hover:underline bg-primary-50 dark:bg-primary-900/30 px-1 rounded">Figure 1</button> for a schematic.
</p>
</div>

<!-- Fake Modal -->
<div id="fig1-modal" class="hidden absolute inset-0 bg-white dark:bg-gray-800/95 backdrop-blur flex items-center justify-center z-20 p-4 transition-opacity">
<div class="text-center max-w-sm">
<div class="bg-slate-100 rounded-lg p-8 mb-4 border-2 border-dashed border-slate-300">
<i class="fas fa-image text-4xl text-slate-300 mb-2"></i>
<p class="text-slate-400 font-bold">Schematic placeholder</p>
</div>
<p class="text-sm text-slate-600 dark:text-slate-400 font-medium">Figure 1: Blocking PD-1 signalling restores T-cell function in the tumour microenvironment.</p>
<button onclick="toggleModal()" class="mt-4 px-4 py-2 bg-slate-800 text-white rounded-lg text-sm hover:bg-slate-700 transition-colors">Close</button>
</div>
</div>
</div>

<!-- Bonus: Gemini Tool -->
<div class="glass-card p-8 rounded-2xl mt-8 border-l-4 border-purple-500 relative overflow-hidden">
<div class="absolute -right-10 -top-10 w-40 h-40 bg-purple-100 rounded-full blur-3xl -z-10"></div>
<h3 class="text-xl font-bold text-slate-900 dark:text-slate-100 mb-2 flex items-center gap-2">
<i class="fas fa-magic text-purple-500"></i>
✨ Bonus: an academic explainer powered by Gemini
</h3>
<p class="text-sm text-slate-600 dark:text-slate-400 mb-4">
Not sure what a passage means? Paste it here and let Gemini write a plain-language explanation for you.
</p>
<textarea id="gemini-input" class="w-full p-4 rounded-xl bg-white dark:bg-gray-800/50 border border-slate-200 dark:border-slate-700 text-sm font-serif mb-4 focus:ring-2 focus:ring-purple-500 outline-none transition-all" rows="4" placeholder="Paste a dense academic abstract here..."></textarea>
<button onclick="callGemini()" class="px-6 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-lg font-medium transition-colors flex items-center gap-2 shadow-lg shadow-purple-500/20">
<i class="fas fa-sparkles"></i> Explain in plain terms
</button>
<div id="gemini-output" class="mt-6 hidden">
<div class="p-4 bg-purple-50 rounded-xl border border-purple-100 text-slate-700 dark:text-slate-300 text-sm leading-relaxed"></div>
</div>
<div id="gemini-loading" class="mt-6 hidden">
<div class="flex items-center gap-2 text-purple-500 text-sm font-medium animate-pulse">
<i class="fas fa-circle-notch fa-spin"></i> Working through the logic...
</div>
</div>
</div>

<!-- 3.1 Choosing a prompt and its structure -->
<div class="mt-8 grid md:grid-cols-3 gap-4 text-xs text-slate-600 dark:text-slate-400">
<div class="bg-white dark:bg-gray-800/80 border border-slate-100 rounded-xl p-4">
<h4 class="font-bold text-slate-800 mb-2 flex items-center gap-2 text-sm">
<span class="w-1.5 h-4 bg-primary-50 dark:bg-primary-900/300 rounded-full"></span>
Which prompt for which task?
</h4>
<ul class="space-y-1.5">
<li>· <span class="font-semibold text-slate-800">Basic layout</span> (re-laying out one paper, a first try): use "1. Paper-to-web-page prompt (basic)".</li>
<li>· <span class="font-semibold text-slate-800">Deeper rebuild</span> (TOC, term tooltips, figures beside text): use "2. Paper rebuild, improved (main one)" or "13. Paper rebuild, revised".</li>
<li>· <span class="font-semibold text-slate-800">Popular-science / WeChat article rewrite</span>: use "23. Paper rebuild (WeChat article)" or "24. AI article rebuild".</li>
<li>· <span class="font-semibold text-slate-800">Gemini-specific version</span>: use "22. Paper rebuild (Gemini 3 version)".</li>
</ul>
</div>

<div class="bg-white dark:bg-gray-800/80 border border-slate-100 rounded-xl p-4">
<h4 class="font-bold text-slate-800 mb-2 flex items-center gap-2 text-sm">
<span class="w-1.5 h-4 bg-emerald-500 rounded-full"></span>
Jump straight to the prompts in Notion
</h4>
<p class="mb-2">Each link opens the corresponding entry in a new tab, ready to copy and adapt (the prompts themselves are in Chinese):</p>
<div class="space-y-1.5">
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-80a8-9123-eea881d6e654" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
<i class="fas fa-link text-[10px]"></i>
<span>1. Basic · paper to web page</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-80f5-90ba-d7ff952bd71c" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>2. Paper rebuild, improved (main one)</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2a66ff12-2f6b-8051-be51-da86b0e4b598" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>13. Paper rebuild, revised</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2b36ff12-2f6b-802f-87c3-e7fd0f3e3909" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>23. Paper rebuild (WeChat article)</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2b76ff12-2f6b-809f-a21e-ec7922db6063" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>24. AI article rebuild</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2b26ff12-2f6b-8095-937a-e97cff0bd133" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>22. Paper rebuild (Gemini 3 version)</span>
</a>
</div>
</div>

<div class="bg-slate-900 text-slate-50 rounded-xl p-4">
<h4 class="font-bold mb-2 flex items-center gap-2 text-sm">
<span class="w-1.5 h-4 bg-amber-400 rounded-full"></span>
Anatomy of a prompt: what paper-rebuild prompts share
</h4>
<ol class="space-y-1.5 list-decimal list-inside text-[11px] leading-relaxed">
<li><span class="font-semibold text-white">System role</span>: e.g. "front-end engineer + medical expert", so the AI understands both layout and the domain.</li>
<li><span class="font-semibold text-white">Input description</span>: tell the AI whether it will receive HTML source, Markdown, or plain paragraphs.</li>
<li><span class="font-semibold text-white">Output structure</span>: state which modules you need, such as "single-file HTML", "TOC", "figures beside text", "term tooltips".</li>
<li><span class="font-semibold text-white">Constraints and safety</span>: stress that it must not invent data or change what the figures mean; it only re-lays out and adds explanations.</li>
<li><span class="font-semibold text-white">Interaction and style</span>: specify font, colours, white space and mobile support, so you end up with a reusable "visual template".</li>
</ol>
</div>
</div>
</div>

### 3.2 Rethinking presentations: from static PPT to interactive slides

<div class="glass-card p-8 rounded-2xl relative overflow-hidden">
<div class="absolute top-0 right-0 w-24 h-24 bg-orange-50 rounded-bl-full -z-10"></div>

<div class="bg-orange-50 rounded-lg p-5 mb-6 text-sm text-orange-800 leading-relaxed">
<strong>The idea</strong>: traditional PPT talks come with familiar problems: large files, version chaos (final_v3_real_final.pptx), animations that do not survive a change of platform, and no easy way to embed interactive charts.<br>
HTML slides built on <strong>Reveal.js</strong> are simply a web page: a single <code>index.html</code> plays in any modern browser without special software, and is easier to keep and share long-term through Git or cloud storage.<br>
In this mode you only give the AI an <strong>outline + the key content blocks</strong> in words (e.g. "code example", "interactive results chart"), and it writes a complete deck with transitions, code highlighting and Plotly chart placeholders.<br>
For a journal club or lab meeting, this frees you from the cosmetic work of fixing slides. You can spend the time on the logic and on choosing the key figures, and still get a more modern presentation that works well for sharing online.
</div>

<div class="grid md:grid-cols-2 gap-8 mb-8">
<div>
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide">Steps</h4>
<ol class="space-y-3 text-sm text-slate-600 dark:text-slate-400">
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">1</span>
<span>Prepare your talk outline (a simple Markdown list).</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">2</span>
<span>Send the prompt on the right to the AI.</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">3</span>
<span>Save the generated code as <code>presentation.html</code>.</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">4</span>
<span>Double-click to open it and press the space bar to advance.</span>
</li>
</ol>
</div>
<div class="flex flex-col">
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide flex justify-between items-center">
AI Prompt (copy as is)
<button class="text-primary-600 hover:text-primary-800 text-xs font-normal" onclick="copyToClipboard('prompt-3-2')"><i class="fas fa-copy mr-1"></i> Copy</button>
</h4>
<div class="bg-slate-800 p-4 rounded-lg text-xs font-mono text-green-400 overflow-x-auto flex-grow leading-relaxed" id="prompt-3-2">
I need to give an academic talk (journal club).
Using the Reveal.js framework, generate a single-file HTML presentation for me.
Topic: [fill in the topic, e.g. applications of single-cell sequencing in lung cancer]
Outline:
1. [Background: ...]
2. [Methods: ...]
3. [Results: ...]
Requirements:
- Use the 'white' theme.
- In the "Methods" section, embed a Python code example with syntax highlighting enabled.
- In the "Results" section, reserve a spot for an interactive bar chart (using Plotly.js).
- Load all JS/CSS from a CDN so nothing needs to be downloaded locally.
</div>
</div>
</div>

<div class="mt-4 mb-10 text-xs text-slate-500 dark:text-slate-400 flex flex-wrap gap-3 items-center">
<span class="font-semibold text-slate-600 dark:text-slate-400 flex items-center gap-1"><i class="fas fa-compass text-primary-500"></i> State-of-the-art tools:</span>
<a href="https://revealjs.com/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fas fa-laptop text-[10px]"></i><span>Reveal.js documentation</span>
</a>
<a href="https://marp.app/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fas fa-sliders-h text-[10px]"></i><span>Marp (Markdown slides)</span>
</a>
</div>

<!-- Live Demo 3.2 -->
<div class="mt-6 aspect-video bg-slate-900 rounded-xl relative overflow-hidden shadow-2xl border border-slate-700 group">
<div class="absolute top-4 left-4 text-xs font-mono text-slate-500 dark:text-slate-400">index.html (Reveal.js Mockup)</div>

<div id="slide-container" class="w-full h-full flex items-center justify-center p-12 text-center transition-all duration-500 transform">
<!-- Slide Content -->
</div>

<div class="absolute bottom-4 right-4 flex gap-2 opacity-50 group-hover:opacity-100 transition-opacity">
<button onclick="changeSlide(-1)" class="w-8 h-8 bg-white dark:bg-gray-800/10 hover:bg-white dark:bg-gray-800/20 rounded text-white flex items-center justify-center backdrop-blur"><i class="fas fa-chevron-left"></i></button>
<button onclick="changeSlide(1)" class="w-8 h-8 bg-white dark:bg-gray-800/10 hover:bg-white dark:bg-gray-800/20 rounded text-white flex items-center justify-center backdrop-blur"><i class="fas fa-chevron-right"></i></button>
</div>

</div>
</div>

<!-- Practice: Code Reading Prompts -->
<div class="glass-card p-6 md:p-8 rounded-2xl relative overflow-hidden border border-slate-100">
<div class="absolute -right-8 -top-8 w-32 h-32 bg-slate-900/5 rounded-full blur-3xl -z-10"></div>
<h3 class="text-lg font-bold text-slate-900 dark:text-slate-100 mb-4 flex items-center gap-2">
<i class="fas fa-code text-slate-700 dark:text-slate-300"></i>
Exercise: have AI help you read code
</h3>
<div class="grid md:grid-cols-2 gap-6 text-sm text-slate-600 dark:text-slate-400">
<div class="space-y-3">
<p>These notes already include several small HTML + JS apps (the Reveal slides, the GCS calculator and so on). I suggest you <strong>work backwards from these examples</strong>: use a dedicated code-reading prompt and ask the AI to turn the code into a human-friendly tutorial.</p>
<ol class="space-y-2 text-xs md:text-sm">
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-[11px]">1</span>
<span>Copy a piece of front-end code from these notes or your own project (a component or a small tool both work).</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-[11px]">2</span>
<span>In your AI tool, send the code-reading prompt first and wait for it to reply "please paste the code".</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-[11px]">3</span>
<span>Paste the code and ask the AI to explain it along three lines (module structure / data flow / interaction logic) and to suggest changes you can make directly.</span>
</li>
</ol>
</div>
<div class="space-y-3 text-xs md:text-sm">
<div>
<h4 class="font-bold text-slate-800 mb-2 text-sm flex items-center gap-2">
<span class="w-1.5 h-4 bg-sky-500 rounded-full"></span>
Recommended code-related prompts
</h4>
<div class="space-y-1.5">
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-805e-804a-eb6c5d2d74af" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-900 text-slate-50 hover:bg-slate-800">
<i class="fas fa-book-open text-[10px]"></i>
<span>7. Code reading (new version)</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-8040-9c27-efb436a50a4a" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-book-open text-[10px]"></i>
<span>4. Code explanation prompt</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-80cf-94ec-caaa3a28bb24" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-robot text-[10px]"></i>
<span>3. AI research engineer coding prompt</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2786ff12-2f6b-805f-8234-e85c775fdd78" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-laptop-code text-[10px]"></i>
<span>12. Front-end engineer</span>
</a>
</div>
</div>
<p class="text-[11px] text-slate-500 dark:text-slate-400 leading-relaxed">Tip: use a code-reading prompt first to understand an existing demo, then use the "front-end engineer / AI research engineer" prompt to have the AI build a small tool of your own from scratch (a new scoring scale, an experiment logger, and so on).</p>
</div>
</div>
</div>

### 3.3 Rethinking concepts: from static diagrams to living models

<div class="glass-card p-8 rounded-2xl relative overflow-hidden">
<div class="absolute top-0 right-0 w-24 h-24 bg-emerald-50 rounded-bl-full -z-10"></div>

<div class="bg-emerald-50 rounded-lg p-5 mb-6 text-sm text-emerald-800 leading-relaxed">
<strong>The idea</strong>: research training constantly asks us to draw flowcharts, signalling pathways or diagnostic decision trees. Drawing them by hand or in PowerPoint is slow, and when the protocol changes you more or less start over.<br>
<strong>Mermaid.js</strong> lets you "draw with text": you describe the nodes and arrows in something close to natural language (what points to what, where a branch happens), the AI writes standard Mermaid code, and the browser renders it as a vector diagram.<br>
The benefit is that the diagram's source of truth is no longer the picture but the text logic behind it. When your protocol changes, you edit a few lines and the diagram updates itself, with no manual alignment or layout.<br>
For complex concepts (multi-step signal transduction, clinical stratification pathways and so on), this "text as model" approach is especially good for quick iteration and discussion in lab meetings or class.
</div>

<div class="mb-6 text-xs text-slate-500 dark:text-slate-400 flex flex-wrap gap-3 items-center">
<span class="font-semibold text-slate-600 dark:text-slate-400 flex items-center gap-1"><i class="fas fa-compass text-emerald-500"></i> State-of-the-art resources:</span>
<a href="https://mermaid.js.org/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-emerald-100 hover:bg-emerald-50 hover:text-emerald-700">
<i class="fas fa-project-diagram text-[10px]"></i><span>Mermaid.js documentation</span>
</a>
<a href="https://mermaid.live/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-emerald-100 hover:bg-emerald-50 hover:text-emerald-700">
<i class="fas fa-pen-nib text-[10px]"></i><span>Mermaid Live Editor</span>
</a>
</div>

<div class="grid md:grid-cols-2 gap-8 mb-8">
<div>
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide">Steps</h4>
<ol class="space-y-3 text-sm text-slate-600 dark:text-slate-400">
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">1</span>
<span>Work out the logic you want to show (a signalling pathway, a diagnostic workflow).</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">2</span>
<span>Send the prompt to the AI.</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">3</span>
<span>The AI returns a piece of HTML that contains Mermaid code.</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">4</span>
<span>Open the HTML and the diagram draws itself. To change the logic, edit the text; no redrawing.</span>
</li>
</ol>
</div>
<div class="flex flex-col">
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide flex justify-between items-center">
AI Prompt (copy as is)
<button class="text-primary-600 hover:text-primary-800 text-xs font-normal" onclick="copyToClipboard('prompt-3-3')"><i class="fas fa-copy mr-1"></i> Copy</button>
</h4>
<div class="bg-slate-800 p-4 rounded-lg text-xs font-mono text-green-400 overflow-x-auto flex-grow leading-relaxed" id="prompt-3-3">
Please generate a single-file HTML page that uses Mermaid.js to draw a flowchart.
Logic: [Wet Lab: sample collection -> RNA extraction -> QC -> library prep and sequencing] -> [Dry Lab: alignment -> differential expression analysis -> pathway enrichment]
Requirements:
1. Load mermaid.min.js from a CDN.
2. Make the chart look clean; use rounded rectangles for nodes.
3. Separate 'Wet Lab' and 'Dry Lab' into two subgraphs and fill them with different colours.
</div>
</div>
</div>

<!-- Live Demo 3.3 (Mermaid) -->
<div class="mt-6 bg-white dark:bg-gray-800 rounded-xl shadow-lg border border-slate-200 dark:border-slate-700 overflow-hidden mb-8">
<div class="bg-slate-50 dark:bg-slate-900 p-4 border-b border-slate-200 dark:border-slate-700 flex justify-between items-center">
<div class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Mermaid.js Protocol Demo</div>
<button onclick="renderMermaid()" class="text-xs bg-emerald-100 text-emerald-700 px-2 py-1 rounded font-bold hover:bg-emerald-200 transition-colors">
<i class="fas fa-sync-alt mr-1"></i> Render
</button>
</div>
<div class="grid md:grid-cols-2">
<div class="p-0 border-r border-slate-200 dark:border-slate-700 bg-slate-800">
<textarea id="mermaid-input" class="w-full h-64 p-4 bg-slate-800 text-green-400 font-mono text-xs focus:outline-none resize-none" spellcheck="false">
graph TD
subgraph Wet_Lab ["🧪 Wet lab: sample preparation"]
A[Sample collection] --> B[Cell lysis]
B --> C[RNA extraction]
C --> D{"QC: RIN > 7 ?"}
D -- No --> E[Discard sample]
D -- Yes --> F[Library prep]
F --> G["Sequencing (Illumina)"]
end

subgraph Dry_Lab ["💻 Dry lab: bioinformatics"]
G --> H["Raw reads (FASTQ)"]
H --> I["Quality check (FastQC)"]
I --> J["Alignment (STAR/HISAT2)"]
J --> K[Count matrix]
K --> L["Differential expression (DESeq2)"]
end

style Wet_Lab fill:#e0f2fe,stroke:#3b82f6
style Dry_Lab fill:#f3e8ff,stroke:#a855f7
</textarea>
</div>
<div class="p-4 bg-white dark:bg-gray-800 flex items-center justify-center overflow-auto" id="mermaid-output">
    <div class="text-sm text-slate-400">Graph will render here...</div>
</div>
</div>
</div>

<!-- Live Demo 3.3 (CSS Animation) -->
<div class="mt-6 bg-slate-50 dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-700 flex flex-col items-center justify-center overflow-hidden relative h-48">
<div class="absolute top-2 left-2 text-xs font-mono text-slate-400">CSS Animation: Receptor Binding</div>

<!-- Membrane -->
<div class="absolute bottom-0 w-full h-4 bg-slate-300 border-t border-slate-400"></div>

<!-- Receptor -->
<div class="absolute bottom-4 left-1/2 -translate-x-1/2 w-12 h-16 border-2 border-slate-400 rounded-t-full flex items-center justify-center bg-white dark:bg-gray-800 z-10">
<div class="w-8 h-8 border-b-2 border-slate-300 rounded-full"></div>
</div>

<!-- Ligand -->
<div id="ligand" class="w-6 h-6 bg-emerald-500 rounded-full shadow-lg absolute top-10 left-1/2 -translate-x-1/2 z-20 cursor-pointer transition-all duration-1000 ease-in-out flex items-center justify-center text-white text-xs font-bold hover:scale-110">
L
</div>

<!-- Signal -->
<div id="signal" class="w-2 h-2 bg-yellow-400 rounded-full absolute bottom-6 left-1/2 -translate-x-1/2 opacity-0 transition-all duration-500"></div>

<div class="absolute top-4 right-4">
<button onclick="activateSignal()" class="bg-white dark:bg-gray-800 border border-slate-200 dark:border-slate-700 px-3 py-1 rounded text-xs font-bold hover:bg-slate-50 dark:bg-slate-900 shadow-sm text-slate-600 dark:text-slate-400">
<i class="fas fa-play mr-1"></i> Trigger
</button>
</div>
</div>
</div>

### 3.4 Rethinking logic: from passive lookup to tools built for you

<div class="glass-card p-8 rounded-2xl relative overflow-hidden border border-slate-100 shadow-xl shadow-slate-200/40">
<div class="absolute top-0 right-0 w-24 h-24 bg-indigo-50 rounded-bl-full -z-10"></div>

<div class="bg-indigo-50 rounded-lg p-5 mb-6 text-sm text-indigo-800 leading-relaxed">
<strong>The idea</strong>: in clinical work and research we make "if... then..." judgements every day: scoring scales (GCS, CHA<sub>2</sub>DS<sub>2</sub>-VASc), staging and grading, dose adjustments. The usual approach is either a paper form or rules memorised by rote, which is error-prone and hard to share across a team.<br>
With a reactive framework such as <strong>Vue.js</strong>, we can have the AI turn these rules into small tools: change an input and the score and risk message update immediately; when the total crosses a threshold, the background turns red and a warning appears.<br>
More importantly, each of these tools is a <strong>single HTML file</strong>. You can save it offline on a phone or tablet and open it on the ward, in clinic or at a meeting. When a rule changes, you edit the logic in one place and everyone gets the same version of the decision support.<br>
Over time, this lets each clinician and researcher build up a small toolkit specific to their own project or field, rather than a pile of scattered screenshots and notes.
</div>

<div class="mb-6 text-xs text-slate-500 dark:text-slate-400 flex flex-wrap gap-3 items-center">
<span class="font-semibold text-slate-600 dark:text-slate-400 flex items-center gap-1"><i class="fas fa-compass text-indigo-500"></i> State-of-the-art ecosystem:</span>
<a href="https://vuejs.org/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fab fa-vuejs text-[10px]"></i><span>Vue.js documentation</span>
</a>
<a href="https://vuetifyjs.com/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fas fa-layer-group text-[10px]"></i><span>Vuetify (Material component library)</span>
</a>
<a href="https://mdcalc.com/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fas fa-stethoscope text-[10px]"></i><span>MDCalc (reference for clinical scores)</span>
</a>
</div>

<div class="grid md:grid-cols-2 gap-8 mb-8">
<div>
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide">Steps</h4>
<ol class="space-y-3 text-sm text-slate-600 dark:text-slate-400">
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">1</span>
<span>Pin down your calculation logic (e.g. A+B=C; if C>10, raise an alert).</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">2</span>
<span>Send the prompt to the AI.</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">3</span>
<span>The AI generates a single HTML file containing the calculation logic.</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">4</span>
<span>Save it to your phone or computer and use it offline whenever you need.</span>
</li>
</ol>
</div>
<div class="flex flex-col">
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide flex justify-between items-center">
AI Prompt (copy as is)
<button class="text-primary-600 hover:text-primary-800 text-xs font-normal" onclick="copyToClipboard('prompt-3-4')"><i class="fas fa-copy mr-1"></i> Copy</button>
</h4>
<div class="bg-slate-800 p-4 rounded-lg text-xs font-mono text-green-400 overflow-x-auto flex-grow leading-relaxed" id="prompt-3-4">
You are a senior front-end engineer. Please build me a small single-file HTML app.
Function: a GCS (Glasgow Coma Scale) calculator.
Logic:
- Eye opening (4 points), verbal response (5 points), motor response (6 points).
- Total = sum of the three.
Interface requirements:
- Use Vue.js (CDN) for the reactive logic.
- iOS-like style with large buttons, suitable for touch screens.
- Visual feedback: when the total is <= 8, turn the result area red and show the text "Note: intubation required".
</div>
</div>
</div>

<!-- Live Demo 3.4 -->
<div class="mt-8 max-w-xs mx-auto bg-white dark:bg-gray-800 rounded-3xl shadow-2xl border border-slate-100 overflow-hidden transform transition-transform hover:scale-105">
<!-- Header -->
<div class="bg-slate-50 dark:bg-slate-900 p-4 border-b border-slate-100 flex justify-between items-center">
<div class="text-xs font-bold text-slate-400">9:41</div>
<div class="text-sm font-bold text-slate-800">GCS Calculator</div>
<div class="flex gap-1">
<div class="w-4 h-2 bg-slate-300 rounded-sm"></div>
<div class="w-1 h-2 bg-slate-300 rounded-sm"></div>
</div>
</div>

<!-- App Body -->
<div class="p-5 space-y-4">
<div>
<label class="text-xs font-bold text-slate-400 uppercase mb-1 block">Eye opening</label>
<select id="eye" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-sm outline-none focus:border-indigo-500" onchange="calcGCS()">
<option value="4">4 - Spontaneous</option>
<option value="3">3 - To voice</option>
<option value="2">2 - To pain</option>
<option value="1">1 - None</option>
</select>
</div>
<div>
<label class="text-xs font-bold text-slate-400 uppercase mb-1 block">Verbal response</label>
<select id="verbal" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-sm outline-none focus:border-indigo-500" onchange="calcGCS()">
<option value="5">5 - Oriented</option>
<option value="4">4 - Confused</option>
<option value="3">3 - Inappropriate words</option>
<option value="2">2 - Incomprehensible sounds</option>
<option value="1">1 - None</option>
</select>
</div>
<div>
<label class="text-xs font-bold text-slate-400 uppercase mb-1 block">Motor response</label>
<select id="motor" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-sm outline-none focus:border-indigo-500" onchange="calcGCS()">
<option value="6">6 - Obeys commands</option>
<option value="5">5 - Localises pain</option>
<option value="4">4 - Withdraws</option>
<option value="3">3 - Abnormal flexion</option>
<option value="2">2 - Extension</option>
<option value="1">1 - None</option>
</select>
</div>

<!-- Result -->
<div id="gcs-result-box" class="mt-6 p-4 rounded-xl bg-emerald-100 text-emerald-900 transition-all duration-300">
<div class="text-center">
<span class="text-xs font-bold opacity-60 uppercase">Total</span>
<div class="text-4xl font-bold my-1" id="gcs-score">15</div>
<div class="text-xs font-bold" id="gcs-status">Normal</div>
</div>
</div>
</div>
</div>
</div>

### 3.5 Rethinking knowledge: from textbooks to a multi-step flashcard pipeline

<div class="glass-card p-8 rounded-2xl relative overflow-hidden border border-emerald-100 shadow-xl shadow-emerald-100/40">
<div class="absolute top-0 right-0 w-24 h-24 bg-emerald-50 rounded-bl-full -z-10"></div>

<div class="grid md:grid-cols-2 gap-8 items-start">
<div class="space-y-4 text-sm text-slate-600 dark:text-slate-400">
<div class="bg-emerald-50 rounded-lg p-5 leading-relaxed">
<strong>The idea</strong>: rather than rereading a thick textbook from the start again and again, break the knowledge into self-contained cards that you can review and track. With a set of prompts that hand off to one another, we can build a pipeline:<br>
<span class="font-mono text-emerald-700 text-xs md:text-sm">Book images / PDF → Markdown text → structured knowledge extraction → ANKI / USMLE flashcards</span><br>
Each step is handled by its own system prompt, which cuts out mechanical repetition while keeping as much of the original's rigour as possible.
</div>
<h4 class="font-bold text-slate-800 text-sm uppercase tracking-wide">Steps (suggested workflow)</h4>
<ol class="space-y-2 text-xs md:text-sm">
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-[11px]">1</span>
<span>Use <strong>20. Book images to Markdown</strong> to turn scanned textbook pages or question-bank screenshots into clean Markdown.</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-[11px]">2</span>
<span>Use a <strong>paper-rebuild prompt</strong> (e.g. "2. Paper rebuild, improved", "13. Paper rebuild, revised") to organise the structure: extract the section hierarchy and mark key points and frequently tested topics.</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-[11px]">3</span>
<span>Pass the organised content to the <strong>USMLE / ANKI prompts</strong> (5 / 6 / 8 / 21 / 17-19) to generate layered, self-contained cards as JSON or as text you can import directly.</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-[11px]">4</span>
<span>Use <strong>10. USMLE tutor</strong> or another tutor-style prompt to quiz you on the cards regularly: weekly review plans and mock oral exam questions.</span>
</li>
</ol>
</div>

<div class="space-y-4 text-xs md:text-sm">
<div>
<h4 class="font-bold text-slate-800 mb-2 text-sm flex items-center gap-2">
<span class="w-1.5 h-4 bg-emerald-500 rounded-full"></span>
Recommended prompt set (click to open)
</h4>
<div class="space-y-1.5">
<a href="https://rune-gem-5ee.notion.site/2aa6ff12-2f6b-80ec-9102-fcd34f7a01eb" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-emerald-50 text-emerald-800 hover:bg-emerald-100">
<i class="fas fa-image text-[10px]"></i>
<span>20. Book images to Markdown</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-80f5-90ba-d7ff952bd71c" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-file-alt text-[10px]"></i>
<span>2. Paper rebuild, improved (main one)</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2a36ff12-2f6b-800d-a8c3-ca88e40f0ba3" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-sitemap text-[10px]"></i>
<span>17-19. ANKI refinement series</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2ab6ff12-2f6b-80a1-bed8-fd6e2b323d3d" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-900 text-slate-50 hover:bg-slate-800">
<i class="fas fa-clone text-[10px]"></i>
<span>21. ANKI_USMLE essentials (in use)</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2786ff12-2f6b-802a-a819-fbe5bd3da611" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-microchip text-[10px]"></i>
<span>11. ANKI engineer</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2776ff12-2f6b-80a7-b738-c4021ccd8a1c" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-user-graduate text-[10px]"></i>
<span>10. USMLE tutor</span>
</a>
</div>
</div>

<!-- Mini Anki Card Demo -->
<div class="mt-4 bg-slate-900 text-slate-50 rounded-xl p-4">
<div class="flex items-center justify-between mb-2 text-[11px] uppercase tracking-wide text-slate-400">
<span>ANKI Preview</span>
<button onclick="toggleAnkiDemo()" class="px-2 py-1 rounded bg-slate-800 text-[11px] hover:bg-slate-700">
<span id="anki-toggle-label">Show answer</span>
</button>
</div>
<div class="border border-slate-700 rounded-lg p-3 text-xs leading-relaxed">
<div id="anki-front">
<span class="font-semibold text-emerald-300">Q.</span>
A 24-year-old man is admitted with high fever and cough; bacterial pneumonia is suspected. List three factors to prioritise when choosing empirical intravenous antibiotics.
</div>
<div id="anki-back" class="hidden">
<span class="font-semibold text-emerald-300">A.</span>
① Cover the usual pathogens (e.g. Streptococcus pneumoniae, Haemophilus influenzae);<br>
② Take into account local resistance surveillance data and local epidemiology;<br>
③ Adjust the dose and choice of drug for the individual patient, e.g. renal function and allergy history.
</div>
</div>
<p class="mt-2 text-[10px] text-slate-400">Tip: with the ANKI/USMLE prompts above, you can turn a whole chapter into self-contained cards in this style in one batch.</p>
</div>
</div>
</div>
</div>
</div>

## Appendix: My Prompt Library (AI Studio)

<div class="not-prose glass-card rounded-2xl p-6">
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch">
    <div class="prose prose-slate max-w-none text-sm">
      <p>The small window below embeds, live, the <strong>Prompts List</strong> table I keep in Notion. It collects the system prompts and task prompts used in this course (the prompts are written in Chinese).</p>
      <ul class="text-sm text-slate-600 dark:text-slate-400 list-disc pl-5 space-y-1">
        <li>Tags such as <span class="font-medium">html / code / knowledge / agent</span> match the main threads of these notes: rebuilding papers, reading code, flashcards (USMLE / ANKI), and multi-step agents.</li>
        <li>While reading, you can filter the table by tag, copy the prompts that suit you into your AI tool, and refine them over time.</li>
        <li>When I add new cases to the notes, I only need to add rows in Notion and they show up here automatically, so the library keeps growing.</li>
      </ul>
      <div class="text-sm font-semibold text-slate-800 mt-4 flex items-center gap-2">
        <span class="inline-flex w-1.5 h-4 bg-slate-900 rounded-full"></span>
        A suggested "AI team"
      </div>
      <ul class="text-xs text-slate-600 dark:text-slate-400 list-disc pl-5 space-y-1">
        <li><strong>Academic mentor (long-term companion)</strong>: <a href="https://rune-gem-5ee.notion.site/2736ff12-2f6b-80db-9ed9-d1cef1dd8b1e" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">9. AI professor guidance</a>.</li>
        <li><strong>Exam coach (USMLE / licensing)</strong>: <a href="https://rune-gem-5ee.notion.site/2776ff12-2f6b-80a7-b738-c4021ccd8a1c" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">10. USMLE tutor</a> + <a href="https://rune-gem-5ee.notion.site/2ab6ff12-2f6b-80a1-bed8-fd6e2b323d3d" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">21. ANKI_USMLE essentials</a>.</li>
        <li><strong>Front-end engineer (visualization helper)</strong>: <a href="https://rune-gem-5ee.notion.site/2786ff12-2f6b-805f-8234-e85c775fdd78" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">12. Front-end engineer</a>, turns ideas into small HTML tools.</li>
        <li><strong>Knowledge engineer (card factory)</strong>: <a href="https://rune-gem-5ee.notion.site/2786ff12-2f6b-802a-a819-fbe5bd3da611" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">11. ANKI engineer</a>, generates structured cards from text in bulk.</li>
      </ul>
      <p class="mt-3 text-xs text-slate-500 dark:text-slate-400">Note: if the embedded window does not load because of browser or network settings, click "Open in Notion" on the right.</p>
    </div>
    <div class="relative">
      <div class="flex items-center justify-between mb-2 text-xs text-slate-500 dark:text-slate-400">
        <span class="inline-flex items-center gap-1">
          <i class="fas fa-table text-slate-400"></i>
          <span>Table · My Prompt For AI Studio</span>
        </span>
        <a href="https://rune-gem-5ee.notion.site/Table-My-Prompt-For-AI-Studio-2716ff122f6b806fae7dc5f95183fa25?pvs=74" target="_blank" class="inline-flex items-center gap-1 text-primary-600 hover:text-primary-800">
          <span>Open in Notion</span>
          <i class="fas fa-arrow-up-right-from-square text-[10px]"></i>
        </a>
      </div>
      <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden bg-white dark:bg-gray-800 shadow-inner">
        <iframe
          src="https://rune-gem-5ee.notion.site/Table-My-Prompt-For-AI-Studio-2716ff122f6b806fae7dc5f95183fa25?pvs=74"
          class="w-full h-80"
          loading="lazy"
          referrerpolicy="no-referrer"
        ></iframe>
      </div>
    </div>
  </div>
</div>

## Closing: Be the Product Manager of Your Own Knowledge

Looking back over the history of science, each change in tools has brought a jump in how efficiently we understand things: from hand-copied manuscripts to printing, from static PDFs to today's interactive HTML. In the AI era, **natural language is a programming language**.

<div class="not-prose inline-flex flex-col md:flex-row items-center gap-4 bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg border border-slate-100">
  <div class="flex items-center gap-2">
    <span class="w-8 h-8 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold">1</span>
    <span class="font-bold text-slate-800">Ask</span>
  </div>
  <i class="fas fa-arrow-right text-slate-300 hidden md:block"></i>
  <i class="fas fa-arrow-down text-slate-300 md:hidden"></i>
  <div class="flex items-center gap-2">
    <span class="w-8 h-8 rounded-full bg-primary-100 text-primary-600 flex items-center justify-center font-bold">2</span>
    <span class="font-bold text-primary-700">Wrap</span>
  </div>
  <i class="fas fa-arrow-right text-slate-300 hidden md:block"></i>
  <i class="fas fa-arrow-down text-slate-300 md:hidden"></i>
  <div class="flex items-center gap-2">
    <span class="w-8 h-8 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center font-bold">3</span>
    <span class="font-bold text-emerald-700">View</span>
  </div>
</div>

<p class="mt-12 text-xl font-bold text-primary-600 animate-pulse text-center">
Welcome to a new way of doing research visualization.
</p>

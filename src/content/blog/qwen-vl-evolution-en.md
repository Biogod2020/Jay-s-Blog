---
title: "The Qwen-VL Series: Long-Form Lecture Notes"
description: "A deep walkthrough of how the Qwen-VL family evolved from Qwen-VL to Qwen3-VL, written as long-form deep learning lecture notes."
pubDate: 2025-12-06
externalScripts: ["https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"]
lang: en
---
<!-- MathJax Configuration -->
<script>
window.MathJax = {
tex: {
inlineMath: [['$', '$'], ['\\(', '\\)']],
displayMath: [['$$', '$$'], ['\\[', '\\]']],
processEscapes: true
},
svg: {
fontCache: 'global'
}
};
</script>
<section id="toc" class="mb-10">
<div class="sr-only">

## Guide: How to Read These Notes

</div>

<h2 class="text-2xl font-semibold mb-4">Guide: How to Read These Notes</h2>
<p class="mb-2">
If you picture the whole history of Qwen-VL as an open-world RPG, these notes are your official strategy guide: where the main quest goes, where the side quests and hidden bosses are, and exactly which skill points each generation decided to spend.
</p>
<p class="mb-2">
To help you find your way, the notes roughly follow this structure:
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">01</span>
<h4 class="font-bold text-slate-700">Background and Motivation</h4>
</div>
<p class="text-xs text-slate-500">Why we need Qwen-VL at all, and which pain points of text-only models it addresses.</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">02</span>
<h4 class="font-bold text-slate-700">Catch-up Basics</h4>
</div>
<p class="text-xs text-slate-500">Lay the groundwork on visual encoding, alignment losses and other concepts we will need later.</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">03</span>
<h4 class="font-bold text-slate-700">Family Tree</h4>
</div>
<p class="text-xs text-slate-500">Draw the "academic family tree" of Qwen-VL and see how a small sapling grew into a whole forest.</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">04</span>
<h4 class="font-bold text-slate-700">Method, Generation by Generation</h4>
</div>
<p class="text-xs text-slate-500">The core material: the architecture of each generation from Qwen-VL to Qwen3-VL, and the logic behind each change.</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">05</span>
<h4 class="font-bold text-slate-700">Experiments and Data</h4>
</div>
<p class="text-xs text-slate-500">What actually matters in the results, rather than memorising numbers.</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">06</span>
<h4 class="font-bold text-slate-700">Reproduction and Outlook</h4>
</div>
<p class="text-xs text-slate-500">Practical advice for reproduction and engineering, plus possible future research directions.</p>
</div>
</div>
<p class="mt-3">
I will try to keep this conversational throughout: I will keep throwing out small questions like "What happens if we do it this way?" or "Can we be a bit greedier?", and then walk you through the answer with intuition plus formulas.
</p>
</section>
<section id="background" class="mb-16 scroll-mt-20">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## 1 Part 1: Why Should We Care About Qwen-VL?

</div>

<h2 class="flex items-center text-3xl font-bold text-slate-800 mb-6 group">
<span class="bg-indigo-600 text-white w-8 h-8 rounded-lg inline-flex items-center justify-center text-lg mr-3 shadow-md group-hover:scale-110 transition-transform">1</span>
Part 1: Why Should We Care About Qwen-VL?
</h2>
<p>
Picture this: you are chatting with an LLM that can only talk. It can explain anything, but the moment you hand it a picture, it turns into a <strong>"blind philosopher"</strong>: happy to discuss the meaning of life, yet unable to see the world.
</p>
<p>
That is the typical predicament of a text-only model. Its brain is big and its memory is strong, but its input is one-dimensional text, so when it faces the real world's stream of interleaved images and text, a piece is simply missing.
</p>
<!-- Figure 1 Inserted Here -->
<figure class="my-8 bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
<div class="bg-slate-50 px-4 py-2 border-b border-slate-200 flex items-center">
<span class="text-xs font-mono text-slate-500 uppercase tracking-wider">Reference: Figure 1 from Qwen-VL Paper</span>
</div>
<img src="/images/qwen-vlm/image_001.jpg" 
alt="Qwen-VL Capability Radar" 
class="w-full object-contain max-h-[500px] mx-auto" />
<figcaption class="p-4 text-sm text-slate-600 italic bg-white border-t border-slate-100">
<strong>Figure 1:</strong> Radar chart of Qwen-VL on a range of vision-centric tasks. Compared with other general-purpose models, Qwen-VL pushes outward on dimensions such as VQA, captioning and grounding. Think of it as an all-rounder in the making.
</figcaption>
</figure>
<p>
What the Qwen-VL series sets out to do is give this talking philosopher a pair of eyes, and while it is at it, a pair of AR glasses too: not only seeing every pixel in a picture, but also understanding time, space, text, formulas, UI actions, and even cause and effect across long videos.
</p>
<p>
To be more concrete, it has to get past at least three kinds of real-world "stuck levels":
</p>
<ul class="list-none space-y-4 pl-0">
<li class="flex items-start">
<svg class="w-6 h-6 text-red-500 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
<span><strong>Sees it but doesn't understand it:</strong> traditional OCR or detection models can circle text and draw boxes, but they don't know "where the problem is", let alone "what to do next".</span>
</li>
<li class="flex items-start">
<svg class="w-6 h-6 text-red-500 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
<span><strong>Understands one image, but not a pile of them:</strong> faced with long documents, slide decks, web pages, GUIs and videos, the model cannot build stable memory and reasoning chains across dozens of pages or thousands of frames.</span>
</li>
<li class="flex items-start">
<svg class="w-6 h-6 text-red-500 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
<span><strong>Understands the present, but not the history:</strong> many tasks require combining earlier context, previous dialogue turns, or the state of the previous screen, which demands genuine "long-context, multimodal" ability.</span>
</li>
</ul>
<p>
The Qwen-VL series has been upgrading along exactly these three pain points: from the original "describe what you see", to Qwen2-VL's "any resolution + video + multilingual", to Qwen2.5-VL's stronger reasoning, and finally Qwen3-VL, which pushes context length, long video and thinking ability to a new level.
</p>
<!-- Teacher's Blackboard Component -->
<aside class="not-prose mt-12 mb-12 bg-slate-800 rounded-xl shadow-2xl skew-y-1 transform transition-transform hover:skew-y-0 duration-300 ring-4 ring-slate-900 ring-offset-2">
<div class="px-8 py-6 border border-slate-700/50 rounded-xl bg-[url('https://www.transparenttextures.com/patterns/black-scales.png')]">
<div class="sr-only">

### 👨‍🏫 Teacher's Blackboard

</div>

<h3 class="flex items-center text-xl font-bold text-emerald-400 mb-4 font-mono tracking-tight border-b border-slate-600 pb-2">
<span class="text-3xl mr-3">👨‍🏫</span> Teacher's Blackboard
</h3>
<div class="text-slate-300 text-base space-y-4 font-light leading-relaxed">
<p>
Many students start out thinking: "I'll just take a vision backbone, throw its features into a large language model, and be done, right?" It sounds reasonable, but in practice you step into a whole series of pitfalls:
</p>
<ul class="list-none space-y-2 ml-1">
<li class="flex items-start">
<span class="text-emerald-500 mr-2">➤</span>
<span><strong>How do we discretise visual features into tokens?</strong> If every patch of a 4K image becomes a token, the context window simply explodes.</span>
</li>
<li class="flex items-start">
<span class="text-emerald-500 mr-2">➤</span>
<span><strong>How do we unify the coordinate systems of vision and text?</strong> Images are 2D and text is 1D; using the same positional encoding for both feels very odd.</span>
</li>
<li class="flex items-start">
<span class="text-emerald-500 mr-2">➤</span>
<span><strong>How should the training data be designed?</strong> Using only captions and QA leaves abilities like "grounding" and "fine-grained understanding" badly underfit.</span>
</li>
</ul>
<p class="mt-4 text-sm text-slate-400 italic pt-4 border-t border-slate-700/50">
Many of the design choices in the Qwen-VL series are really answers to these three questions: how, with limited compute, can a model "see wide, see fine, and see long"?
</p>
</div>
</div>
</aside>
<p class="text-lg font-medium text-slate-700 border-l-4 border-slate-300 pl-4 italic">
So instead of treating the Qwen-VL papers as separate technical reports, think of them as a gradually upgraded "skill tree": each generation maxes out or rebuilds a few branches, and the goal of these notes is to help you see that tree clearly, from root to leaf.
</p>
</div>
</section>
<section id="prerequisites" class="mb-24 scroll-mt-24">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## 2 Part 2: Catch-up Basics: From "a Brain That Only Reads" to "a Brain That Sees the World"

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-indigo-500 to-purple-600 text-white w-14 h-14 rounded-2xl inline-flex items-center justify-center text-2xl mr-5 shadow-xl group-hover:scale-110 transition-transform duration-300 ring-4 ring-indigo-50">2</span>
Part 2: Catch-up Basics: From "a Brain That Only Reads" to "a Brain That Sees the World"
</h2>
<div class="mb-12 bg-white p-4 md:p-8 rounded-[2rem] shadow-premium border border-slate-100 relative overflow-hidden">
<div
class="absolute top-0 right-0 w-[400px] h-[400px] bg-indigo-50 rounded-full mix-blend-multiply filter blur-[80px] opacity-60 animate-pulse">
</div>
<p class="text-xl text-slate-700 leading-relaxed relative z-10">
Before we take Qwen-VL apart, we need to reach some <strong>common ground</strong>.
<br>
Many students find multimodal learning hard because it straddles two fields: CV (computer vision) and NLP (natural language processing). CV people are used to pixels, convolutions and IoU; NLP people are used to tokens, attention
and perplexity.
</p>
<p class="text-xl text-slate-700 leading-relaxed mt-4 relative z-10">
But in fact, <strong>mathematically they are entirely compatible</strong>.
<br>
In this section we will use intuition first and run quickly through the three most essential concepts: <strong>ViT (turning vision into language), RoPE (rotary position encoding), and Cross-Attention (the bridge between modalities)</strong>. These three are the foundation for understanding all of
Qwen-VL's later clever tricks (such as M-RoPE and DeepStack).
</p>
</div>
<!-- 2.1 ViT -->
<div class="mb-20">
<div class="sr-only">

### 2.1 Turning Vision into Language: ViT (Vision Transformer)

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
2.1 Turning Vision into Language: ViT (Vision Transformer)
</h3>
<p class="text-lg text-slate-600 mb-6">
If we want an LLM to understand images, the first step must be <strong>turning the image into a form the LLM can understand</strong>. What can an LLM understand? Only a <strong>sequence</strong>.
<br>
So ViT does exactly one thing: <span
class="bg-indigo-100 text-indigo-800 px-1 rounded font-bold">it chops a 2D image into a 1D sequence of vectors.</span>
</p>
<!-- SVG: Patching Process -->
<div class="my-10 bg-white p-4 md:p-8 rounded-3xl border border-slate-200 shadow-lg relative">
<h4 class="text-center font-serif text-xl font-bold text-slate-800 mb-8">🎨 Illustrated: From Pixel to Patch Embedding
</h4>
<div class="flex justify-center overflow-x-auto">
<svg width="800" height="300" viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg"
class="font-sans">
<defs>
<marker id="arrow-vit" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#6366f1" />
</marker>
<filter id="patch-shadow" x="-20%" y="-20%" width="140%" height="140%">
<feDropShadow dx="2" dy="2" stdDeviation="2" flood-opacity="0.1" />
</filter>
</defs>
<!-- Input Image -->
<g transform="translate(50, 50)">
<text x="60" y="-15" text-anchor="middle" font-weight="bold" fill="#334155">Image (H x
W)</text>
<rect x="0" y="0" width="120" height="120" fill="#e0e7ff" stroke="#6366f1"
stroke-width="2" />
<!-- Grid -->
<path d="M 40 0 L 40 120 M 80 0 L 80 120 M 0 40 L 120 40 M 0 80 L 120 80" stroke="#a5b4fc"
stroke-width="1" />
<!-- Highlight Patch 1 -->
<rect x="0" y="0" width="40" height="40" fill="#818cf8" stroke="#4338ca" stroke-width="2" />
<text x="20" y="25" text-anchor="middle" fill="white" font-size="12"
font-weight="bold">x₁</text>
<!-- Highlight Patch 9 -->
<rect x="80" y="80" width="40" height="40" fill="#c7d2fe" stroke="#6366f1"
stroke-width="1" />
<text x="100" y="105" text-anchor="middle" fill="#4338ca" font-size="12">x₉</text>
</g>
<!-- Operation: Flatten & Project -->
<g transform="translate(200, 100)">
<path d="M 0 10 L 50 10" stroke="#6366f1" stroke-width="2" marker-end="url(#arrow-vit)" />
<text x="25" y="-5" text-anchor="middle" font-size="10" fill="#6366f1">Flatten</text>
<rect x="60" y="-20" width="80" height="60" rx="8" fill="#f8fafc" stroke="#94a3b8" />
<text x="100" y="5" text-anchor="middle" font-size="12" font-weight="bold"
fill="#475569">Linear</text>
<text x="100" y="25" text-anchor="middle" font-size="12" font-weight="bold"
fill="#475569">Proj (E)</text>
<path d="M 150 10 L 200 10" stroke="#6366f1" stroke-width="2"
marker-end="url(#arrow-vit)" />
</g>
<!-- Output Sequence -->
<g transform="translate(450, 50)">
<text x="100" y="-15" text-anchor="middle" font-weight="bold" fill="#334155">Sequence of
Embeddings</text>
<!-- Token 1 -->
<g transform="translate(0, 0)">
<rect x="0" y="0" width="20" height="120" fill="#818cf8" stroke="#4338ca" rx="2"
filter="url(#patch-shadow)" />
<text x="10" y="140" text-anchor="middle" font-size="12" font-weight="bold"
fill="#4338ca">z₁</text>
</g>
<!-- Token 2 -->
<g transform="translate(30, 0)">
<rect x="0" y="0" width="20" height="120" fill="#a5b4fc" stroke="#6366f1" rx="2"
opacity="0.8" />
</g>
<!-- Ellipsis -->
<text x="75" y="65" font-size="20" fill="#94a3b8">...</text>
<!-- Token 9 -->
<g transform="translate(100, 0)">
<rect x="0" y="0" width="20" height="120" fill="#c7d2fe" stroke="#818cf8" rx="2" />
<text x="10" y="140" text-anchor="middle" font-size="12" font-weight="bold"
fill="#4338ca">z₉</text>
</g>
<!-- Class Token (Optional) -->
<g transform="translate(140, 0)">
<rect x="0" y="0" width="20" height="120" fill="#fcd34d" stroke="#d97706" rx="2" />
<text x="10" y="140" text-anchor="middle" font-size="12" font-weight="bold"
fill="#b45309">[CLS]</text>
</g>
</g>
<!-- Math Annotation -->
<text x="400" y="250" text-anchor="middle" font-family="monospace" font-size="14"
fill="#64748b">
z_i = Linear(Flatten(Patch_i)) + Pos_Embed_i
</text>
</svg>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
<div class="bg-indigo-50 p-6 rounded-xl border border-indigo-100">
<h4 class="font-bold text-indigo-900 mb-3 text-lg">💡 Why cut the image into patches?</h4>
<p class="text-indigo-800 text-sm leading-relaxed">
If every pixel were a token, a 224x224 image would have 50,176 tokens, and the attention cost would explode ($O(N^2)$).
<br>
After cutting into 16x16 patches, there are only $14 \times 14 = 196$
tokens, which strikes a balance between <strong>computational efficiency</strong> and <strong>information retention</strong>.
</p>
</div>
<div class="bg-purple-50 p-6 rounded-xl border border-purple-100">
<h4 class="font-bold text-purple-900 mb-3 text-lg">⚠️ Foreshadowing for Qwen-VL</h4>
<p class="text-purple-800 text-sm leading-relaxed">
A standard ViT needs a fixed resolution (say 224 or 336).
<br>
<strong>Question:</strong> What if a tall phone screenshot (1080x2400) comes in? Forced resizing distorts it, and zero-padding wastes compute. This problem is exactly the core pain point that
<strong>Qwen2-VL Dynamic Resolution</strong> sets out to solve.
</p>
</div>
</div>
</div>
<!-- 2.2 RoPE -->
<div class="mb-20">
<div class="sr-only">

### 2.2 Elegant Position Encoding: RoPE (Rotary Positional Embedding)

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-purple-500 rounded-full mr-4 shadow-md"></span>
2.2 Elegant Position Encoding: RoPE (Rotary Positional Embedding)
</h3>
<p class="text-lg text-slate-600 mb-6">
The attention mechanism in a Transformer is essentially "position-agnostic" (permutation invariant). If you shuffle the words of a sentence, the attention
scores come out the same. So we have to tell the model <strong>"who comes before whom"</strong>.
<br>
RoPE is currently the most elegant solution. Instead of adding a position vector, it <strong>rotates</strong> the word vector by some angle in space.
</p>
<div class="bg-slate-900 p-4 md:p-8 rounded-3xl shadow-2xl relative overflow-hidden mb-10 group">
<div
class="absolute -top-20 -right-20 w-64 h-64 bg-gradient-to-br from-purple-500 to-indigo-500 rounded-full filter blur-[80px] opacity-30 group-hover:opacity-50 transition-opacity duration-500">
</div>
<h4 class="text-center font-bold text-white mb-8 text-xl tracking-wider">The geometric intuition of RoPE: relative distance = difference in rotation angle</h4>
<div class="flex justify-center">
<svg width="400" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
<!-- Coordinate System -->
<line x1="200" y1="280" x2="200" y2="20" stroke="#475569" stroke-width="1" />
<line x1="50" y1="150" x2="350" y2="150" stroke="#475569" stroke-width="1" />
<!-- Unit Circle -->
<circle cx="200" cy="150" r="100" fill="none" stroke="#334155" stroke-dasharray="4 4" />
<!-- Vector q at pos m -->
<g transform="rotate(-30, 200, 150)"> <!-- m*theta -->
<line x1="200" y1="150" x2="300" y2="150" stroke="#a78bfa" stroke-width="3" />
<circle cx="300" cy="150" r="4" fill="#a78bfa" />
<text x="310" y="155" fill="#a78bfa" font-weight="bold" font-size="14">q (pos m)</text>
</g>
<!-- Vector k at pos n -->
<g transform="rotate(-75, 200, 150)"> <!-- n*theta -->
<line x1="200" y1="150" x2="300" y2="150" stroke="#38bdf8" stroke-width="3" />
<circle cx="300" cy="150" r="4" fill="#38bdf8" />
<text x="310" y="155" fill="#38bdf8" font-weight="bold" font-size="14">k (pos n)</text>
</g>
<!-- Angle difference -->
<path d="M 270 110 A 80 80 0 0 0 230 75" fill="none" stroke="#fbbf24" stroke-width="2" />
<text x="260" y="90" fill="#fbbf24" font-weight="bold">Δθ = (n-m)θ</text>
<!-- Math -->
<text x="200" y="290" text-anchor="middle" fill="#94a3b8" font-family="monospace"
font-size="12">
Attention Score = q · k = |q||k| cos((n-m)θ)
</text>
</svg>
</div>
</div>
<div class="prose prose-slate text-slate-600">
<p>
<strong>Why does RoPE matter so much for Qwen-VL?</strong>
<br>
Because the Qwen-VL series has to handle not just 1D text, but also 2D images and 3D video.
<br>
In Qwen2-VL, to unify these modalities, the authors proposed <strong>M-RoPE (Multimodal RoPE)</strong>, which extends the rotation into 3D space (time, height, width). If you don't grasp
RoPE's core intuition that "relative position is determined by the rotation angle", you won't be able to see how M-RoPE "decouples" position information across three dimensions.
</p>
</div>
</div>
<!-- 2.3 Cross-Attention -->
<div class="mb-20">
<div class="sr-only">

### 2.3 The Bridge Between Modalities: Cross-Attention

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-emerald-500 rounded-full mr-4 shadow-md"></span>
2.3 The Bridge Between Modalities: Cross-Attention
</h3>
<p class="text-lg text-slate-600 mb-6">
This is the key mechanism by which Qwen-VL injects visual features into the LLM. In self-attention, the query, key and value all come from the same sequence. In cross-attention, they part ways.
</p>
<div class="bg-white p-4 md:p-8 rounded-3xl border border-slate-200 shadow-xl">
<div class="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
<!-- Diagram -->
<div class="relative">
<svg width="400" height="250" viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg">
<!-- LLM Side -->
<rect x="20" y="50" width="80" height="150" rx="8" fill="#f0f9ff" stroke="#0ea5e9"
stroke-width="2" />
<text x="60" y="30" text-anchor="middle" font-weight="bold" fill="#0369a1">LLM</text>
<text x="60" y="130" text-anchor="middle" font-weight="bold" fill="#0ea5e9"
font-size="20">Q</text>
<text x="60" y="150" text-anchor="middle" font-size="10" fill="#64748b">Queries</text>
<!-- Vision Side -->
<rect x="300" y="50" width="80" height="150" rx="8" fill="#ecfdf5" stroke="#10b981"
stroke-width="2" />
<text x="340" y="30" text-anchor="middle" font-weight="bold" fill="#047857">Vision</text>
<text x="340" y="120" text-anchor="middle" font-weight="bold" fill="#10b981"
font-size="20">K</text>
<text x="340" y="150" text-anchor="middle" font-weight="bold" fill="#10b981"
font-size="20">V</text>
<text x="340" y="170" text-anchor="middle" font-size="10" fill="#64748b">Keys /
Values</text>
<!-- Attention Mechanism -->
<circle cx="200" cy="125" r="40" fill="#fffbeb" stroke="#f59e0b" stroke-width="2" />
<text x="200" y="130" text-anchor="middle" font-weight="bold" fill="#b45309">Attn</text>
<!-- Flows -->
<path d="M 100 125 L 160 125" stroke="#0ea5e9" stroke-width="3"
marker-end="url(#arrow-blue)" />
<path d="M 300 125 L 240 125" stroke="#10b981" stroke-width="3"
marker-end="url(#arrow-green)" />
<!-- Output -->
<path d="M 200 165 L 200 210" stroke="#f59e0b" stroke-width="3"
marker-end="url(#arrow-orange)" />
<text x="200" y="230" text-anchor="middle" font-size="12" font-weight="bold"
fill="#475569">Fused Features</text>
<defs>
<marker id="arrow-blue" markerWidth="10" markerHeight="10" refX="9" refY="3"
orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#0ea5e9" />
</marker>
<marker id="arrow-green" markerWidth="10" markerHeight="10" refX="9" refY="3"
orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#10b981" />
</marker>
<marker id="arrow-orange" markerWidth="10" markerHeight="10" refX="9" refY="3"
orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#f59e0b" />
</marker>
</defs>
</svg>
</div>
<!-- Analogy -->
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-100">
<h4 class="font-bold text-slate-800 mb-3 flex items-center">
<span class="text-xl mr-2">💊</span> The pharmacy analogy
</h4>
<p class="text-slate-600 text-sm leading-relaxed mb-3">
Imagine the LLM is an old-school herbal pharmacist, and the vision encoder is a giant cabinet of herb drawers.
</p>
<ul class="list-disc list-inside text-slate-600 text-sm space-y-2">
<li><strong>Query (Q):</strong> the "prescription" in the pharmacist's hand (what information does the current text context need? e.g. "Where is the cat in the picture?").</li>
<li><strong>Key (K):</strong> the "label" on each drawer (the texture, shape and position features of the image).</li>
<li><strong>Value (V):</strong> the actual "herbs" inside the drawer (the concrete visual feature vectors).</li>
</ul>
<p class="text-slate-600 text-sm mt-3">
Cross-attention is the pharmacist taking the prescription (Q), matching it against the drawer labels (K), pulling out the corresponding herbs (V), and mixing them into the current diagnosis (text generation).
</p>
</div>
</div>
</div>
<div class="mt-8 p-4 bg-yellow-50 border-l-4 border-yellow-400 text-yellow-900 rounded-r-lg">
<p class="font-bold mb-1">Note:</p>
<p class="text-sm">
The first Qwen-VL used a similar mechanism (an adapter), but later versions (Qwen2-VL) switched, for efficiency, to a more direct <strong>MLP Merger (a C-Former
variant)</strong>. We study cross-attention to understand "why we map visual features into the language space at all".
</p>
</div>
</div>
<!-- 2.4 Coordinate Tokenization -->
<div class="mb-20">
<div class="sr-only">

### 2.4 Discretising Coordinates: Turning "Drawing a Box" into "Speaking"

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-amber-500 rounded-full mr-4 shadow-md"></span>
2.4 Discretising Coordinates: Turning "Drawing a Box" into "Speaking"
</h3>
<p class="text-lg text-slate-600 mb-6">
Qwen-VL can do more than look at images; it can also draw boxes around objects in them (grounding).
<br>
Many students intuitively assume: surely this is done with regression? Predicting continuous values for x and y?
<br>
<span class="text-amber-600 font-bold">Wrong! Completely wrong!</span>
In an LLM's world there are only tokens. For an LLM to output coordinates, we must force continuous pixel coordinates into discrete vocabulary words.
</p>
<div class="bg-white p-4 md:p-8 rounded-3xl border border-slate-200 shadow-xl mb-10">
<h4 class="text-center font-bold text-slate-700 mb-8 text-xl">🎯 Illustrated: Binning, or putting the world on a grid</h4>
<div class="flex justify-center overflow-x-auto">
<svg width="700" height="320" viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" class="font-sans">
<defs>
<marker id="arrow-amber" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#d97706" />
</marker>
<pattern id="grid-pattern" width="40" height="40" patternUnits="userSpaceOnUse">
<path d="M 40 0 L 0 0 0 40" fill="none" stroke="#e2e8f0" stroke-width="1" />
</pattern>
</defs>
<!-- Image Space -->
<g transform="translate(50, 50)">
<text x="100" y="-15" text-anchor="middle" font-weight="bold" fill="#334155">Image (1000 x
1000)</text>
<!-- The Image -->
<rect x="0" y="0" width="200" height="200" fill="#fffbeb" stroke="#f59e0b" stroke-width="2" />
<rect x="0" y="0" width="200" height="200" fill="url(#grid-pattern)" />
<!-- A Bounding Box -->
<rect x="60" y="80" width="80" height="60" fill="rgba(245, 158, 11, 0.2)" stroke="#d97706"
stroke-width="3" stroke-dasharray="5,2" />
<!-- Coordinates -->
<circle cx="60" cy="80" r="4" fill="#d97706" />
<text x="50" y="70" font-family="monospace" font-size="10" fill="#d97706">(300, 400)</text>
<circle cx="140" cy="140" r="4" fill="#d97706" />
<text x="150" y="155" font-family="monospace" font-size="10" fill="#d97706">(700, 700)</text>
</g>
<!-- Transformation -->
<g transform="translate(280, 140)">
<path d="M 0 0 L 60 0" stroke="#d97706" stroke-width="3" marker-end="url(#arrow-amber)" />
<text x="30" y="-10" text-anchor="middle" font-size="12" fill="#b45309"
font-weight="bold">Quantize</text>
<text x="30" y="20" text-anchor="middle" font-size="10" fill="#b45309">Range [0, 1000]</text>
</g>
<!-- Vocabulary Space -->
<g transform="translate(380, 50)">
<text x="100" y="-15" text-anchor="middle" font-weight="bold" fill="#334155">LLM Vocabulary</text>
<!-- Token Dictionary Visual -->
<rect x="20" y="0" width="160" height="220" fill="#f8fafc" stroke="#94a3b8" rx="8" />
<text x="40" y="30" font-family="monospace" fill="#94a3b8">... </text>
<text x="40" y="50" font-family="monospace" fill="#64748b">ID: 32001 -> "apple"</text>
<text x="40" y="70" font-family="monospace" fill="#64748b">ID: 32002 -> "banana"</text>
<line x1="30" y1="85" x2="170" y2="85" stroke="#cbd5e1" stroke-dasharray="2,2" />
<!-- Special Coordinate Tokens -->
<g fill="#d97706" font-weight="bold">
<text x="40" y="110" font-family="monospace">ID: 40300 -> &lt;300&gt;</text>
<text x="40" y="130" font-family="monospace">ID: 40400 -> &lt;400&gt;</text>
<text x="40" y="150" font-family="monospace">ID: 40700 -> &lt;700&gt;</text>
</g>
<line x1="30" y1="165" x2="170" y2="165" stroke="#cbd5e1" stroke-dasharray="2,2" />
<text x="40" y="190" font-family="monospace" fill="#94a3b8">... </text>
</g>
<!-- Output Sequence -->
<text x="350" y="300" text-anchor="middle" font-family="monospace" font-size="14" fill="#334155">
Output: &lt;box&gt; <tspan fill="#d97706" font-weight="bold">&lt;300&gt; &lt;400&gt; &lt;700&gt;
&lt;700&gt;</tspan> &lt;/box&gt;
</text>
</svg>
</div>
</div>
<div class="prose prose-slate text-slate-600">
<p>
<strong>What Qwen-VL does:</strong>
<ul class="list-disc list-inside">
<li>Add 1000 special tokens to the vocabulary: <code>&lt;0&gt;</code>, <code>&lt;1&gt;</code>, ... <code>&lt;999&gt;</code>.</li>
<li>Normalise the image's width and height to [0, 1000].</li>
<li>When the model needs to output a coordinate, it is actually answering <strong>a 1000-way multiple-choice question</strong>.</li>
</ul>
</p>
<div class="bg-amber-50 p-4 rounded-lg border-l-4 border-amber-500 italic">
<strong>🤔 A question from the teacher:</strong> Why cut into 1000 bins? Would 100 work? Would 10000?
<br>
<span class="text-sm not-italic text-slate-500">
Answer: too few (100) and localisation isn't precise enough, so boxes are off; too many (10000) and the vocabulary blows up, and the classification head becomes extremely hard to train (far too many classes). 1000 is an empirical sweet
spot.
</span>
</div>
</div>
</div>
<!-- 2.5 Attention Mask -->
<div class="mb-20">
<div class="sr-only">

### 2.5 The Art of Masking: Causal vs. Bidirectional Mask

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
2.5 The Art of Masking: Causal vs. Bidirectional Mask
</h3>
<p class="text-lg text-slate-600 mb-6">
One last key point: <strong>how time and space differ inside attention</strong>.
<br>
An LLM (GPT-style) is unidirectional (causal), because you cannot see the tenth word while saying the first one (that would be cheating).
<br>
But looking at an image is <strong>bidirectional</strong>! When you look at a photo, do you scan from the left eye to the right, or the right to the left? You take it all in at once! Pixels in an image have no "order".
</p>
<p class="text-lg text-slate-600 mb-6">
<strong>Here comes the conflict:</strong> when we stuff "bidirectional image tokens" into a "unidirectional LLM", how should the attention mask be drawn?
</p>
<div class="flex flex-col md:flex-row gap-8 items-start">
<!-- The Matrix Visual -->
<div class="w-full md:w-1/2 bg-white p-6 rounded-2xl border border-slate-200 shadow-md">
<h4 class="text-center font-bold text-slate-700 mb-4 text-sm">Hybrid Attention Mask Matrix</h4>
<div class="flex justify-center">
<svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
<!-- Background Grid -->
<rect x="0" y="0" width="300" height="300" fill="#f8fafc" stroke="#cbd5e1" />
<!-- Legend -->
<g transform="translate(10, 10)">
<rect x="0" y="0" width="10" height="10" fill="#3b82f6" />
<text x="15" y="8" font-size="10" fill="#64748b">Visible (1)</text>
<rect x="0" y="15" width="10" height="10" fill="#e2e8f0" />
<text x="15" y="23" font-size="10" fill="#64748b">Masked (0)</text>
</g>
<!-- Zones Definition -->
<!-- V: Image Tokens (First 100) -->
<!-- T: Text Tokens (Next 100) -->
<!-- 1. Vision-to-Vision: Bidirectional (Full Attention) -->
<rect x="30" y="30" width="100" height="100" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" />
<text x="80" y="80" text-anchor="middle" font-weight="bold" fill="#1e40af" font-size="12">Vision ↔
Vision</text>
<text x="80" y="95" text-anchor="middle" fill="#1e40af" font-size="10">(all visible)</text>
<!-- 2. Text-to-Vision: Text can see Vision -->
<rect x="30" y="150" width="100" height="120" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" />
<text x="80" y="210" text-anchor="middle" font-weight="bold" fill="#1e40af" font-size="12">Text →
Vision</text>
<!-- 3. Vision-to-Text: Vision CANNOT see Text -->
<rect x="150" y="30" width="120" height="100" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1" />
<line x1="150" y1="30" x2="270" y2="130" stroke="#cbd5e1" />
<line x1="270" y1="30" x2="150" y2="130" stroke="#cbd5e1" />
<text x="210" y="80" text-anchor="middle" font-weight="bold" fill="#64748b" font-size="12">🚫 Vis ↛
Text</text>
<!-- 4. Text-to-Text: Causal (Triangular) -->
<path d="M 150 150 L 150 270 L 270 270 Z" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" />
<path d="M 150 150 L 270 150 L 270 270" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1" />
<text x="180" y="240" text-anchor="middle" font-weight="bold" fill="#1e40af" font-size="12">Text →
Text</text>
<text x="180" y="255" text-anchor="middle" fill="#1e40af" font-size="10">(causal triangle)</text>
<!-- Axis Labels -->
<text x="15" y="80" text-anchor="middle" font-size="12" fill="#475569"
transform="rotate(-90, 15, 80)">Image Tokens</text>
<text x="15" y="210" text-anchor="middle" font-size="12" fill="#475569"
transform="rotate(-90, 15, 210)">Text Tokens</text>
<text x="80" y="290" text-anchor="middle" font-size="12" fill="#475569">Image</text>
<text x="210" y="290" text-anchor="middle" font-size="12" fill="#475569">Text</text>
</svg>
</div>
</div>
<!-- Explanation -->
<div class="w-full md:w-1/2 flex flex-col justify-center">
<div class="bg-slate-50 p-6 rounded-2xl border-l-4 border-slate-400">
<h5 class="font-bold text-slate-800 mb-3">Key rules:</h5>
<ul class="list-disc list-inside space-y-3 text-slate-600 text-sm">
<li>
<strong>Inside the image (top left):</strong> <span class="bg-blue-100 text-blue-800 px-1 rounded">all-ones
matrix</span>. All patches of the image can see each other, because they are spatial information that exists all at once.
</li>
<li>
<strong>Inside the text (bottom right):</strong> <span
class="bg-slate-200 text-slate-800 px-1 rounded">lower-triangular matrix</span>. Text must obey causality: token $t$ can only see $1 \dots
t-1$.
</li>
<li>
<strong>Text looking at image (bottom left):</strong> <span class="bg-blue-100 text-blue-800 px-1 rounded">all
ones</span>. Wherever the text has got to, it can look back at the whole image.
</li>
<li>
<strong>Image looking at text (top right):</strong> <span class="bg-slate-200 text-slate-800 px-1 rounded">all
zeros</span>. When the image is there, the text that follows has not been generated yet, so of course it cannot be seen (to prevent leakage).
</li>
</ul>
</div>
<p class="mt-4 text-slate-600 text-sm italic">
This special mask design is the underlying guarantee that lets decoder-only models like Qwen-VL handle both understanding and generation tasks.
</p>
</div>
</div>
</div>
</div>
</section>
<section id="genealogy" class="mb-16 scroll-mt-20">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## 3 Part 3: The Qwen Family Tree: From Qwen-LM to Qwen3-VL

</div>

<h2 class="flex items-center text-3xl font-bold text-slate-800 mb-6 group">
<span class="bg-indigo-600 text-white w-8 h-8 rounded-lg inline-flex items-center justify-center text-lg mr-3 shadow-md group-hover:scale-110 transition-transform">3</span>
Part 3: The Qwen Family Tree: From Qwen-LM to Qwen3-VL
</h2>
<p>
Let's first take a bird's-eye view: what does the Qwen family actually look like? Which members are "text-only siblings", which are "vision editions", which "specialise in images", and which "focus on long context and reasoning"?
</p>
<p>
The earliest is the Qwen-LM family, which laid the foundation for the text-only world. On that foundation, Qwen-VL plugged in the ability to "see images". Then the Qwen2 series upgraded both language and vision, giving rise to Qwen2-VL. After that came Qwen2.5 and Qwen2.5-VL, with stronger reasoning and longer context. Finally, Qwen3-VL brings everything together with a 256K context and strong thinking ability.
</p>
<p>
Let's draw this whole lineage as a "version evolution tree" in one diagram.
</p>
<!-- SVG Diagram: Qwen Family Tree -->
<div class="my-12 bg-white rounded-xl shadow-premium p-4 md:p-8 border border-slate-100 overflow-x-auto">
<h4 class="text-center font-bold text-slate-700 mb-8 text-lg font-serif">Illustrated: The Qwen Family Phylogeny Tree</h4>
<div class="min-w-[700px] flex justify-center">
<svg width="800" height="360" viewBox="0 0 800 360" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="arrowGray" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" />
</marker>
<marker id="arrowBrand" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#0ea5e9" />
</marker>
<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
<feDropShadow dx="2" dy="2" stdDeviation="2" flood-opacity="0.1"/>
</filter>
</defs>
<!-- Background Zones -->
<rect x="50" y="20" width="700" height="120" rx="10" fill="#f8fafc" stroke="#e2e8f0" stroke-dasharray="4 4" />
<text x="70" y="45" font-weight="bold" fill="#64748b" font-size="12">Language Foundation (text-only base)</text>
<rect x="50" y="200" width="700" height="140" rx="10" fill="#f0f9ff" stroke="#bae6fd" stroke-dasharray="4 4" />
<text x="70" y="225" font-weight="bold" fill="#0369a1" font-size="12">Vision-Language Evolution (multimodal)</text>
<!-- Nodes: Text Models (Top Row) -->
<!-- Qwen1 -->
<g transform="translate(150, 90)">
<rect x="-60" y="-20" width="120" height="40" rx="20" fill="white" stroke="#94a3b8" stroke-width="2" filter="url(#shadow)" />
<text x="0" y="5" text-anchor="middle" font-weight="600" fill="#475569" font-size="14">Qwen-7B</text>
</g>
<!-- Qwen2 -->
<g transform="translate(350, 90)">
<rect x="-60" y="-20" width="120" height="40" rx="20" fill="white" stroke="#94a3b8" stroke-width="2" filter="url(#shadow)" />
<text x="0" y="5" text-anchor="middle" font-weight="600" fill="#475569" font-size="14">Qwen2</text>
</g>
<!-- Qwen2.5 -->
<g transform="translate(550, 90)">
<rect x="-60" y="-20" width="120" height="40" rx="20" fill="white" stroke="#94a3b8" stroke-width="2" filter="url(#shadow)" />
<text x="0" y="5" text-anchor="middle" font-weight="600" fill="#475569" font-size="14">Qwen2.5 / 3</text>
</g>
<!-- Nodes: Vision Models (Bottom Row) -->
<!-- Qwen-VL -->
<g transform="translate(150, 270)">
<rect x="-70" y="-25" width="140" height="50" rx="8" fill="white" stroke="#0ea5e9" stroke-width="2.5" filter="url(#shadow)" />
<text x="0" y="0" text-anchor="middle" font-weight="bold" fill="#0369a1" font-size="15">Qwen-VL</text>
<text x="0" y="18" text-anchor="middle" font-size="10" fill="#64748b">Basic VQA + Grounding</text>
</g>
<!-- Qwen2-VL -->
<g transform="translate(350, 270)">
<rect x="-70" y="-25" width="140" height="50" rx="8" fill="white" stroke="#0ea5e9" stroke-width="2.5" filter="url(#shadow)" />
<text x="0" y="0" text-anchor="middle" font-weight="bold" fill="#0369a1" font-size="15">Qwen2-VL</text>
<text x="0" y="18" text-anchor="middle" font-size="10" fill="#64748b">Dynamic Res + M-RoPE</text>
</g>
<!-- Qwen2.5/3-VL -->
<g transform="translate(550, 270)">
<rect x="-75" y="-30" width="150" height="60" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="3" filter="url(#shadow)" />
<text x="0" y="-5" text-anchor="middle" font-weight="bold" fill="#0c4a6e" font-size="16">Qwen3-VL</text>
<text x="0" y="15" text-anchor="middle" font-size="10" fill="#0369a1">256K Context</text>
<text x="0" y="27" text-anchor="middle" font-size="10" fill="#0369a1">Thinking Mode</text>
</g>
<!-- Connectors: Evolution (Horizontal) -->
<path d="M 210 90 L 290 90" stroke="#cbd5e1" stroke-width="2" marker-end="url(#arrowGray)" />
<path d="M 410 90 L 490 90" stroke="#cbd5e1" stroke-width="2" marker-end="url(#arrowGray)" />
<path d="M 220 270 L 280 270" stroke="#7dd3fc" stroke-width="3" marker-end="url(#arrowBrand)" />
<path d="M 420 270 L 475 270" stroke="#7dd3fc" stroke-width="3" marker-end="url(#arrowBrand)" />
<!-- Connectors: Base Influence (Vertical Dashed) -->
<path d="M 150 110 L 150 245" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrowGray)" />
<text x="155" y="180" font-size="10" fill="#94a3b8" transform="rotate(-90 155,180)">Based on</text>
<path d="M 350 110 L 350 245" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrowGray)" />
<path d="M 550 110 L 550 240" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrowGray)" />
</svg>
</div>
</div>
<div class="bg-blue-50 border-l-4 border-blue-500 p-4 mb-8 text-sm text-blue-800">
<p class="mb-0"><strong>Key fact:</strong><span class="font-semibold">A vision-language model is not a separate species; it is a branch growing on the tree of large language models.</span> Whenever the underlying language model is upgraded, the vision version has to be rebuilt too, and that rebuild often brings new training strategies and new vision module designs along with it.</p>
</div>
<p>
So to understand the Qwen-VL branch, it helps to keep an invisible timeline of "Qwen text-only history" in mind: every upgrade of the text backbone (from Qwen to Qwen2, then Qwen2.5 and Qwen3) brings the vision version longer context, better alignment and stronger reasoning.
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-12 mb-12">
<!-- Card 1 -->
<div class="bg-white p-6 rounded-xl shadow-premium border border-slate-100 hover:shadow-float transition-all duration-300 group">
<h4 class="text-xl font-bold text-brand-700 mb-2 font-serif group-hover:text-brand-500 transition-colors">3.1 Generation 1: Qwen-VL</h4>
<p class="text-sm text-slate-600 leading-relaxed">Built on Qwen-LM, with a carefully designed visual receptor and input/output interface, this was the first time the model could reliably "describe images + ground objects + read text". The focus of this generation was filling in all the <span class="bg-brand-50 px-1 rounded text-brand-700">basic visual abilities</span>.</p>
</div>
<!-- Card 2 -->
<div class="bg-white p-6 rounded-xl shadow-premium border border-slate-100 hover:shadow-float transition-all duration-300 group">
<h4 class="text-xl font-bold text-brand-700 mb-2 font-serif group-hover:text-brand-500 transition-colors">3.2 Generation 2: Qwen2-VL</h4>
<p class="text-sm text-slate-600 leading-relaxed">Key words: <strong>Dynamic Resolution</strong> and <strong>M-RoPE</strong>. No longer bound by a fixed resolution, and no longer willing to treat video as a pile of unrelated images. It gained a clear edge on documents, UIs and long videos.</p>
</div>
<!-- Card 3 -->
<div class="bg-white p-6 rounded-xl shadow-premium border border-slate-100 hover:shadow-float transition-all duration-300 group">
<h4 class="text-xl font-bold text-brand-700 mb-2 font-serif group-hover:text-brand-500 transition-colors">3.3 Generation 3: Qwen2.5-VL</h4>
<p class="text-sm text-slate-600 leading-relaxed">Its role was "refining inner strength": stronger mathematical reasoning, code understanding and structured extraction (JSON, tables), plus a longer context so the model holds steady on long documents.</p>
</div>
<!-- Card 4 -->
<div class="bg-white p-6 rounded-xl shadow-premium border border-slate-100 hover:shadow-float transition-all duration-300 group">
<h4 class="text-xl font-bold text-brand-700 mb-2 font-serif group-hover:text-brand-500 transition-colors">3.4 Generation 4: Qwen3-VL</h4>
<p class="text-sm text-slate-600 leading-relaxed"><strong>256K context + DeepStack + thinking mode</strong>. It completely rebuilt the relationship between "long context + multimodality + reasoning": visual information is injected at multiple layers, a thinking mode is supported, and it aims squarely at top closed-source models.</p>
</div>
</div>
<p class="mt-8 text-slate-600">
In the next few sections we will go version by version, breaking each of the four Qwen-VL generations into four modules: model architecture, loss design, training pipeline and typical abilities. That way you can clearly feel how each generation upgrades, step by step, on top of the "V1 naive solution".
</p>
</div>
</section>
<section id="method-qwenvl" class="mb-24">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 4 Part 4: First Stop: Qwen-VL, or the Art of Giving a Brain "Prosthetic Eyes"

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-10 group tracking-tight">
<span
class="bg-gradient-to-br from-brand-500 to-blue-600 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:rotate-12 transition-transform duration-300">4</span>
Part 4: First Stop: Qwen-VL, or the Art of Giving a Brain "Prosthetic Eyes"
</h2>
<!-- Intro Block -->
<div class="mb-10 bg-white p-8 rounded-3xl shadow-premium border border-slate-100 relative overflow-hidden">
<div
class="absolute top-0 right-0 w-64 h-64 bg-brand-50 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-blob">
</div>
<div
class="absolute -bottom-8 -left-8 w-64 h-64 bg-purple-50 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-blob animation-delay-2000">
</div>
<p class="text-xl text-slate-700 leading-relaxed relative z-10">
Welcome, everyone, to the world of Qwen-VL. If we think of the text-only model (Qwen-7B) as a learned but blind sage, then what the Qwen-VL
project sets out to do is <strong>perform delicate surgery on him: fitting a pair of "prosthetic eyes"</strong>.
</p>
<p class="text-xl text-slate-700 leading-relaxed mt-4 relative z-10">
But this surgery isn't simple! You can't wire the optic nerve straight into the language centre, because they speak completely different "languages": the optic nerve carries pixel signals, while the language centre wants semantic symbols (tokens).
</p>
<p class="text-xl text-slate-700 leading-relaxed mt-4 relative z-10 font-semibold text-brand-700">
Qwen-VL's core contribution is a clever "translator" (the adapter) plus a rigorous "rehabilitation programme" (3-stage training), which together teach two modules that never used to talk to each other to work as a team.
</p>
</div>
<!-- 4.1 Model Architecture -->
<div class="sr-only">

### 4.1 Architecture: The Philosophy Behind Choosing the Three Parts

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-brand-500 rounded-full mr-4 shadow-md"></span>
4.1 Architecture: The Philosophy Behind Choosing the Three Parts
</h3>
<p class="text-xl text-slate-600 mb-8 leading-loose">
This is what I always call <strong>Step 1: Define a Function Set</strong>. Qwen-VL's
network architecture is a classic, built from three core components. It looks like stacking building blocks, but every block was chosen with care (SOTA selection).
</p>
<!-- Architecture Cards -->
<div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12">
<!-- Component 1: LLM -->
<div
class="group bg-slate-50 rounded-3xl p-8 border-2 border-slate-100 hover:border-brand-200 hover:bg-white hover:shadow-xl transition-all duration-300 cursor-default">
<div class="flex items-center justify-between mb-6">
<div
class="w-16 h-16 bg-white rounded-2xl shadow-md flex items-center justify-center text-4xl border border-slate-100 group-hover:scale-110 transition-transform">
🧠</div>
<span class="bg-slate-200 text-slate-600 text-sm font-bold px-3 py-1 rounded-full">The Brain</span>
</div>
<h4 class="text-2xl font-bold text-slate-800 mb-2">Qwen-7B</h4>
<p class="text-lg text-slate-500 font-medium mb-4 font-mono">LLM Backbone</p>
<p class="text-base text-slate-600 leading-relaxed">
This is the base. Why choose
Qwen-7B? Because at the time (2023) it performed very well among models of its size. Note: in the first training stage <strong>it is frozen</strong>, like a proud professor who refuses to change his parameters lightly.
</p>
</div>
<!-- Component 2: Vision Encoder -->
<div
class="group bg-slate-50 rounded-3xl p-8 border-2 border-slate-100 hover:border-blue-200 hover:bg-white hover:shadow-xl transition-all duration-300 cursor-default">
<div class="flex items-center justify-between mb-6">
<div
class="w-16 h-16 bg-white rounded-2xl shadow-md flex items-center justify-center text-4xl border border-slate-100 group-hover:scale-110 transition-transform">
👁️</div>
<span class="bg-blue-100 text-blue-600 text-sm font-bold px-3 py-1 rounded-full">The Eyes</span>
</div>
<h4 class="text-2xl font-bold text-slate-800 mb-2">ViT-bigG</h4>
<p class="text-lg text-blue-500 font-medium mb-4 font-mono">OpenCLIP Init</p>
<p class="text-base text-slate-600 leading-relaxed">
A full 1.9B parameters! This is a huge vision encoder. It cuts high-resolution 448×448 images into small patches and turns them into a sequence of dense feature vectors. <strong>It, too, is frozen first and unfrozen later.</strong>
</p>
</div>
<!-- Component 3: Adapter -->
<div
class="group bg-gradient-to-br from-indigo-50 to-purple-50 rounded-3xl p-8 border-2 border-indigo-100 hover:border-indigo-300 hover:shadow-2xl transition-all duration-300 relative overflow-hidden">
<div class="absolute -right-6 -top-6 w-24 h-24 bg-indigo-200 rounded-full blur-2xl opacity-50"></div>
<div class="flex items-center justify-between mb-6 relative z-10">
<div
class="w-16 h-16 bg-white rounded-2xl shadow-md flex items-center justify-center text-4xl border border-indigo-50 group-hover:scale-110 transition-transform">
🔗</div>
<span class="bg-indigo-600 text-white text-sm font-bold px-3 py-1 rounded-full shadow-lg">Key
Innovation</span>
</div>
<h4 class="text-2xl font-bold text-indigo-900 mb-2 relative z-10">VL Adapter</h4>
<p class="text-lg text-indigo-600 font-medium mb-4 font-mono relative z-10">Position-aware C-Attn</p>
<p class="text-base text-slate-700 leading-relaxed relative z-10">
This is the "translator". Unlike LLaVA's simple, brute-force linear projection, Qwen-VL uses a single-layer <strong>cross-attention</strong>
module that "compresses" the visual features to a fixed length (256).
</p>
</div>
</div>
<!-- SVG Diagram: Architecture Details -->
<div class="my-16">
<div class="bg-white rounded-3xl shadow-premium border border-slate-200 p-8 overflow-hidden">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
🔍 Under the microscope: Qwen-VL's data flow
</h4>
<div class="flex justify-center overflow-x-auto pb-4">
<!-- SVG Start -->
<svg width="900" height="450" viewBox="0 0 900 450" xmlns="http://www.w3.org/2000/svg"
class="font-sans">
<defs>
<marker id="arrow-head" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#64748b" />
</marker>
<filter id="shadow-card" x="-20%" y="-20%" width="140%" height="140%">
<feDropShadow dx="4" dy="4" stdDeviation="5" flood-opacity="0.1" />
</filter>
<linearGradient id="grad-adapter" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#e0e7ff;stop-opacity:1" />
<stop offset="100%" style="stop-color:#c7d2fe;stop-opacity:1" />
</linearGradient>
</defs>
<!-- Image Input -->
<g transform="translate(50, 150)">
<rect x="0" y="0" width="100" height="100" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"
rx="8" />
<text x="50" y="55" text-anchor="middle" font-size="32">🖼️</text>
<text x="50" y="125" text-anchor="middle" font-size="14" fill="#64748b"
font-weight="bold">Input Image</text>
<text x="50" y="145" text-anchor="middle" font-size="12" fill="#94a3b8"
font-family="monospace">448x448</text>
</g>
<!-- Arrow -->
<path d="M 160 200 L 200 200" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-head)" />
<!-- Vision Encoder -->
<g transform="translate(210, 100)">
<rect x="0" y="0" width="120" height="200" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"
rx="12" filter="url(#shadow-card)" />
<text x="60" y="40" text-anchor="middle" font-size="16" font-weight="bold"
fill="#1e40af">ViT-bigG</text>
<line x1="20" y1="60" x2="100" y2="60" stroke="#bfdbfe" stroke-width="2" />
<!-- Patches -->
<g transform="translate(35, 80)">
<rect x="0" y="0" width="15" height="15" fill="#93c5fd" stroke="#3b82f6" />
<rect x="18" y="0" width="15" height="15" fill="#93c5fd" stroke="#3b82f6" />
<rect x="36" y="0" width="15" height="15" fill="#93c5fd" stroke="#3b82f6" />
<rect x="0" y="18" width="15" height="15" fill="#93c5fd" stroke="#3b82f6" />
<rect x="18" y="18" width="15" height="15" fill="#93c5fd" stroke="#3b82f6" />
<rect x="36" y="18" width="15" height="15" fill="#93c5fd" stroke="#3b82f6" />
<text x="25" y="55" font-size="12" fill="#1e40af">...</text>
<text x="25" y="75" font-size="10" fill="#1e40af">~1000 patches</text>
</g>
</g>
<!-- Arrow -->
<path d="M 340 200 L 380 200" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-head)" />
<!-- Adapter (The Hero) -->
<g transform="translate(390, 80)">
<rect x="0" y="0" width="220" height="240" fill="url(#grad-adapter)" stroke="#6366f1"
stroke-width="2" rx="16" filter="url(#shadow-card)" />
<text x="110" y="30" text-anchor="middle" font-size="16" font-weight="bold"
fill="#3730a3">VL Adapter</text>
<text x="110" y="50" text-anchor="middle" font-size="12" fill="#4338ca">(Single Layer
Cross-Attn)</text>
<!-- Internal Logic -->
<g transform="translate(20, 70)">
<!-- Queries -->
<rect x="0" y="0" width="180" height="40" fill="white" stroke="#a5b4fc" rx="4" />
<text x="90" y="25" text-anchor="middle" font-size="12" font-weight="bold"
fill="#4f46e5">Trainable Queries (256)</text>
<!-- Operation -->
<text x="90" y="65" text-anchor="middle" font-size="18" font-weight="bold"
fill="#6366f1">⬇ Attend ⬇</text>
<!-- Keys/Values -->
<rect x="0" y="80" width="180" height="40" fill="#dbeafe" stroke="#3b82f6" rx="4" />
<text x="90" y="105" text-anchor="middle" font-size="12" font-weight="bold"
fill="#1e40af">Image Features (Keys/Values)</text>
<!-- Positional Emb -->
<g transform="translate(0, 135)">
<rect x="0" y="0" width="180" height="25" fill="#fef3c7" stroke="#f59e0b" rx="4" />
<text x="90" y="17" text-anchor="middle" font-size="11" font-weight="bold"
fill="#92400e">+ 2D Positional Embedding</text>
</g>
</g>
</g>
<!-- Arrow -->
<path d="M 620 200 L 660 200" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-head)" />
<!-- LLM -->
<g transform="translate(670, 100)">
<rect x="0" y="0" width="120" height="200" fill="#fdf2f8" stroke="#db2777" stroke-width="2"
rx="12" filter="url(#shadow-card)" />
<text x="60" y="40" text-anchor="middle" font-size="16" font-weight="bold"
fill="#9d174d">Qwen-LM</text>
<!-- Tokens In -->
<g transform="translate(10, 70)">
<rect x="0" y="0" width="100" height="25" fill="#c7d2fe" stroke="#4f46e5" />
<text x="50" y="17" text-anchor="middle" font-size="10" fill="#312e81">Visual Tokens
(256)</text>
<rect x="0" y="30" width="100" height="25" fill="#ffffff" stroke="#cbd5e1" />
<text x="50" y="47" text-anchor="middle" font-size="10" fill="#475569">Text
Tokens</text>
<text x="50" y="80" text-anchor="middle" font-size="20">⬇</text>
<text x="50" y="105" text-anchor="middle" font-size="12" font-weight="bold"
fill="#db2777">Generate</text>
</g>
</g>
</svg>
<!-- SVG End -->
</div>
<div class="mt-6 p-4 bg-indigo-50 border-l-4 border-indigo-500 rounded-r-lg text-slate-700 text-base">
<p class="font-bold mb-2 text-indigo-800">🎓 The teacher's aside: why use attention for compression?</p>
<p class="leading-relaxed">
Think about it: if we only used a fully connected (linear) layer or a pooling layer, wouldn't that be too "rigid"?
<strong>The beauty of cross-attention lies in its query mechanism.</strong>
We set up 256 learnable query vectors; you can think of them as 256
"probes". During training these probes learn to "search" the image features for different kinds of information: some specialise in texture, some in shape, some in position.
That is why Qwen-VL can keep very few tokens (256) while still retaining rich visual detail.
</p>
</div>
</div>
</div>
<!-- 4.2 Training Pipeline -->
<div class="sr-only">

### 4.2 Training in Three Acts: Teaching a Model Like Teaching a Student

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-brand-500 rounded-full mr-4 shadow-md"></span>
4.2 Training in Three Acts: Teaching a Model Like Teaching a Student
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Qwen-VL's training process is a classic, practically a textbook for multimodal training. It uses a <strong>3-stage training
pipeline</strong>. It's a lot like how we teach human students: first learn to read, then learn to solve problems, and finally learn to hold a polite conversation.
</p>
<div class="relative border-l-4 border-slate-200 ml-8 space-y-12">
<!-- Stage 1 -->
<div class="relative pl-12">
<div
class="absolute -left-[22px] top-0 w-10 h-10 bg-slate-100 border-4 border-slate-300 rounded-full flex items-center justify-center text-lg font-bold text-slate-500 z-10">
1</div>
<div
class="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:border-slate-300 transition-colors">
<h4 class="text-2xl font-bold text-slate-800 mb-4">Stage 1: Pre-training: "Visual Alignment"</h4>
<div class="flex flex-wrap gap-3 mb-4">
<span class="bg-slate-100 text-slate-600 px-3 py-1 rounded-full text-sm font-mono">Target:
Vision-Language Alignment</span>
<span class="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm font-mono">Data:
Image-Text Pairs</span>
</div>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
<strong>Task:</strong> teach the model to match images with simple descriptions (captions).
<br>
<strong>State:</strong>
<ul class="list-disc list-inside ml-4 mt-2 text-slate-600">
<li><span class="text-blue-600 font-bold">Vision Encoder:</span> Frozen (not updated)</li>
<li><span class="text-red-600 font-bold">Adapter:</span> Learnable (updated)</li>
<li><span class="text-blue-600 font-bold">LLM:</span> Frozen (not updated)</li>
</ul>
</p>
<p class="text-base text-slate-500 italic bg-slate-50 p-4 rounded-lg border border-slate-100">
"At this point the brain (LLM) and the eyes (ViT) are both locked, and only the translator in the middle (the adapter) is working hard to learn how to turn what the eyes see into a language the brain can understand."
</p>
</div>
</div>
<!-- Stage 2 -->
<div class="relative pl-12">
<div
class="absolute -left-[22px] top-0 w-10 h-10 bg-indigo-100 border-4 border-indigo-300 rounded-full flex items-center justify-center text-lg font-bold text-indigo-600 z-10">
2</div>
<div
class="bg-white p-8 rounded-2xl shadow-lg border-2 border-indigo-100 hover:border-indigo-300 transition-colors relative overflow-hidden">
<div class="absolute top-0 right-0 w-32 h-32 bg-indigo-50 rounded-bl-full -mr-10 -mt-10"></div>
<h4 class="text-2xl font-bold text-indigo-900 mb-4 relative z-10">Stage 2: Multi-task Pre-training
("Unlocking the Brain")</h4>
<div class="flex flex-wrap gap-3 mb-4 relative z-10">
<span class="bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full text-sm font-mono">Target:
Fine-grained Understanding</span>
<span class="bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full text-sm font-mono">Data: VQA,
OCR, Grounding</span>
</div>
<p class="text-lg text-slate-600 leading-relaxed mb-4 relative z-10">
<strong>Task:</strong> bring in higher-resolution input (448x448) and train harder tasks, such as "box the cat in the picture" or "read out the text in the image".
<br>
<strong>State:</strong>
<ul class="list-disc list-inside ml-4 mt-2 text-slate-600 relative z-10">
<li><span class="text-red-600 font-bold">Vision Encoder:</span> Learnable (finally unfrozen!)</li>
<li><span class="text-red-600 font-bold">Adapter:</span> Learnable</li>
<li><span class="text-red-600 font-bold">LLM:</span> Learnable (the brain starts adapting to visual signals)</li>
</ul>
</p>
<p
class="text-base text-indigo-700 italic bg-indigo-50 p-4 rounded-lg border border-indigo-100 relative z-10">
"This step is a qualitative leap. We unfreeze the whole model (full fine-tuning). Why unfreeze? Because the translator alone is no longer enough; the brain itself has to learn to handle new visual knowledge, especially to adapt to higher resolution and finer-grained tasks (such as
grounding)."
</p>
</div>
</div>
<!-- Stage 3 -->
<div class="relative pl-12">
<div
class="absolute -left-[22px] top-0 w-10 h-10 bg-brand-100 border-4 border-brand-300 rounded-full flex items-center justify-center text-lg font-bold text-brand-600 z-10">
3</div>
<div
class="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:border-brand-300 transition-colors">
<h4 class="text-2xl font-bold text-slate-800 mb-4">Stage 3: Supervised Fine-tuning (SFT): "Learning to Chat"
</h4>
<div class="flex flex-wrap gap-3 mb-4">
<span class="bg-brand-50 text-brand-700 px-3 py-1 rounded-full text-sm font-mono">Target:
Instruction Following</span>
<span class="bg-brand-50 text-brand-700 px-3 py-1 rounded-full text-sm font-mono">Data: Chat
Data (Human-like)</span>
</div>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
<strong>Task:</strong> use dialogue-formatted data (ChatML) to teach the model to talk like an assistant, rather than coldly spitting out labels.
<br>
<strong>State:</strong>
<ul class="list-disc list-inside ml-4 mt-2 text-slate-600">
<li><span class="text-blue-600 font-bold">Vision Encoder:</span> Frozen (usually, for stability)</li>
<li><span class="text-red-600 font-bold">Adapter:</span> Learnable</li>
<li><span class="text-red-600 font-bold">LLM:</span> Learnable</li>
</ul>
</p>
</div>
</div>
</div>
<!-- 4.3 Key Innovation Details -->
<div class="sr-only">

### 4.3 The Core Trick: How Does the Model "Point Where You Ask"? (Grounding)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-brand-500 rounded-full mr-4 shadow-md"></span>
4.3 The Core Trick: How Does the Model "Point Where You Ask"? (Grounding)
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
You may have noticed that one of Qwen-VL's most impressive abilities is <strong>visual grounding</strong>. Ask it "Where is the dog?" and it not only says "on the grass", it also draws you a box
<code>[x1, y1, x2, y2]</code>. How does it do that?
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
<div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
<h4 class="text-xl font-bold text-slate-800 mb-4">🔴 The pain point of traditional approaches</h4>
<p class="text-lg text-slate-600">
A traditional LLM vocabulary has no concept of coordinates at all. If we output numbers like "256, 334..." directly, they get split into several tokens, and it is hard for the model to understand that these tokens represent one continuous position in 2D space.
</p>
</div>
<div class="bg-emerald-50 p-6 rounded-2xl shadow-sm border border-emerald-200">
<h4 class="text-xl font-bold text-emerald-900 mb-4">🟢 Qwen-VL's answer</h4>
<p class="text-lg text-emerald-800">
<strong>Position normalisation + special tokens</strong>.<br>
1. Normalise all coordinates to the range <code>[0, 1000)</code>.<br>
2. Introduce two special symbols, <code>&lt;box&gt;</code> and <code>&lt;/box&gt;</code>.<br>
3. The training data looks like this: <code
class="bg-white px-2 py-1 rounded text-sm">Describe the dog &lt;ref&gt;the dog&lt;/ref&gt;&lt;box&gt;(200,200),(500,600)&lt;/box&gt;</code>
</p>
</div>
</div>
<p class="text-xl text-slate-600 mt-8 leading-relaxed">
This design is extremely clever. It turns a "detection task" into a "language generation task". For an LLM, outputting <code>(200,200)</code> is no different in essence from outputting a word. That is the charm of <strong>next-token
prediction</strong> unifying everything!
</p>
<!-- Transition to Next Section -->
<div class="mt-16 p-6 bg-slate-100 rounded-xl border-l-4 border-slate-400 text-slate-600">
<p class="text-lg font-medium">
<strong>Summary:</strong> Qwen-VL showed that with a good adapter and a staged training strategy, even a 7B language model can achieve SOTA-level
visual understanding. But it still had one regret: <strong>the resolution was fixed (448x448)</strong>, so long images or tall, narrow documents get distorted. The next chapter, Qwen2-VL, solves this problem in a revolutionary way.
</p>
</div>
</div>
</section>
<section id="method-qwen2vl" class="mb-24">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 5 Part 5: Second Stop: Qwen2-VL, or No More Cutting the Foot to Fit the Shoe

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-10 group tracking-tight">
<span
class="bg-gradient-to-br from-blue-500 to-indigo-600 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:-rotate-12 transition-transform duration-300">5</span>
Part 5: Second Stop: Qwen2-VL, or No More Cutting the Foot to Fit the Shoe
</h2>
<!-- Intro Block -->
<div class="mb-12 bg-white p-8 rounded-3xl shadow-premium border border-slate-100 relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-blue-400 via-indigo-500 to-purple-500">
</div>
<div
class="absolute -right-10 -top-10 w-40 h-40 bg-blue-50 rounded-full mix-blend-multiply filter blur-3xl opacity-50">
</div>
<div class="sr-only">

### 🤔 Question for the class: where did Qwen-VL's "short-sightedness" come from?

</div>

<h3 class="text-xl font-bold text-slate-800 mb-4 flex items-center">
<span class="text-2xl mr-2">🤔</span> Question for the class: where did Qwen-VL's "short-sightedness" come from?
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
Everyone, remember Qwen-VL from the last chapter? It was a fine "describe the picture" player, but it had one fatal weakness: <strong>"short-sightedness"</strong>.
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
Whether you give it a tall screenshot of a long social media post or a widescreen IMAX movie poster, it bluntly resizes the image into a <code
class="bg-slate-100 px-2 py-0.5 rounded text-red-600 font-mono font-bold">448×448</code> square.
</p>
<div class="bg-red-50 border-l-4 border-red-400 p-6 rounded-r-lg mb-6">
<p class="text-red-800 font-bold mb-2 text-lg">The consequences are serious:</p>
<ul class="list-disc list-inside text-red-700 space-y-2">
<li><strong>Lost detail:</strong> lots of small text turns into noise once the image is shrunk.</li>
<li><strong>Distorted proportions:</strong> tall, thin people become short and stout, circles become ellipses, and the model's view of the world gets warped.</li>
<li><strong>Wasted compute:</strong> for a small 256x256 image, you have to upscale or pad it to reach 448, wasting precious compute.</li>
</ul>
</div>
<p class="text-lg text-slate-600 leading-relaxed">
<strong>Qwen2-VL's mission is to solve this problem once and for all.</strong> It introduces two killer features that sound academic but are, at heart, very intuitive:
<br><br>
<span
class="inline-flex items-center px-3 py-1 rounded-full text-sm font-bold bg-blue-100 text-blue-800 border border-blue-200 shadow-sm mx-1">Naive
Dynamic Resolution</span>
<span class="text-slate-400 mx-2">+</span>
<span
class="inline-flex items-center px-3 py-1 rounded-full text-sm font-bold bg-purple-100 text-purple-800 border border-purple-200 shadow-sm mx-1">M-RoPE
(Multimodal Rotary Position Embedding)</span>.
</p>
</div>
<!-- 5.1 Naive Dynamic Resolution -->
<div class="sr-only">

### 5.1 Dynamic Resolution (Naive Dynamic Resolution): Handling Images Like Playing Tetris

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center" id="dynamic-resolution">
<span class="w-2 h-10 bg-blue-500 rounded-full mr-4 shadow-md"></span>
5.1 Dynamic Resolution (Naive Dynamic Resolution): Handling Images Like Playing Tetris
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
The most fundamental change in this generation: <strong>we no longer force-resize images!</strong> Or, more precisely, we no longer resize images to one fixed square.
</p>
<p class="text-lg text-slate-600 mb-8 leading-relaxed">
But a Transformer still fundamentally needs a sequence. If images come in different sizes, the number of tokens differs, so how do we squeeze them into the same batch for training? Qwen2-VL
didn't invent some extremely complicated mathematical transform; it came up with a very engineering-minded, very practical method, which we'll call "<strong>dynamic patching</strong>".
</p>
<!-- Concept Explanation -->
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 hover:shadow-md transition-shadow">
<h4 class="font-bold text-slate-800 mb-3 text-lg">Step 1: What does "Naive" mean here?</h4>
<p class="text-slate-600">
It refers to the simplest possible strategy: we still resize the image, but the target is no longer a fixed $H \times W$; it is <strong>the multiple of $14 \times 14$ closest to the original resolution
</strong>.
</p>
<div class="mt-4 p-3 bg-white rounded border border-slate-100 font-mono text-sm text-slate-500">
Input: 100x200<br>
Target: (14*N) x (14*M)<br>
Result: 98x196 (closest)
</div>
</div>
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 hover:shadow-md transition-shadow">
<h4 class="font-bold text-slate-800 mb-3 text-lg">Step 2: 2x2 Pooling (feature compression)</h4>
<p class="text-slate-600">
To cut the token count further, the patch features output by the ViT (14x14) go through a <span class="font-bold text-blue-600">2x2
pooling</span> step. This means every visual token that finally enters the LLM actually represents a <span
class="font-bold text-blue-600">28x28</span> pixel region of the original image.
</p>
</div>
</div>
<!-- SVG Visualization: Dynamic Resolution Process -->
<div class="my-12">
<div class="bg-white rounded-3xl shadow-premium border border-slate-200 p-8 overflow-hidden relative">
<div class="absolute top-0 right-0 w-32 h-32 bg-blue-50 rounded-bl-full opacity-50 pointer-events-none">
</div>
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-10">
🎨 Illustrated in depth: the full transformation from "any image" to "token stream"
</h4>
<div class="flex justify-center overflow-x-auto pb-4">
<svg width="960" height="480" viewBox="0 0 960 480" xmlns="http://www.w3.org/2000/svg"
class="font-sans">
<defs>
<marker id="arrow-blue-lg" markerWidth="12" markerHeight="12" refX="10" refY="4"
orient="auto">
<path d="M0,0 L0,8 L12,4 z" fill="#3b82f6" />
</marker>
<filter id="soft-shadow" x="-50%" y="-50%" width="200%" height="200%">
<feGaussianBlur in="SourceAlpha" stdDeviation="3" />
<feOffset dx="2" dy="2" result="offsetblur" />
<feComponentTransfer>
<feFuncA type="linear" slope="0.2" />
</feComponentTransfer>
<feMerge>
<feMergeNode />
<feMergeNode in="SourceGraphic" />
</feMerge>
</filter>
<pattern id="small-grid" width="14" height="14" patternUnits="userSpaceOnUse">
<path d="M 14 0 L 0 0 0 14" fill="none" stroke="#bfdbfe" stroke-width="0.5" />
</pattern>
<pattern id="large-grid" width="28" height="28" patternUnits="userSpaceOnUse">
<rect width="28" height="28" fill="white" />
<path d="M 28 0 L 0 0 0 28" fill="none" stroke="#60a5fa" stroke-width="1" />
</pattern>
</defs>
<!-- --- STAGE 1: RAW INPUT --- -->
<g transform="translate(50, 120)">
<text x="60" y="-30" text-anchor="middle" font-weight="bold" fill="#334155"
font-size="16">1. Raw input</text>
<text x="60" y="-10" text-anchor="middle" fill="#64748b" font-size="12">Any aspect ratio (e.g.
tall screenshot)</text>
<!-- Raw Image -->
<rect x="0" y="0" width="120" height="240" rx="6" fill="#eff6ff" stroke="#2563eb"
stroke-width="2" filter="url(#soft-shadow)" />
<!-- Content placeholder -->
<path d="M 20 40 L 100 40" stroke="#93c5fd" stroke-width="4" stroke-linecap="round" />
<path d="M 20 60 L 80 60" stroke="#93c5fd" stroke-width="4" stroke-linecap="round" />
<circle cx="60" cy="120" r="20" fill="#dbeafe" />
<path d="M 20 180 L 100 180" stroke="#93c5fd" stroke-width="4" stroke-linecap="round" />
<!-- Dimensions -->
<text x="60" y="260" text-anchor="middle" fill="#1e40af" font-size="12"
font-weight="bold">H_raw × W_raw</text>
</g>
<!-- Arrow 1 -->
<g transform="translate(190, 220)">
<path d="M 0 0 L 40 0" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-blue-lg)"
stroke-dasharray="4,4" />
<text x="20" y="-10" text-anchor="middle" font-size="10" fill="#64748b">Resize to</text>
<text x="20" y="15" text-anchor="middle" font-size="10" fill="#64748b">Grid (14x14)</text>
</g>
<!-- --- STAGE 2: GRID RESIZING --- -->
<g transform="translate(260, 120)">
<text x="70" y="-30" text-anchor="middle" font-weight="bold" fill="#334155"
font-size="16">2. Grid alignment</text>
<text x="70" y="-10" text-anchor="middle" fill="#64748b" font-size="12">Snap to multiples of 14</text>
<!-- Resized Image Container -->
<rect x="0" y="0" width="140" height="224" fill="white" stroke="#3b82f6" stroke-width="2"
filter="url(#soft-shadow)" />
<!-- The Grid -->
<rect x="0" y="0" width="140" height="224" fill="url(#small-grid)" />
<!-- Highlight a Patch -->
<rect x="0" y="0" width="14" height="14" fill="#f59e0b" stroke="#b45309" stroke-width="1"
opacity="0.8" />
<text x="20" y="0" font-size="10" fill="#b45309" font-weight="bold">Patch (14x14)</text>
<!-- Dimensions -->
<text x="70" y="245" text-anchor="middle" fill="#1e40af" font-size="12"
font-weight="bold">H' = 14×M</text>
<text x="70" y="260" text-anchor="middle" fill="#1e40af" font-size="12"
font-weight="bold">W' = 14×N</text>
</g>
<!-- Arrow 2 -->
<g transform="translate(420, 220)">
<path d="M 0 0 L 40 0" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-blue-lg)" />
<text x="20" y="-10" text-anchor="middle" font-size="10" fill="#64748b">ViT Encode</text>
</g>
<!-- --- STAGE 3: ViT + POOLING --- -->
<g transform="translate(480, 100)">
<text x="90" y="-10" text-anchor="middle" font-weight="bold" fill="#334155"
font-size="16">3. ViT & compression</text>
<!-- ViT Box -->
<rect x="20" y="20" width="140" height="60" rx="8" fill="url(#large-grid)" stroke="#4f46e5"
stroke-width="2" filter="url(#soft-shadow)" />
<text x="90" y="55" text-anchor="middle" fill="#4338ca" font-weight="bold"
font-size="14">ViT Encoder</text>
<!-- Down Arrow -->
<path d="M 90 80 L 90 110" stroke="#6366f1" stroke-width="2"
marker-end="url(#arrow-blue-lg)" />
<!-- Pooling Visual -->
<g transform="translate(65, 120)">
<!-- 2x2 Grid input -->
<rect x="0" y="0" width="50" height="50" fill="#e0e7ff" stroke="#6366f1" />
<line x1="25" y1="0" x2="25" y2="50" stroke="#6366f1" />
<line x1="0" y1="25" x2="50" y2="25" stroke="#6366f1" />
<text x="25" y="65" text-anchor="middle" font-size="10" fill="#4338ca">4 Patches</text>
<!-- Combine Arrow -->
<path d="M 55 25 L 75 25" stroke="#6366f1" stroke-width="2"
marker-end="url(#arrow-blue-lg)" />
<!-- 1 Token Output -->
<rect x="85" y="10" width="30" height="30" fill="#818cf8" stroke="#312e81"
stroke-width="2" rx="4" />
<text x="100" y="30" text-anchor="middle" font-size="12" fill="white"
font-weight="bold">T</text>
</g>
<text x="90" y="190" text-anchor="middle" fill="#4f46e5" font-size="12"
font-weight="bold">2x2 Pooling (C-Former)</text>
<text x="90" y="205" text-anchor="middle" fill="#64748b" font-size="10">Much shorter sequence</text>
</g>
<!-- Arrow 3 -->
<g transform="translate(680, 220)">
<path d="M 0 0 L 40 0" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-blue-lg)" />
<text x="20" y="-10" text-anchor="middle" font-size="10" fill="#64748b">Flatten</text>
</g>
<!-- --- STAGE 4: PACKED SEQUENCE --- -->
<g transform="translate(740, 140)">
<text x="100" y="-30" text-anchor="middle" font-weight="bold" fill="#334155"
font-size="16">4. Variable-length sequence</text>
<!-- The Sequence Bar -->
<g transform="translate(0, 20)">
<!-- <vision_start> -->
<path d="M 0 0 L 30 0 L 35 20 L 30 40 L 0 40 L 5 20 Z" fill="#94a3b8" stroke="white" />
<text x="18" y="25" text-anchor="middle" fill="white" font-size="10"
font-weight="bold">&lt;S&gt;</text>
<!-- Visual Tokens -->
<rect x="38" y="0" width="140" height="40" fill="#93c5fd" stroke="#2563eb"
stroke-width="2" />
<text x="108" y="25" text-anchor="middle" fill="#1e40af" font-size="14"
font-weight="bold">Visual Tokens...</text>
<!-- <vision_end> -->
<path d="M 181 0 L 211 0 L 216 20 L 211 40 L 181 40 L 186 20 Z" fill="#94a3b8"
stroke="white" />
<text x="199" y="25" text-anchor="middle" fill="white" font-size="10"
font-weight="bold">&lt;E&gt;</text>
</g>
<text x="105" y="90" text-anchor="middle" fill="#0f172a" font-size="12"
font-weight="bold">Length = (H'×W') / (14×14×4)</text>
<text x="105" y="110" text-anchor="middle" fill="#ef4444" font-size="12"
font-weight="bold">No Padding! No filler!</text>
</g>
</svg>
</div>
<div class="mt-10 grid grid-cols-1 lg:grid-cols-2 gap-8">
<div class="bg-blue-50 p-6 rounded-2xl border border-blue-100">
<h5 class="font-bold text-blue-800 mb-3 text-lg flex items-center">
<span
class="bg-blue-200 text-blue-800 rounded-full w-6 h-6 flex items-center justify-center text-sm mr-2">1</span>
What does "Naive" mean?
</h5>
<p class="text-slate-700 leading-relaxed">
"Naive" here
is modesty. It doesn't mean the algorithm is childish; it means <strong>the strategy is plain</strong>: no complicated object-detection crops, no multi-scale pyramids, just the simplest thing:<br>
<span class="bg-white px-1 font-mono text-blue-700 rounded">Resize to the nearest multiple of 14 -> cut patches ->
feed the ViT</span>.<br>
This simplicity keeps training stable and also makes the engineering implementation (FlashAttention VarLen) possible.
</p>
</div>
<div class="bg-purple-50 p-6 rounded-2xl border border-purple-100">
<h5 class="font-bold text-purple-800 mb-3 text-lg flex items-center">
<span
class="bg-purple-200 text-purple-800 rounded-full w-6 h-6 flex items-center justify-center text-sm mr-2">2</span>
Why the 2x2 pooling works so well
</h5>
<p class="text-slate-700 leading-relaxed">
Why do a 2x2 pooling at the end?<br>
Because the ViT patch size is 14x14, so for high-resolution images the token count explodes (448x448 already gives 1024 tokens).<br>
2x2 pooling halves each side of the feature map (each token now covers 28x28 pixels), so <strong>the token count drops by 75%</strong>! That greatly lightens the LLM's
load while keeping enough visual semantics.
</p>
</div>
</div>
</div>
</div>
<!-- 5.2 M-RoPE -->
<div class="sr-only">

### 5.2 M-RoPE: Giving Tokens a "3D GPS"

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-purple-500 rounded-full mr-4 shadow-md"></span>
5.2 M-RoPE: Giving Tokens a "3D GPS"
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
With resolution solved, we face a thornier problem: <strong>loss of positional awareness</strong>.
</p>
<div class="flex flex-col md:flex-row gap-8 mb-10">
<div class="flex-1">
<p class="text-lg text-slate-600 mb-4">
In a traditional text-only LLM, position is one-dimensional (1st word, 2nd word...). That's simple, and RoPE handles it perfectly.
</p>
<p class="text-lg text-slate-600">
But in Qwen2-VL, visual tokens arrive "flattened". If you flatten a 2D image into a 1D sequence, <strong>the original up-and-down neighbour relations are completely scrambled</strong>. Not to mention video, which is 3D
(time + space); flattening that is a disaster.
</p>
</div>
<div class="flex-1 bg-slate-100 p-6 rounded-xl border-l-4 border-slate-400 italic text-slate-600">
"It's like taking a jigsaw puzzle apart and laying the pieces out in a single row. If you don't write the row and column number on the back of each piece, not even God could put it back together."
</div>
</div>
<div class="bg-slate-900 text-white p-10 rounded-3xl shadow-2xl relative overflow-hidden mb-16 group">
<!-- Background Effects -->
<div
class="absolute top-0 right-0 w-64 h-64 bg-purple-600 rounded-full filter blur-[100px] opacity-20 group-hover:opacity-40 transition-opacity duration-700">
</div>
<div
class="absolute bottom-0 left-0 w-64 h-64 bg-blue-600 rounded-full filter blur-[100px] opacity-20 group-hover:opacity-40 transition-opacity duration-700">
</div>
<h4 class="text-3xl font-bold mb-8 flex items-center relative z-10">
<span class="text-4xl mr-4">🧭</span> The core idea of M-RoPE: decoupling 3D position
</h4>
<p class="text-xl text-slate-300 mb-10 leading-relaxed max-w-3xl relative z-10">
Qwen2-VL's <strong>M-RoPE (Multimodal Rotary Positional Embedding)</strong> takes an approach with real geometric elegance: it introduces no extra
embedding layer, and instead operates directly on the rotation matrix. It <strong>splits each token's embedding vector into three segments</strong>, each controlled by its own rotation matrix, corresponding to time, height and width.
</p>
<!-- M-RoPE Visualization SVG -->
<div class="flex justify-center relative z-10">
<svg width="800" height="360" viewBox="0 0 800 360" xmlns="http://www.w3.org/2000/svg" class="w-full">
<defs>
<marker id="arrowHead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"
markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" />
</marker>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
<feGaussianBlur stdDeviation="3" result="blur" />
<feComposite in="SourceGraphic" in2="blur" operator="over" />
</filter>
</defs>
<!-- The 3D Coordinate System -->
<g transform="translate(150, 250)">
<!-- Center -->
<circle cx="0" cy="0" r="4" fill="#cbd5e1" />
<!-- T-Axis (Up) -->
<line x1="0" y1="0" x2="0" y2="-150" stroke="#a78bfa" stroke-width="3"
marker-end="url(#arrowHead)" />
<text x="10" y="-130" font-weight="bold" fill="#c4b5fd" font-size="14">Time (t)</text>
<!-- H-Axis (Down Left) -->
<line x1="0" y1="0" x2="-120" y2="80" stroke="#60a5fa" stroke-width="3"
marker-end="url(#arrowHead)" />
<text x="-100" y="50" font-weight="bold" fill="#93c5fd" font-size="14">Height (h)</text>
<!-- W-Axis (Right) -->
<line x1="0" y1="0" x2="180" y2="0" stroke="#34d399" stroke-width="3"
marker-end="url(#arrowHead)" />
<text x="160" y="-15" font-weight="bold" fill="#6ee7b7" font-size="14">Width (w)</text>
</g>
<!-- The Vector Split -->
<g transform="translate(450, 80)">
<text x="0" y="-30" font-weight="bold" fill="white" font-size="16">Embedding Vector
Splitting</text>
<!-- Full Vector Container -->
<rect x="0" y="0" width="300" height="60" rx="8" fill="#1e293b" stroke="#475569" />
<!-- Part 1: Time -->
<rect x="0" y="0" width="100" height="60" rx="8" fill="#7c3aed" opacity="0.8" />
<text x="50" y="35" text-anchor="middle" fill="white" font-weight="bold"
font-size="14">Temporal</text>
<text x="50" y="85" text-anchor="middle" fill="#a78bfa" font-size="12">Rotary( t )</text>
<path d="M 50 65 L 50 75" stroke="#a78bfa" stroke-width="2" />
<!-- Part 2: Height -->
<rect x="100" y="0" width="100" height="60" rx="0" fill="#2563eb" opacity="0.8" />
<text x="150" y="35" text-anchor="middle" fill="white" font-weight="bold"
font-size="14">Height</text>
<text x="150" y="85" text-anchor="middle" fill="#93c5fd" font-size="12">Rotary( h )</text>
<path d="M 150 65 L 150 75" stroke="#93c5fd" stroke-width="2" />
<!-- Part 3: Width -->
<rect x="200" y="0" width="100" height="60" rx="8" fill="#059669" opacity="0.8" />
<!-- Mask to square corners -->
<rect x="200" y="0" width="10" height="60" fill="#059669" opacity="0.0" />
<text x="250" y="35" text-anchor="middle" fill="white" font-weight="bold"
font-size="14">Width</text>
<text x="250" y="85" text-anchor="middle" fill="#6ee7b7" font-size="12">Rotary( w )</text>
<path d="M 250 65 L 250 75" stroke="#6ee7b7" stroke-width="2" />
</g>
<!-- Logic Connection -->
<path d="M 150 180 Q 300 50 450 110" stroke="white" stroke-width="2" stroke-dasharray="6,6"
opacity="0.3" fill="none" />
<text x="300" y="100" text-anchor="middle" fill="white" font-size="12" opacity="0.8">Mapping</text>
<!-- Legend -->
<g transform="translate(450, 200)">
<text x="0" y="0" fill="#cbd5e1" font-size="13" font-family="monospace">Total Dim = D</text>
<text x="0" y="25" fill="#a78bfa" font-size="13" font-family="monospace">Section 1: 0 ~ D/3 -->
t</text>
<text x="0" y="50" fill="#93c5fd" font-size="13" font-family="monospace">Section 2: D/3 ~ 2D/3
--> h</text>
<text x="0" y="75" fill="#6ee7b7" font-size="13" font-family="monospace">Section 3: 2D/3 ~ D -->
w</text>
</g>
</svg>
</div>
</div>
<!-- Figure 3 Analysis -->
<div class="my-16">
<div
class="bg-white p-4 rounded-2xl border border-slate-200 shadow-md hover:shadow-xl transition-shadow duration-300">
<h4 class="text-xl font-bold text-slate-800 mb-6 px-4 pt-2">📊 A close reading of the paper's Figure 3</h4>
<div class="overflow-hidden rounded-xl mb-6 border border-slate-100">
<img src="/images/qwen-vlm/image_003.jpg"
alt="M-RoPE Illustration from Paper"
class="w-full object-cover transform hover:scale-105 transition-transform duration-500" />
</div>
<div class="px-4 pb-4">
<div class="prose prose-slate text-slate-600">
<p class="mb-4">
This figure (Figure 3) is the key to understanding M-RoPE. It shows how the three components "collapse" or "activate" under different modalities:
</p>
<ul class="list-none space-y-4 pl-0">
<li class="flex items-start">
<span
class="flex-shrink-0 w-8 h-8 bg-slate-100 rounded-full flex items-center justify-center mr-3 text-lg">📄</span>
<div>
<strong class="text-slate-800 block">Text</strong>
<span class="text-sm">Text is a 1D linear stream. So for the text part, we make the temporal, height and width IDs
<strong>exactly the same</strong> (all equal to the sequence index $i$). This collapses M-RoPE into ordinary 1D
RoPE, staying compatible with the pre-trained language model.</span>
</div>
</li>
<li class="flex items-start">
<span
class="flex-shrink-0 w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-3 text-lg">🖼️</span>
<div>
<strong class="text-blue-800 block">Image</strong>
<span class="text-sm">An image is a static 2D plane. So <strong>the temporal ID is frozen to a constant (say 0)</strong>, while the
height and width IDs change as we scan the pixel grid. This way the model can sense 2D spatial structure.</span>
</div>
</li>
<li class="flex items-start">
<span
class="flex-shrink-0 w-8 h-8 bg-purple-100 rounded-full flex items-center justify-center mr-3 text-lg">🎬</span>
<div>
<strong class="text-purple-800 block">Video</strong>
<span class="text-sm">A video is a stack of images. Here all three dimensions <strong>fire at full power</strong>: the temporal ID gives the frame number (Frame
1, Frame 2...), and within each frame the 2D H/W variation is kept. The model thus gets full 3D spatio-temporal awareness.</span>
</div>
</li>
</ul>
</div>
</div>
</div>
</div>
<!-- Inserted after section 5.2 of the Qwen2-VL chapter, before section 5.3 -->
<div class="my-20">
<div class="sr-only">

### 5.X Going Deeper: The Puzzle of the Adapter's "Reverse Evolution"

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-amber-500 rounded-full mr-4 shadow-md"></span>
5.X Going Deeper: The Puzzle of the Adapter's "Reverse Evolution"
</h3>
<div class="bg-amber-50 border-l-4 border-amber-400 p-8 rounded-r-2xl shadow-sm relative overflow-hidden">
<div class="absolute top-0 right-0 w-32 h-32 bg-amber-100 rounded-bl-full opacity-50"></div>
<h4 class="text-xl font-bold text-amber-900 mb-4 flex items-center">
<span class="text-3xl mr-3">🤔</span> Teacher's Blackboard: why "take a step back"?
</h4>
<p class="text-amber-800 text-lg leading-relaxed mb-6">
Sharp-eyed students may have noticed:
<br>
<strong>Qwen-VL (v1)</strong> used <span class="font-mono bg-white px-1 rounded">Cross-Attention (256
Queries)</span>, which looks sophisticated and compresses an image into a very short sequence.
<br>
<strong>Qwen2-VL (v2)</strong>, however, went back to a simple <span class="font-mono bg-white px-1 rounded">2x2 Pooling +
MLP</span>, which looks like a technical "step backwards".
<br>
<strong>Why?</strong>
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
<!-- Cross-Attention Issue -->
<div class="bg-white p-6 rounded-xl border border-amber-200">
<h5 class="font-bold text-slate-800 mb-2">The cost of cross-attention</h5>
<p class="text-sm text-slate-600">
The queries are a set of <strong>learnable vectors</strong>. Like a swarm of "probes", they roam all over the image features.
<br>
<span class="text-red-500 font-bold">Drawback:</span> they scramble the spatial topology! The position encoding is still there, but the physical intuition that "pixel A is to the left of
pixel B" gets weaker. That is bad news for tasks that need <strong>precise coordinate localisation (grounding)</strong>.
</p>
</div>
<!-- MLP Merger Advantage -->
<div class="bg-white p-6 rounded-xl border border-amber-200">
<h5 class="font-bold text-slate-800 mb-2">The return of the MLP merger</h5>
<p class="text-sm text-slate-600">
2x2 pooling is a <strong>hard-wired connection</strong>. It forces tokens to keep the original 2D spatial structure.
<br>
<span class="text-emerald-600 font-bold">Advantage:</span> there are more tokens (lower compression), but it perfectly preserves the spatial information of "where am I". This is exactly
the secret behind Qwen2-VL's dominance in document parsing and UI operation.
</p>
</div>
</div>
<p class="mt-6 text-amber-900 font-medium italic text-center">
"Sometimes preserving the original physical structure matters more than extracting abstract semantics." (Qwen2-VL's design philosophy)
</p>
</div>
</div>
<!-- 5.3 Model Sizes & Capabilities -->
<div class="sr-only">

### 5.3 New Family Members: 2B / 7B / 72B, from Edge to Cloud

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-green-500 rounded-full mr-4 shadow-md"></span>
5.3 New Family Members: 2B / 7B / 72B, from Edge to Cloud
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Qwen2-VL is no longer a lone soldier: it comes in three sizes, covering everything from on-device phones to cloud supercomputers. There's a very interesting design detail here: <strong>however large the LLM, they all share the same 600M-parameter
vision encoder (ViT)!</strong>
</p>
<p class="text-lg text-slate-600 mb-8 bg-green-50 p-4 rounded-lg border-l-4 border-green-500">
This means even the smallest 2B model has "eyes" as sharp as the 72B model; only the "brain's" ability to process information differs.
</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
<!-- 2B -->
<div
class="bg-white border border-slate-200 rounded-3xl p-8 hover:border-green-400 hover:shadow-xl transition-all duration-300 group relative overflow-hidden">
<div class="absolute top-0 right-0 w-24 h-24 bg-green-50 rounded-bl-full -mr-12 -mt-12 z-0"></div>
<div class="relative z-10">
<div class="text-5xl mb-6 group-hover:scale-110 transition-transform origin-left">📱</div>
<h4 class="text-2xl font-bold text-slate-800 mb-2">Qwen2-VL-2B</h4>
<p class="text-sm text-slate-500 uppercase tracking-wide font-bold mb-6">Edge / Mobile</p>
<ul class="space-y-2 text-slate-600 text-sm">
<li class="flex items-start"><span class="text-green-500 mr-2">✓</span> Runs smoothly on a phone</li>
<li class="flex items-start"><span class="text-green-500 mr-2">✓</span> Document scanning, live translation</li>
<li class="flex items-start"><span class="text-green-500 mr-2">✓</span> No cut in visual perception</li>
</ul>
</div>
</div>
<!-- 7B -->
<div
class="bg-gradient-to-b from-white to-blue-50 border-2 border-blue-400 rounded-3xl p-8 shadow-2xl transform scale-105 z-20 relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-1 bg-blue-500"></div>
<div class="absolute top-4 right-4 bg-blue-500 text-white text-xs font-bold px-3 py-1 rounded-full">
Mainstream</div>
<div class="relative z-10">
<div class="text-5xl mb-6 group-hover:scale-110 transition-transform origin-left">💻</div>
<h4 class="text-2xl font-bold text-blue-900 mb-2">Qwen2-VL-7B</h4>
<p class="text-sm text-blue-600 uppercase tracking-wide font-bold mb-6">Consumer GPU</p>
<ul class="space-y-2 text-slate-700 text-sm font-medium">
<li class="flex items-start"><span class="text-blue-500 mr-2">✓</span> Best value for money</li>
<li class="flex items-start"><span class="text-blue-500 mr-2">✓</span> Runs on a single RTX 3090/4090</li>
<li class="flex items-start"><span class="text-blue-500 mr-2">✓</span> The default pick for most demos and apps</li>
</ul>
</div>
</div>
<!-- 72B -->
<div
class="bg-slate-900 border border-slate-700 rounded-3xl p-8 text-white hover:shadow-2xl hover:border-purple-500 transition-all duration-300 group relative overflow-hidden">
<div class="absolute bottom-0 right-0 w-32 h-32 bg-purple-900 rounded-tl-full -mr-8 -mb-8 opacity-50">
</div>
<div class="relative z-10">
<div class="text-5xl mb-6 group-hover:scale-110 transition-transform origin-left">🚀</div>
<h4 class="text-2xl font-bold text-white mb-2">Qwen2-VL-72B</h4>
<p class="text-sm text-purple-400 uppercase tracking-wide font-bold mb-6">SOTA Killer</p>
<ul class="space-y-2 text-slate-300 text-sm">
<li class="flex items-start"><span class="text-purple-400 mr-2">✓</span> Goes head to head with closed GPT-4V</li>
<li class="flex items-start"><span class="text-purple-400 mr-2">✓</span> Complex long-video analysis</li>
<li class="flex items-start"><span class="text-purple-400 mr-2">✓</span> Agent planning and decision-making</li>
</ul>
</div>
</div>
</div>
<!-- Figure 2 Capabilities -->
<div class="my-16">
<div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-lg">
<h4 class="text-lg font-bold text-slate-700 mb-4 ml-2">🌟 All-round performance (Capabilities Overview)</h4>
<img src="/images/qwen-vlm/image_002.jpg"
alt="Qwen2-VL Capabilities" class="w-full rounded-2xl shadow-inner" />
<p class="mt-4 text-sm text-slate-500 text-center italic px-8">
Figure 2: Overview of Qwen2-VL's capabilities. Whether it is identifying plant species, following a complex plot in a video, solving hard geometry problems or doing multilingual OCR, it handles them with ease.
</p>
</div>
</div>
<!-- Transition -->
<div
class="mt-20 p-8 bg-gradient-to-r from-slate-100 to-white rounded-3xl border-l-8 border-slate-400 text-slate-600 shadow-sm">
<h4 class="text-xl font-bold text-slate-800 mb-3">Chapter summary</h4>
<p class="text-lg font-medium leading-relaxed">
Qwen2-VL cured "short-sightedness" with <strong>Naive Dynamic Resolution</strong> and cured "directional blindness" with <strong>M-RoPE</strong>.
It's like a super assistant whose vision has been corrected, who now wears 3D glasses, and whose IQ is still fully online.
</p>
<p class="text-lg font-medium mt-4 leading-relaxed">
But the story isn't over. Faced with especially complex documents (dense invoices, financial reports) or scenarios that need very strong logical reasoning, it still sometimes "sees more than it can do". At the next stop we meet
<strong>Qwen2.5-VL</strong>, and see how it polishes the details further and becomes a true "document expert".
</p>
</div>
</div>
</section>
<section id="method-qwen25vl" class="mb-24">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 6 Part 6: Third Stop: Qwen2.5-VL, the Detail Fanatic Who Goes from "Can See" to "Masters It"

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-10 group tracking-tight">
<span
class="bg-gradient-to-br from-emerald-500 to-teal-600 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:rotate-12 transition-transform duration-300">6</span>
Part 6: Third Stop: Qwen2.5-VL, the Detail Fanatic Who Goes from "Can See" to "Masters It"
</h2>
<!-- Intro Block -->
<div class="mb-12 bg-white p-8 rounded-3xl shadow-premium border border-slate-100 relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-emerald-400 via-teal-500 to-cyan-500">
</div>
<div
class="absolute -right-10 -bottom-10 w-40 h-40 bg-emerald-50 rounded-full mix-blend-multiply filter blur-3xl opacity-50">
</div>
<div class="sr-only">

### 🥪 Why do we need Qwen2.5-VL?

</div>

<h3 class="text-xl font-bold text-slate-800 mb-4 flex items-center">
<span class="text-2xl mr-2">🥪</span> Why do we need Qwen2.5-VL?
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
If Qwen2-VL solved "can it see images of different shapes clearly", then Qwen2.5-VL sets out to solve <strong>"can it understand the most complicated details"</strong>.
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
In the technical report, the authors use a vivid metaphor: current multimodal models are like <strong>"the cream filling of a sandwich cookie"</strong>. They can do many tasks, but they are still a bite short of the top level (the tasty cookie layers on either side).
</p>
<div class="bg-emerald-50 border-l-4 border-emerald-400 p-6 rounded-r-lg mb-6">
<p class="text-emerald-800 font-medium mb-2">
<strong>Where exactly is that "one bite" missing?</strong>
</p>
<ul class="list-disc list-inside text-emerald-700 space-y-2 text-base">
<li><strong>Document parsing:</strong> dense tables, sheet music and chemical structures used to make earlier models dizzy at first glance.</li>
<li><strong>Precise grounding:</strong> not just drawing a box, but pinpointing individual points and even counting.</li>
<li><strong>Time awareness:</strong> video isn't a slideshow played at constant speed. With fast-forward, slow motion and hour-long videos, how do you locate the moment at 59 minutes 30 seconds?</li>
</ul>
</div>
<p class="text-lg text-slate-600 leading-relaxed">
To fill in this last piece of the puzzle, Qwen2.5-VL brings out four big moves:
<span
class="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-emerald-100 text-emerald-800 mx-1">Native
Dynamic ViT</span>
<span
class="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-teal-100 text-teal-800 mx-1">Window
Attention</span>
<span
class="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-cyan-100 text-cyan-800 mx-1">Absolute
Time M-RoPE</span>
and
<span
class="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-slate-100 text-slate-800 mx-1">4.1T
Tokens Data</span>.
</p>
</div>
<!-- 6.1 Architecture Overview -->
<div class="sr-only">

### 6.1 Architecture Overview: More Native, Better at Time

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-emerald-500 rounded-full mr-4 shadow-md"></span>
6.1 Architecture Overview: More Native, Better at Time
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
First, let's look at a full-body portrait of Qwen2.5-VL (Figure 1). If you compare it carefully with the previous generation, the structure looks similar, but the internals have been replaced.
</p>
<!-- Figure 1 from paper -->
<div class="my-12 bg-white p-4 rounded-2xl border border-slate-200 shadow-lg">
<div class="overflow-hidden rounded-xl">
<img src="/images/qwen-vlm/image_004.jpg"
alt="Qwen2.5-VL Framework"
class="w-full object-cover hover:scale-105 transition-transform duration-500" />
</div>
<p class="mt-4 text-sm text-slate-500 text-center italic">
Figure 1: Qwen2.5-VL architecture. Note the prominent "Native Resolution Input" and "Align with Absolute Time" in the middle.
</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200">
<h4 class="font-bold text-slate-800 mb-4 text-lg flex items-center">
<span class="bg-white p-2 rounded-lg shadow-sm mr-3 text-xl">🖼️</span>
Spatial: Native Dynamic ViT
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
No longer just "slice + resize". Qwen2.5-VL trains from scratch a Vision Transformer that <strong>natively supports dynamic resolution</strong>. It introduces
<strong>window attention</strong>, bringing the cost down from $O(N^2)$, so it can easily swallow 4K or even higher-resolution images.
</p>
</div>
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200">
<h4 class="font-bold text-slate-800 mb-4 text-lg flex items-center">
<span class="bg-white p-2 rounded-lg shadow-sm mr-3 text-xl">⏱️</span>
Temporal: Absolute Time M-RoPE
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
No longer just counting "which frame". Qwen2.5-VL aligns the temporal dimension of M-RoPE with <strong>absolute physical time (seconds)</strong>. Even if the video speeds up and slows down (dynamic FPS), the model knows that this is "second
30" rather than simply "frame 150".
</p>
</div>
</div>
<!-- 6.2 Native Dynamic Resolution & Window Attention -->
<div class="sr-only">

### 6.2 Native Dynamic Resolution: The Evolution from Naive to Native

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-teal-500 rounded-full mr-4 shadow-md"></span>
6.2 Native Dynamic Resolution: The Evolution from Naive to Native
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
Everyone, Qwen2-VL's version is called <strong>Naive</strong> Dynamic Resolution, and Qwen2.5-VL's is called <strong>Native</strong> Dynamic
Resolution. What does that one-letter difference actually change?
</p>
<div class="bg-white p-8 rounded-2xl shadow-premium border border-slate-100 mb-10">
<h4 class="text-xl font-bold text-slate-800 mb-6 text-center">Naive vs. Native: how visual processing evolved</h4>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
<!-- Qwen2-VL (Naive) -->
<div class="relative group">
<div
class="absolute inset-0 bg-red-50 rounded-xl transform rotate-1 transition-transform group-hover:rotate-2">
</div>
<div class="relative bg-white p-6 rounded-xl border-2 border-red-100">
<h5 class="text-lg font-bold text-red-800 mb-2">🔴 Naive (Qwen2-VL)</h5>
<p class="text-sm text-slate-600 mb-4">
Take an off-the-shelf ViT (usually trained at a fixed resolution) and force images of different proportions into patches to feed it.
</p>
<div class="bg-red-50 p-3 rounded border border-red-100 text-xs font-mono text-red-700">
Attention = Global (Full N²)
</div>
<p class="text-sm text-slate-500 mt-2">
<strong>Pain point:</strong> if the image is too large (say a long document), the token count explodes and global attention blows straight through GPU memory.
</p>
</div>
</div>
<!-- Qwen2.5-VL (Native) -->
<div class="relative group">
<div
class="absolute inset-0 bg-emerald-50 rounded-xl transform -rotate-1 transition-transform group-hover:-rotate-2">
</div>
<div class="relative bg-white p-6 rounded-xl border-2 border-emerald-100">
<h5 class="text-lg font-bold text-emerald-800 mb-2">🟢 Native (Qwen2.5-VL)</h5>
<p class="text-sm text-slate-600 mb-4">
Train a ViT from scratch that is used to variable-length input from birth, and add <strong>window attention</strong> inside it.
</p>
<div
class="bg-emerald-50 p-3 rounded border border-emerald-100 text-xs font-mono text-emerald-700">
Attention = Windowed (Linear O(N))
</div>
<p class="text-sm text-slate-500 mt-2">
<strong>Advantage:</strong> cut the image into 112x112 windows. Most layers only look inside their window; only a few layers look globally. Compute cost drops sharply!
</p>
</div>
</div>
</div>
</div>
<!-- SVG: Window Attention -->
<div class="my-12">
<div class="bg-slate-50 rounded-3xl p-8 border border-slate-200 shadow-inner">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
🪟 Illustrated: how window attention saves GPU memory
</h4>
<div class="flex justify-center overflow-x-auto">
<svg width="800" height="400" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg"
class="font-sans">
<defs>
<pattern id="patch-grid" width="20" height="20" patternUnits="userSpaceOnUse">
<path d="M 20 0 L 0 0 0 20" fill="none" stroke="#cbd5e1" stroke-width="0.5" />
</pattern>
<marker id="arrow-teal" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#0d9488" />
</marker>
</defs>
<!-- Image Input -->
<g transform="translate(50, 50)">
<text x="100" y="-10" text-anchor="middle" font-weight="bold" fill="#334155">Input Feature
Map</text>
<rect x="0" y="0" width="200" height="200" fill="white" stroke="#475569" stroke-width="2" />
<rect x="0" y="0" width="200" height="200" fill="url(#patch-grid)" />
<!-- Windows -->
<g stroke="#0d9488" stroke-width="2" fill="none" stroke-dasharray="4 2">
<rect x="0" y="0" width="100" height="100" />
<rect x="100" y="0" width="100" height="100" />
<rect x="0" y="100" width="100" height="100" />
<rect x="100" y="100" width="100" height="100" />
</g>
<text x="50" y="50" text-anchor="middle" fill="#0d9488" font-size="12" opacity="0.5">Window
1</text>
<text x="150" y="150" text-anchor="middle" fill="#0d9488" font-size="12"
opacity="0.5">Window 4</text>
</g>
<!-- Attention Matrix Comparison -->
<g transform="translate(350, 50)">
<!-- Global Attention -->
<g transform="translate(0, 0)">
<text x="80" y="-10" text-anchor="middle" font-weight="bold" fill="#ef4444">Global Attn
(Full)</text>
<rect x="0" y="0" width="160" height="160" fill="#fee2e2" stroke="#ef4444"
stroke-width="2" />
<text x="80" y="80" text-anchor="middle" fill="#b91c1c" font-size="14">Dense
O(N²)</text>
</g>
<!-- Window Attention -->
<g transform="translate(220, 0)">
<text x="80" y="-10" text-anchor="middle" font-weight="bold" fill="#059669">Window Attn
(Sparse)</text>
<rect x="0" y="0" width="160" height="160" fill="#f1f5f9" stroke="#cbd5e1"
stroke-width="2" />
<!-- Block Diagonal -->
<rect x="0" y="0" width="40" height="40" fill="#d1fae5" stroke="#059669" />
<rect x="40" y="40" width="40" height="40" fill="#d1fae5" stroke="#059669" />
<rect x="80" y="80" width="40" height="40" fill="#d1fae5" stroke="#059669" />
<rect x="120" y="120" width="40" height="40" fill="#d1fae5" stroke="#059669" />
<text x="100" y="40" text-anchor="middle" fill="#059669" font-size="14">Masked
(0)</text>
</g>
</g>
<!-- Description -->
<g transform="translate(50, 300)">
<text x="0" y="0" font-size="14" fill="#334155">
<tspan x="0" dy="0" font-weight="bold">Deep Insight:</tspan>
<tspan x="0" dy="25">Most ViT layers only exchange information inside a window (e.g. 112x112).</tspan>
<tspan x="0" dy="25">Only a few layers (Full Attention Block Indexes) break the windows and go global.</tspan>
<tspan x="0" dy="25">This keeps fine local detail while greatly reducing GPU memory use.</tspan>
</text>
</g>
</svg>
</div>
</div>
</div>
<!-- 6.3 Absolute Time M-RoPE -->
<div class="sr-only">

### 6.3 Absolute Time Encoding: Solving the "Variable-Speed Motion" Problem

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-cyan-500 rounded-full mr-4 shadow-md"></span>
6.3 Absolute Time Encoding: Solving the "Variable-Speed Motion" Problem
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
Qwen2-VL used M-RoPE to introduce a temporal ID, which was a huge step forward. But the old temporal ID was based on <strong>frame index</strong>: frame 1, frame 2
...
</p>
<p class="text-lg text-slate-600 mb-8">
<strong>What's the problem with that?</strong> In real life, the video sampling rate (FPS) changes!
<br>
<span class="bg-slate-100 px-2 py-1 rounded text-sm">Scenario A:</span> sample 1 frame per second. Frame 5 means second 5.
<br>
<span class="bg-slate-100 px-2 py-1 rounded text-sm">Scenario B:</span> sample 5 frames per second. Frame 5 means second 1.
<br>
If the model only knows "this is frame 5", it has no idea how much time that represents.
</p>
<!-- SVG: Absolute Time -->
<div class="my-12">
<div class="bg-white rounded-3xl shadow-premium border border-slate-200 p-8">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
⏱️ Illustrated: Relative Index vs. Absolute Time
</h4>
<div class="flex justify-center overflow-x-auto">
<svg width="800" height="350" viewBox="0 0 800 350" xmlns="http://www.w3.org/2000/svg"
class="font-sans">
<defs>
<marker id="arrow-time" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#64748b" />
</marker>
</defs>
<!-- Old Way: Frame Index -->
<g transform="translate(50, 50)">
<text x="0" y="0" font-weight="bold" fill="#ef4444" font-size="16">Old: Frame Index</text>
<!-- Timeline -->
<line x1="0" y1="40" x2="700" y2="40" stroke="#cbd5e1" stroke-width="2"
marker-end="url(#arrow-time)" />
<!-- Video A (1 FPS) -->
<g transform="translate(0, 40)">
<circle cx="50" cy="0" r="6" fill="#fca5a5" />
<text x="50" y="-15" text-anchor="middle" font-size="12" fill="#b91c1c">ID:1</text>
<circle cx="150" cy="0" r="6" fill="#fca5a5" />
<text x="150" y="-15" text-anchor="middle" font-size="12" fill="#b91c1c">ID:2</text>
<text x="600" y="0" text-anchor="start" font-size="12" fill="#ef4444">Video A
(Slow)</text>
</g>
<!-- Video B (2 FPS) -->
<g transform="translate(0, 80)">
<line x1="0" y1="0" x2="700" y2="0" stroke="#cbd5e1" stroke-width="2"
marker-end="url(#arrow-time)" />
<circle cx="50" cy="0" r="6" fill="#fda4af" />
<text x="50" y="-15" text-anchor="middle" font-size="12" fill="#be123c">ID:1</text>
<circle cx="100" cy="0" r="6" fill="#fda4af" />
<text x="100" y="-15" text-anchor="middle" font-size="12" fill="#be123c">ID:2</text>
<text x="600" y="0" text-anchor="start" font-size="12" fill="#be123c">Video B
(Fast)</text>
</g>
<text x="350" y="120" text-anchor="middle" font-size="14" fill="#b91c1c"
font-style="italic">
"ID:2 means 2 s on top but 1 s below. The model is lost!"
</text>
</g>
<!-- New Way: Absolute Time -->
<g transform="translate(50, 220)">
<text x="0" y="0" font-weight="bold" fill="#059669" font-size="16">New: Absolute Time
(Qwen2.5-VL)</text>
<!-- Timeline -->
<line x1="0" y1="40" x2="700" y2="40" stroke="#0d9488" stroke-width="3"
marker-end="url(#arrow-time)" />
<!-- Time Markers -->
<line x1="50" y1="35" x2="50" y2="45" stroke="#0f766e" stroke-width="2" />
<text x="50" y="65" text-anchor="middle" font-size="12" fill="#0f766e">1.0s</text>
<line x1="150" y1="35" x2="150" y2="45" stroke="#0f766e" stroke-width="2" />
<text x="150" y="65" text-anchor="middle" font-size="12" fill="#0f766e">3.0s</text>
<!-- Frames mapped to physical time -->
<circle cx="50" cy="40" r="8" fill="#34d399" stroke="#065f46" stroke-width="2" />
<text x="50" y="25" text-anchor="middle" font-size="12" fill="#065f46"
font-weight="bold">ID: X</text>
<circle cx="150" cy="40" r="8" fill="#34d399" stroke="#065f46" stroke-width="2" />
<text x="150" y="25" text-anchor="middle" font-size="12" fill="#065f46"
font-weight="bold">ID: Y</text>
<text x="350" y="100" text-anchor="middle" font-size="14" fill="#047857"
font-style="italic">
"IDs map straight to physical time. At any sampling rate, 1 s is 1 s!"
</text>
</g>
</svg>
</div>
</div>
</div>
<p class="text-lg text-slate-600 mb-8">
Qwen2.5-VL ties the temporal ID
directly to <strong>absolute time (seconds)</strong>. This way the model understands not only "what comes first" but also "how fast things move". That is crucial for understanding long videos (such as an hour-long film).
</p>
<!-- 6.4 Data: The Soul of Qwen2.5-VL -->
<div class="sr-only">

### 6.4 Data Engineering: Not Just "More", but "Better"

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-cyan-500 rounded-full mr-4 shadow-md"></span>
6.4 Data Engineering: Not Just "More", but "Better"
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
The architecture is just the skeleton; data is the soul. Qwen2.5-VL's pre-training data reached a staggering <strong>4.1 trillion tokens</strong> (more than three times Qwen2-VL's).
</p>
<p class="text-lg text-slate-600 mb-8">
But what deserves more attention is how it built the data for its <strong>special abilities</strong>.
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
<!-- Doc Omni-Parsing -->
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 hover:border-cyan-300 transition-colors">
<h4 class="font-bold text-slate-800 mb-3 flex items-center">
<span class="text-2xl mr-2">📄</span> Document Omni-Parsing
</h4>
<p class="text-sm text-slate-600 mb-3">
To turn the model into an "all-round document reader", the Qwen team synthesised a large amount of document data in <strong>HTML format</strong>.
</p>
<div
class="bg-white p-3 rounded border border-slate-200 font-mono text-xs text-slate-500 overflow-x-auto">
&lt;html&gt;&lt;body&gt;<br>
# paragraph<br>
&lt;p bbox="x1 y1 x2 y2"&gt; content &lt;/p&gt;<br>
# table<br>
&lt;table bbox="..."&gt; ... &lt;/table&gt;<br>
...
</div>
<p class="text-sm text-slate-600 mt-3">
<strong>Key Innovation:</strong> every piece of content (text, tables, formulas) carries a bounding box. The model learns not only to read characters but also the layout.
</p>
</div>
<!-- Grounding -->
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 hover:border-emerald-300 transition-colors">
<h4 class="font-bold text-slate-800 mb-3 flex items-center">
<span class="text-2xl mr-2">🎯</span> Absolute Grounding
</h4>
<p class="text-sm text-slate-600 mb-3">
To support high-precision grounding, Qwen2.5-VL uses <strong>absolute coordinates</strong> (based on the original resolution) instead of the earlier normalised coordinates (0-1000).
</p>
<p class="text-sm text-slate-600">
The data sources are serious stuff:
<ul class="list-disc list-inside mt-2 text-xs text-slate-500">
<li>PixMo (Pointing & Counting)</li>
<li>Synthetic Data from Grounding DINO & SAM</li>
<li>Oven-Vocabulary Detection Data</li>
</ul>
</p>
</div>
</div>
<!-- 6.5 Performance -->
<div class="sr-only">

### 6.5 Showing Its Strength: A Leap in DocVQA and Agent Abilities

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
6.5 Showing Its Strength: A Leap in DocVQA and Agent Abilities
</h3>
<p class="text-xl text-slate-600 mb-8">
In the Qwen2.5-VL technical report, the most eye-catching results are in <strong>document understanding</strong> and <strong>agent</strong> abilities.
</p>
<div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm mb-12">
<h4 class="text-lg font-bold text-slate-800 mb-4">🏆 DocVQA & InfoVQA report card</h4>
<div class="overflow-x-auto">
<table class="min-w-full text-sm text-left text-slate-600">
<thead class="text-xs text-slate-700 uppercase bg-slate-50">
<tr>
<th class="px-6 py-3">Model</th>
<th class="px-6 py-3">DocVQA (test)</th>
<th class="px-6 py-3">InfoVQA (test)</th>
<th class="px-6 py-3">ChartQA (test)</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-slate-100">
<td class="px-6 py-4 font-medium text-slate-900">GPT-4o</td>
<td class="px-6 py-4">91.1</td>
<td class="px-6 py-4">80.7</td>
<td class="px-6 py-4">86.7</td>
</tr>
<tr class="border-b border-slate-100">
<td class="px-6 py-4 font-medium text-slate-900">Claude 3.5 Sonnet</td>
<td class="px-6 py-4">95.2</td>
<td class="px-6 py-4">74.3</td>
<td class="px-6 py-4">90.8</td>
</tr>
<tr class="bg-emerald-50 border-b border-emerald-100">
<td class="px-6 py-4 font-bold text-emerald-900">Qwen2.5-VL-72B</td>
<td class="px-6 py-4 font-bold text-emerald-700">96.4 👑</td>
<td class="px-6 py-4 font-bold text-emerald-700">87.3 👑</td>
<td class="px-6 py-4 font-bold text-emerald-700">89.5</td>
</tr>
</tbody>
</table>
</div>
<p class="mt-4 text-xs text-slate-500 text-right">
* Source: Technical Report Table 5
</p>
</div>
<p class="text-lg text-slate-600 leading-relaxed mb-6">
On DocVQA, Qwen2.5-VL-72B reached a remarkable <span class="font-bold text-emerald-600">96.4</span>,
which shows that when it comes to document details it has already surpassed most closed-source models.
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-12">
On top of that, on <strong>agent</strong>-related benchmarks (such as Android World and OSWorld), Qwen2.5-VL
also shows impressive decision-making. This comes from bringing large amounts of GUI screenshots and action traces into the training data.
</p>
<!-- Transition -->
<div
class="mt-20 p-8 bg-gradient-to-r from-slate-100 to-white rounded-3xl border-l-8 border-slate-400 text-slate-600 shadow-sm">
<h4 class="text-xl font-bold text-slate-800 mb-3">Chapter summary</h4>
<p class="text-lg font-medium leading-relaxed">
Qwen2.5-VL is a "refinement" revolution in the Qwen-VL family.
<br>It uses <strong>Native Dynamic Resolution + Window Attention</strong> to solve compute efficiency at ultra-high resolution;
<br>it uses <strong>Absolute Time M-RoPE</strong> to solve time awareness in long videos;
<br>it uses <strong>DocOmni Data</strong> to solve structured understanding of complex documents.
</p>
<p class="text-lg font-medium mt-4 leading-relaxed text-slate-500">
At this point we seem to have pushed perception as far as it goes. But if we want to handle <strong>ultra-long contexts of hundreds of thousands of tokens</strong>, or carry out <strong>complex logical reasoning (Thinking
Mode)</strong>, is the existing architecture still enough?
<br>
Next stop, the final form: <strong>Qwen3-VL</strong> takes the stage.
</p>
</div>
</div>
</section>
<section id="method-qwen3vl" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 6 Fourth Stop: Qwen3-VL, the Final Form: 256K Context and DeepStack Change the Game

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-purple-600 to-pink-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:scale-110 transition-transform duration-300">6</span>
<div class="flex flex-col">
<span
class="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600">Fourth Stop: Qwen3-VL</span>
<span class="text-2xl text-slate-500 font-medium mt-2">The final form: 256K context and DeepStack change the game</span>
</div>
</h2>
<!-- Intro Block -->
<div class="mb-16 bg-white p-10 rounded-[2rem] shadow-premium border border-slate-100 relative overflow-hidden">
<!-- Decorative Background Elements -->
<div
class="absolute top-0 right-0 w-[400px] h-[400px] bg-purple-50 rounded-full mix-blend-multiply filter blur-[80px] opacity-60 animate-pulse">
</div>
<div
class="absolute bottom-0 left-0 w-[300px] h-[300px] bg-pink-50 rounded-full mix-blend-multiply filter blur-[60px] opacity-60">
</div>
<div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-full h-full bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMSIgY3k9IjEiIHI9IjEiIGZpbGw9InJnYmEoMjAwL 200L 255, 0.2)"
/]')] opacity-50"></div>
<div class="sr-only">

### 🚀 The Leap from "Understanding" to "Thinking"

</div>

<h3 class="text-2xl font-bold text-slate-800 mb-6 flex items-center relative z-10">
<span class="text-3xl mr-3">🚀</span> The leap from "understanding" to "thinking"
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
Everyone, if we compare Qwen2.5-VL to a sharp-eyed "document expert" who misses nothing, then Qwen3-VL
is a "sage" with <strong>near-limitless memory</strong> who <strong>thinks things through</strong>.
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
In this generation, the Qwen team is no longer content to "see clearly" one image or a few seconds of video; they go after three "holy grails" of the multimodal field:
</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 relative z-10">
<div
class="bg-white/80 backdrop-blur-sm p-5 rounded-xl border border-purple-100 shadow-sm hover:shadow-md transition-all group">
<div class="text-3xl mb-3 group-hover:-translate-y-1 transition-transform">📚</div>
<h4 class="font-bold text-purple-900 mb-2">Native 256K context</h4>
<p class="text-sm text-slate-600">Not just a simple RoPE extension: from the start of training, the model gets used to "devouring" whole books and whole films. At this scale, vision and text are truly free to interleave.
</p>
</div>
<div
class="bg-white/80 backdrop-blur-sm p-5 rounded-xl border border-pink-100 shadow-sm hover:shadow-md transition-all group">
<div class="text-3xl mb-3 group-hover:-translate-y-1 transition-transform">🧠</div>
<h4 class="font-bold text-pink-900 mb-2">System 2 Thinking</h4>
<p class="text-sm text-slate-600">Introduces a "slow thinking" mode similar to OpenAI o1. Faced with a hard geometry problem or reasoning task, the model first generates a long chain of thought (CoT) and then gives the answer.
</p>
</div>
<div
class="bg-white/80 backdrop-blur-sm p-5 rounded-xl border border-indigo-100 shadow-sm hover:shadow-md transition-all group">
<div class="text-3xl mb-3 group-hover:-translate-y-1 transition-transform">🏗️</div>
<h4 class="font-bold text-indigo-900 mb-2">DeepStack architecture</h4>
<p class="text-sm text-slate-600">Breaks with the tradition of "injecting vision only at the input layer" and builds a "visual highway" straight into the deep layers. An important small innovation in large-model architecture.</p>
</div>
</div>
</div>
<!-- 7.1 Architecture Deep Dive -->
<div class="sr-only">

### 7.1 Architectural Innovation: DeepStack and the "Seepage" of Visual Signals

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-10 flex items-center">
<span class="w-2 h-10 bg-purple-600 rounded-full mr-4 shadow-md"></span>
7.1 Architectural Innovation: DeepStack and the "Seepage" of Visual Signals
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Let's first look at this extremely important architecture diagram (Figure 1). Please focus on the seemingly complicated connection structure on the far right: that is <strong>DeepStack</strong>.
</p>
<!-- Figure 1 Original Image -->
<div
class="my-12 bg-white p-4 rounded-2xl border border-slate-200 shadow-lg hover:shadow-xl transition-shadow duration-500">
<div class="overflow-hidden rounded-xl bg-slate-50">
<img src="/images/qwen-vlm/image_005.jpg"
alt="Qwen3-VL Architecture"
class="w-full object-contain hover:scale-[1.02] transition-transform duration-500" />
</div>
<p class="mt-4 text-sm text-slate-500 text-center italic border-t border-slate-100 pt-3">
Figure 1: Qwen3-VL architecture overview. Note the dashed box on the right: visual features are no longer a one-off delivery, but are injected layer by layer at different depths of the LLM.
</p>
</div>
<div class="mb-12 prose prose-slate text-slate-600">
<p class="font-bold text-lg text-slate-800">Why do we need DeepStack? (The Vanishing Vision Problem)</p>
<p>
Traditional LVLMs (such as LLaVA and Qwen-VL v1/v2) usually adopt an <strong>"early fusion"</strong> strategy: visual tokens and text tokens are concatenated and fed together into the LLM's
first layer.
</p>
<p>
But as LLMs get deeper and deeper (Qwen2.5-72B has 80 layers!), the low-level visual signal, after passing through dozens of layers of self-attention and FFN
transformations, is gradually diluted or even drowned out by "language patterns". It's like looking at a picture in first grade and then being asked, in a PhD thesis written after 80 years of schooling, to describe its details: you'd have forgotten it all long ago.
</p>
<p>
<strong>DeepStack's solution:</strong> if you're afraid of forgetting, "take a few more looks".
</p>
</div>
<!-- DeepStack Mechanism SVG -->
<div class="my-16">
<div class="bg-slate-50 rounded-[2.5rem] p-10 border border-slate-200 shadow-inner relative">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-10">
🏗️ Illustrated in depth: DeepStack's "gradient highway"
</h4>
<div class="flex justify-center overflow-x-auto pb-6">
<svg width="900" height="500" viewBox="0 0 900 500" xmlns="http://www.w3.org/2000/svg"
class="font-sans">
<defs>
<marker id="arrow-purple" markerWidth="10" markerHeight="10" refX="9" refY="3"
orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#7c3aed" />
</marker>
<marker id="arrow-gray" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
<path d="M0,0 L0,6 L7,3 z" fill="#94a3b8" />
</marker>
<linearGradient id="vit-grad" x1="0%" y1="0%" x2="0%" y2="100%">
<stop offset="0%" style="stop-color:#dcfce7;stop-opacity:1" />
<stop offset="100%" style="stop-color:#16a34a;stop-opacity:1" />
</linearGradient>
<linearGradient id="llm-grad" x1="0%" y1="0%" x2="0%" y2="100%">
<stop offset="0%" style="stop-color:#f3e8ff;stop-opacity:1" />
<stop offset="100%" style="stop-color:#7c3aed;stop-opacity:1" />
</linearGradient>
</defs>
<!-- Vision Encoder (SigLIP-2) -->
<g transform="translate(50, 50)">
<text x="60" y="-15" text-anchor="middle" font-weight="bold" fill="#15803d"
font-size="14">Vision Encoder (SigLIP-2)</text>
<!-- Tower -->
<rect x="20" y="0" width="80" height="400" rx="8" fill="url(#vit-grad)" stroke="#166534"
stroke-width="2" />
<!-- Layer Levels -->
<line x1="20" y1="100" x2="100" y2="100" stroke="white" stroke-width="1"
stroke-dasharray="4" />
<line x1="20" y1="200" x2="100" y2="200" stroke="white" stroke-width="1"
stroke-dasharray="4" />
<line x1="20" y1="300" x2="100" y2="300" stroke="white" stroke-width="1"
stroke-dasharray="4" />
<text x="60" y="50" text-anchor="middle" fill="#064e3b" font-size="12"
font-weight="bold">High Level</text>
<text x="60" y="350" text-anchor="middle" fill="white" font-size="12" font-weight="bold">Low
Level</text>
</g>
<!-- LLM Backbone -->
<g transform="translate(600, 50)">
<text x="60" y="-15" text-anchor="middle" font-weight="bold" fill="#5b21b6"
font-size="14">LLM Backbone (Qwen3)</text>
<!-- Tower -->
<rect x="20" y="0" width="80" height="400" rx="8" fill="url(#llm-grad)" stroke="#5b21b6"
stroke-width="2" />
<!-- Injection Points (Blocks) -->
<rect x="10" y="80" width="100" height="40" rx="4" fill="#ffffff" stroke="#7c3aed"
stroke-width="2" />
<text x="60" y="105" text-anchor="middle" fill="#7c3aed" font-size="12"
font-weight="bold">Block N</text>
<rect x="10" y="180" width="100" height="40" rx="4" fill="#ffffff" stroke="#7c3aed"
stroke-width="2" />
<text x="60" y="205" text-anchor="middle" fill="#7c3aed" font-size="12"
font-weight="bold">Block M</text>
<rect x="10" y="280" width="100" height="40" rx="4" fill="#ffffff" stroke="#7c3aed"
stroke-width="2" />
<text x="60" y="305" text-anchor="middle" fill="#7c3aed" font-size="12"
font-weight="bold">Block 1</text>
</g>
<!-- The Bridges (DeepStack Connections) -->
<g transform="translate(0, 0)">
<!-- Bridge 1 (Low) -->
<path d="M 100 300 C 250 300, 350 300, 500 300" stroke="#fbbf24" stroke-width="3"
fill="none" />
<rect x="300" y="280" width="100" height="40" rx="6" fill="#fffbeb" stroke="#f59e0b"
stroke-width="2" />
<text x="350" y="305" text-anchor="middle" fill="#b45309" font-size="12"
font-weight="bold">Merger (MLP)</text>
<line x1="400" y1="300" x2="610" y2="300" stroke="#f59e0b" stroke-width="2"
marker-end="url(#arrow-purple)" stroke-dasharray="5,5" />
<!-- Bridge 2 (Mid) -->
<path d="M 100 200 C 250 200, 350 200, 500 200" stroke="#fbbf24" stroke-width="3"
fill="none" />
<rect x="300" y="180" width="100" height="40" rx="6" fill="#fffbeb" stroke="#f59e0b"
stroke-width="2" />
<text x="350" y="205" text-anchor="middle" fill="#b45309" font-size="12"
font-weight="bold">Merger (MLP)</text>
<line x1="400" y1="200" x2="610" y2="200" stroke="#f59e0b" stroke-width="2"
marker-end="url(#arrow-purple)" stroke-dasharray="5,5" />
<!-- Bridge 3 (High) -->
<path d="M 100 100 C 250 100, 350 100, 500 100" stroke="#fbbf24" stroke-width="3"
fill="none" />
<rect x="300" y="80" width="100" height="40" rx="6" fill="#fffbeb" stroke="#f59e0b"
stroke-width="2" />
<text x="350" y="105" text-anchor="middle" fill="#b45309" font-size="12"
font-weight="bold">Merger (MLP)</text>
<line x1="400" y1="100" x2="610" y2="100" stroke="#f59e0b" stroke-width="2"
marker-end="url(#arrow-purple)" stroke-dasharray="5,5" />
</g>
<!-- Gradient Highway Annotation -->
<g transform="translate(750, 200)">
<text x="0" y="0" font-size="14" fill="#64748b" font-weight="bold">Backprop path</text>
<path d="M -20 20 L -60 20" stroke="#ef4444" stroke-width="3"
marker-end="url(#arrow-gray)" />
<text x="0" y="25" font-size="12" fill="#ef4444">Gradient Highway</text>
<path d="M -140 0 Q -200 0 -240 0" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"
opacity="0.6" />
</g>
<!-- Insight Box -->
<g transform="translate(50, 440)">
<rect x="0" y="0" width="800" height="50" rx="8" fill="#f1f5f9" stroke="#cbd5e1" />
<text x="20" y="30" font-size="14" fill="#334155">
<tspan font-weight="bold" fill="#7c3aed">Mechanism:</tspan> multi-level Vision Encoder
features, each via its own Merger, are
<tspan font-weight="bold">added</tspan> to LLM hidden states. No extra tokens, more depth.
</text>
</g>
</svg>
</div>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
<div class="bg-purple-50 p-6 rounded-2xl border border-purple-100">
<h5 class="font-bold text-purple-900 mb-3 flex items-center">
<span class="text-xl mr-2">🎯</span> What it solves
</h5>
<ul class="list-disc list-inside text-slate-700 text-sm space-y-2">
<li><strong>Forgetting:</strong> it ensures the LLM's deep layers (responsible for complex reasoning) can directly access the original visual features, instead of relying only on "second-hand information" passed up from earlier layers.</li>
<li><strong>Vanishing gradients:</strong> during training, gradients can flow back to the vision encoder directly through these lateral shortcuts, speeding up convergence.</li>
</ul>
</div>
<div class="bg-amber-50 p-6 rounded-2xl border border-amber-100">
<h5 class="font-bold text-amber-900 mb-3 flex items-center">
<span class="text-xl mr-2">⚡</span> A clever design detail
</h5>
<p class="text-slate-700 text-sm leading-relaxed">
Note that DeepStack <strong>adds</strong> the visual tokens to the LLM's hidden states, or injects them as the
key/value of a cross-attention (depending on the implementation; Qwen3-VL uses a residual connection). That means it <strong>does not increase the LLM's context
length</strong>! At inference time, this is a nearly free performance boost.
</p>
</div>
</div>
<!-- 7.2 Interleaved MRoPE -->
<div class="sr-only">

### 7.2 Interleaved MRoPE: Rebalancing the Frequency Spectrum

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-pink-500 rounded-full mr-4 shadow-md"></span>
7.2 Interleaved MRoPE: Rebalancing the Frequency Spectrum
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
Qwen2-VL's M-RoPE was already strong, but ultra-long video understanding exposed a hidden flaw: <strong>spectral imbalance</strong>.
</p>
<div class="bg-slate-50 p-6 rounded-xl border-l-4 border-pink-400 mb-10">
<h4 class="text-lg font-bold text-slate-800 mb-2">🧐 What is spectral imbalance?</h4>
<p class="text-slate-600 text-sm">
A property of RoPE: the first dimensions of the embedding vector correspond to high-frequency rotations (attending to local position), and the later dimensions to low-frequency rotations (attending to global, long-range distance).
<br>
In Qwen2-VL, we split the vector like this: <code>[time T | height H | width W]</code>.
<br>
This means: <strong>temporal information T always occupies the high-frequency band, while spatial information W always occupies the low-frequency band.</strong>
<br>
The result: the model is sensitive to "local changes in time" but weak at sensing "long-range temporal dependencies" (because the low-frequency band is taken by H and W). That is very bad for long-video understanding.
</p>
</div>
<!-- SVG: Interleaved MRoPE -->
<div class="my-12">
<div class="bg-white rounded-3xl shadow-premium border border-slate-200 p-8">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
🌊 Illustrated: the "weaving" of Interleaved MRoPE
</h4>
<div class="flex justify-center overflow-x-auto">
<svg width="800" height="300" viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg"
class="font-sans">
<defs>
<linearGradient id="freq-grad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" style="stop-color:#fca5a5;stop-opacity:1" /> <!-- High Freq -->
<stop offset="100%" style="stop-color:#93c5fd;stop-opacity:1" /> <!-- Low Freq -->
</linearGradient>
</defs>
<!-- Frequency Bar Background -->
<rect x="50" y="40" width="700" height="20" fill="url(#freq-grad)" rx="10" opacity="0.3" />
<text x="50" y="30" font-size="12" fill="#ef4444" font-weight="bold">High Frequency
(Local)</text>
<text x="750" y="30" font-size="12" fill="#3b82f6" text-anchor="end" font-weight="bold">Low
Frequency (Global)</text>
<!-- Old Approach: Block-wise -->
<g transform="translate(50, 80)">
<text x="-20" y="35" text-anchor="end" font-weight="bold" fill="#64748b">Old (Block):</text>
<!-- T Block -->
<rect x="0" y="0" width="233" height="50" fill="#fcd34d" stroke="#d97706"
stroke-width="2" />
<text x="116" y="30" text-anchor="middle" font-weight="bold" fill="#b45309">Time (T)</text>
<!-- H Block -->
<rect x="233" y="0" width="233" height="50" fill="#86efac" stroke="#16a34a"
stroke-width="2" />
<text x="350" y="30" text-anchor="middle" font-weight="bold" fill="#15803d">Height
(H)</text>
<!-- W Block -->
<rect x="466" y="0" width="234" height="50" fill="#93c5fd" stroke="#2563eb"
stroke-width="2" />
<text x="583" y="30" text-anchor="middle" font-weight="bold" fill="#1e40af">Width (W)</text>
<text x="710" y="25" font-size="10" fill="#ef4444">← T: high freq only!</text>
</g>
<!-- New Approach: Interleaved -->
<g transform="translate(50, 180)">
<text x="-20" y="35" text-anchor="end" font-weight="bold" fill="#64748b">New
(Interleaved):</text>
<!-- Pattern -->
<g>
<defs>
<pattern id="pattern-interleaved" x="0" y="0" width="60" height="50"
patternUnits="userSpaceOnUse">
<rect x="0" y="0" width="20" height="50" fill="#fcd34d" stroke="#d97706" />
<text x="10" y="30" text-anchor="middle" font-size="10" fill="#b45309">T</text>
<rect x="20" y="0" width="20" height="50" fill="#86efac" stroke="#16a34a" />
<text x="30" y="30" text-anchor="middle" font-size="10" fill="#15803d">H</text>
<rect x="40" y="0" width="20" height="50" fill="#93c5fd" stroke="#2563eb" />
<text x="50" y="30" text-anchor="middle" font-size="10" fill="#1e40af">W</text>
</pattern>
</defs>
<rect x="0" y="0" width="700" height="50" fill="url(#pattern-interleaved)"
stroke="#475569" stroke-width="2" />
</g>
<text x="350" y="75" text-anchor="middle" font-size="12" fill="#059669" font-weight="bold">
✅ T, H and W spread evenly across all frequency bands, so each captures both local and global information.
</text>
</g>
</svg>
</div>
</div>
</div>
<!-- 7.3 Text-based Time Alignment -->
<div class="sr-only">

### 7.3 The Return of Video Timestamps: Text-based Time Alignment

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
7.3 The Return of Video Timestamps: Text-based Time Alignment
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
Compared with Qwen2.5-VL, there is one more major change in how video is handled: <strong>drop the pure absolute position ID and go back to text-based timestamps.</strong>
</p>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
<!-- Old Way -->
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm opacity-70">
<h4 class="font-bold text-slate-500 mb-3 text-lg line-through decoration-2 decoration-red-400">Absolute
Pos ID (Old)</h4>
<p class="text-sm text-slate-600 mb-2">
Map second $t$ directly to a very large position ID (e.g. ID=30000).
</p>
<p class="text-xs text-red-600 font-bold">
Problem: very long videos push the IDs beyond RoPE's extrapolation limit, and it is very sensitive to variable frame rates (variable FPS).
</p>
</div>
<!-- New Way -->
<div class="bg-indigo-50 p-6 rounded-2xl border border-indigo-200 shadow-md">
<h4 class="font-bold text-indigo-800 mb-3 text-lg">Explicit Text Timestamp (New)</h4>
<p class="text-sm text-indigo-900 mb-2">
Insert <strong>timestamps written as text</strong> directly into the visual token sequence.
</p>
<div class="bg-white p-3 rounded border border-indigo-100 font-mono text-xs text-indigo-600 mt-2">
[Image Frame 1] ... <strong>&lt;00:01&gt;</strong> ... [Image Frame 2] ...
<strong>&lt;00:05&gt;</strong>
</div>
<p class="text-xs text-indigo-700 font-bold mt-3">
Advantage: "time awareness" becomes a "text reading" task. The model only needs to read the string <code>&lt;00:05&gt;</code> to know which second it is, with no limit from ID size.
</p>
</div>
</div>
<!-- 7.4 Post-training & Thinking Mode -->
<div class="sr-only">

### 7.4 Post-training: The Birth of Thinking Mode

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-pink-600 rounded-full mr-4 shadow-md"></span>
7.4 Post-training: The Birth of Thinking Mode
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Qwen3-VL's post-training stage introduces an exciting feature: <strong>System 2 Thinking (slow-thinking mode)</strong>. It is clearly inspired by OpenAI o1,
but what does it mean in the multimodal setting?
</p>
<div class="bg-white p-8 rounded-3xl border border-pink-100 shadow-lg mb-12 relative overflow-hidden">
<div class="absolute -top-10 -right-10 w-32 h-32 bg-pink-50 rounded-full blur-2xl"></div>
<h4 class="text-2xl font-bold text-slate-800 mb-6 text-center">Thinking Process in VLM</h4>
<div class="space-y-6">
<!-- Step 1 -->
<div class="flex items-start">
<div
class="flex-shrink-0 w-8 h-8 bg-pink-100 rounded-full flex items-center justify-center text-pink-600 font-bold mt-1">
1</div>
<div class="ml-4">
<h5 class="font-bold text-slate-800">Extracting visual information (Perception)</h5>
<p class="text-sm text-slate-600 bg-slate-50 p-2 rounded mt-1 border border-slate-100">
"I see a red triangle and a blue square in the picture, partly overlapping..."
</p>
</div>
</div>
<!-- Step 2 -->
<div class="flex items-start">
<div
class="flex-shrink-0 w-8 h-8 bg-purple-100 rounded-full flex items-center justify-center text-purple-600 font-bold mt-1">
2</div>
<div class="ml-4">
<h5 class="font-bold text-slate-800">Logical deduction (Reasoning)</h5>
<p class="text-sm text-slate-600 bg-slate-50 p-2 rounded mt-1 border border-slate-100">
"The question asks for the overlapping area. First I need to work out the triangle's equations from the coordinates, then..."
</p>
</div>
</div>
<!-- Step 3 -->
<div class="flex items-start">
<div
class="flex-shrink-0 w-8 h-8 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 font-bold mt-1">
3</div>
<div class="ml-4">
<h5 class="font-bold text-slate-800">Self-reflection (Reflection)</h5>
<p class="text-sm text-slate-600 bg-slate-50 p-2 rounded mt-1 border border-slate-100">
"Wait, I misread that. It's not a square, it's a rectangle. I need to recalculate..."
</p>
</div>
</div>
<!-- Step 4 -->
<div class="flex items-start">
<div
class="flex-shrink-0 w-8 h-8 bg-emerald-100 rounded-full flex items-center justify-center text-emerald-600 font-bold mt-1">
4</div>
<div class="ml-4">
<h5 class="font-bold text-slate-800">Final answer (Conclusion)</h5>
<p class="text-sm text-slate-600 bg-slate-50 p-2 rounded mt-1 border border-slate-100">
"The overlapping area is 5.5 square centimetres."
</p>
</div>
</div>
</div>
</div>
<p class="text-lg text-slate-600 leading-relaxed">
Qwen3-VL comes in two versions: <strong>Thinking</strong> and <strong>Non-thinking</strong>.
<br>
For simple OCR or description tasks, the Non-thinking version is fast and cheap.
<br>
For hard geometry problems or long-video reasoning, the Thinking version is slower (it generates lots of CoT tokens), but its accuracy takes a qualitative leap.
</p>
<!-- 7.5 Experiments Highlights -->
<div class="sr-only">

### 7.5 Experimental Highlights: Topping the Leaderboards

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
7.5 Experimental Highlights: Topping the Leaderboards
</h3>
<div class="bg-slate-50 p-8 rounded-3xl border border-slate-200">
<div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
<div>
<h5 class="text-slate-500 text-sm font-bold uppercase tracking-wider mb-2">MMMU (Reasoning)</h5>
<div class="text-4xl font-extrabold text-purple-600">80.6</div>
<p class="text-xs text-slate-400 mt-1">Qwen3-VL-235B (Thinking)</p>
</div>
<div>
<h5 class="text-slate-500 text-sm font-bold uppercase tracking-wider mb-2">MathVista (Math)</h5>
<div class="text-4xl font-extrabold text-purple-600">85.8</div>
<p class="text-xs text-slate-400 mt-1">State-of-the-Art</p>
</div>
<div>
<h5 class="text-slate-500 text-sm font-bold uppercase tracking-wider mb-2">DocVQA (Doc)</h5>
<div class="text-4xl font-extrabold text-purple-600">96.5</div>
<p class="text-xs text-slate-400 mt-1">Near Perfect</p>
</div>
</div>
<p class="mt-8 text-sm text-slate-600 text-center border-t border-slate-200 pt-4">
* Source: Table 2 from Qwen3-VL Technical Report. Comparison models include GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro.
</p>
</div>
<!-- Transition -->
<div
class="mt-20 p-8 bg-gradient-to-r from-slate-100 to-white rounded-3xl border-l-8 border-slate-400 text-slate-600 shadow-sm">
<h4 class="text-xl font-bold text-slate-800 mb-3">Series summary</h4>
<p class="text-lg font-medium leading-relaxed">
From Qwen-VL "first seeing the light", to Qwen2-VL's "vision correction", to Qwen2.5-VL's "attention to fine detail", and finally to Qwen3-VL, "widely read, with a long memory, and thoughtful".
</p>
<p class="text-lg font-medium mt-4 leading-relaxed text-slate-700">
Along the way, we have watched multimodal models overcome one technical bottleneck after another: resolution, position encoding, modality alignment, long context. Qwen3-VL is not just a model but a synthesis of everything before it; it represents the current state of the art in open-source multimodal models, and it lights a lamp on the road towards
AGI.
</p>
</div>
</div>
</section>
<section id="experiments" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 7 Part 8: Experiments and Data Lineage: The Real Story Behind the Numbers, from Leaderboard Chasing to Emergent Abilities

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-amber-500 to-orange-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:rotate-6 transition-transform duration-300">7</span>
<div class="flex flex-col">
<span
class="text-transparent bg-clip-text bg-gradient-to-r from-amber-600 to-orange-600">Part 8: Experiments and Data Lineage</span>
<span class="text-2xl text-slate-500 font-medium mt-2">The real story behind the numbers: from leaderboard chasing to emergent abilities</span>
</div>
</h2>
<!-- Intro Block -->
<div class="mb-16 bg-white p-10 rounded-[2rem] shadow-premium border border-slate-100 relative overflow-hidden">
<!-- Decorative Background -->
<div
class="absolute top-0 right-0 w-[500px] h-[500px] bg-amber-50 rounded-full mix-blend-multiply filter blur-[100px] opacity-60">
</div>
<div
class="absolute bottom-0 left-0 w-[300px] h-[300px] bg-orange-50 rounded-full mix-blend-multiply filter blur-[80px] opacity-60">
</div>
<div class="sr-only">

### 📊 Don't Just Look at SOTA; Look at How the "Capability Frontier" Expands

</div>

<h3 class="text-2xl font-bold text-slate-800 mb-6 flex items-center relative z-10">
<span class="text-3xl mr-3">📊</span> Don't just look at SOTA; look at how the "capability frontier" expands
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
Everyone, when we pick up a hefty technical report like Qwen3-VL's, the easiest mistake is to flip straight to the final table, glance at the bold numbers, sigh "wow, SOTA again", and close the paper.
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
<strong>That is an extremely shallow way to read!</strong>
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
The experiments section is actually the most honest part of a paper. It isn't just showing off muscle; it tells you: <span
class="bg-amber-100 text-amber-800 px-1 rounded font-bold">What exactly did we teach the model? What can it do now? Where does it still fall over?</span>
</p>
<div class="bg-white/60 backdrop-blur-md border-l-4 border-amber-500 p-6 rounded-r-xl relative z-10">
<p class="text-amber-900 font-medium italic">
"A benchmark is a projection of a model's abilities. If we connect these scattered numbers, we see a clear evolutionary curve: from the most basic 'reading characters' (OCR), to 'understanding' (VQA), and now to 'thinking' (reasoning)."
</p>
</div>
</div>
<!-- 8.1 Ability Pyramid SVG -->
<div class="my-16">
<div class="bg-slate-50 rounded-[2.5rem] p-8 border border-slate-200 shadow-inner">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
⛰️ Illustrated: the capability pyramid of the Qwen-VL series
</h4>
<div class="flex justify-center overflow-x-auto">
<svg width="800" height="400" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg"
class="font-sans">
<defs>
<filter id="glow-amber" x="-20%" y="-20%" width="140%" height="140%">
<feGaussianBlur stdDeviation="4" result="blur" />
<feComposite in="SourceGraphic" in2="blur" operator="over" />
</filter>
<linearGradient id="grad-level1" x1="0%" y1="0%" x2="0%" y2="100%">
<stop offset="0%" style="stop-color:#bfdbfe;stop-opacity:1" />
<stop offset="100%" style="stop-color:#60a5fa;stop-opacity:1" />
</linearGradient>
<linearGradient id="grad-level2" x1="0%" y1="0%" x2="0%" y2="100%">
<stop offset="0%" style="stop-color:#a78bfa;stop-opacity:1" />
<stop offset="100%" style="stop-color:#7c3aed;stop-opacity:1" />
</linearGradient>
<linearGradient id="grad-level3" x1="0%" y1="0%" x2="0%" y2="100%">
<stop offset="0%" style="stop-color:#fbbf24;stop-opacity:1" />
<stop offset="100%" style="stop-color:#d97706;stop-opacity:1" />
</linearGradient>
</defs>
<!-- Level 1: Perception -->
<path d="M 100 350 L 700 350 L 600 250 L 200 250 Z" fill="url(#grad-level1)" stroke="#2563eb"
stroke-width="2" />
<text x="400" y="310" text-anchor="middle" font-size="20" font-weight="bold"
fill="#1e3a8a">Level 1: Basic Perception</text>
<text x="400" y="335" text-anchor="middle" font-size="14" fill="#1e40af">OCR, Caption, Detection
(Qwen-VL's strength)</text>
<!-- Level 2: Understanding -->
<path d="M 200 250 L 600 250 L 500 150 L 300 150 Z" fill="url(#grad-level2)" stroke="#6d28d9"
stroke-width="2" />
<text x="400" y="210" text-anchor="middle" font-size="20" font-weight="bold"
fill="#4c1d95">Level 2: Structured Understanding</text>
<text x="400" y="235" text-anchor="middle" font-size="14" fill="#5b21b6">ChartQA, DocVQA,
VideoQA (Qwen2/2.5-VL's strength)</text>
<!-- Level 3: Reasoning -->
<g filter="url(#glow-amber)">
<path d="M 300 150 L 500 150 L 400 50 Z" fill="url(#grad-level3)" stroke="#b45309"
stroke-width="2" />
<text x="400" y="110" text-anchor="middle" font-size="20" font-weight="bold"
fill="#78350f">Level 3: Complex Reasoning</text>
<text x="400" y="135" text-anchor="middle" font-size="14" fill="#92400e">MMMU, MathVista,
Agent (Qwen3-VL's strength)</text>
</g>
<!-- Arrow Up -->
<line x1="720" y1="350" x2="720" y2="50" stroke="#94a3b8" stroke-width="2"
stroke-dasharray="5,5" marker-end="url(#arrow)" />
<text x="730" y="200" font-size="12" fill="#64748b" style="writing-mode: tb;">Data Quality &
Context Length ↑</text>
</svg>
</div>
</div>
</div>
<!-- 8.1 Image Caption & General VQA -->
<div class="sr-only">

### 8.1 Image Captioning and General VQA: The Touchstone of Basic Ability

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-blue-500 rounded-full mr-4 shadow-md"></span>
8.1 Image Captioning and General VQA: The Touchstone of Basic Ability
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
This is like a primary-school pupil's sentence-making and picture-description exercises. Simple, yes, but it is the foundation of every complex ability. If a model can't even say correctly how many people are in a picture or what they're wearing, there's no point talking about reasoning.
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
<h4 class="text-lg font-bold text-blue-900 mb-4 flex items-center">
<span class="bg-blue-100 p-2 rounded-lg mr-3">🖼️</span>
Zero-shot Captioning
</h4>
<p class="text-slate-600 text-sm mb-4">
On datasets such as <strong>Nocaps</strong> and <strong>Flickr30k</strong>, even the early versions of Qwen-VL showed remarkable generalisation. This shows that its visual
encoder (ViT-bigG) and alignment layer (adapter) really did translate image features into a language the LLM can understand.
</p>
<div class="bg-blue-50 p-3 rounded border border-blue-100 text-xs font-mono text-blue-700">
Qwen2.5-VL: CIDEr score far above models of its class
</div>
</div>
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
<h4 class="text-lg font-bold text-indigo-900 mb-4 flex items-center">
<span class="bg-indigo-100 p-2 rounded-lg mr-3">❓</span>
General VQA
</h4>
<p class="text-slate-600 text-sm mb-4">
<strong>VQAv2, GQA, OKVQA</strong>. These tasks test "localisation + recognition". Qwen3-VL's gains here owe more to the huge volume of real-world images it saw during pre-training (world
knowledge); it is no longer a bookworm that has only ever looked at ImageNet.
</p>
<div class="bg-indigo-50 p-3 rounded border border-indigo-100 text-xs font-mono text-indigo-700">
MMBench: Qwen3-VL reaches 88.8 (Thinking)
</div>
</div>
</div>
<!-- 8.2 Document Understanding -->
<div class="sr-only">

### 8.2 Document Understanding and Structured Extraction: From "Reading Characters" to "Understanding the Logic"

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-purple-500 rounded-full mr-4 shadow-md"></span>
8.2 Document Understanding and Structured Extraction: From "Reading Characters" to "Understanding the Logic"
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
This is where Qwen2.5-VL and Qwen3-VL rule absolutely.
</p>
<div class="bg-slate-50 border-l-4 border-purple-400 p-6 rounded-r-lg mb-10">
<h4 class="text-lg font-bold text-slate-800 mb-2">💡 Question: does a high OCR score mean strong document understanding?</h4>
<p class="text-slate-600 text-sm leading-relaxed">
Some models score 99 on OCR but only 60 on DocVQA. Why?
<br>Because OCR only recognises the characters (perception), while DocVQA requires you to understand the <strong>layout</strong>, the <strong>table
structure</strong> and the <strong>semantic links across lines and pages</strong>.
<br>For example: "What is the number in row 3, column 2 of the table minus the one in row 1, column 2?" That needs extremely precise spatial awareness.
</p>
</div>
<div class="overflow-x-auto mb-12">
<table class="min-w-full bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden">
<thead class="bg-purple-50 text-purple-900">
<tr>
<th class="px-6 py-4 text-left font-bold">Benchmark</th>
<th class="px-6 py-4 text-left font-bold">Task Description</th>
<th class="px-6 py-4 text-left font-bold">Qwen3-VL Performance</th>
<th class="px-6 py-4 text-left font-bold">Key Enabler</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-100">
<tr class="hover:bg-slate-50 transition-colors">
<td class="px-6 py-4 font-mono text-sm font-bold text-slate-700">DocVQA</td>
<td class="px-6 py-4 text-sm text-slate-600">QA on scanned documents</td>
<td class="px-6 py-4 font-bold text-emerald-600">96.5 (SOTA)</td>
<td class="px-6 py-4 text-xs text-slate-500">Native Dynamic Res (sharpness)</td>
</tr>
<tr class="hover:bg-slate-50 transition-colors">
<td class="px-6 py-4 font-mono text-sm font-bold text-slate-700">ChartQA</td>
<td class="px-6 py-4 text-sm text-slate-600">Chart data analysis</td>
<td class="px-6 py-4 font-bold text-emerald-600">90.3</td>
<td class="px-6 py-4 text-xs text-slate-500">High-res Input + CoT</td>
</tr>
<tr class="hover:bg-slate-50 transition-colors">
<td class="px-6 py-4 font-mono text-sm font-bold text-slate-700">InfoVQA</td>
<td class="px-6 py-4 text-sm text-slate-600">Complex infographic understanding</td>
<td class="px-6 py-4 font-bold text-emerald-600">89.5</td>
<td class="px-6 py-4 text-xs text-slate-500">DeepStack (deep semantics)</td>
</tr>
</tbody>
</table>
</div>
<!-- Inserted after section 8.2 of the experiments chapter -->
<div class="my-20">
<div class="sr-only">

### 8.X The Secret Weapon: The Synthetic Data Factory

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
8.X The Secret Weapon: The Synthetic Data Factory
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Why can Qwen2.5-VL understand such complicated HTML pages and PDFs? Did they hire a million annotators to label everything by hand?
<br>
<strong>Of course not.</strong> Its secret weapon is a fully automated "synthetic data factory".
</p>
<div class="bg-white p-8 rounded-3xl border border-slate-200 shadow-xl overflow-hidden">
<h4 class="text-center font-serif text-xl font-bold text-slate-700 mb-8">🏭 The Data Synthesis Pipeline</h4>
<div class="flex justify-center overflow-x-auto">
<svg width="800" height="300" viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg" class="font-sans">
<defs>
<marker id="arrow-factory" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#64748b" />
</marker>
</defs>
<!-- Stage 1: Raw Data -->
<g transform="translate(50, 100)">
<rect x="0" y="0" width="100" height="80" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2" rx="4" />
<text x="50" y="35" text-anchor="middle" font-weight="bold" fill="#475569">Raw PDF</text>
<text x="50" y="55" text-anchor="middle" font-size="10" fill="#64748b">/ HTML / ArXiv</text>
</g>
<!-- Arrow -->
<path d="M 110 140 L 150 140" stroke="#cbd5e1" stroke-width="2" marker-end="url(#arrow-factory)" />
<!-- Stage 2: Parsing (The Teacher) -->
<g transform="translate(160, 80)">
<rect x="0" y="0" width="140" height="120" fill="#e0e7ff" stroke="#6366f1" stroke-width="2"
rx="8" />
<text x="70" y="30" text-anchor="middle" font-weight="bold" fill="#4338ca">Specialized Parser</text>
<text x="70" y="50" text-anchor="middle" font-size="10" fill="#6366f1">(LayoutLM / PDFMiner)</text>
<rect x="20" y="70" width="100" height="30" fill="white" stroke="#c7d2fe" />
<text x="70" y="90" text-anchor="middle" font-size="10" fill="#4338ca">Extract Layout</text>
</g>
<!-- Arrow -->
<path d="M 310 140 L 350 140" stroke="#cbd5e1" stroke-width="2" marker-end="url(#arrow-factory)" />
<!-- Stage 3: Rendering (The Trick) -->
<g transform="translate(360, 60)">
<rect x="0" y="0" width="160" height="160" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"
rx="8" />
<text x="80" y="30" text-anchor="middle" font-weight="bold" fill="#166534">Rendering Engine</text>
<!-- Code to Image -->
<g transform="translate(20, 50)">
<rect x="0" y="0" width="50" height="60" fill="white" stroke="#86efac" />
<text x="25" y="30" text-anchor="middle" font-size="10" fill="#16a34a">Markdown</text>
</g>
<text x="80" y="80" text-anchor="middle" font-bold="true" fill="#16a34a">→</text>
<!-- Output Image -->
<g transform="translate(90, 50)">
<rect x="0" y="0" width="50" height="60" fill="#dcfce7" stroke="#16a34a" />
<text x="25" y="25" text-anchor="middle" font-size="8" fill="#14532d">Title</text>
<line x1="5" y1="35" x2="45" y2="35" stroke="#16a34a" />
<line x1="5" y1="40" x2="45" y2="40" stroke="#16a34a" />
</g>
<text x="80" y="140" text-anchor="middle" font-size="10" fill="#15803d" font-weight="bold">"We know
the GT!"</text>
</g>
<!-- Arrow -->
<path d="M 530 140 L 570 140" stroke="#cbd5e1" stroke-width="2" marker-end="url(#arrow-factory)" />
<!-- Stage 4: Training Data -->
<g transform="translate(580, 100)">
<rect x="0" y="0" width="140" height="80" fill="#fffbeb" stroke="#d97706" stroke-width="2" rx="4" />
<text x="70" y="25" text-anchor="middle" font-weight="bold" fill="#92400e">Training Pair</text>
<g transform="translate(20, 40)">
<rect x="0" y="0" width="40" height="30" fill="#fcd34d" />
<text x="20" y="20" text-anchor="middle" font-size="8">Image</text>
</g>
<text x="70" y="60" text-anchor="middle" font-size="12">+</text>
<g transform="translate(80, 40)">
<rect x="0" y="0" width="40" height="30" fill="white" stroke="#d97706" />
<text x="20" y="20" text-anchor="middle" font-size="8">Struct JSON</text>
</g>
</g>
</svg>
</div>
<div class="mt-8 bg-slate-50 p-6 rounded-xl border border-slate-200">
<h5 class="font-bold text-slate-800 mb-2">💡 The core logic:</h5>
<p class="text-slate-600 text-sm leading-relaxed">
If annotating real documents is hard, why not <strong>generate the documents ourselves</strong>?
<br>
1. Take clean Markdown / LaTeX text.
<br>
2. Render it into images with a browser rendering engine (Chrome/Puppeteer).
<br>
3. Because we control the rendering, we naturally know the <strong>exact coordinates (bounding box)</strong> of every character and every table cell.
<br>
This gives us <strong>unlimited, perfectly annotated</strong> OCR and layout data!
</p>
</div>
</div>
</div>
<!-- 8.3 Video Understanding -->
<div class="sr-only">

### 8.3 Video Understanding: The "Needle in a Haystack" Challenge

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-amber-500 rounded-full mr-4 shadow-md"></span>
8.3 Video Understanding: The "Needle in a Haystack" Challenge
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
For video, Qwen3-VL ran a very demanding test: <strong>Video Needle-in-a-Haystack (NIAH)</strong>.
This isn't just checking whether the model can remember a video; it checks whether, faced with an hour-long video (tens of thousands of frames), it can pinpoint a tiny detail in <strong>that one frame</strong>.
</p>
<div class="flex flex-col md:flex-row gap-8 mb-12">
<div class="w-full md:w-1/2">
<img src="/images/qwen-vlm/image_006.jpg"
class="rounded-xl shadow-lg border border-slate-200 w-full h-auto object-cover"
alt="Video NIAH Heatmap">
<p class="text-center text-xs text-slate-500 mt-2 italic">Figure 3: Heat map of the video needle-in-a-haystack test. All green means 100% recall.</p>
</div>
<div class="w-full md:w-1/2 flex flex-col justify-center">
<h4 class="text-xl font-bold text-amber-900 mb-4">📊 Reading the experiment</h4>
<p class="text-slate-600 mb-4 leading-relaxed">
Look at the heat map on the left: almost all of it is <span class="text-emerald-600 font-bold">green</span>. That means:
<br>even when the video is 30 minutes or even an hour long (context length maxed out), Qwen3-VL can still pinpoint events happening at any moment.
</p>
<p class="text-slate-600 leading-relaxed">
<strong>Who deserves the credit?</strong>
<br>
1. <strong>Interleaved MRoPE</strong>: ensures the time dimension doesn't lose high-frequency information over long sequences.
<br>
2. <strong>Text-based Timestamp</strong>: explicit timestamp tokens provide strong anchors.
</p>
</div>
</div>
<!-- 8.4 Multimodal Reasoning -->
<div class="sr-only">

### 8.4 Multimodal Reasoning: Thinking Mode in a League of Its Own

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-pink-500 rounded-full mr-4 shadow-md"></span>
8.4 Multimodal Reasoning: Thinking Mode in a League of Its Own
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
This is the most exciting part of Qwen3-VL. On hard reasoning benchmarks such as MMMU and MathVista, Qwen3-VL's Thinking mode shows impressive strength.
</p>
<!-- SVG Radar Chart -->
<div class="my-12 flex justify-center">
<div class="bg-white rounded-3xl shadow-xl p-8 border border-slate-100 w-full max-w-3xl relative">
<div class="absolute top-4 right-4 bg-pink-100 text-pink-800 text-xs px-2 py-1 rounded font-bold">
Comparision (Score)</div>
<h4 class="text-center font-serif text-xl font-bold text-slate-800 mb-6">
🕸️ Radar chart of multimodal reasoning ability
</h4>
<svg width="600" height="400" viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"
class="mx-auto font-sans">
<!-- Background Grid (Polygon) -->
<g transform="translate(300, 200)">
<!-- Axes -->
<line x1="0" y1="0" x2="0" y2="-150" stroke="#cbd5e1" />
<line x1="0" y1="0" x2="130" y2="-75" stroke="#cbd5e1" />
<line x1="0" y1="0" x2="130" y2="75" stroke="#cbd5e1" />
<line x1="0" y1="0" x2="0" y2="150" stroke="#cbd5e1" />
<line x1="0" y1="0" x2="-130" y2="75" stroke="#cbd5e1" />
<line x1="0" y1="0" x2="-130" y2="-75" stroke="#cbd5e1" />
<!-- Labels -->
<text x="0" y="-160" text-anchor="middle" font-size="12" font-weight="bold"
fill="#475569">MMMU</text>
<text x="145" y="-80" text-anchor="middle" font-size="12" font-weight="bold"
fill="#475569">MathVista</text>
<text x="145" y="90" text-anchor="middle" font-size="12" font-weight="bold"
fill="#475569">MathVision</text>
<text x="0" y="170" text-anchor="middle" font-size="12" font-weight="bold"
fill="#475569">DynaMath</text>
<text x="-145" y="90" text-anchor="middle" font-size="12" font-weight="bold"
fill="#475569">ZeroBench</text>
<text x="-145" y="-80" text-anchor="middle" font-size="12" font-weight="bold"
fill="#475569">LogicVista</text>
<!-- Grid Levels -->
<polygon points="0,-150 130,-75 130,75 0,150 -130,75 -130,-75" fill="none" stroke="#e2e8f0" />
<polygon points="0,-100 86,-50 86,50 0,100 -86,50 -86,-50" fill="none" stroke="#e2e8f0" />
<!-- Data: Qwen3-VL Thinking (Pink) -->
<polygon points="0,-120 128,-73 110,65 124,142 100,40 -108,-54" fill="rgba(236, 72, 153, 0.2)"
stroke="#db2777" stroke-width="2" />
<circle cx="0" cy="-120" r="3" fill="#db2777" />
<circle cx="128" cy="-73" r="3" fill="#db2777" />
<circle cx="110" cy="65" r="3" fill="#db2777" />
<!-- Data: Gemini 1.5 Pro (Gray) -->
<polygon points="0,-115 124,-68 108,60 117,135 -10,5 -103,-51" fill="none" stroke="#94a3b8"
stroke-width="2" stroke-dasharray="4" />
</g>
<!-- Legend -->
<g transform="translate(400, 350)">
<rect x="0" y="0" width="10" height="10" fill="#db2777" />
<text x="15" y="10" font-size="10" fill="#64748b">Qwen3-VL (Thinking)</text>
<line x1="0" y1="20" x2="10" y2="20" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4" />
<text x="15" y="25" font-size="10" fill="#64748b">Competitors (Avg)</text>
</g>
</svg>
</div>
</div>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Look at the MathVista and MMMU scores. With Thinking mode on, Qwen3-VL can generate reasoning steps thousands of tokens long, which greatly improves how it handles complex geometry and physics problems.
<br><br>
<span class="font-bold text-slate-800">A key insight:</span>
We found that adding dedicated chain-of-thought (CoT) data to training not only improved maths ability but also generalised to code generation and agent planning. This suggests that "reasoning ability" is general in the deep semantic space.
</p>
<!-- Transition -->
<div class="mt-24 p-8 bg-slate-900 rounded-3xl text-center relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-amber-500 to-orange-500"></div>
<h4 class="text-2xl font-bold text-white mb-4">Chapter summary</h4>
<p class="text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed">
The experimental data tell us that each upgrade in the Qwen-VL series was not just "piling on parameters", but an <strong class="text-amber-400">architecture-level breakthrough</strong> aimed at a specific pain point (resolution, time, reasoning).
<br>
By now you understand where it came from and why it is so strong. Next, it's time to move this big fellow into your own project.
</p>
<a href="#practical-guide"
class="inline-block mt-8 px-8 py-3 bg-gradient-to-r from-amber-500 to-orange-600 text-white font-bold rounded-full hover:shadow-lg hover:scale-105 transition-all duration-300">
🚀 Next chapter: a guide to reproduction and practice
</a>
</div>
</div>
</section>
<section id="practical-guide" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 8 Part 9: A Guide to Reproduction and Practice: Moving the Qwen-VL of the Papers into Your Own Engineering

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-cyan-500 to-blue-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:rotate-3 transition-transform duration-300">8</span>
<div class="flex flex-col">
<span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 to-blue-600">Part 9: A Guide to Reproduction and Practice</span>
<span class="text-2xl text-slate-500 font-medium mt-2">Moving the Qwen-VL of the papers into your own engineering</span>
</div>
</h2>
<!-- Intro Block -->
<div class="mb-16 bg-white p-10 rounded-[2rem] shadow-premium border border-slate-100 relative overflow-hidden">
<!-- Decorative Background -->
<div
class="absolute top-0 right-0 w-[400px] h-[400px] bg-cyan-50 rounded-full mix-blend-multiply filter blur-[80px] opacity-60">
</div>
<div
class="absolute bottom-0 left-0 w-[300px] h-[300px] bg-blue-50 rounded-full mix-blend-multiply filter blur-[60px] opacity-60">
</div>
<div class="sr-only">

### 🛠️ Don't Just Read the Paper; Running It Is the Real Test

</div>

<h3 class="text-2xl font-bold text-slate-800 mb-6 flex items-center relative z-10">
<span class="text-3xl mr-3">🛠️</span> Don't just read the paper; running it is the real test
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
After the architecture walkthrough, I trust you now have a solid theoretical grasp of the Qwen-VL series. But as an engineer or researcher who has to put the model to work, you probably still have three ultimate questions:
</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 relative z-10">
<div class="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-cyan-100 shadow-sm">
<span class="text-2xl">🤔</span>
<p class="font-bold text-cyan-900 mt-2">Which version?</p>
<p class="text-xs text-slate-500">2B/7B/72B? Qwen2.5 or Qwen3?</p>
</div>
<div class="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-blue-100 shadow-sm">
<span class="text-2xl">💻</span>
<p class="font-bold text-blue-900 mt-2">How do I call it?</p>
<p class="text-xs text-slate-500">How do I fit multiple images, videos and long documents into a prompt?</p>
</div>
<div class="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-indigo-100 shadow-sm">
<span class="text-2xl">🔧</span>
<p class="font-bold text-indigo-900 mt-2">How do I fine-tune it?</p>
<p class="text-xs text-slate-500">I have private data. Can I make it understand my domain better?</p>
</div>
</div>
</div>
<!-- 9.1 Model Selection Guide -->
<div class="sr-only">

### 9.1 Choosing a Model: Pick It Like Picking a Class in an RPG

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-cyan-500 rounded-full mr-4 shadow-md"></span>
9.1 Choosing a Model: Pick It Like Picking a Class in an RPG
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
The Qwen-VL family is big these days, and picking the wrong model is like putting your mage's points into strength: lots of effort, little reward. I've put together a <strong>"lazy person's decision tree"</strong> for you.
</p>
<div class="my-12 bg-slate-50 p-8 rounded-3xl border border-slate-200 shadow-inner">
<div class="flex flex-col items-center space-y-6 font-sans text-sm">
<!-- Question 1 -->
<div
class="bg-white border-2 border-slate-800 text-slate-800 px-6 py-3 rounded-full font-bold shadow-lg relative z-10">
Q1: How much GPU memory do you have?
</div>
<div class="flex w-full max-w-3xl justify-between px-10 relative">
<div class="absolute top-[-20px] left-1/2 w-0.5 h-10 bg-slate-300 -z-0"></div>
<div class="absolute top-0 left-[20%] right-[20%] h-0.5 bg-slate-300 -z-0"></div>
<div class="absolute top-0 left-[20%] w-0.5 h-6 bg-slate-300"></div>
<div class="absolute top-0 right-[20%] w-0.5 h-6 bg-slate-300"></div>
<!-- Branch A: Low Resource -->
<div class="flex flex-col items-center w-1/2">
<div class="bg-green-100 text-green-800 px-3 py-1 rounded text-xs font-bold mb-2">&lt; 16GB (single
3090/4090)</div>
<div class="bg-white border border-green-200 p-4 rounded-xl shadow-sm text-center w-full">
<h5 class="font-bold text-green-700 text-lg mb-1">Qwen2.5-VL-7B</h5>
<p class="text-xs text-slate-500">Best value for money. Runs most demos, supports video and documents.</p>
<p class="text-xs text-slate-400 mt-2 border-t border-slate-100 pt-1">Plan B: Qwen2-VL-2B
(phone / Raspberry Pi)</p>
</div>
</div>
<!-- Branch B: High Resource -->
<div class="flex flex-col items-center w-1/2">
<div class="bg-blue-100 text-blue-800 px-3 py-1 rounded text-xs font-bold mb-2">&gt; 48GB
(A100/H800)</div>
<div
class="bg-white border-2 border-slate-800 p-4 rounded-xl shadow-sm text-center w-full relative">
<div
class="absolute -top-3 -right-3 bg-red-500 text-white text-xs px-2 py-1 rounded-full font-bold animate-bounce">
Q2</div>
<p class="font-bold text-slate-700 mb-2">What tasks do you need to handle?</p>
<div class="flex justify-around text-xs gap-2">
<div class="bg-blue-50 p-2 rounded border border-blue-100 w-1/2">
<span class="block font-bold text-blue-700">General VQA / simple documents</span>
<span class="block mt-1 text-slate-500">Qwen2.5-VL-72B</span>
</div>
<div class="bg-purple-50 p-2 rounded border border-purple-100 w-1/2">
<span class="block font-bold text-purple-700">Complex reasoning / long video</span>
<span class="block mt-1 text-slate-500">Qwen3-VL (Thinking)</span>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<!-- 9.2 Code Snippet -->
<div class="sr-only">

### 9.2 Minimal End-to-End Code: From Pixels to Tokens

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-blue-500 rounded-full mr-4 shadow-md"></span>
9.2 Minimal End-to-End Code: From Pixels to Tokens
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Talk is cheap, show me the code. Below is a minimal inference script based on the Hugging Face <code>transformers</code> library.
<br>Pay attention to the comments marked <span class="bg-slate-800 text-white px-1 rounded text-sm">Teacher's key point</span>: that is where people trip up most often.
</p>
<div class="bg-slate-900 rounded-2xl overflow-hidden shadow-2xl border border-slate-700">
<div class="flex items-center px-4 py-2 bg-slate-800 border-b border-slate-700">
<div class="flex space-x-2">
<div class="w-3 h-3 bg-red-500 rounded-full"></div>
<div class="w-3 h-3 bg-yellow-500 rounded-full"></div>
<div class="w-3 h-3 bg-green-500 rounded-full"></div>
</div>
<div class="ml-4 text-xs text-slate-400 font-mono">inference_demo.py</div>
</div>
<pre class="p-6 overflow-x-auto text-sm font-mono leading-relaxed"><code class="language-python text-slate-300"><span class="text-purple-400">from</span> transformers <span class="text-purple-400">import</span> Qwen2_5_VLForConditionalGeneration, AutoProcessor
<span class="text-purple-400">from</span> qwen_vl_utils <span class="text-purple-400">import</span> process_vision_info
<span class="text-purple-400">import</span> torch
<span class="text-slate-500"># [Teacher's key point]: be sure to add device_map="auto", or a large model may overflow a single GPU's memory</span>
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
<span class="text-green-400">"Qwen/Qwen2.5-VL-7B-Instruct"</span>, 
torch_dtype=torch.bfloat16, 
device_map=<span class="text-green-400">"auto"</span>
)
<span class="text-slate-500"># The processor handles image resizing and tokenization</span>
<span class="text-slate-500"># It is the "magic black box" of the Qwen-VL series and handles Dynamic Resolution automatically</span>
processor = AutoProcessor.from_pretrained(<span class="text-green-400">"Qwen/Qwen2.5-VL-7B-Instruct"</span>)
messages = [
{
<span class="text-green-400">"role"</span>: <span class="text-green-400">"user"</span>,
<span class="text-green-400">"content"</span>: [
{
<span class="text-green-400">"type"</span>: <span class="text-green-400">"image"</span>,
<span class="text-green-400">"image"</span>: <span class="text-green-400">"https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"</span>,
},
{<span class="text-green-400">"type"</span>: <span class="text-green-400">"text"</span>, <span class="text-green-400">"text"</span>: <span class="text-green-400">"Describe this image in detail."</span>},
],
}
]
<span class="text-slate-500"># Prepare inputs: turn image pixels into tensors and text into input IDs</span>
text = processor.apply_chat_template(messages, tokenize=<span class="text-blue-400">False</span>, add_generation_prompt=<span class="text-blue-400">True</span>)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
text=[text],
images=image_inputs,
videos=video_inputs,
padding=<span class="text-blue-400">True</span>,
return_tensors=<span class="text-green-400">"pt"</span>,
)
inputs = inputs.to(<span class="text-green-400">"cuda"</span>)
<span class="text-slate-500"># [Teacher's key point]: generated_ids contains input + output</span>
<span class="text-slate-500"># so slice before decoding and decode only the new tokens, or you'll see the question repeated back</span>
generated_ids = model.generate(**inputs, max_new_tokens=<span class="text-orange-400">128</span>)
generated_ids_trimmed = [
out_ids[len(in_ids) :] <span class="text-purple-400">for</span> in_ids, out_ids <span class="text-purple-400">in</span> <span class="text-yellow-400">zip</span>(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
generated_ids_trimmed, skip_special_tokens=<span class="text-blue-400">True</span>, clean_up_tokenization_spaces=<span class="text-blue-400">False</span>
)
<span class="text-yellow-400">print</span>(output_text)</code></pre>
</div>
<!-- 9.3 Advanced Techniques -->
<div class="sr-only">

### 9.3 Advanced Use: Multiple Images and Long Context

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
9.3 Advanced Use: Multiple Images and Long Context
</h3>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
<h4 class="text-lg font-bold text-slate-800 mb-4">📚 Handling long documents (PDF)</h4>
<p class="text-sm text-slate-600 mb-4">
When you feed a 10-page PDF to the model, don't naively treat each page as an unrelated image.
</p>
<div class="bg-slate-50 p-3 rounded border border-slate-100 text-xs font-mono text-slate-600 mb-4">
Prompt:<br>
[Img Page 1]<br>
[Img Page 2]<br>
...<br>
"Using the table on page 1 and the conclusion on page 5, analyse..."
</div>
<p class="text-sm text-slate-600">
<strong>Tip:</strong> put a text anchor before each page image, e.g. <code>Image 1: Page 1</code>. That makes it easier for the model, during attention,
to locate a specific page.
</p>
</div>
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
<h4 class="text-lg font-bold text-slate-800 mb-4">🎬 Handling long videos</h4>
<p class="text-sm text-slate-600 mb-4">
Frame sampling is the key. Qwen2.5-VL supports dynamic FPS, but you have to keep the total token count under control.
</p>
<div class="bg-slate-50 p-3 rounded border border-slate-100 text-xs font-mono text-slate-600 mb-4">
Sample Strategy:<br>
1 fps (for short clip) <br>
0.1 fps (for long movie)
</div>
<p class="text-sm text-slate-600">
<strong>Tip:</strong> thanks to Qwen2.5-VL's absolute time encoding, you can ask in the prompt "What happens at around 00:15?", and the model can use the timestamps to answer precisely.
</p>
</div>
</div>
<!-- 9.4 Fine-tuning Guide -->
<div class="sr-only">

### 9.4 Fine-tuning in Practice: LoRA Is Your Friend

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-pink-500 rounded-full mr-4 shadow-md"></span>
9.4 Fine-tuning in Practice: LoRA Is Your Friend
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
Don't jump straight into full fine-tuning unless you have a few hundred A100s. For most domain-specific tasks (such as medical imaging reports or industrial quality inspection), <strong>LoRA (Low-Rank
Adaptation)</strong> is enough.
</p>
<div class="bg-pink-50 border-l-4 border-pink-400 p-6 rounded-r-lg mb-8">
<h4 class="text-lg font-bold text-pink-800 mb-2">💡 Fine-tuning pitfalls to avoid</h4>
<ul class="list-disc list-inside text-pink-700 text-sm space-y-2">
<li><strong>Freeze the ViT:</strong> normally the visual encoder doesn't need to change. It has already seen trillions of tokens of data and understands vision better than the few thousand images you have.</li>
<li><strong>Tune only the LLM and projector:</strong> attach LoRA to the LLM's `q_proj` and `v_proj`, or even fine-tune only the MLP Merger
(projector), and you can get decent domain adaptation.</li>
<li><strong>Match the data format:</strong> your fine-tuning data must strictly follow the ChatML format, including special tokens such as `<|vision_start|>`, or the model will get badly confused.</li>
</ul>
</div>
<!-- 9.5 Common Pitfalls -->
<div class="sr-only">

### 9.5 Common Failure Scenes (Common Pitfalls)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-orange-500 rounded-full mr-4 shadow-md"></span>
9.5 Common Failure Scenes (Common Pitfalls)
</h3>
<div class="space-y-6">
<!-- Pitfall 1 -->
<div
class="flex items-start p-4 bg-white rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div
class="flex-shrink-0 w-10 h-10 bg-red-100 rounded-full flex items-center justify-center text-red-600 font-bold text-xl mr-4">
🚫</div>
<div>
<h4 class="font-bold text-slate-800 text-base mb-1">OOM (GPU memory blow-up)</h4>
<p class="text-sm text-slate-600">
<strong>Symptom:</strong> CUDA Out of Memory partway through a run.<br>
<strong>Cause:</strong> Qwen2-VL uses dynamic resolution, so if you feed it a huge 8K image it cuts out thousands of tokens and instantly blows up GPU memory.<br>
<strong>Fix:</strong> set a <code>max_pixels</code> limit in <code>process_vision_info</code>, or manually
resize very large images.
</p>
</div>
</div>
<!-- Pitfall 2 -->
<div
class="flex items-start p-4 bg-white rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div
class="flex-shrink-0 w-10 h-10 bg-amber-100 rounded-full flex items-center justify-center text-amber-600 font-bold text-xl mr-4">
😵‍💫</div>
<div>
<h4 class="font-bold text-slate-800 text-base mb-1">Parrot mode</h4>
<p class="text-sm text-slate-600">
<strong>Symptom:</strong> the model keeps repeating the same sentence, or outputs gibberish.<br>
<strong>Cause:</strong> usually the prompt format is wrong: a missing <code>&lt;|im_end|&gt;</code>, or a system prompt
that is way off.<br>
<strong>Fix:</strong> carefully check the string produced by <code>apply_chat_template</code> and make sure the special tokens are intact.
</p>
</div>
</div>
</div>
<!-- Transition -->
<div class="mt-24 p-8 bg-slate-900 rounded-3xl text-center relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-cyan-500 to-blue-500"></div>
<h4 class="text-2xl font-bold text-white mb-4">Ready to Build?</h4>
<p class="text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed">
The theory is covered and the demo code is there. You now have everything you need to tame Qwen-VL, this multimodal giant.
<br>
Whether you're doing academic research or building the next hit AI application, the road is right in front of you.
</p>
<a href="#future-work"
class="inline-block mt-8 px-8 py-3 bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-bold rounded-full hover:shadow-lg hover:scale-105 transition-all duration-300">
🔮 Next chapter: looking ahead
</a>
</div>
</div>
</section>
<section id="future-work" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 9 Part 10: Looking Ahead: Where Is the Next "Holy Grail" for Multimodal Models?

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-violet-600 to-fuchsia-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:scale-110 transition-transform duration-300">9</span>
<div class="flex flex-col">
<span
class="text-transparent bg-clip-text bg-gradient-to-r from-violet-600 to-fuchsia-600">Part 10: Looking Ahead</span>
<span class="text-2xl text-slate-500 font-medium mt-2">Where is the next "holy grail" for multimodal models?</span>
</div>
</h2>
<!-- Intro Block -->
<div class="mb-16 bg-white p-10 rounded-[2rem] shadow-premium border border-slate-100 relative overflow-hidden">
<div
class="absolute top-0 right-0 w-[400px] h-[400px] bg-violet-50 rounded-full mix-blend-multiply filter blur-[80px] opacity-60 animate-pulse">
</div>
<div
class="absolute bottom-0 left-0 w-[300px] h-[300px] bg-fuchsia-50 rounded-full mix-blend-multiply filter blur-[60px] opacity-60">
</div>
<p class="text-xl text-slate-700 leading-relaxed relative z-10">
Qwen3-VL has already pushed context to 256K and reasoning to Thinking Mode. Does that mean multimodal models have reached the end of the road?
</p>
<p class="text-xl text-slate-700 leading-relaxed mt-4 relative z-10 font-bold">
Clearly not. Quite the opposite: we are only standing at the foot of the mountain.
</p>
<p class="text-lg text-slate-600 leading-relaxed mt-4 relative z-10">
If we compare today's models to a high-school student who has just learned to "write an essay about a picture", then the models of the future should be super agents who can "understand films, operate computers, and even predict the future". In this section, let's set specific benchmarks aside and talk about the
<strong>Open Problems</strong> that are truly worth tackling.
</p>
</div>
<!-- 10.1 Efficient Vision -->
<div class="sr-only">

### 10.1 The Limits of Visual Efficiency: Are Fewer Tokens Always Better?

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-violet-500 rounded-full mr-4 shadow-md"></span>
10.1 The Limits of Visual Efficiency: Are Fewer Tokens Always Better?
</h3>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
<div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm">
<h4 class="text-xl font-bold text-slate-800 mb-4">📉 Current state and pain points</h4>
<p class="text-slate-600 mb-4">
Qwen2.5-VL introduced dynamic resolution, but at heart it is still "compressing". A 4K image gets squeezed into a few hundred tokens, and lots of high-frequency detail (texture, tiny defects) is inevitably lost.
</p>
<div class="bg-slate-50 p-4 rounded-xl border-l-4 border-red-400 text-sm text-slate-700">
<strong>The Trade-off:</strong> want to see details -> tokens explode -> context overflow / GPU OOM.
</div>
</div>
<div class="bg-violet-50 p-8 rounded-2xl border border-violet-100 shadow-sm">
<h4 class="text-xl font-bold text-violet-900 mb-4">🚀 Possible breakthroughs</h4>
<ul class="space-y-4">
<li class="flex items-start">
<span class="bg-white p-1 rounded text-lg mr-3 shadow-sm">✂️</span>
<div>
<strong class="text-violet-800 block">Dynamic Pruning</strong>
<span class="text-sm text-violet-700">At inference time, decide on the fly which patches are background, drop them, and keep only foreground tokens.</span>
</div>
</li>
<li class="flex items-start">
<span class="bg-white p-1 rounded text-lg mr-3 shadow-sm">🧱</span>
<div>
<strong class="text-violet-800 block">Multi-granularity Tokens</strong>
<span class="text-sm text-violet-700">A big stretch of blue sky gets one "coarse-grained token"; a face gets a hundred "fine-grained tokens".</span>
</div>
</li>
</ul>
</div>
</div>
<!-- 10.2 Explainability -->
<div class="sr-only">

### 10.2 The Evolution of Interpretability: From "Black Box" to "Glass Box"

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-fuchsia-500 rounded-full mr-4 shadow-md"></span>
10.2 The Evolution of Interpretability: From "Black Box" to "Glass Box"
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
Today's Thinking Mode can output a textual chain of thought, but it still can't tell us: <strong>"Which part of the image are you actually looking at?"</strong>
</p>
<div class="bg-white p-8 rounded-3xl border border-slate-200 shadow-lg mb-12 relative overflow-hidden">
<div class="absolute top-0 right-0 w-32 h-32 bg-fuchsia-50 rounded-bl-full opacity-50"></div>
<h4 class="text-center font-bold text-slate-800 mb-8 text-xl">What might future multimodal explanations look like?</h4>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
<!-- Concept 1 -->
<div
class="group p-6 rounded-xl bg-slate-50 hover:bg-fuchsia-50 transition-colors border border-slate-100 hover:border-fuchsia-200 cursor-pointer">
<div class="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">🔦</div>
<h5 class="font-bold text-slate-800 mb-2">Visual Grounding in CoT</h5>
<p class="text-sm text-slate-600">
The chain of thought is no longer just words; it is interspersed with <code>&lt;box&gt;</code> coordinates.
<br>
<span
class="text-xs bg-white px-1 rounded border border-slate-200 mt-2 inline-block italic">"Because this region
[10,10,50,50] is red..."</span>
</p>
</div>
<!-- Concept 2 -->
<div
class="group p-6 rounded-xl bg-slate-50 hover:bg-purple-50 transition-colors border border-slate-100 hover:border-purple-200 cursor-pointer">
<div class="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">🎬</div>
<h5 class="font-bold text-slate-800 mb-2">Temporal Attribution</h5>
<p class="text-sm text-slate-600">
When answering questions about a video, highlight the key segments on the timeline.
<br>
<span
class="text-xs bg-white px-1 rounded border border-slate-200 mt-2 inline-block italic">"Conclusion inferred from the frames
between 00:15 and 00:20."</span>
</p>
</div>
<!-- Concept 3 -->
<div
class="group p-6 rounded-xl bg-slate-50 hover:bg-indigo-50 transition-colors border border-slate-100 hover:border-indigo-200 cursor-pointer">
<div class="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">🧠</div>
<h5 class="font-bold text-slate-800 mb-2">Mechanism Interpretation</h5>
<p class="text-sm text-slate-600">
Open up DeepStack's black box and see what visual features each layer has actually learned.
</p>
</div>
</div>
</div>
<!-- 10.3 World Model -->
<div class="sr-only">

### 10.3 Towards a World Model: Predicting the Future

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
10.3 Towards a World Model: Predicting the Future
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Today's Qwen-VL is still a <strong>passive observer</strong>: it analyses whatever you show it. But a true agent needs to be able to <strong>predict the future</strong>.
</p>
<div class="bg-indigo-900 text-white p-8 rounded-3xl shadow-2xl relative overflow-hidden">
<!-- Animated Pulse -->
<div
class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-indigo-500 rounded-full blur-[120px] opacity-20 animate-pulse">
</div>
<div class="relative z-10 flex flex-col md:flex-row items-center gap-8">
<div class="w-full md:w-1/2">
<h4 class="text-2xl font-bold mb-4 text-indigo-100">Next Token Prediction <br>→ <span
class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-300 to-blue-300">Next Frame
Prediction</span></h4>
<p class="text-indigo-200 text-sm leading-relaxed mb-6">
If a model can predict not only the next word but also the next frame, it has common sense about the physical world.
</p>
<div class="space-y-3">
<div class="flex items-center bg-indigo-800/50 p-3 rounded-lg border border-indigo-700">
<span class="mr-3">🤖</span>
<span class="text-xs text-indigo-100">Robotics: if I accidentally knock over this cup, where will the water flow?</span>
</div>
<div class="flex items-center bg-indigo-800/50 p-3 rounded-lg border border-indigo-700">
<span class="mr-3">🚗</span>
<span class="text-xs text-indigo-100">Autonomous driving: the car ahead just lit its brake lights. What happens next?</span>
</div>
</div>
</div>
<div class="w-full md:w-1/2 border-l border-indigo-700 pl-8">
<p class="text-sm text-indigo-300 font-bold mb-2 uppercase tracking-wider">Research Frontier</p>
<p class="text-lg font-serif text-white leading-relaxed italic">
"Generative models are not just for creating pretty pictures. They are the engines of
imagination, allowing agents to simulate outcomes before acting."
</p>
<div class="mt-6 flex gap-2">
<span class="px-3 py-1 bg-indigo-600 rounded-full text-xs">Unified Generation</span>
<span class="px-3 py-1 bg-indigo-600 rounded-full text-xs">Video Prediction</span>
</div>
</div>
</div>
</div>
<!-- 10.4 Evaluation 2.0 -->
<div class="sr-only">

### 10.4 An Evaluation Revolution: From Leaderboard Chasing to Real-World Scenarios

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
10.4 An Evaluation Revolution: From Leaderboard Chasing to Real-World Scenarios
</h3>
<div class="border-l-4 border-amber-500 pl-6 py-2 mb-8">
<p class="text-xl text-slate-700 font-medium">
"When a measure becomes a target, it ceases to be a good measure." (Goodhart's law)
</p>
</div>
<p class="text-lg text-slate-600 mb-8 leading-relaxed">
Today's benchmarks (MMMU, MathVista) are hard, but mostly they are still static "exam questions". Future evaluation should be closer to <strong>the dynamic real world</strong>.
</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
<!-- Card 1 -->
<div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
<div class="h-10 w-10 bg-slate-100 rounded-full flex items-center justify-center text-xl mb-4">🕵️</div>
<h5 class="font-bold text-slate-800 mb-2">Long-term Stability</h5>
<p class="text-xs text-slate-500">
Let the model run continuously for 24 hours, or handle 1000 rounds of dialogue. Will it "go off the rails"? Will it forget the settings it was given earlier?
</p>
</div>
<!-- Card 2 -->
<div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
<div class="h-10 w-10 bg-slate-100 rounded-full flex items-center justify-center text-xl mb-4">🎮</div>
<h5 class="font-bold text-slate-800 mb-2">Interactive Env</h5>
<p class="text-xs text-slate-500">
Drop the model into Minecraft or a real OS environment and see whether it can complete a task like "create a new folder and rename it", which is simple but needs a closed loop.
</p>
</div>
<!-- Card 3 -->
<div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
<div class="h-10 w-10 bg-slate-100 rounded-full flex items-center justify-center text-xl mb-4">🛡️</div>
<h5 class="font-bold text-slate-800 mb-2">Visual Safety</h5>
<p class="text-xs text-slate-500">
Defence against visual jailbreaks. If malicious instructions are hidden in an image, can the model recognise and refuse them?
</p>
</div>
</div>
<!-- Transition -->
<div
class="mt-24 p-8 bg-gradient-to-r from-violet-600 to-fuchsia-600 rounded-3xl text-center relative overflow-hidden shadow-2xl">
<div
class="absolute top-0 left-0 w-full h-full bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-10">
</div>
<h4 class="text-3xl font-bold text-white mb-6 relative z-10">Closing words</h4>
<p class="text-lg text-violet-100 max-w-3xl mx-auto leading-relaxed mb-8 relative z-10">
These very long lecture notes end here. We started from Qwen-VL's first attempt and walked all the way to the showdown at the top with Qwen3-VL.
<br><br>
I hope that after these lecture-style explanations, what stays in your head is not just a pile of dry acronyms (ViT, MRoPE, DeepStack), but a <strong>living map of how the technology evolved</strong>.
<br>
The road ahead is long, but the direction is clear. Take this map with you and go build your own multimodal SOTA!
</p>
<div class="flex justify-center space-x-4 relative z-10">
<span class="text-4xl animate-bounce">🎓</span>
<span class="text-4xl animate-bounce animation-delay-200">🚀</span>
<span class="text-4xl animate-bounce animation-delay-500">🌟</span>
</div>
</div>
</div>
</section>
<section id="appendix-math" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## A Appendix 1: Mathematical Intuition and Visualisation: Don't Just Memorise Formulas, See the Shape of the Maths

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-indigo-500 to-violet-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:rotate-12 transition-transform duration-300">A</span>
<div class="flex flex-col">
<span
class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-violet-600">Appendix 1: Mathematical Intuition and Visualisation</span>
<span class="text-2xl text-slate-500 font-medium mt-2">Don't just memorise formulas; see the shape of the maths</span>
</div>
</h2>
<!-- Intro Block -->
<div class="mb-16 bg-white p-10 rounded-[2rem] shadow-premium border border-slate-100 relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-indigo-400 via-violet-500 to-purple-500">
</div>
<div
class="absolute -right-10 -bottom-10 w-64 h-64 bg-indigo-50 rounded-full mix-blend-multiply filter blur-3xl opacity-50">
</div>
<p class="text-xl text-slate-700 leading-relaxed relative z-10">
Many students get a headache the moment they see the <span class="font-serif italic">Math Section</span> of a paper, as if it were written for aliens.
<br>
But in fact, every loss function in deep learning is essentially defining a kind of <strong>"physical force field"</strong>.
</p>
<p class="text-lg text-slate-600 leading-relaxed mt-4 relative z-10">
In this section we won't do complicated derivations or proofs; instead we'll use <strong>geometric intuition</strong> to draw the four most important mathematical concepts in the Qwen-VL
series. Let's see how these formulas act like invisible "hands", pushing tens of billions of parameters around.
</p>
</div>
<!-- A.1 Language Modeling Loss -->
<div class="mb-20">
<div class="flex items-center mb-8">
<div
class="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center text-indigo-600 font-bold text-xl mr-4">
1</div>
<div class="sr-only">

### Language Modelling Loss (The Prediction Game)

</div>

<h3 class="text-3xl font-bold text-slate-800">Language Modelling Loss (The Prediction Game)</h3>
</div>
<!-- Concept Card -->
<div class="bg-white rounded-3xl shadow-lg border border-slate-200 overflow-hidden mb-10">
<!-- Formula Header -->
<div class="bg-slate-50 px-8 py-6 border-b border-slate-200 flex justify-center items-center">
<div class="font-serif text-2xl text-slate-800 tracking-wide">
<!-- HTML Math Representation -->
<span class="italic">L</span><sub>text</sub> =
<span class="mx-2 text-indigo-600">-</span>
<span class="inline-block relative top-1 text-3xl mx-1 text-slate-500">&sum;</span>
<span class="text-sm uppercase tracking-wider text-slate-400 mx-2">log</span>
<span class="italic">P</span>(
<span class="italic font-bold text-indigo-700">x<sub>t</sub></span>
<span class="mx-1 text-slate-400">|</span>
<span class="italic text-slate-600">x<sub>&lt;t</sub></span>,
<span class="italic text-emerald-600 font-bold">V</span>
)
</div>
</div>
<div class="p-8 grid grid-cols-1 lg:grid-cols-2 gap-10">
<!-- Text Explanation -->
<div class="space-y-6">
<div>
<h4 class="font-bold text-indigo-900 mb-2 flex items-center">
<span class="w-2 h-2 bg-indigo-500 rounded-full mr-2"></span>
Breaking down the symbols
</h4>
<ul class="space-y-2 text-slate-600 text-sm font-mono">
<li><span class="bg-indigo-50 text-indigo-700 px-1 rounded">x<sub>t</sub></span> :
the "correct answer" we want the model to predict (the ground-truth token).</li>
<li><span class="bg-slate-100 text-slate-600 px-1 rounded">x<sub>&lt;t</sub></span> :
everything that has been said so far (the context).</li>
<li><span class="bg-emerald-50 text-emerald-700 px-1 rounded">V</span> : the visual signal (visual
tokens), the biggest difference between an LVLM and an LLM.</li>
</ul>
</div>
<div>
<h4 class="font-bold text-indigo-900 mb-2 flex items-center">
<span class="w-2 h-2 bg-indigo-500 rounded-full mr-2"></span>
Physical intuition: a tug of war
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
Imagine the vocabulary has 100,000 words, and each word is a "hole". The model holds a "ball" (probability mass, total weight 1).
<br>
The goal of this formula is to <strong>force the model to throw as much of that ball as possible into the "correct answer" hole.</strong>
<br>
If it misses (say it predicts "dog" instead of "cat"), <span class="font-mono text-red-500">-log(P)</span>
becomes huge (the penalty), and backpropagation kicks the parameters back into line.
</p>
</div>
</div>
<!-- SVG Visualization -->
<div
class="flex flex-col items-center justify-center bg-slate-50 rounded-xl p-6 border border-slate-100">
<svg width="350" height="220" viewBox="0 0 350 220" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#64748b" />
</marker>
</defs>
<!-- Text Context -->
<text x="20" y="100" font-family="monospace" font-size="12" fill="#64748b">x_&lt;t: "This is
a"</text>
<!-- Visual Token Injection -->
<circle cx="100" cy="40" r="15" fill="#d1fae5" stroke="#10b981" stroke-width="2" />
<text x="100" y="45" text-anchor="middle" font-size="10" fill="#047857"
font-weight="bold">V</text>
<path d="M 100 60 L 120 90" stroke="#10b981" stroke-width="2" stroke-dasharray="4,2"
marker-end="url(#arrow)" />
<!-- Model Blackbox -->
<rect x="120" y="80" width="80" height="60" rx="8" fill="#e0e7ff" stroke="#6366f1"
stroke-width="2" />
<text x="160" y="115" text-anchor="middle" font-weight="bold" fill="#4338ca"
font-size="14">LLM</text>
<!-- Output Probabilities -->
<g transform="translate(220, 60)">
<!-- Bar 1 (Wrong) -->
<rect x="0" y="80" width="20" height="20" fill="#fca5a5" />
<text x="10" y="115" text-anchor="middle" font-size="10" fill="#64748b">Dog</text>
<!-- Bar 2 (Correct) -->
<rect x="40" y="20" width="20" height="80" fill="#86efac" stroke="#16a34a"
stroke-width="2" />
<text x="50" y="115" text-anchor="middle" font-size="10" fill="#15803d"
font-weight="bold">Cat</text>
<text x="50" y="15" text-anchor="middle" font-size="12" fill="#16a34a"
font-weight="bold">Target!</text>
<!-- Bar 3 (Wrong) -->
<rect x="80" y="90" width="20" height="10" fill="#fca5a5" />
<text x="90" y="115" text-anchor="middle" font-size="10" fill="#64748b">Car</text>
</g>
<!-- Loss Arrow -->
<path d="M 270 20 L 270 10" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow)" />
<text x="270" y="5" text-anchor="middle" font-size="10" fill="#ef4444">Maximize This!</text>
</svg>
<p class="text-xs text-slate-500 mt-4 text-center">
Illustrated: the visual signal V changes the LLM's predicted probability for "Cat".
</p>
</div>
</div>
</div>
</div>
<!-- A.2 Contrastive Loss -->
<div class="mb-20">
<div class="flex items-center mb-8">
<div
class="w-10 h-10 bg-emerald-100 rounded-lg flex items-center justify-center text-emerald-600 font-bold text-xl mr-4">
2</div>
<div class="sr-only">

### Contrastive Loss (The Magnet)

</div>

<h3 class="text-3xl font-bold text-slate-800">Contrastive Loss (The Magnet)</h3>
</div>
<div class="bg-white rounded-3xl shadow-lg border border-slate-200 overflow-hidden mb-10">
<!-- Formula Header -->
<div class="bg-slate-50 px-8 py-6 border-b border-slate-200 flex justify-center items-center">
<div class="font-serif text-xl text-slate-800 tracking-wide">
<!-- HTML Math Representation -->
<span class="italic">L</span><sub>con</sub> =
<span class="mx-2 text-indigo-600">-</span>
<span class="text-lg">log</span>
<div class="inline-block align-middle text-center mx-2">
<div class="border-b border-slate-400 pb-1 mb-1">
exp( sim(<span class="text-blue-600 font-bold">v<sub>i</sub></span>, <span
class="text-emerald-600 font-bold">t<sub>i</sub></span>) / &tau; )
</div>
<div>
<span class="text-slate-500">&sum;</span><sub>j</sub> exp( sim(<span
class="text-blue-600 font-bold">v<sub>i</sub></span>, <span
class="text-rose-600 font-bold">t<sub>j</sub></span>) / &tau; )
</div>
</div>
</div>
</div>
<div class="p-8 grid grid-cols-1 lg:grid-cols-2 gap-10">
<!-- Text Explanation -->
<div class="space-y-6">
<div>
<h4 class="font-bold text-emerald-900 mb-2 flex items-center">
<span class="w-2 h-2 bg-emerald-500 rounded-full mr-2"></span>
Intuition: finding your friend at a party
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
Imagine the high-dimensional space as a huge dance floor.
<br>
<span class="text-blue-600 font-bold">v<sub>i</sub></span> is an image (say "a dog"), and <span
class="text-emerald-600 font-bold">t<sub>i</sub></span> is its description ("A cute
dog"). They are a pair of good friends.
<br>
<span class="text-rose-600 font-bold">t<sub>j</sub></span> are the descriptions of other passers-by (e.g. "A red car").
<br>
<strong>This loss is a magnet:</strong> it pulls the friendly pair <span
class="font-mono text-xs bg-slate-100 p-0.5">i-i</span> hard towards each other (the numerator grows), while pushing all the passers-by
<span class="font-mono text-xs bg-slate-100 p-0.5">i-j</span> hard away (the denominator shrinks).
</p>
</div>
<div class="bg-amber-50 p-4 rounded-lg border-l-4 border-amber-400">
<p class="text-amber-800 text-xs font-bold mb-1">🤔 The teacher's follow-up question:</p>
<p class="text-amber-700 text-xs">
Why does the denominator sum over all
<code>j</code>? Because pulling friends together isn't enough. If you don't push others away, eventually all points collapse onto the same origin, and the model learns that "everyone is the same", which is another form of cheating!
</p>
</div>
</div>
<!-- SVG Visualization -->
<div
class="flex flex-col items-center justify-center bg-slate-50 rounded-xl p-6 border border-slate-100">
<svg width="300" height="250" viewBox="0 0 300 250" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="arrow-pull" markerWidth="10" markerHeight="10" refX="9" refY="3"
orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#10b981" />
</marker>
<marker id="arrow-push" markerWidth="10" markerHeight="10" refX="9" refY="3"
orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#f43f5e" />
</marker>
</defs>
<!-- Central Anchor Image -->
<circle cx="150" cy="125" r="20" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2" />
<text x="150" y="130" text-anchor="middle" font-weight="bold" fill="white"
font-size="12">Img</text>
<!-- Positive Text (Pull) -->
<circle cx="100" cy="80" r="15" fill="#10b981" stroke="#047857" stroke-width="2" />
<text x="100" y="85" text-anchor="middle" font-weight="bold" fill="white"
font-size="10">Text+</text>
<line x1="115" y1="95" x2="135" y2="110" stroke="#10b981" stroke-width="3"
marker-end="url(#arrow-pull)" />
<text x="110" y="60" text-anchor="middle" font-size="10" fill="#10b981"
font-weight="bold">Pull</text>
<!-- Negative Text 1 (Push) -->
<circle cx="200" cy="80" r="15" fill="#f43f5e" stroke="#be123c" stroke-width="2" />
<text x="200" y="85" text-anchor="middle" font-weight="bold" fill="white"
font-size="10">Text-</text>
<line x1="165" y1="110" x2="185" y2="95" stroke="#f43f5e" stroke-width="2"
marker-end="url(#arrow-push)" stroke-dasharray="3,2" />
<!-- Negative Text 2 (Push) -->
<circle cx="150" cy="180" r="15" fill="#f43f5e" stroke="#be123c" stroke-width="2" />
<text x="150" y="185" text-anchor="middle" font-weight="bold" fill="white"
font-size="10">Text-</text>
<line x1="150" y1="145" x2="150" y2="160" stroke="#f43f5e" stroke-width="2"
marker-end="url(#arrow-push)" stroke-dasharray="3,2" />
<text x="220" y="150" text-anchor="middle" font-size="10" fill="#f43f5e"
font-weight="bold">Push Away</text>
<!-- Field lines -->
<circle cx="150" cy="125" r="60" fill="none" stroke="#cbd5e1" stroke-width="1"
stroke-dasharray="4" />
<circle cx="150" cy="125" r="90" fill="none" stroke="#cbd5e1" stroke-width="1"
stroke-dasharray="4" />
</svg>
<p class="text-xs text-slate-500 mt-2 text-center">
Attraction and repulsion in the embedding space
</p>
</div>
</div>
</div>
</div>
<!-- A.3 Grounding Loss -->
<div class="mb-20">
<div class="flex items-center mb-8">
<div
class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center text-purple-600 font-bold text-xl mr-4">
3</div>
<div class="sr-only">

### Grounding Loss (The Anchor)

</div>

<h3 class="text-3xl font-bold text-slate-800">Grounding Loss (The Anchor)</h3>
</div>
<div class="bg-white rounded-3xl shadow-lg border border-slate-200 overflow-hidden mb-10">
<!-- Formula Header -->
<div class="bg-slate-50 px-8 py-6 border-b border-slate-200 flex justify-center items-center">
<div class="font-serif text-xl text-slate-800 tracking-wide">
<span class="italic">L</span><sub>loc</sub> =
<span class="mx-2">&lambda;</span><sub>L1</sub>
<span class="mx-1">||</span>
<span class="text-blue-600 font-bold">b<sub>pred</sub></span> -
<span class="text-emerald-600 font-bold">b<sub>gt</sub></span>
<span class="mx-1">||<sub>1</sub></span>
<span class="mx-2">+</span>
<span class="mx-2">&lambda;</span><sub>GIoU</sub>
<span class="italic">L</span><sub>GIoU</sub>
(
<span class="text-blue-600 font-bold">b<sub>pred</sub></span>,
<span class="text-emerald-600 font-bold">b<sub>gt</sub></span>
)
</div>
</div>
<div class="p-8 grid grid-cols-1 lg:grid-cols-2 gap-10">
<!-- Text Explanation -->
<div class="space-y-6">
<div>
<h4 class="font-bold text-purple-900 mb-2 flex items-center">
<span class="w-2 h-2 bg-purple-500 rounded-full mr-2"></span>
Why do we need two losses?
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
In object detection or grounding tasks, we usually constrain the model with two measures:
</p>
<ul class="list-disc list-inside text-slate-600 text-sm mt-2 space-y-2">
<li>
<strong>L1 Loss:</strong> a simple, blunt "sense of distance". It computes the absolute difference between the corner coordinates of the predicted box and the true box. It's like pulling the predicted box towards the true box with a spring.
</li>
<li>
<strong>GIoU Loss:</strong> a more refined "sense of shape". Relying on L1 alone, two boxes might have close centres yet not overlap at all. IoU looks at the overlapping area, and GIoU
fixes the problem of zero gradient when the boxes don't overlap.
</li>
</ul>
</div>
</div>
<!-- SVG Visualization -->
<div
class="flex flex-col items-center justify-center bg-slate-50 rounded-xl p-6 border border-slate-100">
<svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
<defs>
<pattern id="diag-lines" width="10" height="10" patternUnits="userSpaceOnUse">
<path d="M-1,1 l2,-2 M0,10 l10,-10 M9,11 l2,-2" stroke="#cbd5e1" stroke-width="1" />
</pattern>
</defs>
<!-- Image Frame -->
<rect x="10" y="10" width="280" height="180" fill="white" stroke="#e2e8f0"
stroke-width="2" />
<!-- Ground Truth Box -->
<rect x="150" y="50" width="100" height="80" fill="#d1fae5" stroke="#10b981"
stroke-width="2" stroke-dasharray="5,5" />
<text x="200" y="95" text-anchor="middle" font-size="12" fill="#10b981"
font-weight="bold">GT</text>
<!-- Predicted Box -->
<rect x="50" y="80" width="80" height="60" fill="none" stroke="#3b82f6" stroke-width="2" />
<text x="90" y="115" text-anchor="middle" font-size="12" fill="#3b82f6"
font-weight="bold">Pred</text>
<!-- L1 Force (Springs) -->
<path d="M 90 80 Q 120 40 150 50" stroke="#f59e0b" stroke-width="2" fill="none"
stroke-dasharray="2,1" />
<text x="120" y="50" font-size="10" fill="#f59e0b">L1 Pull</text>
<path d="M 130 140 Q 170 160 200 130" stroke="#f59e0b" stroke-width="2" fill="none"
stroke-dasharray="2,1" />
<text x="160" y="160" font-size="10" fill="#f59e0b">L1 Pull</text>
<!-- GIoU Enclosure (Abstract) -->
<rect x="50" y="50" width="200" height="90" fill="none" stroke="#94a3b8" stroke-width="1"
stroke-dasharray="2,2" />
<text x="55" y="65" font-size="10" fill="#94a3b8">Enclosing Box (for GIoU)</text>
</svg>
<p class="text-xs text-slate-500 mt-2 text-center">
The yellow spring represents the L1 loss; the grey dashed box is used to compute GIoU.
</p>
</div>
</div>
</div>
</div>
<!-- A.4 RoPE Geometry -->
<div class="mb-20">
<div class="flex items-center mb-8">
<div
class="w-10 h-10 bg-amber-100 rounded-lg flex items-center justify-center text-amber-600 font-bold text-xl mr-4">
4</div>
<div class="sr-only">

### The Geometry of RoPE / M-RoPE (The Clock)

</div>

<h3 class="text-3xl font-bold text-slate-800">The Geometry of RoPE / M-RoPE (The Clock)</h3>
</div>
<div class="bg-white rounded-3xl shadow-lg border border-slate-200 overflow-hidden">
<div class="p-8 flex flex-col md:flex-row gap-10 items-center">
<div class="w-full md:w-1/2">
<p class="text-slate-600 text-lg leading-relaxed mb-4">
RoPE (Rotary Positional Embedding) is the cornerstone of every Qwen model.
<br><br>
Its core idea is: <strong>position is not addition, it is rotation.</strong>
<br>
Without positional encoding, tokens are like a pile of words scattered on a table;
<br>
with absolute PE, it's like sticking a number tag on each word;
<br>
with <strong>RoPE</strong>, it's like fitting each word with a "clock". For the word at position $m$, its vector is rotated in space by an angle of $m \times \theta$.
</p>
<div class="bg-slate-900 text-slate-300 p-4 rounded-xl font-mono text-sm shadow-inner">
<span class="text-purple-400">f</span>(q, m) =
<span class="text-blue-400">R</span><sub>m</sub>
<span class="text-white">&middot;</span> q
<br>
<span class="text-slate-500">// R_m is a rotation matrix</span>
</div>
</div>
<div class="w-full md:w-1/2 flex justify-center">
<svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
<!-- Coordinate System -->
<line x1="150" y1="280" x2="150" y2="20" stroke="#cbd5e1" stroke-width="1" />
<line x1="20" y1="150" x2="280" y2="150" stroke="#cbd5e1" stroke-width="1" />
<!-- Circle -->
<circle cx="150" cy="150" r="100" fill="none" stroke="#e2e8f0" stroke-width="1" />
<!-- Vector 0 (Pos 0) -->
<line x1="150" y1="150" x2="250" y2="150" stroke="#94a3b8" stroke-width="2"
stroke-dasharray="4" />
<text x="260" y="155" font-size="12" fill="#94a3b8">Pos 0</text>
<!-- Vector 1 (Pos 1) -->
<g transform="rotate(-30, 150, 150)">
<line x1="150" y1="150" x2="250" y2="150" stroke="#60a5fa" stroke-width="3" />
<circle cx="250" cy="150" r="4" fill="#60a5fa" />
<text x="260" y="155" font-size="12" fill="#60a5fa" font-weight="bold">Pos 1</text>
</g>
<!-- Vector 2 (Pos 2) -->
<g transform="rotate(-60, 150, 150)">
<line x1="150" y1="150" x2="250" y2="150" stroke="#818cf8" stroke-width="3" />
<circle cx="250" cy="150" r="4" fill="#818cf8" />
<text x="260" y="155" font-size="12" fill="#818cf8" font-weight="bold">Pos 2</text>
</g>
<!-- Angle Theta -->
<path d="M 220 150 A 70 70 0 0 0 210.6 115" fill="none" stroke="#f59e0b" stroke-width="2" />
<text x="225" y="130" font-size="14" fill="#f59e0b">&theta;</text>
<!-- Relative Distance -->
<text x="150" y="290" text-anchor="middle" font-size="12" fill="#475569"
font-style="italic">
Relative distance = angle gap (Pos2 - Pos1 = &theta;)
</text>
</svg>
</div>
</div>
<div class="bg-indigo-50 px-8 py-4 border-t border-indigo-100">
<p class="text-sm text-indigo-900 font-bold mb-1">🔍 Extending the intuition to M-RoPE:</p>
<p class="text-sm text-indigo-800">
Once you understand this 2D rotation, M-RoPE is easy: it just cuts the vector into three segments and rotates each in its own <strong>orthogonal</strong> plane.
<br>
One segment rotates along the time axis $t$, one along the height axis $h$, and one along the width axis $w$.
</p>
</div>
</div>
</div>
</div>
</section>
<section id="appendix-cheatsheet" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## B Appendix 2: An AI4S Cheat Sheet: When Qwen-VL Puts On a Lab Coat, from Cells to Galaxies

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-teal-500 to-emerald-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:rotate-6 transition-transform duration-300">B</span>
<div class="flex flex-col">
<span class="text-transparent bg-clip-text bg-gradient-to-r from-teal-600 to-emerald-600">Appendix 2: An AI4S
Cheat Sheet</span>
<span class="text-2xl text-slate-500 font-medium mt-2">When Qwen-VL puts on a lab coat: from cells to galaxies</span>
</div>
</h2>
<!-- Intro Block -->
<div class="mb-16 bg-white p-10 rounded-[2rem] shadow-premium border border-slate-100 relative overflow-hidden">
<div
class="absolute top-0 right-0 w-[400px] h-[400px] bg-teal-50 rounded-full mix-blend-multiply filter blur-[80px] opacity-60 animate-pulse">
</div>
<div
class="absolute bottom-0 left-0 w-[300px] h-[300px] bg-emerald-50 rounded-full mix-blend-multiply filter blur-[60px] opacity-60">
</div>
<div class="sr-only">

### 🧬 Why Do Scientists Need Multimodal Large Models?

</div>

<h3 class="text-2xl font-bold text-slate-800 mb-6 flex items-center relative z-10">
<span class="text-3xl mr-3">🧬</span> Why do scientists need multimodal large models?
</h3>
<p class="text-lg text-slate-600 leading-relaxed relative z-10">
Everyone, in AI for Science (AI4S) we often deal with extremely abstract data: gene sequences, protein structures, pathology slides.
Traditional methods (such as CNNs and U-Net) are good at outputting "probabilities" or "segmentation masks", but they cannot <strong>"explain"</strong> what they see.
</p>
<p class="text-lg text-slate-600 leading-relaxed mt-4 relative z-10">
The value of the Qwen-VL series is that it can translate the <strong>visual signal (pixels)</strong> under the microscope into the biologist's <strong>language (text/code)</strong>.
<br>
This appendix walks you step by step through turning Qwen-VL into your <strong>"round-the-clock AI lab assistant"</strong>.
</p>
</div>
<!-- B.1 Scenario Mapping Table -->
<div class="sr-only">

### B.1 Mapping Research Scenarios: Which Model Fits Your Task?

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-teal-500 rounded-full mr-4 shadow-md"></span>
B.1 Mapping Research Scenarios: Which Model Fits Your Task?
</h3>
<div class="overflow-x-auto mb-12 rounded-2xl border border-slate-200 shadow-lg">
<table class="min-w-full bg-white">
<thead class="bg-slate-900 text-white">
<tr>
<th class="px-6 py-4 text-left font-bold text-lg">Research task (AI4S Task)</th>
<th class="px-6 py-4 text-left font-bold text-lg">Typical scenarios</th>
<th class="px-6 py-4 text-left font-bold text-lg">Recommended model</th>
<th class="px-6 py-4 text-left font-bold text-lg">Main reason</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-100 text-slate-700">
<!-- Row 1: Single Cell -->
<tr class="hover:bg-teal-50 transition-colors group">
<td class="px-6 py-6 font-bold text-teal-700">
<div class="flex items-center">
<span class="text-2xl mr-2">🧫</span> Cell2Sentence
</div>
</td>
<td class="px-6 py-6 text-sm">
Single-cell morphology analysis<br>
Drug Screen Phenotyping<br>
Generating cell-state descriptions from images
</td>
<td class="px-6 py-6">
<span
class="bg-blue-100 text-blue-800 px-2 py-1 rounded font-mono font-bold">Qwen2-VL-7B</span>
</td>
<td class="px-6 py-6 text-sm">
Single-cell images usually have moderate resolution but need strong semantic alignment. 7B is the best value, and fine-tuning is cheap.
</td>
</tr>
<!-- Row 2: Spatial Transcriptomics -->
<tr class="hover:bg-emerald-50 transition-colors group">
<td class="px-6 py-6 font-bold text-emerald-700">
<div class="flex items-center">
<span class="text-2xl mr-2">🗺️</span> HE to ST
</div>
</td>
<td class="px-6 py-6 text-sm">
Predicting spatial transcriptomics from H&E-stained slides<br>
Locating pathological regions (Tumor Region)
</td>
<td class="px-6 py-6">
<span
class="bg-emerald-100 text-emerald-800 px-2 py-1 rounded font-mono font-bold">Qwen2.5-VL</span>
</td>
<td class="px-6 py-6 text-sm">
<strong>Crucial!</strong> Pathology slides (WSI) often run to hundreds of millions of pixels. Qwen2.5-VL's <strong class="text-emerald-600">Native
Dynamic Resolution</strong> can handle huge-resolution slides without losing cell-level detail.
</td>
</tr>
<!-- Row 3: Lab Agent -->
<tr class="hover:bg-indigo-50 transition-colors group">
<td class="px-6 py-6 font-bold text-indigo-700">
<div class="flex items-center">
<span class="text-2xl mr-2">🤖</span> Lab Agent
</div>
</td>
<td class="px-6 py-6 text-sm">
Controlling robotic arms in automated labs<br>
Reading values off old instrument screens<br>
Digitising lab records
</td>
<td class="px-6 py-6">
<span
class="bg-purple-100 text-purple-800 px-2 py-1 rounded font-mono font-bold">Qwen2.5-VL</span>
</td>
<td class="px-6 py-6 text-sm">
Relies on very strong <strong>OCR</strong> (reading instruments) and <strong>grounding</strong> (locating test tubes). Qwen2.5-VL
is the current SOTA here.
</td>
</tr>
<!-- Row 4: Literature Mining -->
<tr class="hover:bg-amber-50 transition-colors group">
<td class="px-6 py-6 font-bold text-amber-700">
<div class="flex items-center">
<span class="text-2xl mr-2">📑</span> Literature Mining
</div>
</td>
<td class="px-6 py-6 text-sm">
Extracting molecular formulas from PDF papers<br>
Parsing experimental data charts (ChartQA)<br>
Meta-analysis
</td>
<td class="px-6 py-6">
<span class="bg-slate-800 text-white px-2 py-1 rounded font-mono font-bold">Qwen3-VL</span>
</td>
<td class="px-6 py-6 text-sm">
Needs the ultra-long context brought by <strong>DeepStack</strong> (to digest a whole paper) and <strong>Thinking Mode</strong> (to reason through complex experimental logic).
</td>
</tr>
</tbody>
</table>
</div>
<!-- B.2 Deep Dive: HE to ST Visualization -->
<div class="sr-only">

### B.2 Illustrated in Depth: When Qwen-VL Meets Pathology Slides (HE to ST)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-emerald-500 rounded-full mr-4 shadow-md"></span>
B.2 Illustrated in Depth: When Qwen-VL Meets Pathology Slides (HE to ST)
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
In spatial transcriptomics (ST), we want to infer the expensive spatial distribution of gene expression from cheap H&E-stained images. The traditional approach is to train a CNN regression model, but Qwen-VL
offers a new, <strong>"semantic-level"</strong> way of thinking.
</p>
<div class="bg-white p-8 rounded-3xl shadow-xl border border-slate-200 my-10">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
🔬 Workflow: From Tissue to Text & Gene
</h4>
<div class="flex justify-center overflow-x-auto">
<svg width="800" height="350" viewBox="0 0 800 350" xmlns="http://www.w3.org/2000/svg"
class="font-sans">
<defs>
<marker id="arrow-sci" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
<path d="M0,0 L0,6 L9,3 z" fill="#475569" />
</marker>
<linearGradient id="cell-grad" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#fecaca;stop-opacity:1" /> <!-- Pinkish for H&E -->
<stop offset="100%" style="stop-color:#fca5a5;stop-opacity:1" />
</linearGradient>
</defs>
<!-- Input: WSI -->
<g transform="translate(50, 100)">
<text x="60" y="-20" text-anchor="middle" font-weight="bold" fill="#be123c">H&E Slide
(WSI)</text>
<rect x="0" y="0" width="120" height="120" fill="url(#cell-grad)" stroke="#be123c"
stroke-width="2" rx="4" />
<!-- Abstract Cells -->
<circle cx="30" cy="30" r="5" fill="#881337" opacity="0.6" />
<circle cx="40" cy="40" r="4" fill="#881337" opacity="0.6" />
<circle cx="80" cy="90" r="8" fill="#4c0519" opacity="0.8" /> <!-- Tumor? -->
<text x="60" y="140" text-anchor="middle" font-size="12" fill="#64748b">Gigapixel Image</text>
</g>
<!-- Dynamic Res Process -->
<g transform="translate(200, 120)">
<path d="M 0 40 L 40 40" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-sci)" />
<rect x="50" y="10" width="140" height="60" fill="#ecfdf5" stroke="#10b981" stroke-width="2"
rx="8" />
<text x="120" y="35" text-anchor="middle" font-weight="bold" fill="#047857"
font-size="12">Qwen2.5-VL</text>
<text x="120" y="55" text-anchor="middle" font-size="10" fill="#059669">Native Dynamic
Res</text>
</g>
<!-- Output 1: Semantic Description -->
<g transform="translate(420, 50)">
<path d="M -30 90 Q 0 90 20 50" stroke="#94a3b8" stroke-width="2"
marker-end="url(#arrow-sci)" />
<rect x="20" y="0" width="180" height="80" fill="#f0f9ff" stroke="#0ea5e9" stroke-width="2"
rx="8" />
<text x="30" y="25" font-size="12" font-weight="bold" fill="#0369a1">Prompt:
"Describe..."</text>
<text x="30" y="45" font-size="10" fill="#334155">"High density of infiltrating</text>
<text x="30" y="60" font-size="10" fill="#334155">lymphocytes in the stromal</text>
<text x="30" y="75" font-size="10" fill="#334155">region..."</text>
<text x="110" y="100" text-anchor="middle" font-size="12" fill="#0ea5e9"
font-weight="bold">Pathology Report</text>
</g>
<!-- Output 2: Spatial Grounding (Gene) -->
<g transform="translate(420, 200)">
<path d="M -30 -10 Q 0 -10 20 40" stroke="#94a3b8" stroke-width="2"
marker-end="url(#arrow-sci)" />
<rect x="20" y="0" width="180" height="100" fill="#fffbeb" stroke="#d97706" stroke-width="2"
rx="8" />
<text x="30" y="25" font-size="12" font-weight="bold" fill="#92400e">Prompt: "Find EGFR+"</text>
<!-- Heatmap sim -->
<rect x="30" y="35" width="160" height="40" fill="#fee2e2" />
<circle cx="150" cy="55" r="15" fill="#ef4444" filter="blur(4px)" />
<text x="30" y="90" font-size="10" fill="#92400e">Output: BBox / Heatmap</text>
<text x="110" y="120" text-anchor="middle" font-size="12" fill="#d97706" font-weight="bold">Gene
Localization</text>
</g>
<!-- Insight -->
<g transform="translate(650, 100)">
<path d="M -30 50 L 0 50" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-sci)"
stroke-dasharray="4" />
<text x="10" y="30" font-size="12" font-weight="bold" fill="#475569">Insight:</text>
<text x="10" y="50" font-size="10" fill="#64748b" width="100">Use visual tokens</text>
<text x="10" y="65" font-size="10" fill="#64748b">as "gene embeddings"</text>
</g>
</svg>
</div>
<div class="mt-6 bg-slate-50 p-4 rounded-xl border-l-4 border-emerald-500 text-sm text-slate-700">
<p><strong>👨‍🏫 Teacher's Blackboard:</strong></p>
<p class="mt-2">
Don't treat Qwen-VL as merely a "chatbot". In the HE to ST task, you can fine-tune Qwen to learn this:
<br>Input: <code>[H&E Image] <|vision_start|>...<|vision_end|> "Locate regions with high CD8+ expression"</code>
<br>Output: <code><box>[256, 256, 512, 512]</box></code>
</p>
<p class="mt-2">
This turns a complex regression problem into the <strong>grounding problem</strong> that multimodal models are best at.
</p>
</div>
</div>
<!-- B.3 Decision Tree -->
<div class="sr-only">

### B.3 A Decision Tree for Research: Don't Use a Nuke to Swat a Mosquito

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
B.3 A Decision Tree for Research: Don't Use a Nuke to Swat a Mosquito
</h3>
<div class="my-12 p-8 bg-slate-900 rounded-3xl text-slate-200 font-sans shadow-2xl relative overflow-hidden">
<div class="absolute -top-20 -left-20 w-60 h-60 bg-blue-500 rounded-full blur-[80px] opacity-20"></div>
<h4 class="text-center font-bold text-2xl text-white mb-10">🔬 AI4S Model Selector</h4>
<div class="space-y-8 relative z-10">
<!-- Decision 1 -->
<div class="flex flex-col items-center">
<div
class="bg-indigo-600 text-white px-6 py-3 rounded-full font-bold mb-4 shadow-lg border border-indigo-400">
Q1: What is your input data?
</div>
<div class="flex gap-8 w-full justify-center">
<!-- Branch Left -->
<div class="w-1/2 flex flex-col items-end pr-4 border-r border-slate-600">
<span class="text-sm text-indigo-300 mb-2">Text only / sequences (DNA/Protein)</span>
<div class="bg-slate-800 p-4 rounded-xl border border-slate-600 w-full max-w-xs">
<p class="font-bold text-white mb-1">👉 Qwen2.5-Coder / Math</p>
<p class="text-xs text-slate-400">No vision module needed. A maths/code fine-tuned version handles sequence logic better.</p>
</div>
</div>
<!-- Branch Right -->
<div class="w-1/2 flex flex-col items-start pl-4">
<span class="text-sm text-emerald-300 mb-2">Images (Cell / Tissue / Plots)</span>
<div class="text-2xl animate-bounce">⬇</div>
</div>
</div>
</div>
<!-- Decision 2 -->
<div class="flex flex-col items-center">
<div
class="bg-emerald-600 text-white px-6 py-3 rounded-full font-bold mb-4 shadow-lg border border-emerald-400">
Q2: What do the image features look like?
</div>
<div class="flex gap-4 w-full justify-center text-xs">
<div
class="bg-slate-800 p-3 rounded-lg border border-slate-600 w-1/3 hover:bg-slate-700 transition">
<span class="block text-emerald-400 font-bold mb-1">Large images, lots of detail (WSI)</span>
<span class="block text-white mb-2">👉 Qwen2.5-VL / Qwen3-VL</span>
<span class="block text-slate-500">You must use Dynamic Resolution, or the cells get scaled down until they vanish.</span>
</div>
<div
class="bg-slate-800 p-3 rounded-lg border border-slate-600 w-1/3 hover:bg-slate-700 transition">
<span class="block text-blue-400 font-bold mb-1">Reading charts/gauges (OCR)</span>
<span class="block text-white mb-2">👉 Qwen2.5-VL-72B</span>
<span class="block text-slate-500">Strongest OCR; handles complex tables and curves.</span>
</div>
<div
class="bg-slate-800 p-3 rounded-lg border border-slate-600 w-1/3 hover:bg-slate-700 transition">
<span class="block text-purple-400 font-bold mb-1">Single-cell micrographs (Small)</span>
<span class="block text-white mb-2">👉 Qwen2-VL-7B</span>
<span class="block text-slate-500">Good value; well suited to deployment on a local lab server.</span>
</div>
</div>
</div>
<!-- Decision 3 -->
<div class="flex flex-col items-center">
<div
class="bg-amber-600 text-white px-6 py-3 rounded-full font-bold mb-4 shadow-lg border border-amber-400">
Q3: How complex is the task?
</div>
<div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30 text-center max-w-lg mx-auto">
<p class="text-sm text-slate-300 mb-2">
If you need <strong>integrated reasoning</strong> across figures from several papers, or need to plan a <strong>multi-step chemical synthesis route</strong>:
</p>
<p class="text-lg font-bold text-amber-400">
🚀 You need Qwen3-VL (Thinking Mode)
</p>
<p class="text-xs text-slate-500 mt-1">
Only the CoT ability of Thinking Mode can handle research problems at this System 2 level.
</p>
</div>
</div>
</div>
</div>
<!-- B.4 Tips -->
<div class="sr-only">

### B.4 The Teacher's Research Tips (Tips for AI4S)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
B.4 The Teacher's Research Tips (Tips for AI4S)
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
<div class="bg-teal-50 border-l-4 border-teal-500 p-6 rounded-r-lg">
<h5 class="font-bold text-teal-900 mb-2">💡 The resolution "myth"</h5>
<p class="text-sm text-teal-800">
For pathology analysis, don't stuff a 10000x10000 WSI in directly! Even Qwen3-VL can't take that.
<br><strong>The right way:</strong> use a sliding window to cut it into 1024x1024 patches, use Qwen's batch
processing to generate local descriptions, and then have an LLM summarise them.
</p>
</div>
<div class="bg-indigo-50 border-l-4 border-indigo-500 p-6 rounded-r-lg">
<h5 class="font-bold text-indigo-900 mb-2">💡 Make good use of "Visual Prompting"</h5>
<p class="text-sm text-indigo-800">
If you want the model to focus on nuclei, overlay semi-transparent red circles (a visual prompt) on the image. Qwen-VL is very sensitive to this kind of visual cue, and it works much better than a text-only description like "look at that round thing".
</p>
</div>
<div class="bg-amber-50 border-l-4 border-amber-500 p-6 rounded-r-lg">
<h5 class="font-bold text-amber-900 mb-2">💡 Don't forget to fine-tune (LoRA)</h5>
<p class="text-sm text-amber-800">
Biomedical terms (such as "Apoptosis" and "Fibrosis") don't appear often in general corpora. Running a LoRA on a few hundred expert-annotated examples can make the model's command of the jargon improve by leaps and bounds.
</p>
</div>
<div class="bg-rose-50 border-l-4 border-rose-500 p-6 rounded-r-lg">
<h5 class="font-bold text-rose-900 mb-2">💡 Structured output is key</h5>
<p class="text-sm text-rose-800">
Don't let the model write prose! Require JSON output in the prompt (for example, when extracting experimental parameters). Qwen2.5-VL is very good at following instructions, so its output can be parsed directly by a Python script.
</p>
</div>
</div>
</div>
</section>
<!-- 14_appendix_glossary.html -->
<section id="appendix-glossary" class="mb-24 scroll-mt-24">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## C Appendix 3: The Ultimate Multimodal Jargon Dictionary (The LVLM Ultimate Glossary)

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-slate-600 to-slate-800 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:rotate-12 transition-transform duration-300">C</span>
Appendix 3: The Ultimate Multimodal Jargon Dictionary (The LVLM Ultimate Glossary)
</h2>
<p class="text-xl text-slate-600 mb-8">
This isn't just a glossary; it's an <strong>"encyclopaedia of the Qwen-VL universe"</strong>. It covers all the key components, model versions and technical terms from Qwen-VL to Qwen3-VL, to help you read the technical reports with full understanding.
</p>
<!-- Category 1: Model Family Genealogy -->
<div class="mb-12">
<div class="sr-only">

### 🌳 Model Family

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">🌳</span> Model Family
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
<!-- Qwen-VL -->
<div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
<h4 class="font-bold text-slate-800">Qwen-VL</h4>
<p class="text-xs text-slate-500 font-mono mb-1">Backbone: Qwen-7B</p>
<p class="text-sm text-slate-600">
The first generation. Based on Qwen-7B, using OpenCLIP ViT-bigG at a fixed 448x448 resolution. It laid the foundation of "three-stage training".
</p>
</div>
<!-- Qwen2-VL -->
<div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
<h4 class="font-bold text-blue-900">Qwen2-VL</h4>
<p class="text-xs text-blue-500 font-mono mb-1">Backbone: Qwen2 (2B/7B/72B)</p>
<p class="text-sm text-slate-600">
The second generation. Introduced <strong>Naive Dynamic Resolution</strong> and <strong>M-RoPE</strong>, supporting any resolution and long-video understanding.
</p>
</div>
<!-- Qwen2.5-VL -->
<div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
<h4 class="font-bold text-emerald-900">Qwen2.5-VL</h4>
<p class="text-xs text-emerald-500 font-mono mb-1">Backbone: Qwen2.5 (3B/7B/72B)</p>
<p class="text-sm text-slate-600">
The detail fanatic. Uses a <strong>Native Dynamic ViT</strong> and introduces <strong>Absolute Time Encoding</strong>, greatly strengthening document and
agent tasks.
</p>
</div>
<!-- Qwen3-VL -->
<div
class="bg-slate-900 p-5 rounded-xl border border-slate-700 shadow-sm col-span-1 md:col-span-2 lg:col-span-3">
<h4 class="font-bold text-white">Qwen3-VL</h4>
<p class="text-xs text-purple-400 font-mono mb-1">Backbone: Qwen3 (Dense & MoE)</p>
<p class="text-sm text-slate-300">
The final form. Supports a <strong>256K context</strong> and introduces <strong>DeepStack</strong> and <strong>Thinking
Mode</strong>. Comes in a 235B MoE version.
</p>
</div>
</div>
</div>
<!-- Category 2: Vision Encoders -->
<div class="mb-12">
<div class="sr-only">

### 👁️ Vision Encoders (the eyes)

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">👁️</span> Vision Encoders (the eyes)
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<!-- ViT-bigG -->
<div class="bg-white p-5 rounded-xl border-l-4 border-indigo-500 shadow-sm">
<h4 class="font-bold text-slate-800">ViT-bigG</h4>
<p class="text-sm text-slate-600 mt-1">
<strong>Used in:</strong> Qwen-VL<br>
<strong>Source:</strong> OpenCLIP (laion-2b)<br>
<strong>Params:</strong> ~1.9B<br>
<strong>Highlights:</strong> a giant ViT, good at fine-grained features, but supports only a fixed resolution.
</p>
</div>
<!-- Qwen2-ViT (Internal) -->
<div class="bg-white p-5 rounded-xl border-l-4 border-blue-500 shadow-sm">
<h4 class="font-bold text-slate-800">Qwen2-ViT (600M)</h4>
<p class="text-sm text-slate-600 mt-1">
<strong>Used in:</strong> Qwen2-VL<br>
<strong>Source:</strong> Trained from scratch (based on SigLIP)<br>
<strong>Params:</strong> ~600M<br>
<strong>Highlights:</strong> supports <strong>Naive Dynamic Resolution</strong>, resizing the input to multiples of 14x14.
</p>
</div>
<!-- Native Dynamic ViT -->
<div class="bg-white p-5 rounded-xl border-l-4 border-emerald-500 shadow-sm">
<h4 class="font-bold text-slate-800">Native Dynamic ViT</h4>
<p class="text-sm text-slate-600 mt-1">
<strong>Used in:</strong> Qwen2.5-VL<br>
<strong>Source:</strong> Trained from scratch<br>
<strong>Highlights:</strong> drops padding entirely and natively supports variable-length input sequences. Introduces <strong>window attention</strong> to cut computational cost.
</p>
</div>
<!-- SigLIP-2 -->
<div class="bg-white p-5 rounded-xl border-l-4 border-purple-500 shadow-sm">
<h4 class="font-bold text-slate-800">SigLIP-2</h4>
<p class="text-sm text-slate-600 mt-1">
<strong>Used in:</strong> Qwen3-VL<br>
<strong>Variant:</strong> SigLIP2-SO-400M / SigLIP2-Large<br>
<strong>Highlights:</strong> Google's improved image-text alignment model with strong multilingual ability; the visual initialisation base of Qwen3-VL.
</p>
</div>
</div>
</div>
<!-- Category 3: Architecture Components -->
<div class="sr-only">

### 🏗️ Core Architecture

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">🏗️</span> Core Architecture
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
<!-- Adapter / Merger -->
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">C-Attn Adapter</h5>
<p class="text-xs text-slate-500 mt-1">
(Qwen-VL) A single cross-attention layer that compresses variable-length visual features into a fixed 256 tokens.
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">MLP Merger (C-Former)</h5>
<p class="text-xs text-slate-500 mt-1">
(Qwen2-VL+) Uses 2x2 pooling + MLP to merge the features of 4 neighbouring patches into 1 token. Simple and efficient, and it keeps spatial structure.
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">DeepStack</h5>
<p class="text-xs text-slate-500 mt-1">
(Qwen3-VL) Multi-layer visual injection. Visual features are injected not only at the input layer but also into the LLM's middle layers, fixing the problem of deep networks "forgetting" the visual signal.
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">SwiGLU</h5>
<p class="text-xs text-slate-500 mt-1">
An activation function. Smoother than ReLU and able to learn more complex non-linear relationships. Standard across the whole Qwen series.
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">RMSNorm</h5>
<p class="text-xs text-slate-500 mt-1">
Root Mean Square Normalization. A normalisation layer that drops the mean computation from LayerNorm; faster, and more stable in training.
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">GQA</h5>
<p class="text-xs text-slate-500 mt-1">
Grouped Query Attention. At inference time it greatly reduces the memory taken by the KV cache and speeds up generation.
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">MoE</h5>
<p class="text-xs text-slate-500 mt-1">
Mixture of Experts. Qwen3-VL has a 30B-A3B version (30B total parameters, 3B active), which is very fast at inference.
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">FlashAttention-2</h5>
<p class="text-xs text-slate-500 mt-1">
A low-level acceleration library. Qwen2-VL relies on its <strong>VarLen</strong> feature for efficient dynamic-resolution computation.
</p>
</div>
</div>
<!-- Category 4: Positional Encodings -->
<div class="sr-only">

### 🧭 Positional Encodings

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">🧭</span> Positional Encodings
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<!-- RoPE -->
<div
class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:border-purple-200 transition-colors">
<h4 class="font-bold text-slate-800">RoPE</h4>
<p class="text-xs text-purple-600 font-mono mb-1">Rotary Positional Embedding</p>
<p class="text-sm text-slate-600">
Encodes position as a rotation angle of the vector. It has good relative-position awareness and is standard in modern LLMs.
</p>
</div>
<!-- M-RoPE -->
<div
class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:border-purple-200 transition-colors">
<h4 class="font-bold text-slate-800">M-RoPE</h4>
<p class="text-xs text-purple-600 font-mono mb-1">Multimodal RoPE</p>
<p class="text-sm text-slate-600">
(Qwen2-VL) Extends RoPE to 3D. The embedding vector is split to encode time (t), height (h) and width (w) separately.
</p>
</div>
<!-- Interleaved M-RoPE -->
<div
class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:border-purple-200 transition-colors">
<h4 class="font-bold text-slate-800">Interleaved M-RoPE</h4>
<p class="text-xs text-purple-600 font-mono mb-1">Qwen3-VL Upgrade</p>
<p class="text-sm text-slate-600">
(Qwen3-VL) To fix the spectral imbalance of the original M-RoPE (the time dimension occupies only high frequencies), it interleaves t, h and w across the whole embedding dimension.
</p>
</div>
<!-- Absolute Time Encoding -->
<div
class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:border-purple-200 transition-colors">
<h4 class="font-bold text-slate-800">Absolute Time Encoding</h4>
<p class="text-xs text-purple-600 font-mono mb-1">Text-based Timestamp</p>
<p class="text-sm text-slate-600">
(Qwen2.5/3-VL) No longer relies entirely on position IDs; instead it inserts text tokens such as <code>&lt;00:05&gt;</code> to mark time explicitly.
</p>
</div>
</div>
<!-- Category 5: Data & Tasks -->
<div class="sr-only">

### 📚 Data & Tasks

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">📚</span> Data & Tasks
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
<!-- Captioning -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Image Captioning</h5>
<p class="text-xs text-amber-800 mt-1">
Describing an image in words. Qwen uses large-scale synthetic data (recaptioning) to make captions more detailed.
</p>
</div>
<!-- VQA -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">VQA</h5>
<p class="text-xs text-amber-800 mt-1">
Visual Question Answering. Answering questions about an image. DocVQA (documents), ChartQA (charts) and InfoVQA (infographics) are the current focus.
</p>
</div>
<!-- Grounding -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Grounding / Referring</h5>
<p class="text-xs text-amber-800 mt-1">
Visual grounding. Text in, bounding box out. Qwen2.5-VL further supports points and counting.
</p>
</div>
<!-- OCR -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">OCR</h5>
<p class="text-xs text-amber-800 mt-1">
Optical Character Recognition. Reading text. Qwen-VL emphasises multilingual OCR.
</p>
</div>
<!-- Interleaved Data -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Interleaved Data</h5>
<p class="text-xs text-amber-800 mt-1">
Interleaved image-text data. Like PDFs or web pages, with text and images mixed together. Trains the model to handle multi-image context and references.
</p>
</div>
<!-- CoT Data -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Long-CoT Data</h5>
<p class="text-xs text-amber-800 mt-1">
Long chain-of-thought data. Maths or logic problems with detailed reasoning steps. Used to train Thinking Mode.
</p>
</div>
<!-- Hallucination -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Hallucination</h5>
<p class="text-xs text-amber-800 mt-1">
The model confidently talks nonsense (for example, describing objects that aren't in the image).
</p>
</div>
<!-- Zero-shot -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Zero-shot</h5>
<p class="text-xs text-amber-800 mt-1">
The model completes a task directly, without having been fine-tuned for that specific task.
</p>
</div>
</div>
</div>
</section>
<!-- 15_appendix_qa.html -->
<section id="appendix-qa" class="mb-24 scroll-mt-24">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## D Appendix 4: The Tough Questions Q&A (Teacher's Office Hours)

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-slate-600 to-slate-800 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:rotate-12 transition-transform duration-300">D</span>
Appendix 4: The Tough Questions Q&A (Teacher's Office Hours)
</h2>
<p class="text-xl text-slate-600 mb-10">
Here are some of the "hard-hitting" questions people ask most often when reproducing, training or deploying Qwen-VL. No bureaucratic answers, just the useful stuff.
</p>
<div class="space-y-10">
<!-- Q1: VRAM & Quantization -->
<div class="flex flex-col md:flex-row gap-6">
<div class="flex-shrink-0 flex flex-col items-center">
<div
class="w-16 h-16 bg-slate-100 rounded-full flex items-center justify-center text-3xl border-4 border-white shadow-md">
💸</div>
</div>
<div
class="bg-white p-8 rounded-3xl rounded-tl-none border border-slate-200 shadow-sm flex-grow relative">
<div
class="absolute top-0 left-0 -ml-3 -mt-0 w-6 h-6 bg-white border-l border-t border-slate-200 transform rotate-45">
</div>
<h4 class="text-slate-800 font-bold text-xl mb-4">Q1: I really don't have enough GPU memory. Will quantization make the model "go blind"?</h4>
<p class="text-slate-600 text-base leading-relaxed mb-4">
<strong>👨‍🏫 Teacher:</strong> That's a very good question.
<br>
Generally, <strong>Int4 / Int8 quantization</strong> has an acceptable effect on language understanding (it just gets a tiny bit dumber). But! For the <strong>vision encoder
(ViT)</strong>, please keep it at half precision (BF16/FP16) and <strong>do not quantize it</strong>!
</p>
<div class="bg-amber-50 p-4 rounded-xl border-l-4 border-amber-400 text-sm text-amber-800">
<strong>⚠️ Pitfall:</strong> the ViT usually accounts for only a small share of the total parameters (e.g. in Qwen-VL-7B only 1.9B is ViT). Quantizing
the ViT to save that 1-2GB of memory badly damages the visual features, and the model may go completely "blind". Not worth it.
<br>
<strong>Best practice:</strong> quantize the LLM to Int4 and keep the ViT in BF16.
</div>
</div>
</div>
<!-- Q2: Data Mixture -->
<div class="flex flex-col md:flex-row gap-6 md:flex-row-reverse text-right">
<div class="flex-shrink-0 flex flex-col items-center">
<div
class="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center text-3xl border-4 border-white shadow-md">
🧪</div>
</div>
<div
class="bg-indigo-50 p-8 rounded-3xl rounded-tr-none border border-indigo-100 shadow-sm flex-grow text-left relative">
<div
class="absolute top-0 right-0 -mr-3 -mt-0 w-6 h-6 bg-indigo-50 border-r border-t border-indigo-100 transform -rotate-45">
</div>
<h4 class="text-indigo-900 font-bold text-xl mb-4">Q2: If I fine-tune, how should I set the data mixture to avoid "catastrophic forgetting"?</h4>
<p class="text-indigo-800 text-base leading-relaxed mb-4">
<strong>👨‍🏫 Teacher:</strong> This question sits at the "dark arts" core of multimodal fine-tuning.
<br>
If you fine-tune only on text, visual ability drops; if you fine-tune only on images, language ability drops. Here's the rule of thumb:
</p>
<ul class="list-disc list-inside text-indigo-700 text-sm space-y-2 mb-4">
<li><strong>Domain fine-tuning:</strong> your own business data (such as medical QA).</li>
<li><strong>General image-text replay:</strong> you must mix in about <strong>10% - 20%</strong> general image-text data (such as COCO Caption,
VQAv2). This acts as "regularisation", stopping the model from forgetting its basic visual abilities.</li>
<li><strong>Text-only replay:</strong> if you care about the model's plain chat ability, it's best to mix in a little text-only dialogue data too.</li>
</ul>
</div>
</div>
<!-- Q3: Thinking Mode -->
<div class="flex flex-col md:flex-row gap-6">
<div class="flex-shrink-0 flex flex-col items-center">
<div
class="w-16 h-16 bg-pink-100 rounded-full flex items-center justify-center text-3xl border-4 border-white shadow-md">
🤯</div>
</div>
<div
class="bg-white p-8 rounded-3xl rounded-tl-none border border-slate-200 shadow-sm flex-grow relative">
<div
class="absolute top-0 left-0 -ml-3 -mt-0 w-6 h-6 bg-white border-l border-t border-slate-200 transform rotate-45">
</div>
<h4 class="text-slate-800 font-bold text-xl mb-4">Q3: Does Thinking Mode (CoT) really improve performance, or is it just padding?</h4>
<p class="text-slate-600 text-base leading-relaxed mb-4">
<strong>👨‍🏫 Teacher:</strong> For simple tasks (like "there's a cat in the picture"), CoT may indeed be padding, and the overly long output can even cause hallucinations.
<br>
But! For <strong>complex reasoning tasks</strong> (like "work out the area of the triangle in the picture" or "analyse the trend in this financial report"), CoT is a <strong>qualitative change</strong>.
</p>
<p class="text-slate-600 text-base leading-relaxed">
An LLM is fundamentally making probabilistic predictions. If you don't let it generate intermediate steps (thinking) first, it has to predict the final answer in a single step, which is far too hard. CoT
gives the model room to "work on scratch paper", breaking a complex problem into simpler ones and so lowering the difficulty of each prediction.
<br>
In Qwen3-VL, Thinking Mode raised scores on maths benchmarks like MathVista by a huge margin. That's the proof.
</p>
</div>
</div>
<!-- Q4: Video FPS -->
<div class="flex flex-col md:flex-row gap-6 md:flex-row-reverse text-right">
<div class="flex-shrink-0 flex flex-col items-center">
<div
class="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center text-3xl border-4 border-white shadow-md">
🎬</div>
</div>
<div
class="bg-emerald-50 p-8 rounded-3xl rounded-tr-none border border-emerald-100 shadow-sm flex-grow text-left relative">
<div
class="absolute top-0 right-0 -mr-3 -mt-0 w-6 h-6 bg-emerald-50 border-r border-t border-emerald-100 transform -rotate-45">
</div>
<h4 class="text-emerald-900 font-bold text-xl mb-4">Q4: When processing video, what FPS should I actually use?</h4>
<p class="text-emerald-800 text-base leading-relaxed mb-4">
<strong>👨‍🏫 Teacher:</strong> Don't get boxed in by FPS; think in terms of your <strong>token budget</strong>.
<br>
The core tension in video processing is: <strong>information vs. GPU memory</strong>.
</p>
<ul class="list-disc list-inside text-emerald-700 text-sm space-y-2">
<li><strong>Short videos (TikTok):</strong> you can use a high FPS (say 1~2 fps) to keep motion detail.</li>
<li><strong>Long films (2 hours):</strong> you must use a very low FPS (say 0.1 fps, or even keyframe extraction), or the context simply explodes.</li>
<li><strong>Qwen2.5-VL's advantage:</strong> it has dynamic resolution +
absolute time encoding. You can mix inputs: many high-resolution frames for key moments, and a few low-resolution frames for quiet stretches. As long as the timestamps line up, the model can follow.</li>
</ul>
</div>
</div>
<!-- Q5: Evaluation -->
<div class="flex flex-col md:flex-row gap-6">
<div class="flex-shrink-0 flex flex-col items-center">
<div
class="w-16 h-16 bg-slate-100 rounded-full flex items-center justify-center text-3xl border-4 border-white shadow-md">
📉</div>
</div>
<div
class="bg-white p-8 rounded-3xl rounded-tl-none border border-slate-200 shadow-sm flex-grow relative">
<div
class="absolute top-0 left-0 -ml-3 -mt-0 w-6 h-6 bg-white border-l border-t border-slate-200 transform rotate-45">
</div>
<h4 class="text-slate-800 font-bold text-xl mb-4">Q5: The CIDEr and Rouge scores in the papers are very high, so why doesn't it feel that magical when I actually use it?
</h4>
<p class="text-slate-600 text-base leading-relaxed mb-4">
<strong>👨‍🏫 Teacher:</strong> Welcome to the real world!
<br>
Traditional NLP metrics (such as Rouge, BLEU and CIDEr) mainly measure N-gram overlap. But in multimodal tasks they often <strong>break down</strong>.
<br>
For example:
<br>GT: "A white dog."
<br>Pred: "A cute puppy with snowy fur."
<br>These two sentences mean exactly the same thing, but their N-gram overlap is low, so the Rouge score is low.
<br>
<strong>The current trend:</strong> people put more weight on LLM-based evaluation (such as <strong>LLM-as-a-Judge</strong>) or on benchmarks for specific abilities (such as
MathVista for maths and DocVQA for documents). Don't put blind faith in a single metric; look at leaderboards across several dimensions.
</p>
</div>
</div>
</div>
</div>
</section>
<!-- 16_closing.html -->
<section id="closing" class="mb-32">
<div
class="bg-gradient-to-br from-slate-900 to-slate-800 rounded-[2.5rem] p-12 text-center relative overflow-hidden shadow-2xl">
<!-- Background Decorations -->
<div
class="absolute top-0 left-0 w-full h-full bg-[url('https://www.transparenttextures.com/patterns/stardust.png')] opacity-20">
</div>
<div
class="absolute -top-24 -left-24 w-64 h-64 bg-blue-500 rounded-full mix-blend-screen filter blur-[80px] opacity-30 animate-pulse">
</div>
<div
class="absolute -bottom-24 -right-24 w-64 h-64 bg-purple-500 rounded-full mix-blend-screen filter blur-[80px] opacity-30 animate-pulse animation-delay-2000">
</div>
<div class="relative z-10 max-w-4xl mx-auto">
<div class="sr-only">

## Closing: Build Your Own Eyes

</div>

<h2 class="text-3xl md:text-5xl font-extrabold text-white mb-8 tracking-tight font-serif">
Closing: Build Your Own Eyes
</h2>
<p class="text-xl text-slate-300 leading-relaxed mb-8">
This long journey is finally coming to an end.
<br>
From Qwen-VL's first attempt to the showdown at the top with Qwen3-VL, what we've seen is not only the evolutionary history of a model family, but also that of the <strong>perception module of AGI</strong>.
</p>
<div class="bg-white/10 backdrop-blur-md rounded-xl p-8 mb-10 border border-white/10 text-left">
<p class="text-slate-200 text-lg italic mb-4 font-serif">
"The eye altering alters all." (William Blake)
</p>
<p class="text-slate-300 text-base leading-relaxed">
When a model has sharper eyesight (Dynamic Resolution), it can see the details of a document;
when a model has a longer memory of time (M-RoPE + Long Context), it can understand cause and effect in video;
when a model can think deeply (Thinking Mode), it can work out the logic behind the picture.
</p>
<p class="text-slate-300 text-base leading-relaxed mt-4">
But this still isn't the end. True physical world models, embodied AI, real-time interaction... countless open problems are waiting for you to solve.
</p>
</div>
<p class="text-lg text-slate-400 mb-12">
Now close these notes, open your IDE, download the weights from Hugging Face, and get your first demo running.
<br>
<strong>Getting your hands dirty is the only shortcut to learning deep learning.</strong>
</p>
<a href="https://github.com/QwenLM/Qwen-VL" target="_blank"
class="inline-flex items-center px-8 py-4 bg-white text-slate-900 font-bold rounded-full hover:bg-blue-50 transition-all hover:scale-105 hover:shadow-lg group">
<span>Start Your Journey on GitHub</span>
<svg class="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" fill="none"
stroke="currentColor" viewBox="0 0 24 24">
<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3">
</path>
</svg>
</a>
</div>
</div>
</section>

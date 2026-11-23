---
title: "Z-Image: How a 6B Single-Stream S3-DiT Gets More from Less"
description: "Z-Image combines a single-stream S3-DiT architecture, 3D-RoPE position encoding and decoupled distillation to reach image quality comparable to an 80B model with only 6B parameters."
pubDate: 2025-12-08
externalScripts: ["https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"]
lang: en
---
<script>
mermaid.initialize({ startOnLoad: true, theme: 'default' });
</script>
<style>
/* Custom font for a more academic look if desired, though Tailwind sans is fine */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
body { font-family: 'Inter', sans-serif; }
/* Animation for the SVG */
@keyframes dash {
to {
stroke-dashoffset: 0;
}
}

/* Hide the default layout title block to avoid duplication */
article > div.mb-8.text-center { display: none !important; }
</style>
<!-- Header -->
<header class="text-center mb-12">
<div class="inline-block px-3 py-1 mb-4 text-xs font-semibold tracking-wider text-indigo-500 uppercase bg-indigo-50 rounded-full border border-indigo-100">
CVPR 2025 Candidates?
</div>
<h1 class="text-4xl md:text-5xl lg:text-6xl mb-6 bg-clip-text text-transparent bg-gradient-to-r from-slate-900 via-indigo-800 to-slate-900">
Z-Image: When a 6B Model<br>Outruns an 80B One
</h1>
<p class="text-xl text-slate-600 max-w-2xl mx-auto leading-relaxed">
Do you really need 80B parameters to generate top-quality images? Z-Image answers with a <strong>"single-stream S3-DiT architecture"</strong>:
<span class="text-indigo-600 font-semibold">Less is More, Unified is Better.</span>
</p>
<div class="flex flex-wrap justify-center gap-3 mt-8">
<span class="px-3 py-1 text-sm font-medium text-emerald-700 bg-emerald-50 rounded-full border border-emerald-200">6B Params</span>
<span class="px-3 py-1 text-sm font-medium text-emerald-700 bg-emerald-50 rounded-full border border-emerald-200">$630K Training Cost</span>
<span class="px-3 py-1 text-sm font-medium text-indigo-700 bg-indigo-50 rounded-full border border-indigo-200">Single-Stream</span>
<span class="px-3 py-1 text-sm font-medium text-amber-700 bg-amber-50 rounded-full border border-amber-200">Turbo 4-Steps</span>
</div>
</header>
<hr class="border-slate-200 my-12" />
<!-- Section 1: Intuition -->
<section class="mb-20">




## <span class="mr-3 text-4xl">🏎️</span> 1. Intuition First: When Bigger Is No Longer the Only Answer


<div class="prose prose-slate max-w-none text-lg text-slate-700 leading-relaxed">
<p class="mb-6">
Generative AI is entering a period after the race for ever-larger models. If we compare the AI race to Formula 1, the theme of the past two years fits in one blunt phrase: <strong class="text-indigo-700 bg-indigo-50 px-1 rounded">"brute force" (Scale at all costs)</strong>.
</p>
<p class="mb-6">
From Hunyuan-Image (20B+) to Flux.1 (12B), the thinking was strikingly uniform: want better images? Add parameters. Want the model to know more concepts? Add data. The result was a series of memory sinks: models so large that only the biggest companies can run them, and so heavy that even a single H800 struggles.
</p>
</div>
<!-- Blue intuition block -->
<div class="my-10 overflow-hidden rounded-xl border border-indigo-100 bg-indigo-50/50 p-8 shadow-sm transition-all hover:shadow-md">
<div class="flex items-start gap-5">
<div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-indigo-600 text-white font-bold text-2xl shadow-indigo-200 shadow-lg">?</div>
<div class="space-y-4">



#### The Key Question (Raised with Gemini)


<p class="text-indigo-800/90 m-0 text-lg leading-relaxed">
But in 2025 we have to stop and ask a counter-intuitive question:<br>
<strong>If a 6-cylinder engine (6B parameters) gets the best possible aerodynamics (architecture design) and the best fuel (data cleaning), can it beat a heavy 12-cylinder machine?</strong>
</p>
<p class="text-indigo-800/90 m-0 text-lg leading-relaxed">
Z-Image's answer: <strong>yes, and it wins with better results at lower cost.</strong>
</p>
</div>
</div>
</div>
<div class="grid md:grid-cols-2 gap-8 my-10">
<div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">




### <span class="bg-red-100 text-red-600 w-8 h-8 rounded-full flex items-center justify-center mr-2">❌</span> The Goliath Trap


<p class="text-slate-600">
Current SOTA models (such as SD3 and Flux) mostly use a <strong>Dual-Stream architecture</strong>. They work like a giant with a split mind: the left brain (Text Encoder) handles text, the right brain (DiT) handles images, and the two sit far apart, communicating only by passing notes (Cross-Attention).
<br><br>
<strong>Consequences:</strong>
<br>1. <strong>Expensive:</strong> often 20B parameters, with huge memory demands.
<br>2. <strong>Slow:</strong> information exchange is inefficient, so more sampling steps are needed.
</p>
</div>
<div class="bg-emerald-50/50 p-6 rounded-xl border border-emerald-100 shadow-sm ring-1 ring-emerald-200/50">




### <span class="bg-emerald-100 text-emerald-600 w-8 h-8 rounded-full flex items-center justify-center mr-2">✅</span> The David Strategy


<p class="text-emerald-800">
Z-Image chooses a <strong>Single-Stream architecture</strong>. It treats text and image as members of one family, concatenating them into a single sequence fed into the Transformer.
<br><br>
<strong>Advantages:</strong>
<br>1. <strong>Dense:</strong> every layer performs deep cross-modal fusion.
<br>2. <strong>Lean:</strong> 6B parameters reach SOTA quality, with roughly half the memory use.
</p>
</div>
</div>
<!-- Figure 1: The Hook -->
<figure class="my-12 bg-slate-100 p-2 rounded-xl border border-slate-200 shadow-sm">
<img src="https://arxiv.org/html/2511.22699v2/figures/showcase_realistic.jpg" alt="Z-Image Realistic Showcase" class="w-full rounded-lg" />
<figcaption class="mt-3 text-center text-sm text-slate-500 font-medium">
Figure 1: To challenge the largest models, image quality has to hold up. These are raw outputs from Z-Image-Turbo; skin texture and lighting detail both reach photographic quality.
</figcaption>
</figure>
<div class="my-8 border-l-4 border-emerald-400 bg-emerald-50 p-6 rounded-r-lg shadow-sm">
<p class="font-medium text-emerald-900 m-0 text-lg">
<strong>📊 The number that caught the field's attention: $628K</strong><br />
This is not a publication fee. It is the <strong>total cost of Z-Image's entire pre-training pipeline</strong>.
By comparison, training a Llama-3 or Flux Pro class model may cost several million dollars.
With only 314k H800 GPU hours, Z-Image shows that <strong>Efficiency is the new Scale.</strong>
</p>
</div>
<!-- SVG Visual: The Scale Wall -->
<figure class="my-12 text-center bg-white p-8 rounded-xl border border-slate-200 shadow-lg transition-transform hover:scale-[1.01]">
<svg viewBox="0 0 600 320" class="w-full max-w-3xl mx-auto" xmlns="http://www.w3.org/2000/svg">
<defs>
<pattern id="grid-pattern" width="20" height="20" patternUnits="userSpaceOnUse">
<path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1" />
</pattern>
<marker id="arrow-gray" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" />
</marker>
<marker id="arrow-indigo" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#6366f1" />
</marker>
</defs>
<!-- Background -->
<rect width="100%" height="100%" fill="url(#grid-pattern)" />
<!-- Axes -->
<line x1="50" y1="280" x2="550" y2="280" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-gray)" />
<line x1="50" y1="280" x2="50" y2="40" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-gray)" />
<text x="500" y="300" font-size="12" fill="#64748b" font-weight="bold">Size / Cost</text>
<text x="30" y="30" font-size="12" fill="#64748b" font-weight="bold" style="writing-mode: vertical-rl;">Quality</text>
<!-- Old Curve -->
<path d="M 50 280 Q 250 260 350 150 T 520 60" fill="none" stroke="#cbd5e1" stroke-width="4" stroke-dasharray="8 8" />
<text x="380" y="120" font-size="14" fill="#94a3b8" transform="rotate(-15 380 120)">Old scaling law (pricier = better)</text>
<!-- 80B Monster -->
<circle cx="520" cy="60" r="35" fill="#fca5a5" opacity="0.3" />
<circle cx="520" cy="60" r="15" fill="#ef4444" />
<text x="520" y="110" text-anchor="middle" font-size="12" fill="#b91c1c" font-weight="bold">80B giant</text>
<text x="520" y="125" text-anchor="middle" font-size="10" fill="#b91c1c">(out of reach for most)</text>
<!-- Z-Image 6B -->
<circle cx="150" cy="100" r="35" fill="#c7d2fe" opacity="0.4" />
<circle cx="150" cy="100" r="15" fill="#4f46e5" />
<text x="150" y="145" text-anchor="middle" font-size="12" fill="#312e81" font-weight="bold">Z-Image (6B)</text>
<text x="150" y="160" text-anchor="middle" font-size="10" fill="#4338ca">Runs on consumer GPUs</text>
<!-- Jump Arrow -->
<path d="M 150 260 Q 150 180 145 125" fill="none" stroke="#6366f1" stroke-width="4" marker-end="url(#arrow-indigo)" />
<text x="70" y="220" font-size="14" fill="#4f46e5" font-weight="bold">Efficiency Gap</text>
<!-- Annotation -->
<text x="220" y="200" font-size="12" fill="#475569" font-style="italic">"S3-DiT architecture dividend"</text>
</svg>
<figcaption class="mt-6 text-sm text-slate-500 italic">
Figure 1.1: The efficiency gap. Z-Image shows that with architectural innovation (blue arrow), a small model can leave the traditional curve and reach the top at one-tenth of the cost.
</figcaption>
</figure>
<p class="text-lg text-slate-700 mb-8">
Z-Image's success is not luck; it is a carefully planned <strong>shift in approach</strong>. Through the chain <strong class="text-slate-900">unified architecture (Single-Stream) + clean data (Data Profiling) + distillation speed-up (Turbo)</strong>, it brings large AI image models down to a level many more people can use.
<br><br>
Next we will take it apart layer by layer. First, let's go back five years and see how this all started.
</p>
</section>
<!-- Sub-chunk: Era 1 - The U-Net Legacy -->
<section class="mb-16">





## 🧬 2. A Short History: From Long-Distance Relationship to One Mind (The Evolution)

### Act 1: The Long-Distance Relationship (The Cross-Attention Era)


<div class="bg-slate-50 p-6 rounded-lg mb-6">
<p class="text-slate-700 leading-relaxed">
The story starts in 2022, when the leading model was <strong>Stable Diffusion 1.5</strong>.
Its architecture was a classic design, but also deeply "split". It consisted of two completely separate brains:
</p>
<ul class="list-disc list-inside text-slate-700 mt-4 space-y-2">
<li><strong>Left brain (Text Encoder):</strong> CLIP ViT-L/14. A rote learner that compresses your prompt into a 768-dimensional vector.</li>
<li><strong>Right brain (Image Generator):</strong> U-Net (860M parameters). A painter that can only paint, taking instructions from the left brain through <strong>Cross-Attention</strong>.</li>
</ul>
</div>
<div class="grid md:grid-cols-2 gap-8 mb-8">
<div>



#### 🚧 The Bottleneck: Cross-Attention


<p class="text-sm text-slate-600 mb-4">
This mechanism works like <strong>"writing a letter"</strong>. The left brain compresses everything into a letter of only 77 tokens.
When the right brain reads "Red Box left of Blue Ball", the letter is often too compressed, and it paints "Red Ball left of Blue Box" instead.
This is the well-known <strong>Attribute Bleeding</strong> problem.
</p>



#### 🩹 The SDXL Patch: Brute Force


<p class="text-sm text-slate-600">
<strong>SDXL</strong> in 2023 did not change the long-distance nature of the setup; it chose to <strong>"write a longer letter"</strong>.
<br>
It introduced <strong>Dual Text Encoders</strong>: CLIP + OpenCLIP-G.
The vector dimension jumped from 768 to 2048.
The U-Net grew to 2.6B parameters.
<br>
<span class="text-xs bg-slate-200 px-2 py-1 rounded mt-1 inline-block">Result:</span> 
Understanding improved, but the architecture stayed separated. Text and image never truly "met".
</p>
</div>
<!-- SVG Visual for Cross-Attention Bottleneck -->
<figure class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
<svg viewBox="0 0 300 200" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">
<!-- Text Brain -->
<rect x="20" y="40" width="80" height="60" rx="4" fill="#cbd5e1" stroke="#64748b" stroke-width="2" />
<text x="60" y="75" text-anchor="middle" font-weight="bold" fill="#475569" font-size="10">CLIP</text>
<text x="60" y="90" text-anchor="middle" font-size="8" fill="#64748b">(768d)</text>
<!-- Image Brain -->
<rect x="180" y="20" width="100" height="120" rx="4" fill="#e2e8f0" stroke="#475569" stroke-width="2" />
<text x="230" y="80" text-anchor="middle" font-weight="bold" fill="#475569" font-size="10">U-Net</text>
<text x="230" y="95" text-anchor="middle" font-size="8" fill="#64748b">(Pixel Space)</text>
<!-- The "Mail" -->
<path d="M 100 70 L 180 70" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#arrow-grey-1)" />
<rect x="120" y="60" width="40" height="20" fill="#fff" stroke="#94a3b8" />
<text x="140" y="74" text-anchor="middle" font-size="8" fill="#64748b">Msg</text>
<!-- Bottleneck Icon -->
<circle cx="140" cy="70" r="12" fill="none" stroke="#ef4444" stroke-width="2" />
<line x1="128" y1="82" x2="152" y2="58" stroke="#ef4444" stroke-width="2" />
<!-- SDXL Upgrade -->
<g transform="translate(0, 150)" opacity="0.6">
<text x="150" y="10" text-anchor="middle" font-size="10" fill="#64748b">SDXL: a bigger envelope (2048d)</text>
<rect x="100" y="20" width="100" height="10" rx="2" fill="#94a3b8" />
</g>
<defs>
<marker id="arrow-grey-1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" />
</marker>
</defs>
</svg>
</figure>
</div>
</section>
<!-- Sub-chunk: Era 2 - Dual Stream -->
<section class="mb-16">




### Act 2: An Expensive Duet (The Dual-Stream Era)


<div class="bg-orange-50 p-6 rounded-lg mb-6 border border-orange-100">
<p class="text-slate-800 leading-relaxed">
To let text and image communicate better, <strong>Stable Diffusion 3 (SD3)</strong> and <strong>Flux.1</strong> opened the dual-stream era.
They dropped Cross-Attention in favor of a more complex Transformer architecture.
</p>
</div>
<div class="space-y-8">
<!-- SD3: MMDiT -->
<div>



#### <span class="bg-orange-200 text-orange-800 px-2 rounded mr-2 text-sm">SD3</span> MM-DiT: Together but Apart


<p class="text-sm text-slate-700 mt-2">
SD3 introduced the <strong>Multimodal Diffusion Transformer (MM-DiT)</strong>.
<br>
<strong>Mechanism:</strong> it has two independent sets of weights, one for text and one for images.
They exchange information in the attention layers, but at heart they remain two separate "personalities".
It is like two people working at the same desk, occasionally glancing at each other's screens.
</p>
</div>
<!-- Flux: Double Stream -->
<div>



#### <span class="bg-lime-200 text-lime-800 px-2 rounded mr-2 text-sm">Flux.1</span> Hybrid Stream: Split First, Merge Later


<p class="text-sm text-slate-700 mt-2">
Flux goes a step further with a hybrid of <strong>Double-Stream Blocks</strong> and <strong>Single-Stream Blocks</strong>.
<br>
1. <strong>Early layers (Double):</strong> text and image run separately; attention is computed over the concatenation, but weights are not shared.
<br>
2. <strong>Later layers (Single):</strong> the two are merged and processed by one set of parameters.
<br>
<strong>Cost:</strong> Flux has 12B parameters, and inference needs a lot of GPU memory (24GB at minimum).
</p>
</div>
<!-- Hunyuan: MoE -->
<div>



#### <span class="bg-red-200 text-red-800 px-2 rounded mr-2 text-sm">Hunyuan</span> Mixture of Experts: Only for the Very Rich


<p class="text-sm text-slate-700 mt-2">
Tencent's Hunyuan-Image takes this to the extreme.
<strong>80B parameters!</strong> (Yes, 80 billion.)
To make it runnable, it uses <strong>MoE (Mixture of Experts)</strong>: 64 expert networks, of which only ~13B parameters are active at a time.
It is like hiring a 64-person expert team and calling only about 10 of them in for each job.
<br>
<span class="text-red-600 font-bold text-xs">Drawback:</span> enormous training cost (>$2M).
</p>
</div>
</div>
<!-- SVG Visual for Dual-Stream Complexity -->
<figure class="mt-8 bg-white p-6 rounded-xl border border-slate-200 shadow-lg">
<svg viewBox="0 0 500 240" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">
<!-- Background indicating separation -->
<rect x="20" y="20" width="200" height="200" rx="8" fill="#fff7ed" stroke="#fdba74" stroke-dasharray="4 4"/>
<rect x="280" y="20" width="200" height="200" rx="8" fill="#ecfccb" stroke="#bef264" stroke-dasharray="4 4"/>
<!-- Text Stream -->
<text x="120" y="45" text-anchor="middle" font-weight="bold" fill="#9a3412">Text Stream</text>
<rect x="50" y="60" width="140" height="140" rx="4" fill="#ffedd5" stroke="#f97316" stroke-width="2"/>
<text x="120" y="100" text-anchor="middle" font-size="11" fill="#c2410c">Text Params</text>
<text x="120" y="120" text-anchor="middle" font-size="24">🧠</text>
<!-- Image Stream -->
<text x="380" y="45" text-anchor="middle" font-weight="bold" fill="#3f6212">Image Stream</text>
<rect x="310" y="60" width="140" height="140" rx="4" fill="#d9f99d" stroke="#84cc16" stroke-width="2"/>
<text x="380" y="100" text-anchor="middle" font-size="11" fill="#4d7c0f">Image Params</text>
<text x="380" y="120" text-anchor="middle" font-size="24">🎨</text>
<!-- Interaction Bridges (Expensive) -->
<path d="M 190 90 L 310 90" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow-orange-2)" stroke-dasharray="2 2"/>
<path d="M 310 150 L 190 150" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow-orange-2)" stroke-dasharray="2 2"/>
<rect x="220" y="80" width="60" height="20" rx="4" fill="#fff" stroke="#f59e0b"/>
<text x="250" y="94" text-anchor="middle" font-size="9" fill="#d97706">Attn</text>
<rect x="220" y="140" width="60" height="20" rx="4" fill="#fff" stroke="#f59e0b"/>
<text x="250" y="154" text-anchor="middle" font-size="9" fill="#d97706">Attn</text>
<!-- Flux Note -->
<g transform="translate(180, 200)">
<rect width="140" height="20" rx="10" fill="#bef264" />
<text x="70" y="14" text-anchor="middle" font-size="10" font-weight="bold" fill="#3f6212">Flux: 12B Params!</text>
</g>
<defs>
<marker id="arrow-orange-2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#f59e0b" />
</marker>
</defs>
</svg>
<figcaption class="text-center text-xs text-orange-800 mt-2 font-mono">
Figure 2.2: Dual-Stream architecture. Two large networks run in parallel; memory use explodes and training is very hard to converge.
</figcaption>
</figure>
</section>
<!-- Sub-chunk: Era 3 - Single Stream Revolution -->
<section class="mb-16">




### Act 3: One Mind (The Single-Stream Revolution)


<div class="grid md:grid-cols-2 gap-8 items-center mb-8">
<div>
<p class="text-slate-700 mb-4">
<strong>Z-Image starts over.</strong>
Why keep text and image apart at all? Why not treat them as <strong>the same language</strong>?
</p>
<p class="text-slate-700 mb-4">
It builds on <strong>DiT (Diffusion Transformer)</strong> and <strong>SiT (Scalable Interpolant Transformer)</strong>
and pushes the idea to its end point: <strong>S3-DiT (Scalable Single-Stream DiT)</strong>.
</p>
<div class="bg-slate-900 text-green-400 p-4 rounded-lg font-mono text-sm mb-4 shadow-inner">
Sequence = Concat([Text_Tokens, Image_Tokens])<br>
Output = Transformer(Sequence)
</div>
<p class="text-slate-700 text-sm">
<strong>The key trick: 3D-RoPE</strong>
<br>
If text and image are mixed together, how does the model know which token is which?
Z-Image uses a three-dimensional position encoding:
<br>
<span class="text-indigo-600 font-bold">x, y</span>: spatial coordinates of the image.
<br>
<span class="text-purple-600 font-bold">t</span>: sequence position of the text.
<br>
This gives one network both a "sense of space" and a "sense of word order".
</p>
</div>
<!-- S3-DiT SVG -->
<div class="bg-white p-2 rounded-xl">
<svg viewBox="0 0 300 320" class="w-full h-auto shadow-lg rounded-xl border border-indigo-100" xmlns="http://www.w3.org/2000/svg">
<rect width="300" height="320" fill="#fff" rx="8" />
<!-- Title -->
<text x="150" y="30" text-anchor="middle" font-weight="bold" fill="#333">S3-DiT Architecture</text>
<!-- Input -->
<g transform="translate(50, 50)">
<rect x="0" y="0" width="80" height="30" fill="#fcd34d" stroke="#d97706" rx="4"/>
<text x="40" y="20" text-anchor="middle" font-size="10" font-weight="bold" fill="#92400e">Text</text>
<rect x="85" y="0" width="115" height="30" fill="#93c5fd" stroke="#2563eb" rx="4"/>
<text x="142" y="20" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e40af">Image Patches</text>
<text x="100" y="45" text-anchor="middle" font-size="10" fill="#64748b">Concat</text>
</g>
<!-- Transformer Block 1 -->
<g transform="translate(50, 90)">
<rect x="0" y="0" width="200" height="50" rx="4" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>
<text x="100" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#3730a3">DiT Block</text>
<text x="100" y="40" text-anchor="middle" font-size="10" fill="#6366f1">Full Self-Attention</text>
<!-- Interaction Lines -->
<path d="M 40 10 Q 100 30 160 10" fill="none" stroke="#f59e0b" stroke-width="1.5" opacity="0.6"/>
<path d="M 50 40 Q 100 20 150 40" fill="none" stroke="#3b82f6" stroke-width="1.5" opacity="0.6"/>
</g>
<!-- Arrow -->
<path d="M 150 145 L 150 160" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-grey-3)"/>
<!-- Transformer Block N -->
<g transform="translate(50, 165)">
<rect x="0" y="0" width="200" height="50" rx="4" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>
<text x="100" y="30" text-anchor="middle" font-size="12" font-weight="bold" fill="#3730a3">DiT Block x N</text>
</g>
<!-- 3D RoPE Tag -->
<rect x="180" y="150" width="90" height="24" rx="12" fill="#10b981" />
<text x="225" y="166" text-anchor="middle" font-size="10" font-weight="bold" fill="#fff">✨ 3D-RoPE</text>
<text x="150" y="260" text-anchor="middle" font-size="11" fill="#475569">
<tspan x="150" dy="0">In every layer,</tspan>
<tspan x="150" dy="16">text and image</tspan>
<tspan x="150" dy="16">attend to each other fully</tspan>
</text>
<defs>
<marker id="arrow-grey-3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" />
</marker>
</defs>
</svg>
</div>
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded-xl p-6 mt-4">



#### 💡 Why "Z" Image?


<p class="text-emerald-800 text-sm">
The paper does not say, but we can guess: Z may stand for the <strong>Z-axis (depth, the third dimension)</strong>.
Standard RoPE (rotary position embedding) is 2D (x, y). Z-Image introduces <strong>3D-RoPE</strong>,
treating the text sequence as a third dimension $t$, which unifies sequence order (text) and space (image) in one mathematical form.
This is the mathematical foundation that lets S3-DiT work efficiently.
</p>
</div>
</section>
<!-- Sub-chunk: 3.1 Data Pipeline -->
<section class="mb-16">





## 🗺️ 3. Method: What Makes Z-Image Work (Methodology)

### 3.1 Data Engineering: The Data Refinery


<div class="bg-emerald-50 p-6 rounded-lg mb-6 border border-emerald-100">
<p class="text-emerald-900 leading-relaxed">
Z-Image's core principle is: <strong>"Scaling data quantity is easy; scaling data quality is hard."</strong>
<br>
It builds a large cleaning system with four engines. Think of it as an <strong>oil refinery</strong> that turns impure internet data (crude oil) step by step into high-octane fuel (Golden Data).
</p>
</div>
<!-- Data Pipeline SVG -->
<figure class="bg-white p-6 rounded-xl border border-slate-200 shadow-lg mb-8">
<svg viewBox="0 0 800 320" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="arrow-green-data-2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#059669" />
</marker>
</defs>
<!-- Raw Data Input -->
<g transform="translate(50, 160)">
<circle r="40" fill="#e5e7eb" stroke="#9ca3af" stroke-width="2" stroke-dasharray="4 2"/>
<text x="0" y="-5" text-anchor="middle" font-size="12" fill="#6b7280" font-weight="bold">Raw Data</text>
<text x="0" y="15" text-anchor="middle" font-size="10" fill="#9ca3af">Impure / Noisy</text>
</g>
<!-- Pipeline Flow -->
<path d="M 100 160 L 140 160" stroke="#059669" stroke-width="2" marker-end="url(#arrow-green-data-2)" />
<!-- Engine 1: Profiling (Filter) -->
<g transform="translate(140, 110)">
<rect width="120" height="100" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>
<text x="60" y="30" text-anchor="middle" font-weight="bold" fill="#065f46">Engine 1: Profiling</text>
<text x="60" y="55" text-anchor="middle" font-size="11" fill="#047857">Profile &amp; filter</text>
<!-- Icon -->
<path d="M 40 70 L 60 90 L 80 60" fill="none" stroke="#059669" stroke-width="2" />
</g>
<!-- Arrow -->
<path d="M 260 160 L 290 160" stroke="#059669" stroke-width="2" marker-end="url(#arrow-green-data-2)" />
<!-- Engine 2: Vector (De-duplicate) -->
<g transform="translate(290, 110)">
<rect width="120" height="100" rx="8" fill="#d1fae5" stroke="#059669" stroke-width="2"/>
<text x="60" y="30" text-anchor="middle" font-weight="bold" fill="#065f46">Engine 2: Vector</text>
<text x="60" y="55" text-anchor="middle" font-size="11" fill="#047857">Vector dedup</text>
<!-- Icon: Clusters -->
<circle cx="50" cy="75" r="3" fill="#059669" />
<circle cx="70" cy="75" r="3" fill="#059669" />
<circle cx="60" cy="85" r="3" fill="#059669" />
</g>
<!-- Arrow -->
<path d="M 410 160 L 440 160" stroke="#059669" stroke-width="2" marker-end="url(#arrow-green-data-2)" />
<!-- Engine 3: Graph (Knowledge) -->
<g transform="translate(440, 110)">
<rect width="120" height="100" rx="8" fill="#a7f3d0" stroke="#059669" stroke-width="2"/>
<text x="60" y="30" text-anchor="middle" font-weight="bold" fill="#065f46">Engine 3: Graph</text>
<text x="60" y="55" text-anchor="middle" font-size="11" fill="#047857">Knowledge graph</text>
<!-- Icon: Network -->
<line x1="50" y1="80" x2="70" y2="70" stroke="#059669" />
<line x1="70" y1="70" x2="90" y2="80" stroke="#059669" />
<circle cx="50" cy="80" r="3" fill="#065f46" />
<circle cx="70" cy="70" r="3" fill="#065f46" />
<circle cx="90" cy="80" r="3" fill="#065f46" />
</g>
<!-- Arrow -->
<path d="M 560 160 L 590 160" stroke="#059669" stroke-width="2" marker-end="url(#arrow-green-data-2)" />
<!-- Engine 4: Active Curation -->
<g transform="translate(590, 110)">
<rect width="120" height="100" rx="8" fill="#6ee7b7" stroke="#059669" stroke-width="2"/>
<text x="60" y="30" text-anchor="middle" font-weight="bold" fill="#065f46">Engine 4: Active</text>
<text x="60" y="55" text-anchor="middle" font-size="11" fill="#047857">Active curation</text>
<!-- Icon: Target -->
<circle cx="60" cy="75" r="10" fill="none" stroke="#065f46" stroke-width="2" />
<circle cx="60" cy="75" r="4" fill="#065f46" />
</g>
<!-- Final Arrow -->
<path d="M 710 160 L 740 160" stroke="#059669" stroke-width="2" marker-end="url(#arrow-green-data-2)" />
<!-- Gold Output -->
<g transform="translate(740, 160)">
<circle r="40" fill="#10b981" stroke="#064e3b" stroke-width="3"/>
<text x="0" y="-5" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">Golden</text>
<text x="0" y="15" text-anchor="middle" font-size="10" fill="#d1fae5">High Octane</text>
</g>
</svg>
<figcaption class="mt-4 text-center text-sm text-slate-500">
Figure 3.1: Z-Image's data purification pipeline. From left to right, each stage raises the information density of the data.
</figcaption>
</figure>
<div class="grid md:grid-cols-2 gap-6">
<div class="bg-slate-50 p-5 rounded-lg border-l-4 border-slate-400">



#### 1. Profiling = Coarse Filter


<p class="text-sm text-slate-600 mt-2">
Measures the "vital signs" of each sample: resolution, aesthetic score, noise level.
Like discarding crude oil that carries too much water or too many impurities.
</p>
</div>
<div class="bg-indigo-50 p-5 rounded-lg border-l-4 border-indigo-400">



#### 2. Vector = Removing Near-Duplicates


<p class="text-sm text-indigo-800 mt-2">
Clusters samples by embedding vectors. About 90% of meme images on the internet are duplicates.
The model must be kept from overfitting to these repeated samples.
</p>
</div>
<div class="bg-amber-50 p-5 rounded-lg border-l-4 border-amber-400">



#### 3. Graph = Weaving Knowledge Together


<p class="text-sm text-amber-800 mt-2">
Builds a concept tree (ontology).
It makes sure the model has seen not only "dog" but also "husky", "shiba inu" and "golden retriever".
This targets the <strong>long-tail distribution</strong> problem.
</p>
</div>
<div class="bg-rose-50 p-5 rounded-lg border-l-4 border-rose-400">



#### 4. Active Curation


<p class="text-sm text-rose-800 mt-2">
<strong>The strongest step.</strong> 
The system first tries to generate. If it finds it cannot draw "squirrel-shaped mandarin fish" (a Chinese dish) well, it <strong>specifically</strong> fetches 500 images of that dish from the web for "remedial lessons".
In short: find the gap, then fill it.
</p>
</div>
</div>
<!-- Restored Original Figures -->
<div class="mt-12 space-y-8">
<!-- Figure 5: Active Curation -->
<figure class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
<div class="overflow-hidden rounded-lg">
<img src="https://arxiv.org/html/2511.22699v2/x6.png" alt="Active Curation Engine Overview" class="w-full h-auto hover:scale-105 transition-transform duration-500" />
</div>
<figcaption class="mt-3 text-center text-sm text-slate-500">
<span class="font-bold text-slate-700">Figure 5 (Original):</span> Overview of the active curation engine.
Note the "Bad Case" at the upper right (such as a badly drawn squirrel-shaped mandarin fish), which triggers a feedback loop that directs the retrieval system to look for specific supplementary data.
</figcaption>
</figure>
<!-- Figure 6: Human-in-the-loop -->
<figure class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
<div class="overflow-hidden rounded-lg">
<img src="https://arxiv.org/html/2511.22699v2/x7.png" alt="Human-in-the-Loop Cycle" class="w-full h-auto hover:scale-105 transition-transform duration-500" />
</div>
<figcaption class="mt-3 text-center text-sm text-slate-500">
<span class="font-bold text-slate-700">Figure 6 (Original):</span> Human-in-the-Loop.
To keep the data clean, Z-Image brings in human experts as the final gatekeepers, who keep correcting the AI's annotations.
</figcaption>
</figure>
</div>
<!-- Deep Dive: Figure 8 Components -->
<div class="mt-12 bg-slate-50 p-6 rounded-xl border border-slate-200">



#### <span class="mr-2">🔍</span> A Closer Look: The Captioner (Z-Captioner)


<p class="text-slate-700 text-sm mb-6">
Another key component of Z-Image is a strong <strong>VLM captioner</strong>. It can write more than "this is an apple": it also reads text in the image (OCR) and draws on deeper common knowledge (World Knowledge).
</p>
<div class="grid md:grid-cols-2 gap-6">
<div class="text-center">
<div class="bg-white p-2 rounded-lg shadow-sm border border-slate-100 mb-2">
<img src="https://arxiv.org/html/2511.22699v2/figures/world_knowledge.png" class="w-full rounded" alt="World Knowledge" />
</div>
<p class="text-xs text-slate-500 font-bold">World Knowledge Recognition</p>
<p class="text-[10px] text-slate-400">Recognizes "Big Ben" rather than just "Clock Tower"</p>
</div>
<div class="text-center">
<div class="bg-white p-2 rounded-lg shadow-sm border border-slate-100 mb-2">
<img src="https://arxiv.org/html/2511.22699v2/figures/ocr_show.png" class="w-full rounded" alt="OCR Augmentation" />
</div>
<p class="text-xs text-slate-500 font-bold">OCR Text Extraction</p>
<p class="text-[10px] text-slate-400">Accurately extracts the text shown in the image</p>
</div>
</div>
</div>
</section>
<!-- Sub-chunk: 3.2 Curriculum Learning -->
<section class="mb-16">




### 3.2 Curriculum Learning: A Three-Stage Education


<div class="bg-purple-50 p-6 rounded-lg mb-6 border border-purple-100">
<p class="text-purple-900 leading-relaxed">
Conventional training feeds all the data in at once. Z-Image instead follows an <strong>"Omni-Pre-training"</strong> curriculum.
It mirrors human schooling: basic knowledge in primary school, skills in secondary school, research at university.
</p>
</div>
<!-- Curriculum SVG -->
<figure class="bg-white p-6 rounded-xl border border-slate-200 shadow-lg mb-8">
<svg viewBox="0 0 600 250" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">
<!-- X Axis: Time/Compute -->
<line x1="50" y1="200" x2="550" y2="200" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-grey-curr)" />
<text x="550" y="220" text-anchor="middle" font-size="12" fill="#64748b">Training Steps</text>
<!-- Stage 1: Elementary -->
<g transform="translate(60, 100)">
<rect width="120" height="100" rx="8" fill="#e0e7ff" stroke="#4338ca" stroke-width="2"/>
<text x="60" y="30" text-anchor="middle" font-weight="bold" fill="#3730a3">Stage 1</text>
<text x="60" y="50" text-anchor="middle" font-size="10" fill="#4338ca">Low-Res (256px)</text>
<text x="60" y="70" text-anchor="middle" font-size="10" fill="#4338ca">Static Bucket</text>
<!-- Metaphor -->
<text x="60" y="130" text-anchor="middle" font-size="12" fill="#4338ca">"Primary: layout"</text>
</g>
<!-- Arrow -->
<path d="M 190 150 L 220 150" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-grey-curr)" />
<!-- Stage 2: Secondary -->
<g transform="translate(230, 80)">
<rect width="140" height="120" rx="8" fill="#f3e8ff" stroke="#7e22ce" stroke-width="2"/>
<text x="70" y="30" text-anchor="middle" font-weight="bold" fill="#581c87">Stage 2: Omni</text>
<text x="70" y="50" text-anchor="middle" font-size="10" fill="#7e22ce">Multi-Res + I2I</text>
<text x="70" y="70" text-anchor="middle" font-size="10" fill="#7e22ce">In-painting</text>
<!-- Metaphor -->
<text x="70" y="150" text-anchor="middle" font-size="12" fill="#7e22ce">"Secondary: skills"</text>
</g>
<!-- Arrow -->
<path d="M 380 150 L 410 150" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-grey-curr)" />
<!-- Stage 3: University -->
<g transform="translate(420, 60)">
<rect width="140" height="140" rx="8" fill="#fce7f3" stroke="#be185d" stroke-width="2"/>
<text x="70" y="30" text-anchor="middle" font-weight="bold" fill="#831843">Stage 3: Fine-Tune</text>
<text x="70" y="50" text-anchor="middle" font-size="10" fill="#be185d">High-Res (1024+)</text>
<text x="70" y="70" text-anchor="middle" font-size="10" fill="#be185d">PE-Enhanced Data</text>
<text x="70" y="90" text-anchor="middle" font-size="10" fill="#be185d">Aes Score > 6.0</text>
<!-- Metaphor -->
<text x="70" y="170" text-anchor="middle" font-size="12" fill="#be185d">"University: create"</text>
</g>
<defs>
<marker id="arrow-grey-curr" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" />
</marker>
</defs>
</svg>
</figure>
<div class="relative pl-8 border-l-2 border-slate-200 space-y-8">
<!-- Stage 1 -->
<div class="relative">
<div class="absolute -left-10 bg-indigo-200 rounded-full w-6 h-6 flex items-center justify-center text-xs font-bold text-indigo-700">1</div>



#### Stage 1: Low-Resolution Bootstrapping


<div class="flex items-center gap-4 mt-2">
<div class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full font-bold">Cost Saver</div>
</div>
<p class="text-slate-600 mt-2 text-sm">
<strong>Core logic:</strong> learning that "a cat has two ears" does not need 4K images. At 256x256 the model can go through a huge amount of data very quickly and learn how objects relate.
Like primary school: learn to read first, and worry about beautiful handwriting later.
</p>
</div>
<!-- Stage 2 -->
<div class="relative">
<div class="absolute -left-10 bg-purple-200 rounded-full w-6 h-6 flex items-center justify-center text-xs font-bold text-purple-700">2</div>



#### Stage 2: Omni-Pre-training (Multi-Task)


<p class="text-slate-600 mt-2 text-sm">
Multi-resolution buckets are introduced. The key addition is the <strong>Joint I2I (image-to-image)</strong> task.
The model sees "before" and "after" pairs of edited images and learns dynamic instructions such as "turn the red apple into a green one".
</p>
</div>
<!-- Stage 3 -->
<div class="relative">
<div class="absolute -left-10 bg-rose-200 rounded-full w-6 h-6 flex items-center justify-center text-xs font-bold text-rose-700">3</div>



#### Stage 3: High-Quality Polish


<p class="text-slate-600 mt-2 text-sm">
Synthetic data generated by a <strong>Prompt Enhancer</strong> is introduced.
<br>This addresses the limited "imagination" of a 6B model. The PE expands a plain "A cat" into a rich description, teaching S3-DiT to produce polished, ArtStation-style images.
</p>
</div>
</div>
</section>
<!-- Sub-chunk: 3.3 Mechanisms (3D-RoPE) -->
<section class="mb-20">




### 3.3 Core Mechanism: A Positioning System for Space and Sequence (3D-RoPE)


<div class="bg-slate-900 rounded-xl p-6 text-slate-300 mb-8">



#### <span class="mr-2">⚙️</span> Engineering Note: How Do You Put a GPS Inside a Transformer?


<p class="mb-4 text-sm leading-relaxed">
When one Transformer handles both 1D text ($T$) and 2D images ($H, W$), position encoding becomes a hard problem.
<br>
Standard RoPE (Rotary Positional Embedding) is 1D or 2D. Z-Image needs <strong>3D-RoPE</strong> so that the model does not "get lost".
</p>
<!-- 3D-RoPE Explanation SVG -->
<div class="bg-slate-800 p-4 rounded-lg border border-slate-700 my-4">
<svg viewBox="0 0 500 200" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">
<!-- Text Token (Time) -->
<g transform="translate(50, 50)">
<rect width="60" height="60" fill="#fcd34d" rx="4" opacity="0.8"/>
<text x="30" y="35" text-anchor="middle" font-weight="bold" fill="#78350f">Token</text>
<!-- Axis -->
<line x1="30" y1="60" x2="30" y2="90" stroke="#fcd34d" stroke-width="2" marker-end="url(#arrow-yellow)" />
<text x="30" y="105" text-anchor="middle" font-size="10" fill="#fcd34d">Time (t)</text>
</g>
<!-- Plus -->
<text x="140" y="85" text-anchor="middle" font-size="20" fill="#94a3b8">+</text>
<!-- Image Patch (Space) -->
<g transform="translate(180, 50)">
<rect width="60" height="60" fill="#93c5fd" rx="4" opacity="0.8"/>
<text x="30" y="35" text-anchor="middle" font-weight="bold" fill="#1e3a8a">Patch</text>
<!-- Axis X -->
<line x1="60" y1="30" x2="90" y2="30" stroke="#93c5fd" stroke-width="2" marker-end="url(#arrow-blue)" />
<text x="100" y="35" text-anchor="middle" font-size="10" fill="#93c5fd">x</text>
<!-- Axis Y -->
<line x1="30" y1="60" x2="30" y2="90" stroke="#93c5fd" stroke-width="2" marker-end="url(#arrow-blue)" />
<text x="30" y="105" text-anchor="middle" font-size="10" fill="#93c5fd">y</text>
</g>
<!-- Arrow -->
<path d="M 280 80 L 320 80" stroke="#fff" stroke-width="2" marker-end="url(#arrow-white)" />
<!-- 3D RoPE Result -->
<g transform="translate(350, 40)">
<cube width="80" height="80" depth="20" /> <!-- Abstract representation -->
<path d="M 20 20 L 60 20 L 40 50 Z" fill="none" stroke="#10b981" stroke-width="2" />
<circle cx="40" cy="35" r="30" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4 2" />
<text x="40" y="85" text-anchor="middle" font-weight="bold" fill="#10b981">3D Rotation</text>
<text x="40" y="100" text-anchor="middle" font-size="10" fill="#a7f3d0">Rot(x, y, t)</text>
</g>
<defs>
<marker id="arrow-yellow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto" fill="#fcd34d">
<path d="M0,0 L0,6 L6,3 z" />
</marker>
<marker id="arrow-blue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto" fill="#93c5fd">
<path d="M0,0 L0,6 L6,3 z" />
</marker>
<marker id="arrow-white" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto" fill="#fff">
<path d="M0,0 L0,6 L6,3 z" />
</marker>
</defs>
</svg>
</div>
<div class="grid grid-cols-2 gap-4 text-xs font-mono">
<div class="bg-slate-800 p-3 rounded border border-slate-700">
<span class="text-green-400 font-bold">Dim 1 & 2 (Spatial)</span>
<p class="mt-1 text-slate-400">
Encode the (x, y) coordinates of the image.
<br>This tells the model that the "cat's head" is above the "cat's body".
</p>
</div>
<div class="bg-slate-800 p-3 rounded border border-slate-700">
<span class="text-purple-400 font-bold">Dim 3 (Temporal)</span>
<p class="mt-1 text-slate-400">
Encodes the position t in the text sequence.
<br>This tells the model that "Red" modifies "Apple".
</p>
</div>
</div>
<p class="mt-4 text-sm italic text-slate-400 border-t border-slate-700 pt-3">
<strong>Technical summary:</strong> 3D-RoPE separates space from sequence order. Image tokens extend freely across 2D space while text tokens extend along the sequence axis; the two do not interfere with each other, yet still interact closely.
</p>
</div>
</section>
<!-- Sub-chunk: 4.1 Performance (David vs Goliath) -->
<section class="mb-16">




## <span class="mr-3 text-4xl">🥊</span> 4. Experiments: David vs Goliath


<div class="bg-indigo-50 p-6 rounded-lg mb-8 border border-indigo-100">
<p class="text-indigo-900 leading-relaxed">
Z-Image (6B) faces opponents 3 to 10 times its size: Hunyuan (80B) and Flux.1 (12B).
This is not a fair fight in size, but it is a clear win on <strong>efficiency</strong>.
<br>
On established benchmarks such as <strong>GenEval</strong> and <strong>DPG-Bench</strong>, Z-Image shows that
<span class="bg-indigo-200 px-1 rounded font-bold">the scaling law is not the only route.</span>
</p>
</div>
<!-- David vs Goliath Scatter Plot SVG -->
<figure class="bg-white p-6 rounded-xl border border-slate-200 shadow-lg mb-8">
<svg viewBox="0 0 600 380" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">
<!-- Grid -->
<g stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4 4">
<line x1="50" y1="330" x2="550" y2="330" /> <!-- X axis -->
<line x1="50" y1="50" x2="50" y2="330" />   <!-- Y axis -->
<line x1="50" y1="260" x2="550" y2="260" />
<line x1="50" y1="190" x2="550" y2="190" />
<line x1="50" y1="120" x2="550" y2="120" />
</g>
<!-- Axis Labels -->
<text x="300" y="365" text-anchor="middle" font-size="12" fill="#64748b" font-weight="bold">Model Size (Billions of Parameters)</text>
<text x="20" y="190" text-anchor="middle" font-size="12" fill="#64748b" font-weight="bold" transform="rotate(-90 20,190)">GenEval Alignment Score</text>
<!-- Zones -->
<path d="M 50 330 L 550 50" stroke="#cbd5e1" stroke-width="240" stroke-opacity="0.05" />
<text x="520" y="40" text-anchor="end" font-size="10" fill="#cbd5e1" font-weight="bold">Inefficiency Zone</text>
<!-- Data Points -->
<!-- SDXL -->
<g transform="translate(100, 280)">
<circle r="8" fill="#94a3b8" />
<text x="0" y="20" text-anchor="middle" font-size="10" fill="#64748b">SDXL (2.6B)</text>
</g>
<!-- SD3 Medium -->
<g transform="translate(140, 250)">
<circle r="10" fill="#94a3b8" />
<text x="0" y="22" text-anchor="middle" font-size="10" fill="#64748b">SD3-Med</text>
</g>
<!-- Flux.1 (Goliath 1) -->
<g transform="translate(250, 100)">
<circle r="18" fill="#facc15" stroke="#ca8a04" stroke-width="2" />
<text x="0" y="32" text-anchor="middle" font-size="11" font-weight="bold" fill="#854d0e">Flux.1 (12B)</text>
<text x="0" y="0" text-anchor="middle" font-size="10" fill="#ca8a04">💰 High Cost</text>
</g>
<!-- Hunyuan (Goliath 2) -->
<g transform="translate(500, 110)">
<circle r="40" fill="#f87171" stroke="#b91c1c" stroke-width="2" opacity="0.8"/>
<text x="0" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="#7f1d1d">Hunyuan (80B)</text>
<text x="0" y="5" text-anchor="middle" font-size="24">🦖</text>
</g>
<!-- Z-Image (The Hero) -->
<g transform="translate(170, 70)">
<circle r="14" fill="#4f46e5" stroke="#312e81" stroke-width="3" />
<text x="0" y="-22" text-anchor="middle" font-size="14" font-weight="bold" fill="#4f46e5">Z-Image (6B)</text>
<text x="0" y="5" text-anchor="middle" font-size="12" fill="#fff">⚡️</text>
<!-- Highlight Ring -->
<circle r="22" fill="none" stroke="#6366f1" stroke-width="1" stroke-dasharray="2 2">
<animate attributeName="r" from="14" to="28" dur="1.5s" repeatCount="indefinite" />
<animate attributeName="opacity" from="1" to="0" dur="1.5s" repeatCount="indefinite" />
</circle>
</g>
<!-- Comparison Line -->
<line x1="170" y1="70" x2="250" y2="100" stroke="#4f46e5" stroke-width="1" stroke-dasharray="2 2" />
<text x="210" y="80" text-anchor="middle" font-size="10" fill="#4f46e5" transform="rotate(15 210,80)">Better & Smaller</text>
</svg>
<figcaption class="text-center text-xs text-slate-500 mt-2">
Figure 4.1: Parameter count vs generation quality. Z-Image sits in the upper-left region (few parameters, high score), ahead of the heavy Hunyuan and the expensive Flux.
</figcaption>
</figure>
<div class="overflow-hidden rounded-xl border border-slate-200 shadow-sm">
<table class="w-full text-left text-sm text-slate-600">
<thead class="bg-slate-100 text-slate-900 font-bold uppercase">
<tr>
<th class="px-6 py-3">Model</th>
<th class="px-6 py-3">Params</th>
<th class="px-6 py-3">Arch</th>
<th class="px-6 py-3 text-right">Training Cost (Est.)</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-200 bg-white">
<tr class="hover:bg-red-50">
<td class="px-6 py-3 font-medium text-slate-800">Hunyuan-Image</td>
<td class="px-6 py-3 font-mono">80B (MoE)</td>
<td class="px-6 py-3">Dual-Stream</td>
<td class="px-6 py-3 text-right text-red-600 font-mono">>$2,000,000</td>
</tr>
<tr class="hover:bg-yellow-50">
<td class="px-6 py-3 font-medium text-slate-800">Flux.1 [Pro]</td>
<td class="px-6 py-3 font-mono">12B</td>
<td class="px-6 py-3">Hybrid</td>
<td class="px-6 py-3 text-right text-orange-600 font-mono">>$1,000,000</td>
</tr>
<tr class="bg-indigo-50 border-l-4 border-indigo-500">
<td class="px-6 py-3 font-bold text-indigo-900">Z-Image</td>
<td class="px-6 py-3 font-mono font-bold text-indigo-700">6B</td>
<td class="px-6 py-3 font-bold text-indigo-700">S3-DiT</td>
<td class="px-6 py-3 text-right text-emerald-600 font-mono font-bold">$628,000</td>
</tr>
</tbody>
</table>
</div>
<!-- Restored Figure 4: Comparison Showcase -->
<div class="mt-12">



#### 4.1.2 In Practice: Seeing Is Believing (Visual Evidence)


<p class="text-slate-700 text-sm mb-4">
Benchmark scores alone are not enough. The figure below compares Z-Image (far right) side by side with other SOTA models.
In <strong>lighting quality</strong> and <strong>fine texture</strong>, the 6B Z-Image holds its own against the 80B model.
</p>
<figure class="bg-slate-900 p-2 rounded-xl border border-slate-700 shadow-2xl">
<div class="overflow-hidden rounded-lg">
<!-- Using x5.png which is Figure 4 -->
<img src="https://arxiv.org/html/2511.22699v2/x5.png" alt="Comparison with SOTA Models" class="w-full h-auto" />
</div>
<figcaption class="mt-3 text-center text-xs text-slate-400">
<span class="font-bold text-indigo-400">Figure 4 (Original):</span> 
Z-Image-Turbo (Rightmost) vs Competitors (SD3, Flux, Hunyuan, etc.).
</figcaption>
</figure>
</div>
</section>
<!-- Sub-chunk: 4.2 Capabilities (Literate & Obedient) -->
<section class="mb-16">




### 4.2 Capabilities: Strong on Text and on Editing


<div class="grid md:grid-cols-2 gap-8 mb-12">
<!-- Feature 1: Text Rendering -->
<div>



#### <span class="bg-purple-200 p-1 rounded mr-2">🔤</span> No Longer Illiterate: Bilingual Text Rendering


<p class="text-slate-700 text-sm mb-4 leading-relaxed">
Z-Image's most surprising ability is that it can "write" text as precisely as layout software.
Not only English: it also gets structurally complex <strong>Chinese characters</strong> right.
</p>
<div class="bg-purple-50 p-4 rounded-lg border border-purple-100 mb-4">
<strong class="text-purple-800 text-sm block mb-2">💡 Why it works?</strong>
<ul class="list-disc list-inside text-xs text-purple-700 space-y-1">
<li><strong>Single-Stream advantage:</strong> text tokens sit directly next to image tokens as "neighbors". Attention lets pixels directly "see" the stroke structure of the characters.</li>
<li><strong>OCR datasets:</strong> it "grew up reading". The training data contain many posters and book covers with text.</li>
</ul>
</div>
<!-- Restored Figure 2: Text Showcase -->
<figure class="mt-4 bg-white p-2 rounded-lg border border-purple-100 shadow-sm">
<img src="https://arxiv.org/html/2511.22699v2/figures/showcase_text.jpg" alt="Bilingual Text Rendering" class="w-full rounded" />
<figcaption class="text-center text-[10px] text-purple-400 mt-1">Figure 2: Mixed Chinese and English text rendering</figcaption>
</figure>
</div>
<!-- Text Rendering SVG Visualization -->
<figure class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
<svg viewBox="0 0 300 200" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">
<!-- Text Tokens -->
<g transform="translate(20, 40)">
<rect width="40" height="20" fill="#fcd34d" rx="2" />
<text x="20" y="14" text-anchor="middle" font-size="8" font-weight="bold">"CO"</text>
<rect x="45" y="0" width="40" height="20" fill="#fcd34d" rx="2" />
<text x="65" y="14" text-anchor="middle" font-size="8" font-weight="bold">"FFEE"</text>
</g>
<!-- Image Grid -->
<g transform="translate(150, 20)">
<rect width="120" height="160" fill="#fff" stroke="#94a3b8" />
<!-- The generated pixels -->
<rect x="20" y="60" width="80" height="40" fill="#e2e8f0" rx="4" /> 
<!-- Letters on cup -->
<text x="60" y="85" text-anchor="middle" font-family="serif" font-weight="bold" font-size="16" fill="#334155">COFFEE</text>
</g>
<!-- Attention Beams -->
<path d="M 40 60 Q 80 100 170 85" stroke="#f59e0b" stroke-width="2" stroke-opacity="0.6" fill="none" />
<path d="M 65 60 Q 90 120 190 85" stroke="#f59e0b" stroke-width="2" stroke-opacity="0.6" fill="none" />
<text x="100" y="140" text-anchor="middle" font-size="10" fill="#d97706" font-style="italic">Direct Attention</text>
</svg>
<figcaption class="text-center text-xs text-slate-400 mt-2">
Figure 4.2.1: Pixels attend directly to character tokens, which makes precise rendering possible.
</figcaption>
</figure>
</div>
<!-- Feature 2: Instruction Editing -->
<div class="mb-8">



#### <span class="bg-cyan-200 p-1 rounded mr-2">🎨</span> A Brush That Follows Instructions: Z-Image-Edit


<div class="bg-cyan-50 p-6 rounded-lg border-l-4 border-cyan-500">
<p class="text-cyan-900 text-sm mb-4">
Thanks to multi-task learning in Omni-Pre-training, Z-Image can edit as well as generate.
It carries out complex <strong>natural-language instructions</strong> without relying on add-ons such as ControlNet, as SDXL does.
</p>
<div class="grid grid-cols-2 gap-4 text-xs font-mono text-cyan-800 mb-4">
<div class="bg-white p-2 rounded shadow-sm">
<strong>Input:</strong> "Make the cat look like a tiger"
<br><span class="text-slate-400">-> texture replaced, structure kept</span>
</div>
<div class="bg-white p-2 rounded shadow-sm">
<strong>Input:</strong> "Add a red hat on the head"
<br><span class="text-slate-400">-> object added, spatially aware</span>
</div>
</div>
<!-- Restored Figure 3: Editing Showcase -->
<figure class="bg-white p-2 rounded-lg border border-cyan-100 shadow-sm">
<img src="https://arxiv.org/html/2511.22699v2/figures/showcase_editing.jpg" alt="Instruction-based Editing" class="w-full rounded" />
<figcaption class="text-center text-[10px] text-cyan-600 mt-1">Figure 3: Precise instruction-following edits (new background, new material, added objects)</figcaption>
</figure>
</div>
</div>
</section>
<!-- Sub-chunk: 4.3 Turbo Speed (Distillation) -->
<section class="mb-20">




### 4.3 Speed: Decoupled Distillation (Decoupled DMD)


<div class="bg-amber-50 p-6 rounded-lg mb-8 border border-amber-100">
<p class="text-amber-900 leading-relaxed">
Z-Image-Turbo cuts inference from 50 steps to <strong>4-8 steps</strong>, generating an image in under a second.
<br>
The technique behind this is <strong>Decoupled DMD (decoupled distribution matching distillation)</strong>.
Conventional distillation tends to blur images, because it forces the student to fit the mean. Z-Image instead trains "follow the prompt accurately" and "look good" as separate objectives.
</p>
</div>
<!-- Distillation Comparison SVG -->
<figure class="bg-white p-6 rounded-xl border border-slate-200 shadow-lg mb-8">
<svg viewBox="0 0 600 280" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">
<!-- Traditional DMD -->
<g transform="translate(50, 40)">
<text x="100" y="0" text-anchor="middle" font-weight="bold" fill="#64748b">Traditional Distillation</text>
<!-- Box -->
<rect x="0" y="20" width="200" height="80" rx="8" fill="#f1f5f9" stroke="#94a3b8" stroke-dasharray="4 2"/>
<!-- Conflicting Goals -->
<text x="100" y="50" text-anchor="middle" font-size="12" fill="#475569">Loss = L_real + L_prompt</text>
<text x="100" y="70" text-anchor="middle" font-size="10" fill="#ef4444">Coupled (in conflict!)</text>
<!-- Result Icon -->
<circle cx="100" cy="140" r="20" fill="#cbd5e1" />
<text x="100" y="175" text-anchor="middle" font-size="10" fill="#64748b">Blurry Result</text>
</g>
<!-- Arrow -->
<path d="M 280 80 L 320 80" stroke="#cbd5e1" stroke-width="2" marker-end="url(#arrow-grey-dmd)" />
<!-- Decoupled DMD (Z-Image) -->
<g transform="translate(350, 40)">
<text x="100" y="0" text-anchor="middle" font-weight="bold" fill="#059669">Decoupled DMD</text>
<!-- Stream 1: CFG Augmentation -->
<rect x="0" y="20" width="200" height="40" rx="4" fill="#dcfce7" stroke="#22c55e"/>
<text x="100" y="45" text-anchor="middle" font-size="11" fill="#15803d">1. CFG Augmentation (obey)</text>
<!-- Plus -->
<text x="100" y="75" text-anchor="middle" font-size="14" fill="#94a3b8">+</text>
<!-- Stream 2: Distribution Matching -->
<rect x="0" y="80" width="200" height="40" rx="4" fill="#dbeafe" stroke="#3b82f6"/>
<text x="100" y="105" text-anchor="middle" font-size="11" fill="#1e40af">2. Distribution Matching (real)</text>
<!-- Result Icon -->
<circle cx="100" cy="150" r="25" fill="#10b981" stroke="#047857" stroke-width="2"/>
<text x="100" y="155" text-anchor="middle" font-size="20">✨</text>
<text x="100" y="190" text-anchor="middle" font-size="10" fill="#047857" font-weight="bold">Crisp & Sharp!</text>
</g>
<defs>
<marker id="arrow-grey-dmd" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#cbd5e1" />
</marker>
</defs>
</svg>
<figcaption class="text-center text-xs text-slate-500 mt-2">
Figure 4.3: Decoupled distillation. "Semantic alignment" and "image quality" are optimized separately so they do not interfere, which gives a large quality gain in Turbo mode.
</figcaption>
</figure>
<!-- Speed Chart -->
<div class="space-y-4 max-w-lg mx-auto bg-slate-50 p-6 rounded-xl border border-slate-200">



#### Inference Latency (H800 GPU)


<!-- Bar 1 -->
<div>
<div class="flex justify-between text-xs text-slate-500 mb-1">
<span>Flux.1 (50 Steps)</span>
<span>5.0s</span>
</div>
<div class="w-full bg-slate-200 rounded-full h-3">
<div class="bg-slate-400 h-3 rounded-full" style="width: 100%"></div>
</div>
</div>
<!-- Bar 2 -->
<div>
<div class="flex justify-between text-xs text-slate-500 mb-1">
<span>Z-Image Base (28 Steps)</span>
<span>2.8s</span>
</div>
<div class="w-full bg-slate-200 rounded-full h-3">
<div class="bg-indigo-400 h-3 rounded-full" style="width: 56%"></div>
</div>
</div>
<!-- Bar 3 (Turbo) -->
<div>
<div class="flex justify-between text-sm font-bold text-emerald-700 mb-1">
<span>Z-Image Turbo (8 Steps)</span>
<span>0.8s ⚡️</span>
</div>
<div class="w-full bg-slate-200 rounded-full h-4 shadow-lg shadow-emerald-100">
<div class="bg-gradient-to-r from-emerald-400 to-emerald-600 h-4 rounded-full" style="width: 16%"></div>
</div>
</div>
</div>
</section>
<!-- Section 5: Epilogue -->
<section class="mb-20">




## <span class="mr-3 text-4xl">🛑</span> 5. A Sober Look and What Comes Next: A New Foundation for Medical AI?


<p class="text-lg text-slate-700 mb-8 leading-relaxed">
After all these impressive results, we need to step back.
For researchers like us, especially in Bio-AI, what does this model actually mean? Is it another toy for generating anime portraits, or a prototype of the next generation of scientific simulators?
</p>
<!-- The Disenchantment (Limitations) -->
<div class="mb-12 bg-rose-50 border-l-4 border-rose-500 p-6 rounded-r-lg">




### ⚠️ Caution: Side Effects of the Prompt Enhancer


<p class="text-rose-800 text-sm leading-relaxed mb-4">
To make up for the limited "imagination" of a 6B model, Z-Image uses a <strong>Prompt Enhancer (PE)</strong> to expand prompts.
<br>
In artistic work this is a strength. You type "doctor", and it expands that into "a handsome futuristic doctor...".
<br>
<strong>In scientific research it is a serious problem.</strong> If a pathologist types "invasive ductal carcinoma, grade 3", the PE may invent features of lymph node metastasis just to make the image "richer".
</p>
<div class="bg-white p-3 rounded border border-rose-200 text-rose-700 font-mono text-xs">
<strong>Recommendation:</strong> for research use, always <strong>bypass the PE module</strong> and run S3-DiT inference directly, so that instructions are followed exactly.
</div>
</div>
<!-- The Future: Z-WSI -->
<div class="mb-12">




### 🚀 An Idea: Z-WSI (Whole Slide Imaging)


<p class="text-slate-700 mb-4">
Z-Image's <strong>Single-Stream (concatenation)</strong> architecture suggests a useful direction for pathology.
Current pathology AI still relies on the clumsy approach of "tiling + multiple-instance learning".
</p>
<!-- SVG: Z-WSI Concept -->
<figure class="bg-indigo-50 p-6 rounded-xl border border-indigo-100 mb-6">
<svg viewBox="0 0 500 180" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">
<!-- Background Pipe -->
<rect x="20" y="60" width="460" height="60" rx="30" fill="#e0e7ff" stroke="#818cf8" stroke-width="2" />
<!-- Text Report Tokens -->
<g transform="translate(50, 75)">
<rect width="80" height="30" rx="4" fill="#fcd34d" stroke="#d97706" />
<text x="40" y="20" text-anchor="middle" font-size="10" font-weight="bold" fill="#92400e">"Tumor..."</text>
<text x="40" y="-10" text-anchor="middle" font-size="10" fill="#92400e">Report</text>
</g>
<!-- Plus Sign -->
<text x="145" y="95" text-anchor="middle" font-size="20" fill="#6366f1" font-weight="bold">+</text>
<!-- WSI Patches -->
<g transform="translate(160, 75)">
<rect width="30" height="30" fill="#fca5a5" stroke="#b91c1c" />
<rect width="30" height="30" x="35" fill="#fca5a5" stroke="#b91c1c" />
<rect width="30" height="30" x="70" fill="#fca5a5" stroke="#b91c1c" />
<text x="50" y="20" text-anchor="middle" font-size="8" fill="#7f1d1d">WSI</text>
<text x="50" y="-10" text-anchor="middle" font-size="10" fill="#7f1d1d">Gigapixel Slide</text>
</g>
<!-- Arrow -->
<path d="M 280 90 L 320 90" stroke="#4f46e5" stroke-width="2" marker-end="url(#arrow-indigo)" />
<!-- Single Brain -->
<g transform="translate(330, 40)">
<path d="M 0 50 Q 50 0 100 50 Q 50 100 0 50" fill="#4f46e5" opacity="0.1" />
<path d="M 10 50 Q 50 20 90 50 Q 50 80 10 50" fill="#4f46e5" opacity="0.2" />
<rect x="20" y="30" width="60" height="40" rx="4" fill="#4338ca" />
<text x="50" y="55" text-anchor="middle" font-size="12" font-weight="bold" fill="#fff">Z-WSI</text>
</g>
<text x="250" y="160" text-anchor="middle" font-size="11" fill="#4338ca" font-style="italic">
"Unified Multi-Modal Attention"
</text>
<defs>
<marker id="arrow-indigo" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L0,6 L9,3 z" fill="#4f46e5" />
</marker>
</defs>
</svg>
<figcaption class="text-center text-xs text-indigo-800 mt-2">
Figure 5.1: What if we applied Z-Image's idea to pathology? The pathology report and the WSI slide would be processed together in a single Transformer.
</figcaption>
</figure>
<div class="bg-indigo-50 p-5 rounded-xl border border-indigo-100">



#### Core idea:


<ul class="space-y-3 text-sm text-indigo-800">
<li class="flex items-start">
<span class="mr-2">🔹</span>
<span><strong>Input sequence:</strong> [pathology report text] + [gigapixel WSI tokens]</span>
</li>
<li class="flex items-start">
<span class="mr-2">🔹</span>
<span><strong>Training goal:</strong> teach the model to "read the report and draw the slide".</span>
</li>
<li class="flex items-start">
<span class="mr-2">🔹</span>
<span><strong>Application:</strong> generate data for very rare cancer subtypes, to address the long tail in medical data.</span>
</li>
</ul>
</div>
</div>
<!-- Implementation Checklist -->
<div class="mb-12">




### 🛠️ A Practical Guide for Engineers


<div class="bg-slate-900 rounded-xl overflow-hidden shadow-2xl">
<div class="flex items-center justify-between px-4 py-2 bg-slate-800 border-b border-slate-700">
<span class="text-xs text-slate-400 font-mono">inference.py</span>
<span class="text-xs text-green-400 font-mono">Run on RTX 4090</span>
</div>
<pre class="p-6 overflow-x-auto text-sm font-mono leading-relaxed text-slate-300"><code><span class="text-purple-400">import</span> torch
<span class="text-purple-400">from</span> z_image_pipeline <span class="text-purple-400">import</span> ZImagePipeline

<span class="text-slate-500"># 1. Load the Turbo model (bf16 to save memory)</span>
pipe = ZImagePipeline.from_pretrained(
<span class="text-green-400">"alibaba/z-image-turbo-6b"</span>, 
torch_dtype=torch.bfloat16
).to(<span class="text-green-400">"cuda"</span>)

<span class="text-slate-500"># 2. Tip for medical fine-tuning (Hypothetical)</span>
<span class="text-slate-500"># pipe.transformer.text_embedder.requires_grad_(False)  # freeze text understanding</span>
<span class="text-slate-500"># pipe.transformer.visual_embedder.train()            # train the visual part only</span>

<span class="text-slate-500"># 3. Fast inference (8 Steps)</span>
prompt = <span class="text-green-400">"A high-res histology slide of lung adenocarcinoma"</span>
image = pipe(
prompt, 
num_inference_steps=<span class="text-orange-400">8</span>,  <span class="text-slate-500"># Turbo mode</span>
guidance_scale=<span class="text-orange-400">3.5</span>
).images[0]

image.save(<span class="text-green-400">"lung_cancer_synth.png"</span>)</code></pre>
</div>
</div>
<!-- Final Takeaway (Triangle of Success SVG) -->
<div class="bg-slate-50 p-8 rounded-2xl text-center border border-slate-200">



#### 📚 Key Takeaways from Gemini (Take Home Message)


<div class="flex justify-center mb-6">
<svg viewBox="0 0 400 300" class="w-full max-w-md h-auto" xmlns="http://www.w3.org/2000/svg">
<!-- Triangle -->
<path d="M 200 20 L 350 250 L 50 250 Z" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 4" />
<!-- Top Node: Architecture -->
<g transform="translate(200, 20)">
<circle r="30" fill="#e0e7ff" stroke="#4338ca" stroke-width="2" />
<text x="0" y="5" text-anchor="middle" font-size="20">🏛️</text>
<text x="0" y="-40" text-anchor="middle" font-weight="bold" fill="#4338ca">Architecture</text>
<text x="0" y="45" text-anchor="middle" font-size="10" fill="#6366f1">Single-Stream</text>
</g>
<!-- Right Node: Data -->
<g transform="translate(350, 250)">
<circle r="30" fill="#ecfdf5" stroke="#059669" stroke-width="2" />
<text x="0" y="5" text-anchor="middle" font-size="20">💎</text>
<text x="0" y="45" text-anchor="middle" font-weight="bold" fill="#047857">Data</text>
<text x="0" y="60" text-anchor="middle" font-size="10" fill="#059669">Quality > Quantity</text>
</g>
<!-- Left Node: Training -->
<g transform="translate(50, 250)">
<circle r="30" fill="#fff7ed" stroke="#ea580c" stroke-width="2" />
<text x="0" y="5" text-anchor="middle" font-size="20">🎓</text>
<text x="0" y="45" text-anchor="middle" font-weight="bold" fill="#c2410c">Training</text>
<text x="0" y="60" text-anchor="middle" font-size="10" fill="#ea580c">Curriculum Learning</text>
</g>
<!-- Center: Z-Image -->
<g transform="translate(200, 160)">
<circle r="40" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
<text x="0" y="5" text-anchor="middle" font-weight="bold" font-size="14" fill="#334155">Z-Image</text>
<text x="0" y="20" text-anchor="middle" font-size="10" fill="#64748b">Efficient Foundation</text>
</g>
</svg>
</div>
<p class="text-slate-600 text-sm max-w-2xl mx-auto">
Z-Image's success does not come from a single breakthrough. It is the combined result of <strong>a leaner architecture, cleaner data and a more principled training schedule</strong>.
That is the first-principles lesson worth taking from it.
</p>
</div>
</section>
<footer class="mt-20 pt-10 border-t border-slate-200 text-center text-slate-400 text-sm mb-10">
<p class="mb-2">Generated by <strong>Gemini Agent</strong> based on "Z-Image: An Efficient Image Generation Foundation Model..."</p>
<p>For academic discussion only; not for clinical diagnosis.</p>

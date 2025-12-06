---
title: "Qwen-VL 系列发展路径：李宏毅风格超长讲义"
description: "从 Qwen-VL 到 Qwen3-VL 的深度演进指南，一份「李宏毅风格」的深度学习讲义。"
pubDate: 2025-12-06
externalScripts: ["https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"]
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

## 导览：这份讲义怎么读？

</div>

<h2 class="text-2xl font-semibold mb-4">导览：这份讲义怎么读？</h2>
<p class="mb-2">
如果把整条 Qwen-VL 发展史想象成一部开放世界 RPG 游戏，那这份讲义就是你的官方攻略书：告诉你主线任务、支线剧情、隐藏 Boss 在哪里，以及每一代版本到底「点了哪些技能点」。
</p>
<p class="mb-2">
为了方便你快速定位，我们大致按照下面的结构来展开：
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">01</span>
<h4 class="font-bold text-slate-700">背景与动机</h4>
</div>
<p class="text-xs text-slate-500">说明「为什么需要 Qwen-VL」，解决纯文本模型的哪些痛点。</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">02</span>
<h4 class="font-bold text-slate-700">基础补课</h4>
</div>
<p class="text-xs text-slate-500">把后面会用到的视觉编码、对齐损失等概念先打好底。</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">03</span>
<h4 class="font-bold text-slate-700">家族谱系</h4>
</div>
<p class="text-xs text-slate-500">画出 Qwen-VL 家族的「学术谱系树」，看它是怎么从一棵小树苗长成一整片森林。</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">04</span>
<h4 class="font-bold text-slate-700">逐代拆解 Method</h4>
</div>
<p class="text-xs text-slate-500">核心干货：逐代拆解 Qwen-VL 到 Qwen3-VL 的架构细节与演进逻辑。</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">05</span>
<h4 class="font-bold text-slate-700">实验与数据</h4>
</div>
<p class="text-xs text-slate-500">看实验结果背后真正值得关注的点，而不是只背数字。</p>
</div>
<div class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-center mb-2">
<span class="w-8 h-8 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold mr-3 text-sm">06</span>
<h4 class="font-bold text-slate-700">复现与展望</h4>
</div>
<p class="text-xs text-slate-500">给出复现与工程实践建议，以及未来可能的研究方向。</p>
</div>
</div>
<p class="mt-3">
整个讲解会尽量保持对话感：我会不断抛出「如果我们这样做会怎样？」、「那能不能再贪心一点？」之类的小问题，然后再用直觉 + 公式带你走完全程。
</p>
</section>
<section id="background" class="mb-16 scroll-mt-20">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## 1 一、为什么要关心 Qwen-VL？

</div>

<h2 class="flex items-center text-3xl font-bold text-slate-800 mb-6 group">
<span class="bg-indigo-600 text-white w-8 h-8 rounded-lg inline-flex items-center justify-center text-lg mr-3 shadow-md group-hover:scale-110 transition-transform">1</span>
一、为什么要关心 Qwen-VL？
</h2>
<p>
先想象这样一个场景：你在和一个只会聊天的 LLM 对话，它什么都能解释，但只要你丢一张图片过去，它就瞬间变成<strong>「失明的哲学家」</strong>——可以聊人生，却看不到世界。
</p>
<p>
这就是纯文本大模型的典型困境：它们的大脑很大，记忆很强，但输入只有一维的文字，面对现实世界里那种「图文交织」的信息流，会天然缺一块。
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
<strong>Figure 1:</strong> Qwen-VL 在各类视觉中心任务上的表现雷达图。可以看到，相比于其他通用大模型，Qwen-VL 在这些维度上（如 VQA、Caption、Grounding 等）都尽量往外扩了一圈。这就像是一个「五边形战士」的初长成。
</figcaption>
</figure>
<p>
而 Qwen-VL 系列想做的事情，就是给这位只会说话的哲学家装上一双眼睛，甚至顺手再加一副 AR 眼镜：不仅能看到画面里的每一个像素，还能理解时间、空间、文本、公式、UI 操作乃至长视频中的因果关系。
</p>
<p>
如果我们再具体一点，它至少要解决三类现实中的「卡关」问题：
</p>
<ul class="list-none space-y-4 pl-0">
<li class="flex items-start">
<svg class="w-6 h-6 text-red-500 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
<span><strong>看得见但看不懂：</strong>传统 OCR 或检测模型可以圈出文字和框，但不知道「问题在哪」，更不知道「下一步该干嘛」。</span>
</li>
<li class="flex items-start">
<svg class="w-6 h-6 text-red-500 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
<span><strong>看得懂一张，看不懂一堆：</strong>面对长文档、PPT、网页、GUI、视频时，模型无法在几十张甚至几千帧信息之间建立稳定的记忆和推理链。</span>
</li>
<li class="flex items-start">
<svg class="w-6 h-6 text-red-500 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
<span><strong>看得懂现在，看不懂历史：</strong>很多任务需要结合前文上下文、之前几轮对话、上一个画面中的状态，这就要求模型拥有真正的「长上下文、多模态」能力。</span>
</li>
</ul>
<p>
Qwen-VL 系列就是沿着这三个痛点一路升级：从最初的「能看图说话」，到 Qwen2-VL 的「任意分辨率 + 视频 + 多语言」，再到 Qwen2.5-VL 的更强推理，最后是 Qwen3-VL 把上下文、长视频和思考能力都拉到一个新高度。
</p>
<!-- 李老师小黑板 Component -->
<aside class="not-prose mt-12 mb-12 bg-slate-800 rounded-xl shadow-2xl skew-y-1 transform transition-transform hover:skew-y-0 duration-300 ring-4 ring-slate-900 ring-offset-2">
<div class="px-8 py-6 border border-slate-700/50 rounded-xl bg-[url('https://www.transparenttextures.com/patterns/black-scales.png')]">
<div class="sr-only">

### 👨‍🏫 李老师小黑板

</div>

<h3 class="flex items-center text-xl font-bold text-emerald-400 mb-4 font-mono tracking-tight border-b border-slate-600 pb-2">
<span class="text-3xl mr-3">👨‍🏫</span> 李老师小黑板
</h3>
<div class="text-slate-300 text-base space-y-4 font-light leading-relaxed">
<p>
很多同学一开始会想：「我就拿一个视觉 backbone，把 feature 丢给大模型，不就完事了吗？」——听起来很合理，但实践中会踩一堆坑：
</p>
<ul class="list-none space-y-2 ml-1">
<li class="flex items-start">
<span class="text-emerald-500 mr-2">➤</span>
<span><strong>视觉特征怎么离散成 token？</strong>一张 4K 图如果每个 patch 都变成一个 token，上下文直接爆炸。</span>
</li>
<li class="flex items-start">
<span class="text-emerald-500 mr-2">➤</span>
<span><strong>视觉和文本的坐标系怎么统一？</strong>2D 的图片和 1D 的文本，用同一套位置编码会很怪。</span>
</li>
<li class="flex items-start">
<span class="text-emerald-500 mr-2">➤</span>
<span><strong>训练数据怎么设计？</strong>只用 caption 和 QA 会严重欠拟合「定位」「细粒度理解」这些能力。</span>
</li>
</ul>
<p class="mt-4 text-sm text-slate-400 italic pt-4 border-t border-slate-700/50">
Qwen-VL 系列的很多设计其实都是在回答这三个问题：如何在算力有限的前提下，让模型「看得广、看得细、看得久」。
</p>
</div>
</div>
</aside>
<p class="text-lg font-medium text-slate-700 border-l-4 border-slate-300 pl-4 italic">
所以，与其把 Qwen-VL 当成一篇篇独立的技术报告，不如把它们看成是一条逐渐升级的「技能树」：每一代都在某几个维度上点满或重构，而这份讲义，就是要帮你把这棵技能树从根到叶都看清楚。
</p>
</div>
</section>
<section id="prerequisites" class="mb-24 scroll-mt-24">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## 2 二、基础补课：从「只会看文字的大脑」到「会看世界的大脑」

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-indigo-500 to-purple-600 text-white w-14 h-14 rounded-2xl inline-flex items-center justify-center text-2xl mr-5 shadow-xl group-hover:scale-110 transition-transform duration-300 ring-4 ring-indigo-50">2</span>
二、基础补课：从「只会看文字的大脑」到「会看世界的大脑」
</h2>
<div class="mb-12 bg-white p-4 md:p-8 rounded-[2rem] shadow-premium border border-slate-100 relative overflow-hidden">
<div
class="absolute top-0 right-0 w-[400px] h-[400px] bg-indigo-50 rounded-full mix-blend-multiply filter blur-[80px] opacity-60 animate-pulse">
</div>
<p class="text-xl text-slate-700 leading-relaxed relative z-10">
在正式拆解 Qwen-VL 之前，我们需要先达成一些<strong>共识</strong>。
<br>
很多同学觉得多模态（Multimodal）很难，是因为它横跨了 CV（计算机视觉）和 NLP（自然语言处理）两个领域。CV 的人习惯看像素、卷积和 IoU；NLP 的人习惯看 Token、Attention
和 Perplexity。
</p>
<p class="text-xl text-slate-700 leading-relaxed mt-4 relative z-10">
但实际上，<strong>它们在数学本质上是完全相通的</strong>。
<br>
这一节，我们将用“李宏毅式”的直觉，快速过一遍三个最核心的基础概念：<strong>ViT（视觉的语言化）、RoPE（位置的旋转编码）、Cross-Attention（模态间的桥梁）</strong>。这三个概念是理解后续所有
Qwen-VL 骚操作（如 M-RoPE, DeepStack）的地基。
</p>
</div>
<!-- 2.1 ViT -->
<div class="mb-20">
<div class="sr-only">

### 2.1 视觉的语言化：ViT (Vision Transformer)

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
2.1 视觉的语言化：ViT (Vision Transformer)
</h3>
<p class="text-lg text-slate-600 mb-6">
如果我们要让 LLM 看懂图片，第一步必须是<strong>把图片变成 LLM 能理解的形式</strong>。LLM 能理解什么？它只能理解 <strong>Sequence (序列)</strong>。
<br>
所以，ViT 做的事情只有一件：<span
class="bg-indigo-100 text-indigo-800 px-1 rounded font-bold">把一张二维的图片，切碎成一串一维的向量序列。</span>
</p>
<!-- SVG: Patching Process -->
<div class="my-10 bg-white p-4 md:p-8 rounded-3xl border border-slate-200 shadow-lg relative">
<h4 class="text-center font-serif text-xl font-bold text-slate-800 mb-8">🎨 图解：从 Pixel 到 Patch Embedding
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
<h4 class="font-bold text-indigo-900 mb-3 text-lg">💡 为什么要切块 (Patching)？</h4>
<p class="text-indigo-800 text-sm leading-relaxed">
如果把每个像素都当成一个 token，一张 224x224 的图就有 50,176 个 token，Attention 计算量直接爆炸（$O(N^2)$）。
<br>
切成 16x16 的 patch 后，只有 $14 \times 14 = 196$ 个
token，这就在<strong>计算效率</strong>和<strong>信息保留</strong>之间找到了平衡。
</p>
</div>
<div class="bg-purple-50 p-6 rounded-xl border border-purple-100">
<h4 class="font-bold text-purple-900 mb-3 text-lg">⚠️ Qwen-VL 的伏笔</h4>
<p class="text-purple-800 text-sm leading-relaxed">
标准的 ViT 需要固定分辨率（比如 224 或 336）。
<br>
<strong>思考题：</strong> 如果来了一张长条形的手机截图（1080x2400）怎么办？强行缩放会变形，补零（Padding）会浪费算力。这个问题正是
<strong>Qwen2-VL Dynamic Resolution</strong> 要解决的核心痛点。
</p>
</div>
</div>
</div>
<!-- 2.2 RoPE -->
<div class="mb-20">
<div class="sr-only">

### 2.2 优雅的位置编码：RoPE (Rotary Positional Embedding)

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-purple-500 rounded-full mr-4 shadow-md"></span>
2.2 优雅的位置编码：RoPE (Rotary Positional Embedding)
</h3>
<p class="text-lg text-slate-600 mb-6">
Transformer 的 Attention 机制本质上是“位置无关”的（Permutation Invariant）。如果你打乱句子的顺序，Attention
算出来的关联度是一样的。所以我们必须告诉模型：<strong>“谁在谁的前面”</strong>。
<br>
RoPE 是目前最优雅的解决方案。它不是把位置向量加（Add）上去，而是把词向量在空间中<strong>旋转（Rotate）</strong>一个角度。
</p>
<div class="bg-slate-900 p-4 md:p-8 rounded-3xl shadow-2xl relative overflow-hidden mb-10 group">
<div
class="absolute -top-20 -right-20 w-64 h-64 bg-gradient-to-br from-purple-500 to-indigo-500 rounded-full filter blur-[80px] opacity-30 group-hover:opacity-50 transition-opacity duration-500">
</div>
<h4 class="text-center font-bold text-white mb-8 text-xl tracking-wider">RoPE 的几何直觉：相对距离 = 旋转角度差</h4>
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
<strong>为什么 RoPE 对 Qwen-VL 这么重要？</strong>
<br>
因为 Qwen-VL 系列需要处理的不仅仅是一维文本，还有二维图像和三维视频。
<br>
在 Qwen2-VL 中，为了统一这些模态，作者提出了 <strong>M-RoPE (Multimodal RoPE)</strong>：把旋转推广到了 3D 空间（时间、高度、宽度）。如果你不理解
RoPE 的“相对位置由旋转角度决定”这个核心直觉，你就无法理解 M-RoPE 是如何在三个维度上“解耦”位置信息的。
</p>
</div>
</div>
<!-- 2.3 Cross-Attention -->
<div class="mb-20">
<div class="sr-only">

### 2.3 模态的桥梁：Cross-Attention

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-emerald-500 rounded-full mr-4 shadow-md"></span>
2.3 模态的桥梁：Cross-Attention
</h3>
<p class="text-lg text-slate-600 mb-6">
这是 Qwen-VL 将视觉特征融入 LLM 的关键机制。在 Self-Attention 中，Query, Key, Value 都来自同一个序列。但在 Cross-Attention 中，它们分家了。
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
<span class="text-xl mr-2">💊</span> 抓药的比喻
</h4>
<p class="text-slate-600 text-sm leading-relaxed mb-3">
想象 LLM 是一个老中医，Vision Encoder 是一个巨大的中药柜。
</p>
<ul class="list-disc list-inside text-slate-600 text-sm space-y-2">
<li><strong>Query (Q):</strong> 老中医手里的“药方”（当前文本上下文需要什么信息？比如“图里的猫在哪？”）。</li>
<li><strong>Key (K):</strong> 药柜上每个抽屉的“标签”（图片的纹理、形状、位置特征）。</li>
<li><strong>Value (V):</strong> 抽屉里实际的“药材”（具体的视觉特征向量）。</li>
</ul>
<p class="text-slate-600 text-sm mt-3">
Cross-Attention 就是老中医拿着药方 (Q)，去匹配药柜上的标签 (K)，然后取出对应的药材 (V)，融合到当前的诊断（文本生成）中。
</p>
</div>
</div>
</div>
<div class="mt-8 p-4 bg-yellow-50 border-l-4 border-yellow-400 text-yellow-900 rounded-r-lg">
<p class="font-bold mb-1">注意：</p>
<p class="text-sm">
Qwen-VL 在第一代使用了类似的机制（Adapter），但在后续版本（Qwen2-VL）中为了效率，改成了更直接的 <strong>MLP Merger（C-Former
变体）</strong>。了解 Cross-Attention 是为了理解“为什么我们要把视觉特征映射到语言空间”。
</p>
</div>
</div>
<!-- 2.4 Coordinate Tokenization -->
<div class="mb-20">
<div class="sr-only">

### 2.4 坐标的离散化：把“画框”变成“说话”

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-amber-500 rounded-full mr-4 shadow-md"></span>
2.4 坐标的离散化：把“画框”变成“说话”
</h3>
<p class="text-lg text-slate-600 mb-6">
Qwen-VL 不仅能看图，还能在图上把物体框出来（Grounding）。
<br>
很多同学直觉上会认为：这肯定是用回归（Regression）做的吧？预测 x, y 的连续数值？
<br>
<span class="text-amber-600 font-bold">错！大错特错！</span>
LLM 的世界里只有 Token。为了让 LLM 能输出坐标，我们必须把连续的像素坐标，强制变成离散的字典词。
</p>
<div class="bg-white p-4 md:p-8 rounded-3xl border border-slate-200 shadow-xl mb-10">
<h4 class="text-center font-bold text-slate-700 mb-8 text-xl">🎯 图解：Binning —— 将世界网格化</h4>
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
<strong>Qwen-VL 的做法：</strong>
<ul class="list-disc list-inside">
<li>在词表中新增 1000 个特殊 token：<code>&lt;0&gt;</code>, <code>&lt;1&gt;</code>, ... <code>&lt;999&gt;</code>。</li>
<li>把图片的长宽归一化到 [0, 1000]。</li>
<li>当模型需要输出坐标时，它实际上是在做<strong>1000 分类的选择题</strong>。</li>
</ul>
</p>
<div class="bg-amber-50 p-4 rounded-lg border-l-4 border-amber-500 italic">
<strong>🤔 李老师的思考题：</strong> 为什么要切成 1000 份？切成 100 份行不行？切成 10000 份行不行？
<br>
<span class="text-sm not-italic text-slate-500">
答：切太少（100），定位精度不够，框不准；切太多（10000），词表会爆炸，而且分类头（Classification Head）会变得极其难训练（类别太多了）。1000 是一个经验上的 Sweet
Spot。
</span>
</div>
</div>
</div>
<!-- 2.5 Attention Mask -->
<div class="mb-20">
<div class="sr-only">

### 2.5 掩码的艺术：Causal vs. Bidirectional Mask

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
2.5 掩码的艺术：Causal vs. Bidirectional Mask
</h3>
<p class="text-lg text-slate-600 mb-6">
最后一个关键点：<strong>时间与空间在 Attention 里的区别</strong>。
<br>
LLM（GPT 类）是单向的（Causal），因为你不能在说第一个字的时候就看到第十个字（那是作弊）。
<br>
但是，看图是<strong>双向的（Bidirectional）</strong>！你看一张照片，是左眼看右眼，还是右眼看左眼？是一眼全看到的！图片里的像素之间没有“先后顺序”。
</p>
<p class="text-lg text-slate-600 mb-6">
<strong>冲突来了：</strong> 当我们把“双向的图片 Token”塞进“单向的 LLM”里时，Attention Mask 该怎么画？
</p>
<div class="flex flex-col md:flex-row gap-8 items-start">
<!-- The Matrix Visual -->
<div class="w-full md:w-1/2 bg-white p-6 rounded-2xl border border-slate-200 shadow-md">
<h4 class="text-center font-bold text-slate-700 mb-4 text-sm">混合 Attention Mask 矩阵</h4>
<div class="flex justify-center">
<svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
<!-- Background Grid -->
<rect x="0" y="0" width="300" height="300" fill="#f8fafc" stroke="#cbd5e1" />
<!-- Legend -->
<g transform="translate(10, 10)">
<rect x="0" y="0" width="10" height="10" fill="#3b82f6" />
<text x="15" y="8" font-size="10" fill="#64748b">可见 (1)</text>
<rect x="0" y="15" width="10" height="10" fill="#e2e8f0" />
<text x="15" y="23" font-size="10" fill="#64748b">不可见 (0)</text>
</g>
<!-- Zones Definition -->
<!-- V: Image Tokens (First 100) -->
<!-- T: Text Tokens (Next 100) -->
<!-- 1. Vision-to-Vision: Bidirectional (Full Attention) -->
<rect x="30" y="30" width="100" height="100" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" />
<text x="80" y="80" text-anchor="middle" font-weight="bold" fill="#1e40af" font-size="12">Vision ↔
Vision</text>
<text x="80" y="95" text-anchor="middle" fill="#1e40af" font-size="10">(全可见)</text>
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
<text x="180" y="255" text-anchor="middle" fill="#1e40af" font-size="10">(Causal 三角)</text>
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
<h5 class="font-bold text-slate-800 mb-3">关键规则：</h5>
<ul class="list-disc list-inside space-y-3 text-slate-600 text-sm">
<li>
<strong>Image 内部 (左上角)：</strong> <span class="bg-blue-100 text-blue-800 px-1 rounded">全 1
矩阵</span>。图片的所有 Patch 可以互相看见，因为它们是同时存在的空间信息。
</li>
<li>
<strong>Text 内部 (右下角)：</strong> <span
class="bg-slate-200 text-slate-800 px-1 rounded">下三角矩阵</span>。文本必须遵守因果律，第 $t$ 个字只能看 $1 \dots
t-1$。
</li>
<li>
<strong>Text 看 Image (左下角)：</strong> <span class="bg-blue-100 text-blue-800 px-1 rounded">全
1</span>。无论说到哪句话，都可以回头去看完整的图片。
</li>
<li>
<strong>Image 看 Text (右上角)：</strong> <span class="bg-slate-200 text-slate-800 px-1 rounded">全
0</span>。图片存在时，后续的文字还没生成呢，当然不能看（防止泄漏）。
</li>
</ul>
</div>
<p class="mt-4 text-slate-600 text-sm italic">
这个特殊的 Mask 设计，是 Qwen-VL 这类 Decoder-only 模型能同时处理理解（Understanding）和生成（Generation）任务的底层逻辑保障。
</p>
</div>
</div>
</div>
</div>
</section>
<section id="genealogy" class="mb-16 scroll-mt-20">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## 3 三、Qwen 家族谱系：从 Qwen-LM 到 Qwen3-VL

</div>

<h2 class="flex items-center text-3xl font-bold text-slate-800 mb-6 group">
<span class="bg-indigo-600 text-white w-8 h-8 rounded-lg inline-flex items-center justify-center text-lg mr-3 shadow-md group-hover:scale-110 transition-transform">3</span>
三、Qwen 家族谱系：从 Qwen-LM 到 Qwen3-VL
</h2>
<p>
接下来我们先从宏观视角看一眼：Qwen 家族到底长成什么样？哪些是「只会文字的兄弟姐妹」，哪些是「视觉版」、哪些是「专攻图片」、哪些又是「主打长上下文和推理」？
</p>
<p>
最早的是 Qwen-LM 家族，负责打好纯文本世界的地基；在这个地基上，Qwen-VL 把「看图」的能力接上来；然后 Qwen2 系列进一步在语言和视觉上双向升级，衍生出 Qwen2-VL；之后是强调更强推理和更长上下文的 Qwen2.5 及 Qwen2.5-VL；最后是把一切整合到 256K 上下文 + 强思考能力上的 Qwen3-VL。
</p>
<p>
我们用一幅 Mermaid 图把这一系列的演化用「版本进化树」的方式画出来。
</p>
<!-- SVG Diagram: Qwen Family Tree -->
<div class="my-12 bg-white rounded-xl shadow-premium p-4 md:p-8 border border-slate-100 overflow-x-auto">
<h4 class="text-center font-bold text-slate-700 mb-8 text-lg font-serif">图解：Qwen 家族进化树 (The Phylogeny Tree)</h4>
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
<text x="70" y="45" font-weight="bold" fill="#64748b" font-size="12">Language Foundation (纯文本基座)</text>
<rect x="50" y="200" width="700" height="140" rx="10" fill="#f0f9ff" stroke="#bae6fd" stroke-dasharray="4 4" />
<text x="70" y="225" font-weight="bold" fill="#0369a1" font-size="12">Vision-Language Evolution (多模态进化)</text>
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
<p class="mb-0"><strong>核心事实：</strong><span class="font-semibold">视觉语言模型不是一个独立物种，而是长在语言大模型这棵树上的一条分支。</span>如果底层语言模型升级了，视觉版本也要跟着重做一遍，而且往往会顺带引入新的训练策略和新的视觉模块设计。</p>
</div>
<p>
因此，要理解 Qwen-VL 这一支，你心里最好先有一个「Qwen 纯文本发展史」的隐形时间轴：每一次文本 backbone 的升级（从 Qwen 到 Qwen2，再到 Qwen2.5 和 Qwen3），都会为视觉版本带来新的上下文长度、更好的对齐能力和更强的推理能力。
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-12 mb-12">
<!-- Card 1 -->
<div class="bg-white p-6 rounded-xl shadow-premium border border-slate-100 hover:shadow-float transition-all duration-300 group">
<h4 class="text-xl font-bold text-brand-700 mb-2 font-serif group-hover:text-brand-500 transition-colors">3.1 第一代：Qwen-VL</h4>
<p class="text-sm text-slate-600 leading-relaxed">在 Qwen-LM 的基础上，通过精心设计的视觉 receptor、输入输出接口，让模型第一次可以稳定地做「看图说话 + 定位 + 读文字」。这一代的重点是把所有 <span class="bg-brand-50 px-1 rounded text-brand-700">基础视觉能力</span> 补全。</p>
</div>
<!-- Card 2 -->
<div class="bg-white p-6 rounded-xl shadow-premium border border-slate-100 hover:shadow-float transition-all duration-300 group">
<h4 class="text-xl font-bold text-brand-700 mb-2 font-serif group-hover:text-brand-500 transition-colors">3.2 第二代：Qwen2-VL</h4>
<p class="text-sm text-slate-600 leading-relaxed">关键词：<strong>Dynamic Resolution</strong> 和 <strong>M-RoPE</strong>。不再被固定分辨率限制，也不想把视频当成无关图片堆叠。它在文档、UI、长视频任务上有了明显优势。</p>
</div>
<!-- Card 3 -->
<div class="bg-white p-6 rounded-xl shadow-premium border border-slate-100 hover:shadow-float transition-all duration-300 group">
<h4 class="text-xl font-bold text-brand-700 mb-2 font-serif group-hover:text-brand-500 transition-colors">3.3 第三代：Qwen2.5-VL</h4>
<p class="text-sm text-slate-600 leading-relaxed">角色是「打磨内功」。进一步加强了数学推理、代码理解和结构化抽取（JSON、表格）的能力，同时拉长了上下文长度，让模型在处理长文档时更稳。</p>
</div>
<!-- Card 4 -->
<div class="bg-white p-6 rounded-xl shadow-premium border border-slate-100 hover:shadow-float transition-all duration-300 group">
<h4 class="text-xl font-bold text-brand-700 mb-2 font-serif group-hover:text-brand-500 transition-colors">3.4 第四代：Qwen3-VL</h4>
<p class="text-sm text-slate-600 leading-relaxed"><strong>256K 上下文 + DeepStack + 思考模式</strong>。彻底重构了「长上下文 + 多模态 + 推理」的关系。视觉信息多层注入，支持 thinking 模式，对标顶尖闭源模型。</p>
</div>
</div>
<p class="mt-8 text-slate-600">
接下来几节，我们会按照「版本迭代式讲解」的方式，分别把四代 Qwen-VL 拆成：模型结构、损失设计、训练流程和典型能力四个模块来讲，让你可以清楚感受到每一代在「V1 naive 方案」的基础上是如何一步一步升级的。
</p>
</div>
</section>
<section id="method-qwenvl" class="mb-24">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 4 四、第一站：Qwen-VL —— 给大脑装上“义眼”的艺术

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-10 group tracking-tight">
<span
class="bg-gradient-to-br from-brand-500 to-blue-600 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:rotate-12 transition-transform duration-300">4</span>
四、第一站：Qwen-VL —— 给大脑装上“义眼”的艺术
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
各位同学，欢迎来到 Qwen-VL 的世界。如果我们把纯文本模型（Qwen-7B）比作一个博学但双目失明的智者，那么 Qwen-VL
这个项目要做的事情，就是<strong>给他做一台精密的手术：装上一双“义眼”</strong>。
</p>
<p class="text-xl text-slate-700 leading-relaxed mt-4 relative z-10">
但这手术没那么简单！你不能直接把视神经接到语言中枢上，因为它们说的“语言”完全不通——视觉神经传的是像素信号（Pixel），语言中枢要的是语义符号（Token）。
</p>
<p class="text-xl text-slate-700 leading-relaxed mt-4 relative z-10 font-semibold text-brand-700">
Qwen-VL 的核心贡献，就在于设计了一个绝妙的“翻译器”（Adapter）和一套严谨的“康复训练流程”（3-Stage Training），让这两个本来老死不相往来的模块，学会了协同工作。
</p>
</div>
<!-- 4.1 Model Architecture -->
<div class="sr-only">

### 4.1 架构拆解：三大件的选择哲学

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-brand-500 rounded-full mr-4 shadow-md"></span>
4.1 架构拆解：三大件的选择哲学
</h3>
<p class="text-xl text-slate-600 mb-8 leading-loose">
这也是李老师经常强调的 <strong>Step 1: Define a Function Set</strong>。Qwen-VL
的网络结构非常经典，它由三个核心组件构成。这看起来像是“搭积木”，但每一块积木的选择都大有讲究（SOTA Selection）。
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
这是基座。为什么选
Qwen-7B？因为在当时（2023年），它在同尺寸模型中表现优异。注意：在第一阶段训练时，<strong>它是被冻结（Frozen）的</strong>，像个高傲的教授，不肯轻易改变自己的参数。
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
参数量高达 1.9B！这是一个巨型视觉编码器。它负责把 448×448 的高分辨率图像切成小块（Patch），变成一串密集的特征向量。<strong>它也是先冻结，后解冻。</strong>
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
这就是那个“翻译器”。不同于 LLaVA 简单暴力的 Linear Projection，Qwen-VL 用了一个单层的 <strong>Cross-Attention</strong>
模块，把视觉特征“压缩”成固定长度（256）。
</p>
</div>
</div>
<!-- SVG Diagram: Architecture Details -->
<div class="my-16">
<div class="bg-white rounded-3xl shadow-premium border border-slate-200 p-8 overflow-hidden">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
🔍 显微镜视角：Qwen-VL 的数据流 (Data Flow)
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
<p class="font-bold mb-2 text-indigo-800">🎓 李老师的画外音：为什么要用 Attention 做压缩？</p>
<p class="leading-relaxed">
大家想一想，如果我们只是用一个全连接层（Linear）或者池化层（Pooling），是不是太“死板”了？
<strong>Cross-Attention 的好处在于“查询”（Query）机制。</strong>
我们设定 256 个可学习的 Query 向量，你可以把它们想象成 256
个“探针”。在训练过程中，这些探针学会了去图像特征里“寻找”不同的信息——有的探针专门找纹理，有的找形状，有的找位置。
这就是为什么 Qwen-VL 能够在保持 token 数量极少（256个）的情况下，依然保留丰富的视觉细节。
</p>
</div>
</div>
</div>
<!-- 4.2 Training Pipeline -->
<div class="sr-only">

### 4.2 训练三部曲：像教学生一样教模型

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-brand-500 rounded-full mr-4 shadow-md"></span>
4.2 训练三部曲：像教学生一样教模型
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Qwen-VL 的训练过程非常经典，堪称多模态训练的教科书。它采用了<strong>三阶段训练法（3-Stage Training
Pipeline）</strong>。这其实很像我们教人类学生：先学认字，再学做题，最后学礼貌对话。
</p>
<div class="relative border-l-4 border-slate-200 ml-8 space-y-12">
<!-- Stage 1 -->
<div class="relative pl-12">
<div
class="absolute -left-[22px] top-0 w-10 h-10 bg-slate-100 border-4 border-slate-300 rounded-full flex items-center justify-center text-lg font-bold text-slate-500 z-10">
1</div>
<div
class="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 hover:border-slate-300 transition-colors">
<h4 class="text-2xl font-bold text-slate-800 mb-4">Stage 1: Pre-training (预训练) —— “视觉对齐”</h4>
<div class="flex flex-wrap gap-3 mb-4">
<span class="bg-slate-100 text-slate-600 px-3 py-1 rounded-full text-sm font-mono">Target:
Vision-Language Alignment</span>
<span class="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm font-mono">Data:
Image-Text Pairs</span>
</div>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
<strong>任务：</strong> 让模型把图片和简单的描述（Caption）对应起来。
<br>
<strong>状态：</strong>
<ul class="list-disc list-inside ml-4 mt-2 text-slate-600">
<li><span class="text-blue-600 font-bold">Vision Encoder:</span> Frozen (不更新)</li>
<li><span class="text-red-600 font-bold">Adapter:</span> Learnable (更新)</li>
<li><span class="text-blue-600 font-bold">LLM:</span> Frozen (不更新)</li>
</ul>
</p>
<p class="text-base text-slate-500 italic bg-slate-50 p-4 rounded-lg border border-slate-100">
"这时候大脑（LLM）和眼睛（ViT）都是锁住的，只有中间的翻译官（Adapter）在拼命学习如何把眼睛看到的信号翻译成大脑能听懂的语言。"
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
(多任务预训练) —— “解锁大脑”</h4>
<div class="flex flex-wrap gap-3 mb-4 relative z-10">
<span class="bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full text-sm font-mono">Target:
Fine-grained Understanding</span>
<span class="bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full text-sm font-mono">Data: VQA,
OCR, Grounding</span>
</div>
<p class="text-lg text-slate-600 leading-relaxed mb-4 relative z-10">
<strong>任务：</strong> 引入更高分辨率的输入（448x448），训练更难的任务，比如“框出图中的猫”、“念出图里的字”。
<br>
<strong>状态：</strong>
<ul class="list-disc list-inside ml-4 mt-2 text-slate-600 relative z-10">
<li><span class="text-red-600 font-bold">Vision Encoder:</span> Learnable (终于解冻了！)</li>
<li><span class="text-red-600 font-bold">Adapter:</span> Learnable</li>
<li><span class="text-red-600 font-bold">LLM:</span> Learnable (大脑开始适应视觉信号)</li>
</ul>
</p>
<p
class="text-base text-indigo-700 italic bg-indigo-50 p-4 rounded-lg border border-indigo-100 relative z-10">
"这一步是质变。我们把全模型都解冻了（Full Fine-tuning）。为什么要解冻？因为光靠翻译官不够了，大脑自己也得学会处理新的视觉知识，尤其是为了适应更高的分辨率和更细粒度的任务（如
Grounding）。"
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
<h4 class="text-2xl font-bold text-slate-800 mb-4">Stage 3: Supervised Fine-tuning (SFT) —— “学会聊天”
</h4>
<div class="flex flex-wrap gap-3 mb-4">
<span class="bg-brand-50 text-brand-700 px-3 py-1 rounded-full text-sm font-mono">Target:
Instruction Following</span>
<span class="bg-brand-50 text-brand-700 px-3 py-1 rounded-full text-sm font-mono">Data: Chat
Data (Human-like)</span>
</div>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
<strong>任务：</strong> 用对话格式的数据（ChatML），教模型怎么像个助手一样说话，而不是只会冷冰冰地输出标签。
<br>
<strong>状态：</strong>
<ul class="list-disc list-inside ml-4 mt-2 text-slate-600">
<li><span class="text-blue-600 font-bold">Vision Encoder:</span> Frozen (通常为了稳定)</li>
<li><span class="text-red-600 font-bold">Adapter:</span> Learnable</li>
<li><span class="text-red-600 font-bold">LLM:</span> Learnable</li>
</ul>
</p>
</div>
</div>
</div>
<!-- 4.3 Key Innovation Details -->
<div class="sr-only">

### 4.3 核心黑科技：如何让模型“指哪打哪”？(Grounding)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-brand-500 rounded-full mr-4 shadow-md"></span>
4.3 核心黑科技：如何让模型“指哪打哪”？(Grounding)
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
大家可能注意到了，Qwen-VL 最惊艳的能力之一是 <strong>Visual Grounding（视觉定位）</strong>。你问它“狗在哪里？”，它不仅能说“在草地上”，还能给你画一个框
<code>[x1, y1, x2, y2]</code>。它是怎么做到的？
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
<div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
<h4 class="text-xl font-bold text-slate-800 mb-4">🔴 传统方法的痛点</h4>
<p class="text-lg text-slate-600">
传统的 LLM 词表里根本没有坐标的概念。如果我们直接输出数字 "256, 334..."，这会被切分成好几个 token，模型很难理解这几个 token 代表一个连续的 2D 空间位置。
</p>
</div>
<div class="bg-emerald-50 p-6 rounded-2xl shadow-sm border border-emerald-200">
<h4 class="text-xl font-bold text-emerald-900 mb-4">🟢 Qwen-VL 的对策</h4>
<p class="text-lg text-emerald-800">
<strong>位置归一化 + 特殊 Token</strong>。<br>
1. 将所有坐标归一化到 <code>[0, 1000)</code> 区间。<br>
2. 引入两个特殊符号 <code>&lt;box&gt;</code> 和 <code>&lt;/box&gt;</code>。<br>
3. 训练数据长这样：<code
class="bg-white px-2 py-1 rounded text-sm">Describe the dog &lt;ref&gt;the dog&lt;/ref&gt;&lt;box&gt;(200,200),(500,600)&lt;/box&gt;</code>
</p>
</div>
</div>
<p class="text-xl text-slate-600 mt-8 leading-relaxed">
这种设计极其聪明。它把“检测任务”变成了一个“语言生成任务”。对于 LLM 来说，输出 <code>(200,200)</code> 和输出一个单词没有任何本质区别。这就是 <strong>Next Token
Prediction</strong> 统一万物的魅力！
</p>
<!-- Transition to Next Section -->
<div class="mt-16 p-6 bg-slate-100 rounded-xl border-l-4 border-slate-400 text-slate-600">
<p class="text-lg font-medium">
<strong>小结：</strong> Qwen-VL 证明了只要有好的适配器（Adapter）和分阶段的训练策略，即便只有 7B 的语言模型，也能拥有 SOTA
级别的视觉理解能力。但它还有个遗憾——<strong>分辨率是固定的（448x448）</strong>，这导致看长图或细长文档时会变形。这个问题，将在下一章 Qwen2-VL 中得到革命性的解决。
</p>
</div>
</div>
</section>
<section id="method-qwen2vl" class="mb-24">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 5 五、第二站：Qwen2-VL —— 打破分辨率的“削足适履”

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-10 group tracking-tight">
<span
class="bg-gradient-to-br from-blue-500 to-indigo-600 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:-rotate-12 transition-transform duration-300">5</span>
五、第二站：Qwen2-VL —— 打破分辨率的“削足适履”
</h2>
<!-- Intro Block -->
<div class="mb-12 bg-white p-8 rounded-3xl shadow-premium border border-slate-100 relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-blue-400 via-indigo-500 to-purple-500">
</div>
<div
class="absolute -right-10 -top-10 w-40 h-40 bg-blue-50 rounded-full mix-blend-multiply filter blur-3xl opacity-50">
</div>
<div class="sr-only">

### 🤔 课堂提问：Qwen-VL 的“近视眼”是怎么来的？

</div>

<h3 class="text-xl font-bold text-slate-800 mb-4 flex items-center">
<span class="text-2xl mr-2">🤔</span> 课堂提问：Qwen-VL 的“近视眼”是怎么来的？
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
同学们，还记得我们在上一章讲的 Qwen-VL 吗？它虽然是个优秀的“看图说话”选手，但它有一个致命的弱点——<strong>“近视眼”</strong>。
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
不管你给它一张长条形的长微博截图，还是一个宽屏的 IMAX 电影海报，它都会粗暴地把图片 Resize 成 <code
class="bg-slate-100 px-2 py-0.5 rounded text-red-600 font-mono font-bold">448×448</code> 的正方形。
</p>
<div class="bg-red-50 border-l-4 border-red-400 p-6 rounded-r-lg mb-6">
<p class="text-red-800 font-bold mb-2 text-lg">后果很严重：</p>
<ul class="list-disc list-inside text-red-700 space-y-2">
<li><strong>细节丢失：</strong> 很多细小的文字在缩小后直接变成了噪点。</li>
<li><strong>比例失真：</strong> 瘦高的人变成了矮胖子，圆变成了椭圆，模型的世界观被扭曲了。</li>
<li><strong>算力浪费：</strong> 如果是一张很小的 256x256 的图，为了凑 448，还得强行放大或者 Padding，浪费了宝贵的计算资源。</li>
</ul>
</div>
<p class="text-lg text-slate-600 leading-relaxed">
<strong>Qwen2-VL 的使命，就是彻底解决这个问题。</strong> 它引入了两大杀手锏，听起来很学术，但本质上非常直觉：
<br><br>
<span
class="inline-flex items-center px-3 py-1 rounded-full text-sm font-bold bg-blue-100 text-blue-800 border border-blue-200 shadow-sm mx-1">Naive
Dynamic Resolution (动态分辨率)</span>
<span class="text-slate-400 mx-2">+</span>
<span
class="inline-flex items-center px-3 py-1 rounded-full text-sm font-bold bg-purple-100 text-purple-800 border border-purple-200 shadow-sm mx-1">M-RoPE
(多模态旋转位置编码)</span>。
</p>
</div>
<!-- 5.1 Naive Dynamic Resolution -->
<div class="sr-only">

### 5.1 动态分辨率 (Naive Dynamic Resolution)：像玩俄罗斯方块一样处理图片

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center" id="dynamic-resolution">
<span class="w-2 h-10 bg-blue-500 rounded-full mr-4 shadow-md"></span>
5.1 动态分辨率 (Naive Dynamic Resolution)：像玩俄罗斯方块一样处理图片
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
这一代模型最核心的改变是：<strong>我们不再强制 Resize 图片了！</strong> 或者更准确地说，我们不再把图片 Resize 成一个固定的正方形。
</p>
<p class="text-lg text-slate-600 mb-8 leading-relaxed">
但是，Transformer 本质上还是需要一个序列（Sequence）。如果图片大小不一，Token 数量就不一样，怎么把它们塞进同一个 Batch 里训练呢？Qwen2-VL
并没有发明什么极其复杂的数学变换，而是想出了一个非常工程化、非常实用的办法，我们称之为“<strong>动态切块法</strong>”。
</p>
<!-- Concept Explanation -->
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 hover:shadow-md transition-shadow">
<h4 class="font-bold text-slate-800 mb-3 text-lg">Step 1: 这里的 "Naive" 是什么意思？</h4>
<p class="text-slate-600">
它指的是一种最朴素的策略：我们依然会对图片做 Resize，但目标不再是固定的 $H \times W$，而是<strong>最接近原始分辨率的 $14 \times 14$
的倍数</strong>。
</p>
<div class="mt-4 p-3 bg-white rounded border border-slate-100 font-mono text-sm text-slate-500">
Input: 100x200<br>
Target: (14*N) x (14*M)<br>
Result: 98x196 (最接近)
</div>
</div>
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 hover:shadow-md transition-shadow">
<h4 class="font-bold text-slate-800 mb-3 text-lg">Step 2: 2x2 Pooling (特征压缩)</h4>
<p class="text-slate-600">
为了进一步减少 Token 数量，ViT 输出的 Patch 特征（14x14）会被做一个 <span class="font-bold text-blue-600">2x2
Pooling</span>。这意味着，最终进入 LLM 的每一个 Visual Token，实际上代表了原图上 <span
class="font-bold text-blue-600">28x28</span> 的像素区域。
</p>
</div>
</div>
<!-- SVG Visualization: Dynamic Resolution Process -->
<div class="my-12">
<div class="bg-white rounded-3xl shadow-premium border border-slate-200 p-8 overflow-hidden relative">
<div class="absolute top-0 right-0 w-32 h-32 bg-blue-50 rounded-bl-full opacity-50 pointer-events-none">
</div>
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-10">
🎨 深度图解：从“任意图片”到“Token流”的完整变形记
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
font-size="16">1. 原始输入</text>
<text x="60" y="-10" text-anchor="middle" fill="#64748b" font-size="12">任意宽高比 (e.g.
手机长图)</text>
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
font-size="16">2. 网格对齐</text>
<text x="70" y="-10" text-anchor="middle" fill="#64748b" font-size="12">变为 14 的倍数</text>
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
font-size="16">3. ViT & 压缩</text>
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
<text x="90" y="205" text-anchor="middle" fill="#64748b" font-size="10">大幅减少序列长度</text>
</g>
<!-- Arrow 3 -->
<g transform="translate(680, 220)">
<path d="M 0 0 L 40 0" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-blue-lg)" />
<text x="20" y="-10" text-anchor="middle" font-size="10" fill="#64748b">Flatten</text>
</g>
<!-- --- STAGE 4: PACKED SEQUENCE --- -->
<g transform="translate(740, 140)">
<text x="100" y="-30" text-anchor="middle" font-weight="bold" fill="#334155"
font-size="16">4. 变长序列</text>
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
font-weight="bold">长度 = (H'×W') / (14×14×4)</text>
<text x="105" y="110" text-anchor="middle" fill="#ef4444" font-size="12"
font-weight="bold">No Padding! 拒绝注水！</text>
</g>
</svg>
</div>
<div class="mt-10 grid grid-cols-1 lg:grid-cols-2 gap-8">
<div class="bg-blue-50 p-6 rounded-2xl border border-blue-100">
<h5 class="font-bold text-blue-800 mb-3 text-lg flex items-center">
<span
class="bg-blue-200 text-blue-800 rounded-full w-6 h-6 flex items-center justify-center text-sm mr-2">1</span>
什么是 "Naive"？
</h5>
<p class="text-slate-700 leading-relaxed">
这里的 Naive
是一种自谦。它指的不是算法幼稚，而是<strong>策略上的朴素</strong>：我们不搞复杂的物体检测裁剪（Crop），也不搞多尺度金字塔，就是最简单的：<br>
<span class="bg-white px-1 font-mono text-blue-700 rounded">Resize 到最近的 14 倍数 -> 切 Patch ->
进 ViT</span>。<br>
这种简单性保证了训练的稳定性，也让工程实现（FlashAttention VarLen）变得可能。
</p>
</div>
<div class="bg-purple-50 p-6 rounded-2xl border border-purple-100">
<h5 class="font-bold text-purple-800 mb-3 text-lg flex items-center">
<span
class="bg-purple-200 text-purple-800 rounded-full w-6 h-6 flex items-center justify-center text-sm mr-2">2</span>
2x2 Pooling 的妙处
</h5>
<p class="text-slate-700 leading-relaxed">
为什么要最后做一次 2x2 Pooling？<br>
因为 ViT 的 Patch Size 是 14x14，对于高分辨率图片，Token 数量会爆炸（448x448 就有 1024 个 token）。<br>
2x2 Pooling 相当于把特征图的尺寸缩小了一半（分辨率变成 28x28），<strong>Token 数量直接减少了 75%</strong>！这大大减轻了 LLM
的负担，同时保留了足够的视觉语义。
</p>
</div>
</div>
</div>
</div>
<!-- 5.2 M-RoPE -->
<div class="sr-only">

### 5.2 M-RoPE：给 Token 装上“三维 GPS”

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-purple-500 rounded-full mr-4 shadow-md"></span>
5.2 M-RoPE：给 Token 装上“三维 GPS”
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
解决了分辨率问题，我们迎来了一个更棘手的问题：<strong>位置感（Positional Awareness）的丢失</strong>。
</p>
<div class="flex flex-col md:flex-row gap-8 mb-10">
<div class="flex-1">
<p class="text-lg text-slate-600 mb-4">
在传统的纯文本 LLM 中，位置是一维的（第1个字，第2个字...）。这很简单，用 RoPE 就能完美解决。
</p>
<p class="text-lg text-slate-600">
但在 Qwen2-VL 中，视觉 Token 是被“压扁”后送进来的。如果把一张 2D 图片压成 1D 序列，<strong>原本上下的邻居关系就彻底乱套了</strong>。更别提视频了，那是 3D
的（时间+空间），压扁后更是灾难。
</p>
</div>
<div class="flex-1 bg-slate-100 p-6 rounded-xl border-l-4 border-slate-400 italic text-slate-600">
“这就好比你把一幅拼图拆散了排成一排，如果不给每一块背面写上行号和列号，上帝也拼不回去。”
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
<span class="text-4xl mr-4">🧭</span> M-RoPE 的核心思想：三维位置解耦
</h4>
<p class="text-xl text-slate-300 mb-10 leading-relaxed max-w-3xl relative z-10">
Qwen2-VL 的 <strong>M-RoPE (Multimodal Rotary Positional Embedding)</strong> 采用了一种极具几何美感的做法：它没有引入额外的
Embedding 层，而是直接操作旋转矩阵。它把 Token 的 Embedding 向量<strong>切成三段</strong>，分别由三个独立的旋转矩阵控制，对应时间、高度和宽度。
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
<h4 class="text-xl font-bold text-slate-800 mb-6 px-4 pt-2">📊 论文原图 Figure 3 深度解析</h4>
<div class="overflow-hidden rounded-xl mb-6 border border-slate-100">
<img src="/images/qwen-vlm/image_003.jpg"
alt="M-RoPE Illustration from Paper"
class="w-full object-cover transform hover:scale-105 transition-transform duration-500" />
</div>
<div class="px-4 pb-4">
<div class="prose prose-slate text-slate-600">
<p class="mb-4">
这张图（Figure 3）是理解 M-RoPE 的钥匙。它展示了不同模态下，这三个分量是如何“退化”或“激活”的：
</p>
<ul class="list-none space-y-4 pl-0">
<li class="flex items-start">
<span
class="flex-shrink-0 w-8 h-8 bg-slate-100 rounded-full flex items-center justify-center mr-3 text-lg">📄</span>
<div>
<strong class="text-slate-800 block">Text (纯文本)</strong>
<span class="text-sm">文本是一维的线性流。所以在文本部分，我们让 Temporal, Height, Width 的 ID
<strong>完全相同</strong>（都是序列索引 $i$）。这使得 M-RoPE 退化为普通的 1D
RoPE，兼容了预训练的语言模型能力。</span>
</div>
</li>
<li class="flex items-start">
<span
class="flex-shrink-0 w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-3 text-lg">🖼️</span>
<div>
<strong class="text-blue-800 block">Image (图片)</strong>
<span class="text-sm">图片是静止的 2D 平面。因此，<strong>Temporal ID 被冻结为常数（比如 0）</strong>，而
Height 和 Width ID 则随着像素网格扫描而变化。这样，模型就能感知到二维空间结构。</span>
</div>
</li>
<li class="flex items-start">
<span
class="flex-shrink-0 w-8 h-8 bg-purple-100 rounded-full flex items-center justify-center mr-3 text-lg">🎬</span>
<div>
<strong class="text-purple-800 block">Video (视频)</strong>
<span class="text-sm">视频是多张图片的堆叠。这里三个维度<strong>火力全开</strong>：Temporal ID 表示帧号（Frame
1, Frame 2...），Frame 内部依然保持 H/W 的 2D 变化。模型因此拥有了完整的 3D 时空感知能力。</span>
</div>
</li>
</ul>
</div>
</div>
</div>
</div>
<!-- 插入到 Qwen2-VL 章节的 5.2 节之后，5.3 节之前 -->
<div class="my-20">
<div class="sr-only">

### 5.X 进阶思考：Adapter 的“逆向进化”之谜

</div>

<h3 class="text-3xl font-bold text-slate-800 mb-8 flex items-center">
<span class="w-2 h-10 bg-amber-500 rounded-full mr-4 shadow-md"></span>
5.X 进阶思考：Adapter 的“逆向进化”之谜
</h3>
<div class="bg-amber-50 border-l-4 border-amber-400 p-8 rounded-r-2xl shadow-sm relative overflow-hidden">
<div class="absolute top-0 right-0 w-32 h-32 bg-amber-100 rounded-bl-full opacity-50"></div>
<h4 class="text-xl font-bold text-amber-900 mb-4 flex items-center">
<span class="text-3xl mr-3">🤔</span> 李老师的小黑板：为什么要“退步”？
</h4>
<p class="text-amber-800 text-lg leading-relaxed mb-6">
细心的同学可能发现了：
<br>
<strong>Qwen-VL (v1)</strong> 用的是 <span class="font-mono bg-white px-1 rounded">Cross-Attention (256
Queries)</span>，这看起来很高级，能把图片压缩得很短。
<br>
<strong>Qwen2-VL (v2)</strong> 却改回了简单的 <span class="font-mono bg-white px-1 rounded">2x2 Pooling +
MLP</span>，这看起来像是技术的“退步”。
<br>
<strong>为什么？</strong>
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
<!-- Cross-Attention Issue -->
<div class="bg-white p-6 rounded-xl border border-amber-200">
<h5 class="font-bold text-slate-800 mb-2">Cross-Attention 的代价</h5>
<p class="text-sm text-slate-600">
Query 是这一组<strong>可学习的向量</strong>。它们像一群“探针”，在图片特征里到处乱跑。
<br>
<span class="text-red-500 font-bold">缺点：</span> 它们会打乱空间拓扑结构！虽然位置编码还在，但那种“像素 A 在像素 B
左边”的物理直觉变弱了。这对于需要<strong>精确坐标定位 (Grounding)</strong> 的任务非常不利。
</p>
</div>
<!-- MLP Merger Advantage -->
<div class="bg-white p-6 rounded-xl border border-amber-200">
<h5 class="font-bold text-slate-800 mb-2">MLP Merger 的回归</h5>
<p class="text-sm text-slate-600">
2x2 Pooling 是一种<strong>硬连接</strong>。它强制 Token保留原始的 2D 空间结构。
<br>
<span class="text-emerald-600 font-bold">优点：</span> 虽然 Token 变多了（压缩率低），但它完美保留了“我在哪”的空间信息。这正是
Qwen2-VL 在文档解析和 UI 操作上大杀四方的秘密。
</p>
</div>
</div>
<p class="mt-6 text-amber-900 font-medium italic text-center">
"有时候，保留原始的物理结构比提取抽象的语义更重要。—— Qwen2-VL 的设计哲学"
</p>
</div>
</div>
<!-- 5.3 Model Sizes & Capabilities -->
<div class="sr-only">

### 5.3 家族新成员：2B / 7B / 72B —— 从端侧到云端

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-green-500 rounded-full mr-4 shadow-md"></span>
5.3 家族新成员：2B / 7B / 72B —— 从端侧到云端
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Qwen2-VL 不再是单兵作战，而是推出了三个不同量级的模型，覆盖了从手机端侧到云端超算的全部场景。这里有一个非常有意思的设计细节：<strong>无论 LLM 有多大，它们都共享同一个 600M
参数量的视觉编码器（ViT）！</strong>
</p>
<p class="text-lg text-slate-600 mb-8 bg-green-50 p-4 rounded-lg border-l-4 border-green-500">
这意味着，哪怕是最小的 2B 模型，它的“眼睛”也是和 72B 模型一样锐利的，只是“大脑”处理信息的能力不同。
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
<li class="flex items-start"><span class="text-green-500 mr-2">✓</span> 可以在手机上流畅运行</li>
<li class="flex items-start"><span class="text-green-500 mr-2">✓</span> 文档扫描、实时翻译</li>
<li class="flex items-start"><span class="text-green-500 mr-2">✓</span> 视觉感知能力不缩水</li>
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
<li class="flex items-start"><span class="text-blue-500 mr-2">✓</span> 性价比之王</li>
<li class="flex items-start"><span class="text-blue-500 mr-2">✓</span> 单卡 RTX 3090/4090 可跑</li>
<li class="flex items-start"><span class="text-blue-500 mr-2">✓</span> 大多数 Demo/应用的首选</li>
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
<li class="flex items-start"><span class="text-purple-400 mr-2">✓</span> 对标 GPT-4V 闭源模型</li>
<li class="flex items-start"><span class="text-purple-400 mr-2">✓</span> 复杂长视频分析</li>
<li class="flex items-start"><span class="text-purple-400 mr-2">✓</span> Agent 规划与决策</li>
</ul>
</div>
</div>
</div>
<!-- Figure 2 Capabilities -->
<div class="my-16">
<div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-lg">
<h4 class="text-lg font-bold text-slate-700 mb-4 ml-2">🌟 全能表现 (Capabilities Overview)</h4>
<img src="/images/qwen-vlm/image_002.jpg"
alt="Qwen2-VL Capabilities" class="w-full rounded-2xl shadow-inner" />
<p class="mt-4 text-sm text-slate-500 text-center italic px-8">
Figure 2: Qwen2-VL 的能力全景图。无论是识别植物种类、理解视频中的复杂剧情，还是解决高难度的数学几何题，亦或是多语言 OCR，它都表现得游刃有余。
</p>
</div>
</div>
<!-- Transition -->
<div
class="mt-20 p-8 bg-gradient-to-r from-slate-100 to-white rounded-3xl border-l-8 border-slate-400 text-slate-600 shadow-sm">
<h4 class="text-xl font-bold text-slate-800 mb-3">本章小结</h4>
<p class="text-lg font-medium leading-relaxed">
Qwen2-VL 通过 <strong>Naive Dynamic Resolution</strong> 治好了“近视眼”，通过 <strong>M-RoPE</strong>
治好了“方向盲”。它就像一个视力矫正成功、戴上了 3D 眼镜、智商还在线的超级助手。
</p>
<p class="text-lg font-medium mt-4 leading-relaxed">
但是，故事还没有结束。面对特别复杂的文档（如密密麻麻的发票、报表），或者需要极强逻辑推理能力的场景，它有时候还是会“眼高手低”。下一站，我们将迎来
<strong>Qwen2.5-VL</strong>，看看它是如何进一步打磨细节，成为真正的“文档专家”的。
</p>
</div>
</div>
</section>
<section id="method-qwen25vl" class="mb-24">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 6 六、第三站：Qwen2.5-VL —— 从“能看”到“精通”的细节狂魔

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-10 group tracking-tight">
<span
class="bg-gradient-to-br from-emerald-500 to-teal-600 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:rotate-12 transition-transform duration-300">6</span>
六、第三站：Qwen2.5-VL —— 从“能看”到“精通”的细节狂魔
</h2>
<!-- Intro Block -->
<div class="mb-12 bg-white p-8 rounded-3xl shadow-premium border border-slate-100 relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-emerald-400 via-teal-500 to-cyan-500">
</div>
<div
class="absolute -right-10 -bottom-10 w-40 h-40 bg-emerald-50 rounded-full mix-blend-multiply filter blur-3xl opacity-50">
</div>
<div class="sr-only">

### 🥪 为什么我们需要 Qwen2.5-VL？

</div>

<h3 class="text-xl font-bold text-slate-800 mb-4 flex items-center">
<span class="text-2xl mr-2">🥪</span> 为什么我们需要 Qwen2.5-VL？
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
如果说 Qwen2-VL 解决了“能不能看清不同形状图片”的问题，那么 Qwen2.5-VL 要解决的就是<strong>“能不能看懂最复杂的细节”</strong>。
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-4">
在技术报告中，作者用了一个非常形象的比喻：目前的多模态模型就像是一块<strong>“夹心饼干的中间层”</strong>——虽然能做很多任务，但离顶尖水平（夹心饼干的上下两层美味）还差一口气。
</p>
<div class="bg-emerald-50 border-l-4 border-emerald-400 p-6 rounded-r-lg mb-6">
<p class="text-emerald-800 font-medium mb-2">
<strong>这“一口气”差在哪里？</strong>
</p>
<ul class="list-disc list-inside text-emerald-700 space-y-2 text-base">
<li><strong>文档解析：</strong> 密密麻麻的表格、乐谱、化学分子式，以前的模型一看就晕。</li>
<li><strong>精准定位：</strong> 不只是画个框，而是要精确到像素点（Point）甚至计数（Counting）。</li>
<li><strong>时间感知：</strong> 视频不是匀速播放的幻灯片，快进、慢放、长达一小时的视频，怎么定位到第 59 分 30 秒的那个瞬间？</li>
</ul>
</div>
<p class="text-lg text-slate-600 leading-relaxed">
为了填补这最后一块拼图，Qwen2.5-VL 祭出了四大杀招：
<span
class="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-emerald-100 text-emerald-800 mx-1">Native
Dynamic ViT</span>
<span
class="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-teal-100 text-teal-800 mx-1">Window
Attention</span>
<span
class="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-cyan-100 text-cyan-800 mx-1">Absolute
Time M-RoPE</span>
以及
<span
class="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-slate-100 text-slate-800 mx-1">4.1T
Tokens Data</span>。
</p>
</div>
<!-- 6.1 Architecture Overview -->
<div class="sr-only">

### 6.1 架构总览：更原生，更懂时间

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-emerald-500 rounded-full mr-4 shadow-md"></span>
6.1 架构总览：更原生，更懂时间
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
首先，让我们看一眼 Qwen2.5-VL 的全身照（Figure 1）。如果你仔细对比上一代，会发现结构类似，但内核已经换了。
</p>
<!-- Figure 1 from paper -->
<div class="my-12 bg-white p-4 rounded-2xl border border-slate-200 shadow-lg">
<div class="overflow-hidden rounded-xl">
<img src="/images/qwen-vlm/image_004.jpg"
alt="Qwen2.5-VL Framework"
class="w-full object-cover hover:scale-105 transition-transform duration-500" />
</div>
<p class="mt-4 text-sm text-slate-500 text-center italic">
Figure 1: Qwen2.5-VL 架构图。注意中间醒目的 "Native Resolution Input" 和 "Align with Absolute Time"。
</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200">
<h4 class="font-bold text-slate-800 mb-4 text-lg flex items-center">
<span class="bg-white p-2 rounded-lg shadow-sm mr-3 text-xl">🖼️</span>
Spatial: Native Dynamic ViT
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
不再是简单的“切片+Reszie”。Qwen2.5-VL 从零开始训练了一个<strong>原生支持动态分辨率</strong>的 Vision Transformer。它引入了
<strong>Window Attention</strong>，让计算复杂度从 $O(N^2)$ 降下来，从而轻松吞下 4K 甚至更高清的图。
</p>
</div>
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200">
<h4 class="font-bold text-slate-800 mb-4 text-lg flex items-center">
<span class="bg-white p-2 rounded-lg shadow-sm mr-3 text-xl">⏱️</span>
Temporal: Absolute Time M-RoPE
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
不再只是数“第几帧”。Qwen2.5-VL 将 M-RoPE 的时间维度与<strong>绝对物理时间（秒）</strong>对齐。哪怕视频忽快忽慢（Dynamic FPS），模型也能知道现在是“第
30 秒”而不是简单的“第 150 帧”。
</p>
</div>
</div>
<!-- 6.2 Native Dynamic Resolution & Window Attention -->
<div class="sr-only">

### 6.2 Native Dynamic Resolution：从 Naive 到 Native 的进化

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-teal-500 rounded-full mr-4 shadow-md"></span>
6.2 Native Dynamic Resolution：从 Naive 到 Native 的进化
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
同学们，Qwen2-VL 叫 <strong>Naive</strong> Dynamic Resolution，Qwen2.5-VL 叫 <strong>Native</strong> Dynamic
Resolution。这一字之差，差在哪里？
</p>
<div class="bg-white p-8 rounded-2xl shadow-premium border border-slate-100 mb-10">
<h4 class="text-xl font-bold text-slate-800 mb-6 text-center">Naive vs. Native: 视觉处理的进化</h4>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
<!-- Qwen2-VL (Naive) -->
<div class="relative group">
<div
class="absolute inset-0 bg-red-50 rounded-xl transform rotate-1 transition-transform group-hover:rotate-2">
</div>
<div class="relative bg-white p-6 rounded-xl border-2 border-red-100">
<h5 class="text-lg font-bold text-red-800 mb-2">🔴 Naive (Qwen2-VL)</h5>
<p class="text-sm text-slate-600 mb-4">
利用现成的 ViT（通常是训练在固定分辨率上的），强行把不同比例的图切成 Patch 喂进去。
</p>
<div class="bg-red-50 p-3 rounded border border-red-100 text-xs font-mono text-red-700">
Attention = Global (Full N²)
</div>
<p class="text-sm text-slate-500 mt-2">
<strong>痛点：</strong> 如果图片太大（比如长文档），Token 数量爆炸，全局 Attention 计算量直接炸穿显存。
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
从零训练一个 ViT，天生习惯变长输入。并在内部引入 <strong>Window Attention</strong>。
</p>
<div
class="bg-emerald-50 p-3 rounded border border-emerald-100 text-xs font-mono text-emerald-700">
Attention = Windowed (Linear O(N))
</div>
<p class="text-sm text-slate-500 mt-2">
<strong>优势：</strong> 把图片切成若干个 112x112 的窗口。大部分层只看窗口内，只有少数层看全局。算力开销大幅降低！
</p>
</div>
</div>
</div>
</div>
<!-- SVG: Window Attention -->
<div class="my-12">
<div class="bg-slate-50 rounded-3xl p-8 border border-slate-200 shadow-inner">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
🪟 图解：Window Attention 如何拯救显存
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
<tspan x="0" dy="25">大部分 ViT 层（Layers）只需要在窗口内部（比如 112x112）交流信息。</tspan>
<tspan x="0" dy="25">只有少数几层（Full Attention Block Indexes）会打破窗口，进行全局交流。</tspan>
<tspan x="0" dy="25">这样既保留了局部细节的精细度，又大幅降低了显存占用。</tspan>
</text>
</g>
</svg>
</div>
</div>
</div>
<!-- 6.3 Absolute Time M-RoPE -->
<div class="sr-only">

### 6.3 绝对时间编码：解决“变速运动”的难题

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-cyan-500 rounded-full mr-4 shadow-md"></span>
6.3 绝对时间编码：解决“变速运动”的难题
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
Qwen2-VL 使用 M-RoPE 引入了 Temporal ID，这是一个巨大的进步。但是，旧的 Temporal ID 是基于<strong>帧序号（Index）</strong>的：第 1 帧、第 2
帧...
</p>
<p class="text-lg text-slate-600 mb-8">
<strong>这有什么问题？</strong> 现实中的视频采样率（FPS）是会变的！
<br>
<span class="bg-slate-100 px-2 py-1 rounded text-sm">场景 A：</span> 1 秒抽 1 帧。第 5 帧代表第 5 秒。
<br>
<span class="bg-slate-100 px-2 py-1 rounded text-sm">场景 B：</span> 1 秒抽 5 帧。第 5 帧代表第 1 秒。
<br>
如果模型只知道“这是第 5 帧”，它根本不知道这代表多长的时间跨度。
</p>
<!-- SVG: Absolute Time -->
<div class="my-12">
<div class="bg-white rounded-3xl shadow-premium border border-slate-200 p-8">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
⏱️ 图解：Relative Index vs. Absolute Time
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
"ID:2 在上面代表 2秒，在下面代表 1秒。模型懵了！"
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
"ID 直接映射物理时间。不管采样率多少，1秒就是1秒！"
</text>
</g>
</svg>
</div>
</div>
</div>
<p class="text-lg text-slate-600 mb-8">
Qwen2.5-VL 将 Temporal ID
直接与<strong>绝对时间（秒）</strong>挂钩。通过这种方式，模型不仅能理解“先后顺序”，还能感知“节奏快慢”。这对于理解长视频（比如长达一小时的电影）至关重要。
</p>
<!-- 6.4 Data: The Soul of Qwen2.5-VL -->
<div class="sr-only">

### 6.4 数据工程：不仅仅是“多”，而是“精”

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-cyan-500 rounded-full mr-4 shadow-md"></span>
6.4 数据工程：不仅仅是“多”，而是“精”
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
模型架构只是骨架，数据才是灵魂。Qwen2.5-VL 的预训练数据量达到了惊人的 <strong>4.1 Trillion Tokens</strong>（是 Qwen2-VL 的 3 倍多）。
</p>
<p class="text-lg text-slate-600 mb-8">
但这里更值得关注的是它是如何构建那些<strong>特殊能力数据</strong>的。
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
<!-- Doc Omni-Parsing -->
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 hover:border-cyan-300 transition-colors">
<h4 class="font-bold text-slate-800 mb-3 flex items-center">
<span class="text-2xl mr-2">📄</span> Document Omni-Parsing
</h4>
<p class="text-sm text-slate-600 mb-3">
为了让模型成为“全能读文档专家”，Qwen 团队合成了一大批<strong>HTML 格式</strong>的文档数据。
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
<strong>Key Innovation:</strong> 所有的内容（文字、表格、公式）都带上了 Bounding Box。模型不仅学会了认字，还学会了 Layout（排版布局）。
</p>
</div>
<!-- Grounding -->
<div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 hover:border-emerald-300 transition-colors">
<h4 class="font-bold text-slate-800 mb-3 flex items-center">
<span class="text-2xl mr-2">🎯</span> Absolute Grounding
</h4>
<p class="text-sm text-slate-600 mb-3">
为了支持高精度定位，Qwen2.5-VL 使用了<strong>绝对坐标</strong>（基于原始分辨率），而不是之前的归一化坐标（0-1000）。
</p>
<p class="text-sm text-slate-600">
数据来源非常硬核：
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

### 6.5 实力展示：DocVQA 与 Agent 能力的飞跃

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
6.5 实力展示：DocVQA 与 Agent 能力的飞跃
</h3>
<p class="text-xl text-slate-600 mb-8">
在 Qwen2.5-VL 的技术报告中，最亮眼的成绩单莫过于 <strong>Document Understanding</strong> 和 <strong>Agent</strong> 能力。
</p>
<div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm mb-12">
<h4 class="text-lg font-bold text-slate-800 mb-4">🏆 DocVQA & InfoVQA 成绩单</h4>
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
* 数据来源：Technical Report Table 5
</p>
</div>
<p class="text-lg text-slate-600 leading-relaxed mb-6">
在 DocVQA 上，Qwen2.5-VL-72B 达到了 <span class="font-bold text-emerald-600">96.4</span>
的恐怖分数，这说明它在处理文档细节时已经超越了大多数闭源模型。
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-12">
此外，在 <strong>Agent</strong> 相关的 Benchmark（如 Android World, OSWorld）上，Qwen2.5-VL
也展现出了惊人的决策能力。这得益于它在训练数据中引入了大量 GUI 截图和操作序列（Action Traces）。
</p>
<!-- Transition -->
<div
class="mt-20 p-8 bg-gradient-to-r from-slate-100 to-white rounded-3xl border-l-8 border-slate-400 text-slate-600 shadow-sm">
<h4 class="text-xl font-bold text-slate-800 mb-3">本章小结</h4>
<p class="text-lg font-medium leading-relaxed">
Qwen2.5-VL 是 Qwen-VL 家族的一次“精细化”革命。
<br>它用 <strong>Native Dynamic Resolution + Window Attention</strong> 解决了超高分辨率下的计算效率问题；
<br>它用 <strong>Absolute Time M-RoPE</strong> 解决了长视频的时间感知问题；
<br>它用 <strong>DocOmni Data</strong> 解决了复杂文档的结构化理解问题。
</p>
<p class="text-lg font-medium mt-4 leading-relaxed text-slate-500">
到这里，我们在感知层面似乎已经做到极致了。但是，如果我们要处理<strong>几十万 Token 的超长上下文</strong>，或者进行<strong>复杂的逻辑推理（Thinking
Mode）</strong>，现有的架构还够用吗？
<br>
下一站，终极形态 —— <strong>Qwen3-VL</strong> 登场。
</p>
</div>
</div>
</section>
<section id="method-qwen3vl" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 6 第四站：Qwen3-VL 终极形态：256K 上下文与 DeepStack 的降维打击

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-purple-600 to-pink-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:scale-110 transition-transform duration-300">6</span>
<div class="flex flex-col">
<span
class="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600">第四站：Qwen3-VL</span>
<span class="text-2xl text-slate-500 font-medium mt-2">终极形态：256K 上下文与 DeepStack 的降维打击</span>
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

### 🚀 从“能看懂”到“能思考”的跨越

</div>

<h3 class="text-2xl font-bold text-slate-800 mb-6 flex items-center relative z-10">
<span class="text-3xl mr-3">🚀</span> 从“能看懂”到“能思考”的跨越
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
同学们，如果我们把 Qwen2.5-VL 比作一位眼神犀利、明察秋毫的“文档专家”，那么 Qwen3-VL
就是一位拥有<strong>无限记忆</strong>且<strong>深思熟虑</strong>的“智者”。
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
到了这一代，Qwen 团队不再满足于“看清”一张图或几秒视频，而是向着多模态领域的三个“圣杯”发起了冲击：
</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 relative z-10">
<div
class="bg-white/80 backdrop-blur-sm p-5 rounded-xl border border-purple-100 shadow-sm hover:shadow-md transition-all group">
<div class="text-3xl mb-3 group-hover:-translate-y-1 transition-transform">📚</div>
<h4 class="font-bold text-purple-900 mb-2">原生 256K 上下文</h4>
<p class="text-sm text-slate-600">不再是简单的 RoPE 延展，而是从训练开始就让模型习惯“吞噬”整本书、整部电影。视觉与文本在这个尺度上实现了真正的自由交织。
</p>
</div>
<div
class="bg-white/80 backdrop-blur-sm p-5 rounded-xl border border-pink-100 shadow-sm hover:shadow-md transition-all group">
<div class="text-3xl mb-3 group-hover:-translate-y-1 transition-transform">🧠</div>
<h4 class="font-bold text-pink-900 mb-2">System 2 Thinking</h4>
<p class="text-sm text-slate-600">引入了类似 OpenAI o1 的“慢思考”模式。面对复杂的几何题或推理任务，模型会先生成长长的思维链（CoT），再给出答案。
</p>
</div>
<div
class="bg-white/80 backdrop-blur-sm p-5 rounded-xl border border-indigo-100 shadow-sm hover:shadow-md transition-all group">
<div class="text-3xl mb-3 group-hover:-translate-y-1 transition-transform">🏗️</div>
<h4 class="font-bold text-indigo-900 mb-2">DeepStack 架构</h4>
<p class="text-sm text-slate-600">打破了“视觉仅在输入层注入”的传统，构建了直通深层的“视觉高速公路”。这是大模型架构的一次重要微创新。</p>
</div>
</div>
</div>
<!-- 7.1 Architecture Deep Dive -->
<div class="sr-only">

### 7.1 架构革新：DeepStack 与视觉信号的“渗透”

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-10 flex items-center">
<span class="w-2 h-10 bg-purple-600 rounded-full mr-4 shadow-md"></span>
7.1 架构革新：DeepStack 与视觉信号的“渗透”
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
让我们先看这张极其重要的架构图（Figure 1）。请大家把注意力集中在最右侧那个看似复杂的连接结构上——那就是 <strong>DeepStack</strong>。
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
Figure 1: Qwen3-VL 架构全景。注意右侧的虚线框部分，视觉特征不再是一次性买卖，而是被分层注入到了 LLM 的不同深度。
</p>
</div>
<div class="mb-12 prose prose-slate text-slate-600">
<p class="font-bold text-lg text-slate-800">为什么需要 DeepStack？（The Vanishing Vision Problem）</p>
<p>
传统的 LVLM（如 LLaVA、Qwen-VL v1/v2）通常采用 <strong>"Early Fusion"</strong> 策略：视觉 Token 和文本 Token 拼接后，一起送入 LLM
的第一层。
</p>
<p>
但是，随着 LLM 越来越深（Qwen2.5-72B 有 80 层！），底层的视觉信号在经过几十层的 Self-Attention 和 FFN
变换后，会被“语言模式”逐渐稀释甚至淹没。这就好比你小学一年级看了一张图，让你在读完 80 年书之后的博士论文里描述这张图的细节，你早就忘光了。
</p>
<p>
<strong>DeepStack 的解法：</strong> 既然怕忘，那就“多看几眼”。
</p>
</div>
<!-- DeepStack Mechanism SVG -->
<div class="my-16">
<div class="bg-slate-50 rounded-[2.5rem] p-10 border border-slate-200 shadow-inner relative">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-10">
🏗️ 深度图解：DeepStack 的“梯度高速公路”
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
<text x="0" y="0" font-size="14" fill="#64748b" font-weight="bold">梯度反传路径</text>
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
<tspan font-weight="bold" fill="#7c3aed">Mechanism:</tspan> 从 Vision Encoder
的不同层级（Level）提取特征，通过独立的 Merger 投影，
<tspan font-weight="bold">加（Add）</tspan> 到 LLM 对应层的 Hidden States 上。不增加序列长度，只增加计算深度。
</text>
</g>
</svg>
</div>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
<div class="bg-purple-50 p-6 rounded-2xl border border-purple-100">
<h5 class="font-bold text-purple-900 mb-3 flex items-center">
<span class="text-xl mr-2">🎯</span> 解决的问题
</h5>
<ul class="list-disc list-inside text-slate-700 text-sm space-y-2">
<li><strong>信息遗忘：</strong> 确保 LLM 的深层（负责复杂推理）能直接访问到原始的视觉特征，而不是仅依赖前面层传过来的“二手信息”。</li>
<li><strong>梯度消失：</strong> 在训练时，梯度可以通过这些横向连接（Shortcut）直接回传到 Vision Encoder，加速收敛。</li>
</ul>
</div>
<div class="bg-amber-50 p-6 rounded-2xl border border-amber-100">
<h5 class="font-bold text-amber-900 mb-3 flex items-center">
<span class="text-xl mr-2">⚡</span> 设计巧思
</h5>
<p class="text-slate-700 text-sm leading-relaxed">
注意，DeepStack 是把视觉 Token <strong>相加 (Add)</strong> 到 LLM 的 Hidden States 上，或者是作为 Cross-Attention 的
Key/Value 注入（具体取决于实现，Qwen3-VL 采用的是 Residual Connection 方式）。这意味它<strong>没有增加 LLM 的 Context
Length</strong>！在推理时，这几乎是免费的性能提升。
</p>
</div>
</div>
<!-- 7.2 Interleaved MRoPE -->
<div class="sr-only">

### 7.2 Interleaved MRoPE：频谱再平衡

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-pink-500 rounded-full mr-4 shadow-md"></span>
7.2 Interleaved MRoPE：频谱再平衡
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
Qwen2-VL 的 M-RoPE 已经很强了，但在超长视频理解中暴露出了一个隐蔽的缺陷：<strong>频谱失衡 (Spectral Imbalance)</strong>。
</p>
<div class="bg-slate-50 p-6 rounded-xl border-l-4 border-pink-400 mb-10">
<h4 class="text-lg font-bold text-slate-800 mb-2">🧐 什么是频谱失衡？</h4>
<p class="text-slate-600 text-sm">
RoPE 的特性是：Embedding 向量的前几维对应高频旋转（关注局部位置），后几维对应低频旋转（关注全局长距离）。
<br>
在 Qwen2-VL 中，我们是这样切分向量的：<code>[时间 T | 高度 H | 宽度 W]</code>。
<br>
这意味着：<strong>时间信息 T 总是占据高频段，而空间信息 W 总是占据低频段。</strong>
<br>
结果就是：模型对“局部时间变化”很敏感，但对“长跨度的时间依赖”感知较弱（因为低频段被 H 和 W 占了）。这对长视频理解非常不利。
</p>
</div>
<!-- SVG: Interleaved MRoPE -->
<div class="my-12">
<div class="bg-white rounded-3xl shadow-premium border border-slate-200 p-8">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
🌊 图解：Interleaved MRoPE 的“编织”艺术
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
<text x="710" y="25" font-size="10" fill="#ef4444">← T 只占高频!</text>
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
✅ T, H, W 均匀分布在所有频段，都能捕捉到局部和全局信息。
</text>
</g>
</svg>
</div>
</div>
</div>
<!-- 7.3 Text-based Time Alignment -->
<div class="sr-only">

### 7.3 视频时间戳的回归：Text-based Time Alignment

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
7.3 视频时间戳的回归：Text-based Time Alignment
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
Qwen2.5-VL 在视频处理上还有一个重大改动：<strong>放弃纯粹的 Absolute Position ID，回归 Text-based Timestamp。</strong>
</p>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
<!-- Old Way -->
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm opacity-70">
<h4 class="font-bold text-slate-500 mb-3 text-lg line-through decoration-2 decoration-red-400">Absolute
Pos ID (Old)</h4>
<p class="text-sm text-slate-600 mb-2">
把第 $t$ 秒直接映射到一个很大的 Position ID（比如 ID=30000）。
</p>
<p class="text-xs text-red-600 font-bold">
问题：超长视频会导致 ID 溢出 RoPE 的外推极限；而且对变帧率（Variable FPS）非常敏感。
</p>
</div>
<!-- New Way -->
<div class="bg-indigo-50 p-6 rounded-2xl border border-indigo-200 shadow-md">
<h4 class="font-bold text-indigo-800 mb-3 text-lg">Explicit Text Timestamp (New)</h4>
<p class="text-sm text-indigo-900 mb-2">
直接在视觉 Token 序列里插入<strong>文字形式的时间戳</strong>。
</p>
<div class="bg-white p-3 rounded border border-indigo-100 font-mono text-xs text-indigo-600 mt-2">
[Image Frame 1] ... <strong>&lt;00:01&gt;</strong> ... [Image Frame 2] ...
<strong>&lt;00:05&gt;</strong>
</div>
<p class="text-xs text-indigo-700 font-bold mt-3">
优势：把“时间感知”变成“文本阅读”任务。模型只需要读懂 <code>&lt;00:05&gt;</code> 这个字符串，就能知道现在是第几秒，而不受 ID 大小限制。
</p>
</div>
</div>
<!-- 7.4 Post-training & Thinking Mode -->
<div class="sr-only">

### 7.4 Post-training：Thinking Mode 的诞生

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-pink-600 rounded-full mr-4 shadow-md"></span>
7.4 Post-training：Thinking Mode 的诞生
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Qwen3-VL 的后训练（Post-training）阶段引入了一个激动人心的特性：<strong>System 2 Thinking (慢思考模式)</strong>。这明显是受到了 OpenAI o1
的启发，但在多模态领域，这意味着什么？
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
<h5 class="font-bold text-slate-800">视觉信息提取 (Perception)</h5>
<p class="text-sm text-slate-600 bg-slate-50 p-2 rounded mt-1 border border-slate-100">
"我看到图中有一个红色的三角形和一个蓝色的正方形，它们部分重叠..."
</p>
</div>
</div>
<!-- Step 2 -->
<div class="flex items-start">
<div
class="flex-shrink-0 w-8 h-8 bg-purple-100 rounded-full flex items-center justify-center text-purple-600 font-bold mt-1">
2</div>
<div class="ml-4">
<h5 class="font-bold text-slate-800">逻辑推演 (Reasoning)</h5>
<p class="text-sm text-slate-600 bg-slate-50 p-2 rounded mt-1 border border-slate-100">
"题目问重叠面积。首先我需要根据坐标计算三角形的方程，然后..."
</p>
</div>
</div>
<!-- Step 3 -->
<div class="flex items-start">
<div
class="flex-shrink-0 w-8 h-8 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 font-bold mt-1">
3</div>
<div class="ml-4">
<h5 class="font-bold text-slate-800">自我反思 (Reflection)</h5>
<p class="text-sm text-slate-600 bg-slate-50 p-2 rounded mt-1 border border-slate-100">
"等等，我刚才看错了，那个不是正方形，是个长方形。我需要重新计算..."
</p>
</div>
</div>
<!-- Step 4 -->
<div class="flex items-start">
<div
class="flex-shrink-0 w-8 h-8 bg-emerald-100 rounded-full flex items-center justify-center text-emerald-600 font-bold mt-1">
4</div>
<div class="ml-4">
<h5 class="font-bold text-slate-800">最终回答 (Conclusion)</h5>
<p class="text-sm text-slate-600 bg-slate-50 p-2 rounded mt-1 border border-slate-100">
"重叠面积是 5.5 平方厘米。"
</p>
</div>
</div>
</div>
</div>
<p class="text-lg text-slate-600 leading-relaxed">
Qwen3-VL 提供了 <strong>Thinking</strong> 和 <strong>Non-thinking</strong> 两个版本。
<br>
对于简单的 OCR 或描述任务，Non-thinking 版响应快、成本低。
<br>
对于复杂的数学几何题或长视频推理，Thinking 版虽然慢（生成大量 CoT token），但准确率有质的飞跃。
</p>
<!-- 7.5 Experiments Highlights -->
<div class="sr-only">

### 7.5 实验高光时刻：屠榜！

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
7.5 实验高光时刻：屠榜！
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
* 数据来源：Table 2 from Qwen3-VL Technical Report. 对比模型包括 GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro.
</p>
</div>
<!-- Transition -->
<div
class="mt-20 p-8 bg-gradient-to-r from-slate-100 to-white rounded-3xl border-l-8 border-slate-400 text-slate-600 shadow-sm">
<h4 class="text-xl font-bold text-slate-800 mb-3">全系列总结</h4>
<p class="text-lg font-medium leading-relaxed">
从 Qwen-VL 的“初见光明”，到 Qwen2-VL 的“视力矫正”，再到 Qwen2.5-VL 的“精细入微”，最后到 Qwen3-VL 的“博闻强识、深思熟虑”。
</p>
<p class="text-lg font-medium mt-4 leading-relaxed text-slate-700">
这一路走来，我们见证了多模态模型如何一步步克服分辨率、位置编码、模态对齐、长上下文等技术瓶颈。Qwen3-VL 不仅是一个模型，更是一个集大成者，它代表了当前开源多模态模型的最高水平，也为通往 AGI
的道路点亮了一盏明灯。
</p>
</div>
</div>
</section>
<section id="experiments" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 7 八、实验与数据谱系 数字背后真正的故事：从刷榜到能力涌现

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-amber-500 to-orange-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:rotate-6 transition-transform duration-300">7</span>
<div class="flex flex-col">
<span
class="text-transparent bg-clip-text bg-gradient-to-r from-amber-600 to-orange-600">八、实验与数据谱系</span>
<span class="text-2xl text-slate-500 font-medium mt-2">数字背后真正的故事：从刷榜到能力涌现</span>
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

### 📊 别只看 SOTA，要看“能力边界”的扩张

</div>

<h3 class="text-2xl font-bold text-slate-800 mb-6 flex items-center relative z-10">
<span class="text-3xl mr-3">📊</span> 别只看 SOTA，要看“能力边界”的扩张
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
同学们，当我们拿到一篇像 Qwen3-VL 这样厚重的技术报告时，最容易犯的错误就是直接翻到最后的表格，看一眼 "Bold"（加粗）的数字，然后感叹一句“哇，又 SOTA 了”，接着就把文章关掉了。
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
<strong>这是极其肤浅的阅读方式！</strong>
</p>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
实验章节其实是论文中最诚实的部分。它不仅仅是在秀肌肉，更是在告诉你：<span
class="bg-amber-100 text-amber-800 px-1 rounded font-bold">我们到底教会了模型什么？它现在能做什么？它还在哪里跌倒？</span>
</p>
<div class="bg-white/60 backdrop-blur-md border-l-4 border-amber-500 p-6 rounded-r-xl relative z-10">
<p class="text-amber-900 font-medium italic">
"Benchmark 是模型能力的投影。如果我们把这些分散的数字连起来，就会看到一条清晰的进化曲线：从最基础的‘认字’（OCR），到‘看懂’（VQA），再到现在的‘思考’（Reasoning）。"
</p>
</div>
</div>
<!-- 8.1 Ability Pyramid SVG -->
<div class="my-16">
<div class="bg-slate-50 rounded-[2.5rem] p-8 border border-slate-200 shadow-inner">
<h4 class="text-center font-serif text-2xl font-bold text-slate-800 mb-8">
⛰️ 图解：Qwen-VL 系列的能力进阶金字塔
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
fill="#1e3a8a">Level 1: 基础感知 (Perception)</text>
<text x="400" y="335" text-anchor="middle" font-size="14" fill="#1e40af">OCR, Caption, Detection
(Qwen-VL 强项)</text>
<!-- Level 2: Understanding -->
<path d="M 200 250 L 600 250 L 500 150 L 300 150 Z" fill="url(#grad-level2)" stroke="#6d28d9"
stroke-width="2" />
<text x="400" y="210" text-anchor="middle" font-size="20" font-weight="bold"
fill="#4c1d95">Level 2: 结构化理解 (Understanding)</text>
<text x="400" y="235" text-anchor="middle" font-size="14" fill="#5b21b6">ChartQA, DocVQA,
VideoQA (Qwen2/2.5-VL 强项)</text>
<!-- Level 3: Reasoning -->
<g filter="url(#glow-amber)">
<path d="M 300 150 L 500 150 L 400 50 Z" fill="url(#grad-level3)" stroke="#b45309"
stroke-width="2" />
<text x="400" y="110" text-anchor="middle" font-size="20" font-weight="bold"
fill="#78350f">Level 3: 复杂推理 (Reasoning)</text>
<text x="400" y="135" text-anchor="middle" font-size="14" fill="#92400e">MMMU, MathVista,
Agent (Qwen3-VL 强项)</text>
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

### 8.1 图像 Caption 与通用 VQA：基础能力的试金石

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-blue-500 rounded-full mr-4 shadow-md"></span>
8.1 图像 Caption 与通用 VQA：基础能力的试金石
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
这就像是小学生的语文造句和看图说话。虽然简单，但它是所有复杂能力的基石。如果模型连图里有几个人、穿什么衣服都说不对，后面的推理就无从谈起。
</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
<h4 class="text-lg font-bold text-blue-900 mb-4 flex items-center">
<span class="bg-blue-100 p-2 rounded-lg mr-3">🖼️</span>
Zero-shot Captioning
</h4>
<p class="text-slate-600 text-sm mb-4">
在 <strong>Nocaps</strong> 和 <strong>Flickr30k</strong> 等数据集上，Qwen-VL 早期版本就已经表现出了惊人的泛化能力。这说明它的 Visual
Encoder (ViT-bigG) 和对齐层 (Adapter) 确实把图像特征翻译成了 LLM 能听懂的语言。
</p>
<div class="bg-blue-50 p-3 rounded border border-blue-100 text-xs font-mono text-blue-700">
Qwen2.5-VL: CIDEr Score 远超同级别模型
</div>
</div>
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
<h4 class="text-lg font-bold text-indigo-900 mb-4 flex items-center">
<span class="bg-indigo-100 p-2 rounded-lg mr-3">❓</span>
General VQA
</h4>
<p class="text-slate-600 text-sm mb-4">
<strong>VQAv2, GQA, OKVQA</strong>。这些任务考察的是“定位+识别”。Qwen3-VL 在这里的分数提升，更多归功于它在预训练阶段见过了海量的真实世界图像（World
Knowledge），不再只是只会看 ImageNet 的书呆子。
</p>
<div class="bg-indigo-50 p-3 rounded border border-indigo-100 text-xs font-mono text-indigo-700">
MMBench: Qwen3-VL 达到 88.8 (Thinking)
</div>
</div>
</div>
<!-- 8.2 Document Understanding -->
<div class="sr-only">

### 8.2 文档理解与结构化抽取：从“认字”到“读懂逻辑”

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-purple-500 rounded-full mr-4 shadow-md"></span>
8.2 文档理解与结构化抽取：从“认字”到“读懂逻辑”
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
这是 Qwen2.5-VL 和 Qwen3-VL 的绝对统治区。
</p>
<div class="bg-slate-50 border-l-4 border-purple-400 p-6 rounded-r-lg mb-10">
<h4 class="text-lg font-bold text-slate-800 mb-2">💡 思考题：OCR 分数高 = 文档理解强吗？</h4>
<p class="text-slate-600 text-sm leading-relaxed">
有些模型 OCR 能跑 99 分，但在 DocVQA 上只能跑 60 分。为什么？
<br>因为 OCR 只是把字认出来（Perception），而 DocVQA 需要你理解<strong>布局（Layout）</strong>、<strong>表格结构（Table
Structure）</strong>以及<strong>跨行跨页的语义关联</strong>。
<br>比如：“请问表格第三行第二列的数字减去第一行第二列是多少？” 这需要极其精确的 spatial awareness。
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
<td class="px-6 py-4 text-sm text-slate-600">扫描文档问答</td>
<td class="px-6 py-4 font-bold text-emerald-600">96.5 (SOTA)</td>
<td class="px-6 py-4 text-xs text-slate-500">Native Dynamic Res (清晰度)</td>
</tr>
<tr class="hover:bg-slate-50 transition-colors">
<td class="px-6 py-4 font-mono text-sm font-bold text-slate-700">ChartQA</td>
<td class="px-6 py-4 text-sm text-slate-600">图表数据分析</td>
<td class="px-6 py-4 font-bold text-emerald-600">90.3</td>
<td class="px-6 py-4 text-xs text-slate-500">High-res Input + CoT</td>
</tr>
<tr class="hover:bg-slate-50 transition-colors">
<td class="px-6 py-4 font-mono text-sm font-bold text-slate-700">InfoVQA</td>
<td class="px-6 py-4 text-sm text-slate-600">复杂信息图理解</td>
<td class="px-6 py-4 font-bold text-emerald-600">89.5</td>
<td class="px-6 py-4 text-xs text-slate-500">DeepStack (深层语义)</td>
</tr>
</tbody>
</table>
</div>
<!-- 插入到 实验章节 8.2 节之后 -->
<div class="my-20">
<div class="sr-only">

### 8.X 秘密武器：The Synthetic Data Factory (数据工厂)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
8.X 秘密武器：The Synthetic Data Factory (数据工厂)
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
为什么 Qwen2.5-VL 能看懂那么复杂的 HTML 网页和 PDF？难道是找了一百万个标注员手写的吗？
<br>
<strong>当然不是。</strong> 它的秘密武器是一个全自动的“合成数据工厂”。
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
<h5 class="font-bold text-slate-800 mb-2">💡 核心逻辑：</h5>
<p class="text-slate-600 text-sm leading-relaxed">
既然标注真实文档很难，不如我们<strong>自己生成文档</strong>？
<br>
1. 拿干净的 Markdown / LaTeX 文本。
<br>
2. 用浏览器渲染引擎（Chrome/Puppeteer）把它渲染成图片。
<br>
3. 因为渲染过程是我们控制的，所以我们天然知道每一个字、每一个表格格子的<strong>精确坐标 (Bounding Box)</strong>。
<br>
这样，我们就得到了<strong>无限量的、完美标注的</strong> OCR 和 Layout 数据！
</p>
</div>
</div>
</div>
<!-- 8.3 Video Understanding -->
<div class="sr-only">

### 8.3 视频理解：挑战“大海捞针” (Needle In A Haystack)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-amber-500 rounded-full mr-4 shadow-md"></span>
8.3 视频理解：挑战“大海捞针” (Needle In A Haystack)
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
在视频领域，Qwen3-VL 做了一个非常硬核的测试：<strong>Video Needle-in-a-Haystack (NIAH)</strong>。
这不仅是看模型能不能记住视频，而是看它在面对 1 小时长的视频（数万帧）时，能不能精准找到<strong>那一帧</strong>里的微小细节。
</p>
<div class="flex flex-col md:flex-row gap-8 mb-12">
<div class="w-full md:w-1/2">
<img src="/images/qwen-vlm/image_006.jpg"
class="rounded-xl shadow-lg border border-slate-200 w-full h-auto object-cover"
alt="Video NIAH Heatmap">
<p class="text-center text-xs text-slate-500 mt-2 italic">Figure 3: 视频大海捞针测试热力图。全绿代表 100% 召回。</p>
</div>
<div class="w-full md:w-1/2 flex flex-col justify-center">
<h4 class="text-xl font-bold text-amber-900 mb-4">📊 实验解读</h4>
<p class="text-slate-600 mb-4 leading-relaxed">
看左边的热力图，几乎全是<span class="text-emerald-600 font-bold">绿色</span>。这意味着：
<br>即便视频长度达到 30 分钟甚至 1 小时（Context Length 拉满），Qwen3-VL 依然能精准定位到任意时刻发生的事件。
</p>
<p class="text-slate-600 leading-relaxed">
<strong>功臣是谁？</strong>
<br>
1. <strong>Interleaved MRoPE</strong>：保证了时间维度在长序列中不丢失高频信息。
<br>
2. <strong>Text-based Timestamp</strong>：显式的时间戳 Token 提供了强有力的锚点。
</p>
</div>
</div>
<!-- 8.4 Multimodal Reasoning -->
<div class="sr-only">

### 8.4 多模态推理：Thinking Mode 的降维打击

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-pink-500 rounded-full mr-4 shadow-md"></span>
8.4 多模态推理：Thinking Mode 的降维打击
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
这是 Qwen3-VL 最激动人心的部分。在 MMMU、MathVista 这种硬核推理 Benchmak 上，Qwen3-VL 的 Thinking 模式展现出了惊人的实力。
</p>
<!-- SVG Radar Chart -->
<div class="my-12 flex justify-center">
<div class="bg-white rounded-3xl shadow-xl p-8 border border-slate-100 w-full max-w-3xl relative">
<div class="absolute top-4 right-4 bg-pink-100 text-pink-800 text-xs px-2 py-1 rounded font-bold">
Comparision (Score)</div>
<h4 class="text-center font-serif text-xl font-bold text-slate-800 mb-6">
🕸️ 多模态推理能力雷达图
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
注意看 MathVista 和 MMMU 的分数。Qwen3-VL 在开启 Thinking 模式后，能够生成长达数千 token 的推理步骤，这极大地提升了它处理复杂几何题和物理题的能力。
<br><br>
<span class="font-bold text-slate-800">一个关键的 Insight：</span>
我们发现在训练中加入专门的 CoT 数据（Chain-of-Thought），不仅提升了数学能力，还泛化到了代码生成和 Agent 规划任务中。这说明“推理能力”在深层语义空间是通用的。
</p>
<!-- Transition -->
<div class="mt-24 p-8 bg-slate-900 rounded-3xl text-center relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-amber-500 to-orange-500"></div>
<h4 class="text-2xl font-bold text-white mb-4">本章小结</h4>
<p class="text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed">
实验数据告诉我们，Qwen-VL 系列的每一次升级都不是简单的“参数堆砌”，而是针对特定痛点（分辨率、时间、推理）的<strong class="text-amber-400">架构级突围</strong>。
<br>
现在，你已经看懂了它的前世今生，也看懂了它为何强大。接下来，是时候把这个大家伙搬进你的项目里了。
</p>
<a href="#practical-guide"
class="inline-block mt-8 px-8 py-3 bg-gradient-to-r from-amber-500 to-orange-600 text-white font-bold rounded-full hover:shadow-lg hover:scale-105 transition-all duration-300">
🚀 下一章：复现与实践指南
</a>
</div>
</div>
</section>
<section id="practical-guide" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 8 九、复现与实践指南 把论文里的 Qwen-VL 搬进你的工程里

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-cyan-500 to-blue-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:rotate-3 transition-transform duration-300">8</span>
<div class="flex flex-col">
<span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 to-blue-600">九、复现与实践指南</span>
<span class="text-2xl text-slate-500 font-medium mt-2">把论文里的 Qwen-VL 搬进你的工程里</span>
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

### 🛠️ 别光看论文，跑起来才是真理

</div>

<h3 class="text-2xl font-bold text-slate-800 mb-6 flex items-center relative z-10">
<span class="text-3xl mr-3">🛠️</span> 别光看论文，跑起来才是真理
</h3>
<p class="text-lg text-slate-600 leading-relaxed mb-6 relative z-10">
读完前面的架构解析，相信你已经对 Qwen-VL 系列有了深刻的理论认知。但作为一名要把模型落地的工程师或研究员，你的脑海里可能还有三个终极问题：
</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 relative z-10">
<div class="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-cyan-100 shadow-sm">
<span class="text-2xl">🤔</span>
<p class="font-bold text-cyan-900 mt-2">选哪个版本？</p>
<p class="text-xs text-slate-500">2B/7B/72B? Qwen2.5 还是 Qwen3?</p>
</div>
<div class="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-blue-100 shadow-sm">
<span class="text-2xl">💻</span>
<p class="font-bold text-blue-900 mt-2">怎么调用？</p>
<p class="text-xs text-slate-500">多图、视频、长文档怎么塞进 prompt？</p>
</div>
<div class="bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-indigo-100 shadow-sm">
<span class="text-2xl">🔧</span>
<p class="font-bold text-indigo-900 mt-2">怎么微调？</p>
<p class="text-xs text-slate-500">我有私有数据，能不能让它更懂我的业务？</p>
</div>
</div>
</div>
<!-- 9.1 Model Selection Guide -->
<div class="sr-only">

### 9.1 选型指南：像 RPG 选职业一样选模型

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-cyan-500 rounded-full mr-4 shadow-md"></span>
9.1 选型指南：像 RPG 选职业一样选模型
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Qwen-VL 家族现在人丁兴旺，选错了模型就像法师加了力量点，费力不讨好。我为大家整理了一份<strong>“懒人决策树”</strong>。
</p>
<div class="my-12 bg-slate-50 p-8 rounded-3xl border border-slate-200 shadow-inner">
<div class="flex flex-col items-center space-y-6 font-sans text-sm">
<!-- Question 1 -->
<div
class="bg-white border-2 border-slate-800 text-slate-800 px-6 py-3 rounded-full font-bold shadow-lg relative z-10">
Q1: 你的显存有多少？
</div>
<div class="flex w-full max-w-3xl justify-between px-10 relative">
<div class="absolute top-[-20px] left-1/2 w-0.5 h-10 bg-slate-300 -z-0"></div>
<div class="absolute top-0 left-[20%] right-[20%] h-0.5 bg-slate-300 -z-0"></div>
<div class="absolute top-0 left-[20%] w-0.5 h-6 bg-slate-300"></div>
<div class="absolute top-0 right-[20%] w-0.5 h-6 bg-slate-300"></div>
<!-- Branch A: Low Resource -->
<div class="flex flex-col items-center w-1/2">
<div class="bg-green-100 text-green-800 px-3 py-1 rounded text-xs font-bold mb-2">&lt; 16GB (单卡
3090/4090)</div>
<div class="bg-white border border-green-200 p-4 rounded-xl shadow-sm text-center w-full">
<h5 class="font-bold text-green-700 text-lg mb-1">Qwen2.5-VL-7B</h5>
<p class="text-xs text-slate-500">性价比之王。能跑大多数 Demo，支持视频和文档。</p>
<p class="text-xs text-slate-400 mt-2 border-t border-slate-100 pt-1">Plan B: Qwen2-VL-2B
(手机/树莓派)</p>
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
<p class="font-bold text-slate-700 mb-2">你需要处理什么任务？</p>
<div class="flex justify-around text-xs gap-2">
<div class="bg-blue-50 p-2 rounded border border-blue-100 w-1/2">
<span class="block font-bold text-blue-700">通用 VQA / 简单文档</span>
<span class="block mt-1 text-slate-500">Qwen2.5-VL-72B</span>
</div>
<div class="bg-purple-50 p-2 rounded border border-purple-100 w-1/2">
<span class="block font-bold text-purple-700">复杂推理 / 长视频</span>
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

### 9.2 最小闭环代码：从像素到 Token

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-blue-500 rounded-full mr-4 shadow-md"></span>
9.2 最小闭环代码：从像素到 Token
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
Talk is cheap, show me the code. 下面这是一段基于 Hugging Face <code>transformers</code> 库的最小推理代码。
<br>注意看注释里的<span class="bg-slate-800 text-white px-1 rounded text-sm">李老师划重点</span>部分，那是坑最容易出现的地方。
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
<span class="text-slate-500"># [李老师划重点]：这里一定要加 device_map="auto"，否则大模型可能爆单卡显存</span>
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
<span class="text-green-400">"Qwen/Qwen2.5-VL-7B-Instruct"</span>, 
torch_dtype=torch.bfloat16, 
device_map=<span class="text-green-400">"auto"</span>
)
<span class="text-slate-500"># Processor 负责处理图片 Resize 和 Tokenization</span>
<span class="text-slate-500"># 它是 Qwen-VL 系列的“魔法黑盒”，自动处理 Dynamic Resolution</span>
processor = AutoProcessor.from_pretrained(<span class="text-green-400">"Qwen/Qwen2.5-VL-7B-Instruct"</span>)
messages = [
{
<span class="text-green-400">"role"</span>: <span class="text-green-400">"user"</span>,
<span class="text-green-400">"content"</span>: [
{
<span class="text-green-400">"type"</span>: <span class="text-green-400">"image"</span>,
<span class="text-green-400">"image"</span>: <span class="text-green-400">"https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"</span>,
},
{<span class="text-green-400">"type"</span>: <span class="text-green-400">"text"</span>, <span class="text-green-400">"text"</span>: <span class="text-green-400">"请详细描述这张图片里的内容。"</span>},
],
}
]
<span class="text-slate-500"># 准备输入：把图片像素转成 Tensor，把文本转成 Input IDs</span>
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
<span class="text-slate-500"># [李老师划重点]：generated_ids 包含了输入+输出</span>
<span class="text-slate-500"># 所以解码时要切片，只解出新生成的 token，否则你会看到问题又被复读了一遍</span>
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

### 9.3 进阶玩法：多图与长上下文

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
9.3 进阶玩法：多图与长上下文
</h3>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
<h4 class="text-lg font-bold text-slate-800 mb-4">📚 处理长文档 (PDF)</h4>
<p class="text-sm text-slate-600 mb-4">
当你要把一个 10 页的 PDF 喂给模型时，不要傻傻地把每一页当成一张独立图片。
</p>
<div class="bg-slate-50 p-3 rounded border border-slate-100 text-xs font-mono text-slate-600 mb-4">
Prompt:<br>
[Img Page 1]<br>
[Img Page 2]<br>
...<br>
"请结合第1页的表格和第5页的结论，分析..."
</div>
<p class="text-sm text-slate-600">
<strong>技巧：</strong> 给每一页图片前面加一个文本锚点（Anchor），比如 <code>Image 1: Page 1</code>。这样模型在 Attention
时能更容易定位到特定页面。
</p>
</div>
<div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
<h4 class="text-lg font-bold text-slate-800 mb-4">🎬 处理长视频</h4>
<p class="text-sm text-slate-600 mb-4">
视频抽帧是关键。Qwen2.5-VL 支持动态 FPS，但你得控制总 Token 数。
</p>
<div class="bg-slate-50 p-3 rounded border border-slate-100 text-xs font-mono text-slate-600 mb-4">
Sample Strategy:<br>
1 fps (for short clip) <br>
0.1 fps (for long movie)
</div>
<p class="text-sm text-slate-600">
<strong>技巧：</strong> 利用 Qwen2.5-VL 的绝对时间编码特性，你可以在 Prompt 里问：“在 00:15 秒左右发生了什么？”，模型能利用时间戳精确回答。
</p>
</div>
</div>
<!-- 9.4 Fine-tuning Guide -->
<div class="sr-only">

### 9.4 微调实战：LoRA 是你的好朋友

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-pink-500 rounded-full mr-4 shadow-md"></span>
9.4 微调实战：LoRA 是你的好朋友
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
不要一上来就全参数微调（Full Fine-tuning），除非你有几百张 A100。对于大多数垂直领域任务（比如医学影像报告、工业质检），<strong>LoRA (Low-Rank
Adaptation)</strong> 足够了。
</p>
<div class="bg-pink-50 border-l-4 border-pink-400 p-6 rounded-r-lg mb-8">
<h4 class="text-lg font-bold text-pink-800 mb-2">💡 微调避坑指南</h4>
<ul class="list-disc list-inside text-pink-700 text-sm space-y-2">
<li><strong>冻结 ViT：</strong> 通常情况下，Visual Encoder 不需要动。它已经看过几万亿 token 的数据了，比你手头那几千张图更懂视觉。</li>
<li><strong>只调 LLM 和 Projector：</strong> 把 LoRA 挂在 LLM 的 `q_proj`, `v_proj` 上，甚至只微调 MLP Merger
(Projector)，就能获得不错的领域适应性。</li>
<li><strong>数据格式对齐：</strong> 你的微调数据必须严格遵守 ChatML 格式，包括 `<|vision_start|>` 等特殊 token，否则模型会“精神分裂”。</li>
</ul>
</div>
<!-- 9.5 Common Pitfalls -->
<div class="sr-only">

### 9.5 常见翻车现场 (Common Pitfalls)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-orange-500 rounded-full mr-4 shadow-md"></span>
9.5 常见翻车现场 (Common Pitfalls)
</h3>
<div class="space-y-6">
<!-- Pitfall 1 -->
<div
class="flex items-start p-4 bg-white rounded-xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
<div
class="flex-shrink-0 w-10 h-10 bg-red-100 rounded-full flex items-center justify-center text-red-600 font-bold text-xl mr-4">
🚫</div>
<div>
<h4 class="font-bold text-slate-800 text-base mb-1">OOM (显存爆炸)</h4>
<p class="text-sm text-slate-600">
<strong>现象：</strong> 跑着跑着 CUDA Out of Memory。<br>
<strong>原因：</strong> Qwen2-VL 是动态分辨率，如果你喂了一张 8K 的超大图，它会切出几千个 Token，瞬间撑爆显存。<br>
<strong>解法：</strong> 在 <code>process_vision_info</code> 里设置 <code>max_pixels</code> 限制，或者手动
Resize 超大图。
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
<h4 class="font-bold text-slate-800 text-base mb-1">复读机模式</h4>
<p class="text-sm text-slate-600">
<strong>现象：</strong> 模型不停地重复输出同一句话，或者输出乱码。<br>
<strong>原因：</strong> 通常是 Prompt 格式不对，漏了 <code>&lt;|im_end|&gt;</code>，或者 system prompt
写得太离谱。<br>
<strong>解法：</strong> 严格检查 <code>apply_chat_template</code> 后的字符串，确保特殊 Token 完整。
</p>
</div>
</div>
</div>
<!-- Transition -->
<div class="mt-24 p-8 bg-slate-900 rounded-3xl text-center relative overflow-hidden">
<div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-cyan-500 to-blue-500"></div>
<h4 class="text-2xl font-bold text-white mb-4">Ready to Build?</h4>
<p class="text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed">
理论已经讲透，代码也给了 demo。现在的你，已经具备了驾驭 Qwen-VL 这个多模态巨兽的所有知识。
<br>
无论是做学术研究，还是开发下一个爆款 AI 应用，路就在脚下。
</p>
<a href="#future-work"
class="inline-block mt-8 px-8 py-3 bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-bold rounded-full hover:shadow-lg hover:scale-105 transition-all duration-300">
🔮 下一章：未来展望
</a>
</div>
</div>
</section>
<section id="future-work" class="mb-32">
<div class="prose prose-lg prose-slate max-w-none">
<!-- Section Title -->
<div class="sr-only">

## 9 十、未来展望 多模态大模型的下一个“圣杯”在哪里？

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-violet-600 to-fuchsia-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:scale-110 transition-transform duration-300">9</span>
<div class="flex flex-col">
<span
class="text-transparent bg-clip-text bg-gradient-to-r from-violet-600 to-fuchsia-600">十、未来展望</span>
<span class="text-2xl text-slate-500 font-medium mt-2">多模态大模型的下一个“圣杯”在哪里？</span>
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
Qwen3-VL 已经把上下文推到了 256K，把推理推到了 Thinking Mode，这是否意味着多模态模型已经走到头了？
</p>
<p class="text-xl text-slate-700 leading-relaxed mt-4 relative z-10 font-bold">
答案显然是否定的。恰恰相反，我们才刚刚站在山脚下。
</p>
<p class="text-lg text-slate-600 leading-relaxed mt-4 relative z-10">
如果我们把现在的模型比作一个刚学会“看图写作文”的高中生，那未来的模型应该是一个能“看懂电影、操作电脑、甚至预测未来”的超级特工。这一节，我们抛开具体的 benchmark，来聊聊那些真正值得我们去攻克的
<strong>Open Problems</strong>。
</p>
</div>
<!-- 10.1 Efficient Vision -->
<div class="sr-only">

### 10.1 视觉效率的极限：Token 真的越少越好吗？

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-violet-500 rounded-full mr-4 shadow-md"></span>
10.1 视觉效率的极限：Token 真的越少越好吗？
</h3>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
<div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm">
<h4 class="text-xl font-bold text-slate-800 mb-4">📉 现状与痛点</h4>
<p class="text-slate-600 mb-4">
虽然 Qwen2.5-VL 引入了动态分辨率，但本质上还是在做“压缩”。一张 4K 的图被压成了几百个 Token，大量高频细节（纹理、微小瑕疵）不可避免地丢失了。
</p>
<div class="bg-slate-50 p-4 rounded-xl border-l-4 border-red-400 text-sm text-slate-700">
<strong>The Trade-off:</strong> 想看清细节 -> Token 爆炸 -> 上下文溢出 / 显存 OOM。
</div>
</div>
<div class="bg-violet-50 p-8 rounded-2xl border border-violet-100 shadow-sm">
<h4 class="text-xl font-bold text-violet-900 mb-4">🚀 潜在突破口</h4>
<ul class="space-y-4">
<li class="flex items-start">
<span class="bg-white p-1 rounded text-lg mr-3 shadow-sm">✂️</span>
<div>
<strong class="text-violet-800 block">Dynamic Pruning (动态裁剪)</strong>
<span class="text-sm text-violet-700">推理时动态判断哪些 Patch 是背景，直接丢弃，只保留前景 Token。</span>
</div>
</li>
<li class="flex items-start">
<span class="bg-white p-1 rounded text-lg mr-3 shadow-sm">🧱</span>
<div>
<strong class="text-violet-800 block">Multi-granularity (多粒度 Token)</strong>
<span class="text-sm text-violet-700">大片蓝天用一个“粗粒度 Token”表示，人脸用一百个“细粒度 Token”表示。</span>
</div>
</li>
</ul>
</div>
</div>
<!-- 10.2 Explainability -->
<div class="sr-only">

### 10.2 可解释性的进化：从“黑盒”到“玻璃盒”

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-fuchsia-500 rounded-full mr-4 shadow-md"></span>
10.2 可解释性的进化：从“黑盒”到“玻璃盒”
</h3>
<p class="text-xl text-slate-600 mb-6 leading-relaxed">
现在的 Thinking Mode 虽然能输出文本思考链，但它依然没法告诉我们：<strong>“你到底在看图片的哪一块？”</strong>
</p>
<div class="bg-white p-8 rounded-3xl border border-slate-200 shadow-lg mb-12 relative overflow-hidden">
<div class="absolute top-0 right-0 w-32 h-32 bg-fuchsia-50 rounded-bl-full opacity-50"></div>
<h4 class="text-center font-bold text-slate-800 mb-8 text-xl">未来的多模态解释长什么样？</h4>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
<!-- Concept 1 -->
<div
class="group p-6 rounded-xl bg-slate-50 hover:bg-fuchsia-50 transition-colors border border-slate-100 hover:border-fuchsia-200 cursor-pointer">
<div class="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">🔦</div>
<h5 class="font-bold text-slate-800 mb-2">Visual Grounding in CoT</h5>
<p class="text-sm text-slate-600">
思考链不再只是文字，而是夹杂着 <code>&lt;box&gt;</code> 坐标。
<br>
<span
class="text-xs bg-white px-1 rounded border border-slate-200 mt-2 inline-block italic">"因为这个区域
[10,10,50,50] 是红色的..."</span>
</p>
</div>
<!-- Concept 2 -->
<div
class="group p-6 rounded-xl bg-slate-50 hover:bg-purple-50 transition-colors border border-slate-100 hover:border-purple-200 cursor-pointer">
<div class="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">🎬</div>
<h5 class="font-bold text-slate-800 mb-2">Temporal Attribution</h5>
<p class="text-sm text-slate-600">
在回答视频问题时，高亮时间轴上的关键片段。
<br>
<span
class="text-xs bg-white px-1 rounded border border-slate-200 mt-2 inline-block italic">"结论基于
00:15 到 00:20 的画面推断。"</span>
</p>
</div>
<!-- Concept 3 -->
<div
class="group p-6 rounded-xl bg-slate-50 hover:bg-indigo-50 transition-colors border border-slate-100 hover:border-indigo-200 cursor-pointer">
<div class="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">🧠</div>
<h5 class="font-bold text-slate-800 mb-2">Mechanism Interpretation</h5>
<p class="text-sm text-slate-600">
打开 DeepStack 的黑盒，看看每一层到底学到了什么视觉特征。
</p>
</div>
</div>
</div>
<!-- 10.3 World Model -->
<div class="sr-only">

### 10.3 走向世界模型 (World Model)：预测未来

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
10.3 走向世界模型 (World Model)：预测未来
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
目前的 Qwen-VL 还是一个<strong>被动观察者</strong>：你给它看什么，它就分析什么。但真正的智能体（Agent）需要具备<strong>预测未来</strong>的能力。
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
如果模型不仅能预测下一个文字，还能预测下一帧画面，它就拥有了物理世界的常识。
</p>
<div class="space-y-3">
<div class="flex items-center bg-indigo-800/50 p-3 rounded-lg border border-indigo-700">
<span class="mr-3">🤖</span>
<span class="text-xs text-indigo-100">机器人：如果不小心碰倒这个杯子，水会流向哪里？</span>
</div>
<div class="flex items-center bg-indigo-800/50 p-3 rounded-lg border border-indigo-700">
<span class="mr-3">🚗</span>
<span class="text-xs text-indigo-100">自动驾驶：前面的车亮了刹车灯，接下来会发生什么？</span>
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

### 10.4 评测革命：从刷榜到真实场景

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
10.4 评测革命：从刷榜到真实场景
</h3>
<div class="border-l-4 border-amber-500 pl-6 py-2 mb-8">
<p class="text-xl text-slate-700 font-medium">
“当一个指标变成目标时，它就不再是一个好指标。” —— 古德哈特定律
</p>
</div>
<p class="text-lg text-slate-600 mb-8 leading-relaxed">
现在的 Benchmark (MMMU, MathVista) 虽然难，但大多还是静态的“做题”。未来的评测应该更贴近<strong>动态的真实世界</strong>。
</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
<!-- Card 1 -->
<div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
<div class="h-10 w-10 bg-slate-100 rounded-full flex items-center justify-center text-xl mb-4">🕵️</div>
<h5 class="font-bold text-slate-800 mb-2">Long-term Stability</h5>
<p class="text-xs text-slate-500">
让模型连续运行 24 小时，或者处理 1000 轮对话。它会“发疯”吗？会遗忘之前的设定吗？
</p>
</div>
<!-- Card 2 -->
<div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
<div class="h-10 w-10 bg-slate-100 rounded-full flex items-center justify-center text-xl mb-4">🎮</div>
<h5 class="font-bold text-slate-800 mb-2">Interactive Env</h5>
<p class="text-xs text-slate-500">
把模型扔进 Minecraft 或者真实的 OS 环境里，看它能不能完成“创建一个新文件夹并重命名”这种简单但需要闭环的任务。
</p>
</div>
<!-- Card 3 -->
<div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
<div class="h-10 w-10 bg-slate-100 rounded-full flex items-center justify-center text-xl mb-4">🛡️</div>
<h5 class="font-bold text-slate-800 mb-2">Visual Safety</h5>
<p class="text-xs text-slate-500">
针对 Visual Jailbreak 的防御能力。如果图片里藏着恶意指令，模型能识别并拒绝吗？
</p>
</div>
</div>
<!-- Transition -->
<div
class="mt-24 p-8 bg-gradient-to-r from-violet-600 to-fuchsia-600 rounded-3xl text-center relative overflow-hidden shadow-2xl">
<div
class="absolute top-0 left-0 w-full h-full bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-10">
</div>
<h4 class="text-3xl font-bold text-white mb-6 relative z-10">讲义结语</h4>
<p class="text-lg text-violet-100 max-w-3xl mx-auto leading-relaxed mb-8 relative z-10">
这篇超长的讲义到这里就结束了。我们从 Qwen-VL 的初次尝试，一路走到了 Qwen3-VL 的巅峰对决。
<br><br>
希望你在看完这些“李宏毅式”的讲解后，脑子里留下的不仅仅是那一堆枯燥的缩写（ViT, MRoPE, DeepStack），而是一幅<strong>鲜活的技术演进地图</strong>。
<br>
未来的路很长，但方向已经清晰。带上这份地图，去创造属于你自己的多模态 SOTA 吧！
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

## A 附录一：数学直觉与可视化 不仅要背公式，更要看见数学的形状

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-indigo-500 to-violet-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:rotate-12 transition-transform duration-300">A</span>
<div class="flex flex-col">
<span
class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-violet-600">附录一：数学直觉与可视化</span>
<span class="text-2xl text-slate-500 font-medium mt-2">不仅要背公式，更要看见数学的形状</span>
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
很多同学一看到论文里的 <span class="font-serif italic">Math Section</span> 就头大，觉得那是写给外星人看的。
<br>
但其实，深度学习里的每一个 Loss Function，本质上都是在定义一种<strong>“物理力场”</strong>。
</p>
<p class="text-lg text-slate-600 leading-relaxed mt-4 relative z-10">
在这这一节，我们不搞复杂的求导证明，而是用<strong>几何直觉 (Geometric Intuition)</strong> 把 Qwen-VL
系列中最重要的四个数学概念画出来。我们要看看，这些公式到底是怎么像这就看不见的“手”，推着几百亿个参数跑来跑去的。
</p>
</div>
<!-- A.1 Language Modeling Loss -->
<div class="mb-20">
<div class="flex items-center mb-8">
<div
class="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center text-indigo-600 font-bold text-xl mr-4">
1</div>
<div class="sr-only">

### 语言建模损失 (The Prediction Game)

</div>

<h3 class="text-3xl font-bold text-slate-800">语言建模损失 (The Prediction Game)</h3>
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
符号拆解
</h4>
<ul class="space-y-2 text-slate-600 text-sm font-mono">
<li><span class="bg-indigo-50 text-indigo-700 px-1 rounded">x<sub>t</sub></span> :
我们希望模型预测出的“正确答案”（Ground Truth Token）。</li>
<li><span class="bg-slate-100 text-slate-600 px-1 rounded">x<sub>&lt;t</sub></span> :
历史上已经说过的所有话（Context）。</li>
<li><span class="bg-emerald-50 text-emerald-700 px-1 rounded">V</span> : 视觉信号（Visual
Tokens），这是 LVLM 和 LLM 的最大区别。</li>
</ul>
</div>
<div>
<h4 class="font-bold text-indigo-900 mb-2 flex items-center">
<span class="w-2 h-2 bg-indigo-500 rounded-full mr-2"></span>
物理直觉：拔河比赛
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
想象词表里有 100,000 个单词，每个单词是一个“坑”。模型手里有一个“球”（概率质量，总重为1）。
<br>
这个公式的目标就是：<strong>强迫模型把那个球尽可能多地扔进“正确答案”的坑里。</strong>
<br>
如果扔偏了（比如把“猫”预测成了“狗”），<span class="font-mono text-red-500">-log(P)</span>
就会变得超级大（惩罚），反向传播一脚把参数踢回去。
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
图解：视觉信号 V 改变了 LLM 对 "Cat" 的预测概率。
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

### 对比学习损失 (The Magnet)

</div>

<h3 class="text-3xl font-bold text-slate-800">对比学习损失 (The Magnet)</h3>
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
直觉：派对找朋友
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
想象高维空间是一个巨大的舞池。
<br>
<span class="text-blue-600 font-bold">v<sub>i</sub></span> 是一张图片（比如“一只狗”），<span
class="text-emerald-600 font-bold">t<sub>i</sub></span> 是它的描述文本（“A cute
dog”）。它们是一对好朋友。
<br>
<span class="text-rose-600 font-bold">t<sub>j</sub></span> 是其他路人的描述（比如“A red car”）。
<br>
<strong>这个 Loss 就是一块磁铁：</strong>它要把好朋友 <span
class="font-mono text-xs bg-slate-100 p-0.5">i-i</span> 这一对使劲往一块吸（分子变大），同时把所有路人
<span class="font-mono text-xs bg-slate-100 p-0.5">i-j</span> 使劲推开（分母变小）。
</p>
</div>
<div class="bg-amber-50 p-4 rounded-lg border-l-4 border-amber-400">
<p class="text-amber-800 text-xs font-bold mb-1">🤔 李老师的追问：</p>
<p class="text-amber-700 text-xs">
为什么分母要加所有
<code>j</code>？因为光把朋友拉近是不够的，如果不推开别人，最后所有点都会塌缩到同一个原点（Collapse），模型就学会了“大家都一样”，这也是一种作弊！
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
Embedding Space 中的引力与斥力
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
为什么需要两个 Loss？
</h4>
<p class="text-slate-600 text-sm leading-relaxed">
在目标检测（Detection）或定位（Grounding）任务中，我们通常用两个指标来约束模型：
</p>
<ul class="list-disc list-inside text-slate-600 text-sm mt-2 space-y-2">
<li>
<strong>L1 Loss:</strong> 简单粗暴的“距离感”。计算预测框四个角点坐标和真实框的绝对差值。这就像是用一根弹簧把预测框硬拉向真实框。
</li>
<li>
<strong>GIoU Loss:</strong> 更高级的“形状感”。单纯靠 L1 可能导致两个框虽然中心近了但完全没重叠。IoU 关注重叠面积，GIoU
解决了不重叠时梯度为 0 的问题。
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
黄色弹簧代表 L1 Loss，灰色虚线框用于计算 GIoU。
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

### RoPE / M-RoPE 的几何本质 (The Clock)

</div>

<h3 class="text-3xl font-bold text-slate-800">RoPE / M-RoPE 的几何本质 (The Clock)</h3>
</div>
<div class="bg-white rounded-3xl shadow-lg border border-slate-200 overflow-hidden">
<div class="p-8 flex flex-col md:flex-row gap-10 items-center">
<div class="w-full md:w-1/2">
<p class="text-slate-600 text-lg leading-relaxed mb-4">
RoPE (Rotary Positional Embedding) 是所有 Qwen 模型的基石。
<br><br>
它的核心思想是：<strong>位置不是加法，而是旋转。</strong>
<br>
如果不加位置编码，Token 就像一堆散落在桌子上的词；
<br>
加上 Absolute PE，就像给每个词贴了个号码牌；
<br>
加上 <strong>RoPE</strong>，就像给每个词装了一个“时钟”。第 $m$ 个位置的词，它的向量在空间中旋转了 $m \times \theta$ 的角度。
</p>
<div class="bg-slate-900 text-slate-300 p-4 rounded-xl font-mono text-sm shadow-inner">
<span class="text-purple-400">f</span>(q, m) =
<span class="text-blue-400">R</span><sub>m</sub>
<span class="text-white">&middot;</span> q
<br>
<span class="text-slate-500">// R_m 是一个旋转矩阵</span>
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
相对距离 = 两个向量夹角差 (Pos2 - Pos1 = &theta;)
</text>
</svg>
</div>
</div>
<div class="bg-indigo-50 px-8 py-4 border-t border-indigo-100">
<p class="text-sm text-indigo-900 font-bold mb-1">🔍 M-RoPE 的直觉扩展：</p>
<p class="text-sm text-indigo-800">
如果你理解了这个二维旋转，那么 M-RoPE 就很好理解了：它只是把向量切成了三段，分别在三个<strong>正交</strong>的平面上旋转。
<br>
一段代表时间 $t$ 轴旋转，一段代表高度 $h$ 轴旋转，一段代表宽度 $w$ 轴旋转。
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

## B 附录二：AI4S 专属速查表 当 Qwen-VL 穿上白大褂：从细胞到星系

</div>

<h2 class="flex items-center text-5xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-teal-500 to-emerald-600 text-white w-16 h-16 rounded-2xl inline-flex items-center justify-center text-3xl mr-6 shadow-2xl group-hover:rotate-6 transition-transform duration-300">B</span>
<div class="flex flex-col">
<span class="text-transparent bg-clip-text bg-gradient-to-r from-teal-600 to-emerald-600">附录二：AI4S
专属速查表</span>
<span class="text-2xl text-slate-500 font-medium mt-2">当 Qwen-VL 穿上白大褂：从细胞到星系</span>
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

### 🧬 为什么科学家需要多模态大模型？

</div>

<h3 class="text-2xl font-bold text-slate-800 mb-6 flex items-center relative z-10">
<span class="text-3xl mr-3">🧬</span> 为什么科学家需要多模态大模型？
</h3>
<p class="text-lg text-slate-600 leading-relaxed relative z-10">
各位同学，在 AI for Science (AI4S) 领域，我们经常处理的是极其抽象的数据：基因序列、蛋白质结构、病理切片。
传统方法（如 CNN、U-Net）擅长输出“概率”或“分割掩码”，但它们无法<strong>“解释”</strong>它们看到了什么。
</p>
<p class="text-lg text-slate-600 leading-relaxed mt-4 relative z-10">
Qwen-VL 系列的价值在于：它能把显微镜下的<strong>视觉信号 (Pixel)</strong> 翻译成生物学家的<strong>语言 (Text/Code)</strong>。
<br>
本附录将手把手教你：如何把 Qwen-VL 变成你的<strong>“全天候 AI 实验员”</strong>。
</p>
</div>
<!-- B.1 Scenario Mapping Table -->
<div class="sr-only">

### B.1 科研场景映射表：你的任务适合哪个模型？

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-16 mb-8 flex items-center">
<span class="w-2 h-10 bg-teal-500 rounded-full mr-4 shadow-md"></span>
B.1 科研场景映射表：你的任务适合哪个模型？
</h3>
<div class="overflow-x-auto mb-12 rounded-2xl border border-slate-200 shadow-lg">
<table class="min-w-full bg-white">
<thead class="bg-slate-900 text-white">
<tr>
<th class="px-6 py-4 text-left font-bold text-lg">科研任务 (AI4S Task)</th>
<th class="px-6 py-4 text-left font-bold text-lg">典型场景</th>
<th class="px-6 py-4 text-left font-bold text-lg">推荐模型</th>
<th class="px-6 py-4 text-left font-bold text-lg">核心理由</th>
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
单细胞形态学分析<br>
Drug Screen Phenotyping<br>
由图像生成细胞状态描述
</td>
<td class="px-6 py-6">
<span
class="bg-blue-100 text-blue-800 px-2 py-1 rounded font-mono font-bold">Qwen2-VL-7B</span>
</td>
<td class="px-6 py-6 text-sm">
单细胞图像通常分辨率适中，但需要较强的语义对齐能力。7B 是性价比首选，微调成本低。
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
从 H&E 染色切片预测空间转录组<br>
病理区域定位 (Tumor Region)
</td>
<td class="px-6 py-6">
<span
class="bg-emerald-100 text-emerald-800 px-2 py-1 rounded font-mono font-bold">Qwen2.5-VL</span>
</td>
<td class="px-6 py-6 text-sm">
<strong>关键！</strong> 病理切片 (WSI) 往往是亿级像素。Qwen2.5-VL 的 <strong class="text-emerald-600">Native
Dynamic Resolution</strong> 能处理超大分辨率切片而不丢失细胞级细节。
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
自动化实验室机器臂控制<br>
读取老旧仪器屏幕数值<br>
实验记录电子化
</td>
<td class="px-6 py-6">
<span
class="bg-purple-100 text-purple-800 px-2 py-1 rounded font-mono font-bold">Qwen2.5-VL</span>
</td>
<td class="px-6 py-6 text-sm">
依赖极强的 <strong>OCR</strong> (读仪器) 和 <strong>Grounding</strong> (定位试管位置) 能力。Qwen2.5-VL
在这方面是目前的 SOTA。
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
从 PDF 论文中提取分子式<br>
解析实验数据图表 (ChartQA)<br>
Meta-analysis
</td>
<td class="px-6 py-6">
<span class="bg-slate-800 text-white px-2 py-1 rounded font-mono font-bold">Qwen3-VL</span>
</td>
<td class="px-6 py-6 text-sm">
需要 <strong>DeepStack</strong> 带来的超长上下文（吃透整篇论文）和 <strong>Thinking Mode</strong>（推理复杂的实验逻辑）。
</td>
</tr>
</tbody>
</table>
</div>
<!-- B.2 Deep Dive: HE to ST Visualization -->
<div class="sr-only">

### B.2 深度图解：当 Qwen-VL 遇到病理切片 (HE to ST)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-emerald-500 rounded-full mr-4 shadow-md"></span>
B.2 深度图解：当 Qwen-VL 遇到病理切片 (HE to ST)
</h3>
<p class="text-xl text-slate-600 mb-8 leading-relaxed">
在 Spatial Transcriptomics (ST) 任务中，我们希望从廉价的 H&E 染色图像推断出昂贵的基因表达空间分布。传统的做法是训练一个 CNN 回归模型，但 Qwen-VL
提供了一种<strong>“语义级”</strong>的新思路。
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
<p><strong>👨‍🏫 李老师的小黑板：</strong></p>
<p class="mt-2">
不要把 Qwen-VL 仅仅当成一个“聊天机器人”。在 HE to ST 任务中，你可以微调 Qwen，让它学会：
<br>输入：<code>[H&E Image] <|vision_start|>...<|vision_end|> "Locate regions with high CD8+ expression"</code>
<br>输出：<code><box>[256, 256, 512, 512]</box></code>
</p>
<p class="mt-2">
这相当于把一个复杂的回归问题（Regression），转化成了一个多模态模型最擅长的<strong>定位问题（Grounding）</strong>。
</p>
</div>
</div>
<!-- B.3 Decision Tree -->
<div class="sr-only">

### B.3 科研选型决策树：别用核弹打蚊子

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-indigo-500 rounded-full mr-4 shadow-md"></span>
B.3 科研选型决策树：别用核弹打蚊子
</h3>
<div class="my-12 p-8 bg-slate-900 rounded-3xl text-slate-200 font-sans shadow-2xl relative overflow-hidden">
<div class="absolute -top-20 -left-20 w-60 h-60 bg-blue-500 rounded-full blur-[80px] opacity-20"></div>
<h4 class="text-center font-bold text-2xl text-white mb-10">🔬 AI4S Model Selector</h4>
<div class="space-y-8 relative z-10">
<!-- Decision 1 -->
<div class="flex flex-col items-center">
<div
class="bg-indigo-600 text-white px-6 py-3 rounded-full font-bold mb-4 shadow-lg border border-indigo-400">
Q1: 你的输入数据是什么？
</div>
<div class="flex gap-8 w-full justify-center">
<!-- Branch Left -->
<div class="w-1/2 flex flex-col items-end pr-4 border-r border-slate-600">
<span class="text-sm text-indigo-300 mb-2">纯文本 / 序列 (DNA/Protein)</span>
<div class="bg-slate-800 p-4 rounded-xl border border-slate-600 w-full max-w-xs">
<p class="font-bold text-white mb-1">👉 Qwen2.5-Coder / Math</p>
<p class="text-xs text-slate-400">不需要视觉模块。用数学/代码微调版处理序列逻辑更好。</p>
</div>
</div>
<!-- Branch Right -->
<div class="w-1/2 flex flex-col items-start pl-4">
<span class="text-sm text-emerald-300 mb-2">图像 (Cell / Tissue / Plots)</span>
<div class="text-2xl animate-bounce">⬇</div>
</div>
</div>
</div>
<!-- Decision 2 -->
<div class="flex flex-col items-center">
<div
class="bg-emerald-600 text-white px-6 py-3 rounded-full font-bold mb-4 shadow-lg border border-emerald-400">
Q2: 图像特征是什么样的？
</div>
<div class="flex gap-4 w-full justify-center text-xs">
<div
class="bg-slate-800 p-3 rounded-lg border border-slate-600 w-1/3 hover:bg-slate-700 transition">
<span class="block text-emerald-400 font-bold mb-1">大图、细节极多 (WSI)</span>
<span class="block text-white mb-2">👉 Qwen2.5-VL / Qwen3-VL</span>
<span class="block text-slate-500">必须用 Dynamic Resolution，否则细胞会被缩放得看不见。</span>
</div>
<div
class="bg-slate-800 p-3 rounded-lg border border-slate-600 w-1/3 hover:bg-slate-700 transition">
<span class="block text-blue-400 font-bold mb-1">需要读图表/仪表 (OCR)</span>
<span class="block text-white mb-2">👉 Qwen2.5-VL-72B</span>
<span class="block text-slate-500">OCR 能力最强，能处理复杂表格和曲线。</span>
</div>
<div
class="bg-slate-800 p-3 rounded-lg border border-slate-600 w-1/3 hover:bg-slate-700 transition">
<span class="block text-purple-400 font-bold mb-1">单细胞显微图 (Small)</span>
<span class="block text-white mb-2">👉 Qwen2-VL-7B</span>
<span class="block text-slate-500">性价比高，适合在实验室本地服务器部署。</span>
</div>
</div>
</div>
<!-- Decision 3 -->
<div class="flex flex-col items-center">
<div
class="bg-amber-600 text-white px-6 py-3 rounded-full font-bold mb-4 shadow-lg border border-amber-400">
Q3: 任务复杂度？
</div>
<div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30 text-center max-w-lg mx-auto">
<p class="text-sm text-slate-300 mb-2">
如果需要根据多篇论文的图表进行<strong>综合推理</strong>，或者需要规划<strong>多步化学合成路线</strong>：
</p>
<p class="text-lg font-bold text-amber-400">
🚀 必须上 Qwen3-VL (Thinking Mode)
</p>
<p class="text-xs text-slate-500 mt-1">
只有 Thinking Mode 的 CoT 能力才能处理这种 System 2 级别的科研难题。
</p>
</div>
</div>
</div>
</div>
<!-- B.4 Tips -->
<div class="sr-only">

### B.4 李老师的科研锦囊 (Tips for AI4S)

</div>

<h3 class="text-3xl font-bold text-slate-800 mt-20 mb-8 flex items-center">
<span class="w-2 h-10 bg-slate-500 rounded-full mr-4 shadow-md"></span>
B.4 李老师的科研锦囊 (Tips for AI4S)
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
<div class="bg-teal-50 border-l-4 border-teal-500 p-6 rounded-r-lg">
<h5 class="font-bold text-teal-900 mb-2">💡 关于分辨率的“迷思”</h5>
<p class="text-sm text-teal-800">
做病理分析时，不要把 10000x10000 的 WSI 直接塞进去！即使是 Qwen3-VL 也吃不消。
<br><strong>正确做法：</strong> 使用滑动窗口（Sliding Window）切成 1024x1024 的 Patches，利用 Qwen 的 Batch
处理能力生成局部描述，最后再用 LLM 汇总。
</p>
</div>
<div class="bg-indigo-50 border-l-4 border-indigo-500 p-6 rounded-r-lg">
<h5 class="font-bold text-indigo-900 mb-2">💡 活用 "Visual Prompting"</h5>
<p class="text-sm text-indigo-800">
如果你想让模型关注细胞核，可以在图片上叠加半透明的红色圆圈（Visual Prompt）。Qwen-VL 对这类视觉提示非常敏感，比纯文字描述“看那个圆圆的东西”效果好得多。
</p>
</div>
<div class="bg-amber-50 border-l-4 border-amber-500 p-6 rounded-r-lg">
<h5 class="font-bold text-amber-900 mb-2">💡 别忘了微调 (LoRA)</h5>
<p class="text-sm text-amber-800">
生物医学领域的术语（如 "Apoptosis", "Fibrosis"）在通用语料中出现频率不高。用几百条专业标注数据跑一个 LoRA，能让模型的“专业黑话”水平突飞猛进。
</p>
</div>
<div class="bg-rose-50 border-l-4 border-rose-500 p-6 rounded-r-lg">
<h5 class="font-bold text-rose-900 mb-2">💡 结构化输出是关键</h5>
<p class="text-sm text-rose-800">
不要让模型写散文！在 Prompt 里强制要求输出 JSON 格式（例如提取实验参数）。Qwen2.5-VL 在指令遵循上非常强，能保证输出的数据可以直接被 Python 脚本解析。
</p>
</div>
</div>
</div>
</section>
<!-- 14_appendix_glossary.html -->
<section id="appendix-glossary" class="mb-24 scroll-mt-24">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## C 附录三：多模态黑话大辞典 (The LVLM Ultimate Glossary)

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-slate-600 to-slate-800 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:rotate-12 transition-transform duration-300">C</span>
附录三：多模态黑话大辞典 (The LVLM Ultimate Glossary)
</h2>
<p class="text-xl text-slate-600 mb-8">
这不仅仅是一个名词解释表，更是一个<strong>「Qwen-VL 宇宙的百科全书」</strong>。我们收录了从 Qwen-VL 到 Qwen3-VL 所有的关键组件、模型型号和技术术语，助你彻底读懂技术报告。
</p>
<!-- Category 1: Model Family Genealogy -->
<div class="mb-12">
<div class="sr-only">

### 🌳 Model Family (家族谱系)

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">🌳</span> Model Family (家族谱系)
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
<!-- Qwen-VL -->
<div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
<h4 class="font-bold text-slate-800">Qwen-VL</h4>
<p class="text-xs text-slate-500 font-mono mb-1">Backbone: Qwen-7B</p>
<p class="text-sm text-slate-600">
初代版本。基于 Qwen-7B，使用 OpenCLIP ViT-bigG，固定分辨率 448x448。奠定了“三阶段训练”的基础。
</p>
</div>
<!-- Qwen2-VL -->
<div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
<h4 class="font-bold text-blue-900">Qwen2-VL</h4>
<p class="text-xs text-blue-500 font-mono mb-1">Backbone: Qwen2 (2B/7B/72B)</p>
<p class="text-sm text-slate-600">
二代进化。引入了 <strong>Naive Dynamic Resolution</strong> 和 <strong>M-RoPE</strong>，支持任意分辨率和长视频理解。
</p>
</div>
<!-- Qwen2.5-VL -->
<div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
<h4 class="font-bold text-emerald-900">Qwen2.5-VL</h4>
<p class="text-xs text-emerald-500 font-mono mb-1">Backbone: Qwen2.5 (3B/7B/72B)</p>
<p class="text-sm text-slate-600">
细节狂魔。使用 <strong>Native Dynamic ViT</strong>，引入 <strong>Absolute Time Encoding</strong>，在文档和
Agent 任务上大幅增强。
</p>
</div>
<!-- Qwen3-VL -->
<div
class="bg-slate-900 p-5 rounded-xl border border-slate-700 shadow-sm col-span-1 md:col-span-2 lg:col-span-3">
<h4 class="font-bold text-white">Qwen3-VL</h4>
<p class="text-xs text-purple-400 font-mono mb-1">Backbone: Qwen3 (Dense & MoE)</p>
<p class="text-sm text-slate-300">
终极形态。支持 <strong>256K Context</strong>，引入 <strong>DeepStack</strong> 和 <strong>Thinking
Mode</strong>。拥有 235B MoE 版本。
</p>
</div>
</div>
</div>
<!-- Category 2: Vision Encoders -->
<div class="mb-12">
<div class="sr-only">

### 👁️ Vision Encoders (视觉之眼)

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">👁️</span> Vision Encoders (视觉之眼)
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<!-- ViT-bigG -->
<div class="bg-white p-5 rounded-xl border-l-4 border-indigo-500 shadow-sm">
<h4 class="font-bold text-slate-800">ViT-bigG</h4>
<p class="text-sm text-slate-600 mt-1">
<strong>Used in:</strong> Qwen-VL<br>
<strong>Source:</strong> OpenCLIP (laion-2b)<br>
<strong>Params:</strong> ~1.9B<br>
<strong>特点:</strong> 巨型 ViT，擅长细粒度特征，但只支持固定分辨率。
</p>
</div>
<!-- Qwen2-ViT (Internal) -->
<div class="bg-white p-5 rounded-xl border-l-4 border-blue-500 shadow-sm">
<h4 class="font-bold text-slate-800">Qwen2-ViT (600M)</h4>
<p class="text-sm text-slate-600 mt-1">
<strong>Used in:</strong> Qwen2-VL<br>
<strong>Source:</strong> Trained from scratch (based on SigLIP)<br>
<strong>Params:</strong> ~600M<br>
<strong>特点:</strong> 支持 <strong>Naive Dynamic Resolution</strong>，将输入 resize 为 14x14 的倍数。
</p>
</div>
<!-- Native Dynamic ViT -->
<div class="bg-white p-5 rounded-xl border-l-4 border-emerald-500 shadow-sm">
<h4 class="font-bold text-slate-800">Native Dynamic ViT</h4>
<p class="text-sm text-slate-600 mt-1">
<strong>Used in:</strong> Qwen2.5-VL<br>
<strong>Source:</strong> Trained from scratch<br>
<strong>特点:</strong> 彻底抛弃 Padding，原生支持变长序列输入。引入 <strong>Window Attention</strong> 降低计算复杂度。
</p>
</div>
<!-- SigLIP-2 -->
<div class="bg-white p-5 rounded-xl border-l-4 border-purple-500 shadow-sm">
<h4 class="font-bold text-slate-800">SigLIP-2</h4>
<p class="text-sm text-slate-600 mt-1">
<strong>Used in:</strong> Qwen3-VL<br>
<strong>Variant:</strong> SigLIP2-SO-400M / SigLIP2-Large<br>
<strong>特点:</strong> Google 提出的改进版图文对齐模型，多语言能力强，是 Qwen3-VL 的视觉初始化基座。
</p>
</div>
</div>
</div>
<!-- Category 3: Architecture Components -->
<div class="sr-only">

### 🏗️ Core Architecture (核心组件)

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">🏗️</span> Core Architecture (核心组件)
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
<!-- Adapter / Merger -->
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">C-Attn Adapter</h5>
<p class="text-xs text-slate-500 mt-1">
(Qwen-VL) 单层 Cross-Attention，将不定长视觉特征压缩为固定 256 个 Token。
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">MLP Merger (C-Former)</h5>
<p class="text-xs text-slate-500 mt-1">
(Qwen2-VL+) 使用 2x2 Pooling + MLP，将相邻的 4 个 Patch 特征融合成 1 个 Token。简单高效，保留空间结构。
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">DeepStack</h5>
<p class="text-xs text-slate-500 mt-1">
(Qwen3-VL) 多层视觉注入。不仅在输入层，还在 LLM 的中间层注入视觉特征，解决深层网络“遗忘”视觉信号的问题。
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">SwiGLU</h5>
<p class="text-xs text-slate-500 mt-1">
一种激活函数 (Activation Function)。比 ReLU 更平滑，能学习更复杂的非线性关系。Qwen 全系列的标配。
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">RMSNorm</h5>
<p class="text-xs text-slate-500 mt-1">
Root Mean Square Normalization。一种归一化层，去掉了 LayerNorm 中的 Mean 计算，速度更快，训练更稳。
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">GQA</h5>
<p class="text-xs text-slate-500 mt-1">
Grouped Query Attention。分组查询注意力。在推理时大幅减少 KV Cache 的显存占用，加速生成。
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">MoE</h5>
<p class="text-xs text-slate-500 mt-1">
Mixture of Experts。混合专家模型。Qwen3-VL 有 30B-A3B 版本（总参数 30B，激活 3B），推理极快。
</p>
</div>
<div class="bg-slate-50 p-4 rounded-lg">
<h5 class="font-bold text-slate-800 text-sm">FlashAttention-2</h5>
<p class="text-xs text-slate-500 mt-1">
底层加速库。Qwen2-VL 依赖它的 <strong>VarLen</strong> 特性来实现动态分辨率的高效计算。
</p>
</div>
</div>
<!-- Category 4: Positional Encodings -->
<div class="sr-only">

### 🧭 Positional Encodings (位置编码)

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">🧭</span> Positional Encodings (位置编码)
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<!-- RoPE -->
<div
class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:border-purple-200 transition-colors">
<h4 class="font-bold text-slate-800">RoPE</h4>
<p class="text-xs text-purple-600 font-mono mb-1">Rotary Positional Embedding</p>
<p class="text-sm text-slate-600">
将位置信息编码为向量的旋转角度。具有良好的相对位置感知能力，是现代 LLM 的标配。
</p>
</div>
<!-- M-RoPE -->
<div
class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:border-purple-200 transition-colors">
<h4 class="font-bold text-slate-800">M-RoPE</h4>
<p class="text-xs text-purple-600 font-mono mb-1">Multimodal RoPE</p>
<p class="text-sm text-slate-600">
(Qwen2-VL) 将 RoPE 扩展到 3D。Embedding 向量被切分，分别编码 Time (t), Height (h), Width (w)。
</p>
</div>
<!-- Interleaved M-RoPE -->
<div
class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:border-purple-200 transition-colors">
<h4 class="font-bold text-slate-800">Interleaved M-RoPE</h4>
<p class="text-xs text-purple-600 font-mono mb-1">Qwen3-VL Upgrade</p>
<p class="text-sm text-slate-600">
(Qwen3-VL) 为了解决原版 M-RoPE 的频谱失衡（时间维度只占高频），将 t, h, w 交错分布在整个 embedding 维度上。
</p>
</div>
<!-- Absolute Time Encoding -->
<div
class="bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:border-purple-200 transition-colors">
<h4 class="font-bold text-slate-800">Absolute Time Encoding</h4>
<p class="text-xs text-purple-600 font-mono mb-1">Text-based Timestamp</p>
<p class="text-sm text-slate-600">
(Qwen2.5/3-VL) 不再完全依赖 Position ID，而是插入形如 <code>&lt;00:05&gt;</code> 的文本 Token 来显式标记时间。
</p>
</div>
</div>
<!-- Category 5: Data & Tasks -->
<div class="sr-only">

### 📚 Data & Tasks (数据与任务)

</div>

<h3 class="text-2xl font-bold text-slate-800 mt-10 mb-6 border-b border-slate-200 pb-2 flex items-center">
<span class="mr-3">📚</span> Data & Tasks (数据与任务)
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
<!-- Captioning -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Image Captioning</h5>
<p class="text-xs text-amber-800 mt-1">
看图说话。Qwen 使用大规模合成数据（Recaptioning）来提升 Caption 的详细程度。
</p>
</div>
<!-- VQA -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">VQA</h5>
<p class="text-xs text-amber-800 mt-1">
Visual Question Answering。看图答题。DocVQA (文档), ChartQA (图表), InfoVQA (信息图) 是现在的重点。
</p>
</div>
<!-- Grounding -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Grounding / Referring</h5>
<p class="text-xs text-amber-800 mt-1">
视觉定位。输入文本，输出 Bounding Box。Qwen2.5-VL 进一步支持了 Point (点) 和 Counting (计数)。
</p>
</div>
<!-- OCR -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">OCR</h5>
<p class="text-xs text-amber-800 mt-1">
Optical Character Recognition。文字识别。Qwen-VL 强调多语言 OCR 能力。
</p>
</div>
<!-- Interleaved Data -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Interleaved Data</h5>
<p class="text-xs text-amber-800 mt-1">
图文交错数据。类似 PDF 或网页，文字和图片穿插出现。训练模型处理多图上下文和指代关系。
</p>
</div>
<!-- CoT Data -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Long-CoT Data</h5>
<p class="text-xs text-amber-800 mt-1">
长思维链数据。包含详细推理步骤的数学题或逻辑题。用于训练 Thinking Mode。
</p>
</div>
<!-- Hallucination -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Hallucination</h5>
<p class="text-xs text-amber-800 mt-1">
幻觉。模型一本正经地胡说八道（比如描述了图里没有的物体）。
</p>
</div>
<!-- Zero-shot -->
<div class="bg-amber-50 p-4 rounded-lg">
<h5 class="font-bold text-amber-900 text-sm">Zero-shot</h5>
<p class="text-xs text-amber-800 mt-1">
零样本。模型在没有针对特定任务微调的情况下，直接完成任务。
</p>
</div>
</div>
</div>
</section>
<!-- 15_appendix_qa.html -->
<section id="appendix-qa" class="mb-24 scroll-mt-24">
<div class="prose prose-lg prose-slate max-w-none">
<div class="sr-only">

## D 附录四：灵魂拷问 Q&A (李老师答疑时间)

</div>

<h2 class="flex items-center text-4xl font-extrabold text-slate-900 mb-12 group tracking-tight">
<span
class="bg-gradient-to-br from-slate-600 to-slate-800 text-white w-12 h-12 rounded-xl inline-flex items-center justify-center text-2xl mr-4 shadow-lg group-hover:rotate-12 transition-transform duration-300">D</span>
附录四：灵魂拷问 Q&A (李老师答疑时间)
</h2>
<p class="text-xl text-slate-600 mb-10">
这里收集了一些大家在复现、训练或部署 Qwen-VL 时最常问到的“扎心”问题。我们不打官腔，直接上干货。
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
<h4 class="text-slate-800 font-bold text-xl mb-4">Q1：显存实在不够，量化 (Quantization) 会让模型“瞎眼”吗？</h4>
<p class="text-slate-600 text-base leading-relaxed mb-4">
<strong>👨‍🏫 李老师：</strong> 这是一个非常好的问题。
<br>
一般来说，<strong>Int4 / Int8 量化</strong> 对语言理解能力的影响是可以接受的（只会稍微变笨一点点）。但是！对于<strong>视觉编码器
(ViT)</strong>，请尽量保持半精度 (BF16/FP16)，<strong>不要量化</strong>！
</p>
<div class="bg-amber-50 p-4 rounded-xl border-l-4 border-amber-400 text-sm text-amber-800">
<strong>⚠️ 避坑指南：</strong> ViT 的参数量通常只占总模型的一小部分（例如 Qwen-VL-7B 里只有 1.9B 是 ViT）。为了省这 1-2GB 显存去量化
ViT，会导致视觉特征严重受损，模型可能直接变成“全盲”，得不偿失。
<br>
<strong>最佳实践：</strong> LLM 量化到 Int4，ViT 保持 BF16。
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
<h4 class="text-indigo-900 font-bold text-xl mb-4">Q2：如果我要微调，数据配比 (Data Mixture) 怎么设才不会“灾难性遗忘”？</h4>
<p class="text-indigo-800 text-base leading-relaxed mb-4">
<strong>👨‍🏫 李老师：</strong> 这个问题是多模态微调的“玄学”核心。
<br>
如果你只用纯文本微调，视觉能力会掉；如果你只用纯图片微调，语言能力会掉。经验法则如下：
</p>
<ul class="list-disc list-inside text-indigo-700 text-sm space-y-2 mb-4">
<li><strong>领域微调：</strong> 你的业务数据（如医疗问答）。</li>
<li><strong>通用图文 Replay：</strong> 必须混入约 <strong>10% - 20%</strong> 的通用图文数据（如 COCO Caption,
VQAv2）。这叫 "Regularization"（正则化），防止模型忘掉基础视觉能力。</li>
<li><strong>纯文本 Replay：</strong> 如果你很在意模型的纯聊天能力，最好也混入一点纯文本对话数据。</li>
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
<h4 class="text-slate-800 font-bold text-xl mb-4">Q3：Thinking Mode (CoT) 真的能提升性能吗？还是只是废话文学？</h4>
<p class="text-slate-600 text-base leading-relaxed mb-4">
<strong>👨‍🏫 李老师：</strong> 对于简单任务（比如“图里有只猫”），CoT 确实可能是废话，甚至会因为输出太长导致幻觉。
<br>
但是！对于<strong>复杂推理任务</strong>（比如“算出图中三角形的面积”、“分析这张财报的趋势”），CoT 是<strong>质变</strong>。
</p>
<p class="text-slate-600 text-base leading-relaxed">
LLM 本质上是在做概率预测。如果不让它先生成中间步骤（Thinking），它就得在一步之内直接预测出最终答案，这太难了。CoT
相当于给了模型“打草稿”的空间，让它把复杂问题拆解成简单问题，从而降低了预测难度。
<br>
在 Qwen3-VL 中，Thinking Mode 让 MathVista 这种数学题的分数提升了巨大的幅度，这就是证明。
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
<h4 class="text-emerald-900 font-bold text-xl mb-4">Q4：处理视频时，FPS 到底设多少合适？</h4>
<p class="text-emerald-800 text-base leading-relaxed mb-4">
<strong>👨‍🏫 李老师：</strong> 别被 FPS 框死，要看<strong>Token 预算</strong>。
<br>
视频处理的核心矛盾是：<strong>信息量 vs. 显存</strong>。
</p>
<ul class="list-disc list-inside text-emerald-700 text-sm space-y-2">
<li><strong>短视频 (Tik Tok)：</strong> 可以高 FPS (比如 1~2 fps)，保留动作细节。</li>
<li><strong>长电影 (2小时)：</strong> 必须极低 FPS (比如 0.1 fps，甚至关键帧提取)，否则上下文直接爆炸。</li>
<li><strong>Qwen2.5-VL 的优势：</strong> 它是动态分辨率 +
绝对时间编码。你可以混合输入：关键时刻用高分辨率多帧，平淡时刻用低分辨率少帧。只要时间戳（Timestamp）对上了，模型就能看懂。</li>
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
<h4 class="text-slate-800 font-bold text-xl mb-4">Q5：我看论文里的 CIDEr、Rouge 分数很高，但为什么我在实际用的时候感觉没那么神？
</h4>
<p class="text-slate-600 text-base leading-relaxed mb-4">
<strong>👨‍🏫 李老师：</strong> 欢迎来到真实世界！
<br>
传统的 NLP 指标（如 Rouge, BLEU, CIDEr）主要是比对 N-gram 重合度。但在多模态任务里，它们往往<strong>失效</strong>了。
<br>
比如：
<br>GT: "A white dog."
<br>Pred: "A cute puppy with snowy fur."
<br>这两个句子语义完全一致，但 N-gram 重合度很低，导致 Rouge 分数很低。
<br>
<strong>现在的趋势：</strong> 大家更看重基于 LLM 的评测（如 <strong>LLM-as-a-Judge</strong>）或者针对特定能力的 Benchmark（如
MathVista 测数学，DocVQA 测文档）。不要迷信单一指标，要多看几个维度的榜单。
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

## 结语：Build Your Own Eyes

</div>

<h2 class="text-3xl md:text-5xl font-extrabold text-white mb-8 tracking-tight font-serif">
结语：Build Your Own Eyes
</h2>
<p class="text-xl text-slate-300 leading-relaxed mb-8">
这篇漫长的旅程终于要结束了。
<br>
从 Qwen-VL 的初次尝试，到 Qwen3-VL 的巅峰对决，我们看到的不仅是一个模型家族的进化史，更是<strong>AGI 感知模块</strong>的进化史。
</p>
<div class="bg-white/10 backdrop-blur-md rounded-xl p-8 mb-10 border border-white/10 text-left">
<p class="text-slate-200 text-lg italic mb-4 font-serif">
"The eye altering alters all." —— William Blake
</p>
<p class="text-slate-300 text-base leading-relaxed">
当模型拥有了更清晰的视力（Dynamic Resolution），它就能看到文档的细节；
当模型拥有了更长的时间记忆（M-RoPE + Long Context），它就能理解视频的因果；
当模型拥有了深层思维（Thinking Mode），它就能推导出画面背后的逻辑。
</p>
<p class="text-slate-300 text-base leading-relaxed mt-4">
但这依然不是终点。真正的物理世界模型、具身智能（Embodied AI）、实时交互... 还有无数的 Open Problems 等着你们去解决。
</p>
</div>
<p class="text-lg text-slate-400 mb-12">
现在，把这份讲义关掉，打开你的 IDE，去 Hugging Face 下载权重，去跑通第一个 Demo。
<br>
<strong>动手，才是学习深度学习的唯一捷径。</strong>
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

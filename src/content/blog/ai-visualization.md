---
title: "讲义：AI 时代的科研可视化革命"
description: "从被动阅读到全流程交互重构 - 建立“AI 逻辑 + HTML 呈现”的可视化思维"
pubDate: 2025-12-01
localScripts:
  - "/scripts/ai-visualization.js"
---

<div class="not-prose mb-12 space-y-8">
  <div class="relative text-center space-y-3">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-32 h-32 bg-primary-50 dark:bg-primary-900/20 rounded-full blur-3xl -z-10"></div>
    <div class="inline-flex items-center justify-center px-3 py-1 text-xs font-medium text-primary-700 bg-primary-50 dark:bg-primary-900/30 rounded-full ring-1 ring-inset ring-primary-600/20">
      <i class="fas fa-university mr-2"></i> 复旦大学上海医学院
    </div>
    <div class="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 dark:text-slate-100 leading-tight">
      讲义：AI 时代的 <span class="gradient-text block md:inline">科研可视化革命</span>
    </div>
    <p class="text-xl text-slate-500 dark:text-slate-400 font-light tracking-wide">——从被动阅读到全流程交互重构</p>
  </div>

  <div class="glass-card rounded-2xl p-8 relative overflow-hidden group hover:shadow-lg transition-shadow duration-300">
    <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
      <i class="fas fa-layer-group text-8xl text-primary-500"></i>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 relative z-10 text-left">
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-400 font-bold mb-1">授课对象</div>
        <div class="text-slate-700 dark:text-slate-300 font-medium">高年级本科 / 硕博研究生</div>
      </div>
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-400 font-bold mb-1">课程时长</div>
        <div class="text-slate-700 dark:text-slate-300 font-medium">约 90 分钟</div>
      </div>
      <div>
        <div class="text-xs uppercase tracking-wider text-slate-400 font-bold mb-1">核心目标</div>
        <div class="text-slate-700 dark:text-slate-300 font-medium">建立“AI 逻辑 + HTML 呈现”的可视化思维，掌握科研全流程的降维打击工具。</div>
      </div>
    </div>
  </div>
</div>

## 引言：认知摩擦与沟通的桥梁

在上一章中，我们探讨了 AI 如何作为“第四范式”驱动科学发现。更现实的瓶颈是：**如何让我们的人类大脑高效地读取并理解 AI 的产出？**

我们正面对前所未有的 **认知摩擦（Cognitive Friction）**，源于人机底层思维模式的巨大差异。

<div class="not-prose grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
  <div class="glass-card p-6 rounded-xl border-l-4 border-l-slate-400">
    <div class="flex items-center gap-3 mb-3">
      <i class="fas fa-microchip text-slate-500 dark:text-slate-400 text-xl"></i>
      <span class="text-lg font-bold text-slate-900 dark:text-slate-100">AI 的舒适区</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400 mb-3"><strong>结构化逻辑与线性流</strong></p>
    <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
      AI（尤其是大语言模型）是概率预测引擎，输出被迫坍缩为线性文本流。它最擅长生成<strong>结构化语言</strong>（JSON、Python、HTML、XML），不在乎括号或层级的复杂度。
    </p>
  </div>
  <div class="glass-card p-6 rounded-xl border-l-4 border-l-primary-500">
    <div class="flex items-center gap-3 mb-3">
      <i class="fas fa-eye text-primary-500 text-xl"></i>
      <span class="text-lg font-bold text-slate-900 dark:text-slate-100">人类的舒适区</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400 mb-3"><strong>视觉感知与模式识别</strong></p>
    <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
      人类是视觉动物，对图像、颜色、空间布局、交互的处理速度远高于纯文本。
    </p>
    <ul class="list-none space-y-2 mt-4 text-sm text-slate-500 dark:text-slate-400">
      <li class="flex items-start gap-2">
        <i class="fas fa-exclamation-circle text-amber-500 mt-1"></i>
        <span>大段纯文本是一种高能耗活动，尤其是未格式化的数据或代码。</span>
      </li>
      <li class="flex items-start gap-2">
        <i class="fas fa-arrow-down text-red-500 mt-1"></i>
        <span>高能耗直接拖慢科研效率，易错失洞察。</span>
      </li>
    </ul>
  </div>
</div>

> 核心矛盾：AI 生产的是“高密度的代码/文本”，人类渴望的是“高带宽的视觉/交互”。

解决之道是把 AI 擅长的“结构化代码”实时转译为人类更易理解的视觉体验。那座桥梁，就是 **HTML + 浏览器**。

## 互联网馈赠给科学的礼物

要理解为什么选择 HTML 作为科研可视化的核心载体，需要回顾它的起源：**Web 技术诞生的初衷就是为科学交流服务。**

<div class="not-prose relative border-l-4 border-slate-200 dark:border-slate-700 ml-4 my-10 space-y-12">
  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-slate-100 border-4 border-slate-400 rounded-full"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-2xl text-slate-800">1989</span>
      <span class="font-bold text-primary-600">Web 诞生于 CERN (欧洲核子研究中心)</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400">物理学家 <strong>Tim Berners-Lee</strong> 为了解决论文格式不兼容、信息无法共享的痛点，发明了 HTML。
      <span class="bg-primary-50 dark:bg-primary-900/30 text-primary-700 px-2 py-0.5 rounded text-xs ml-1">基因：为科学交流而生</span>
    </p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://baike.baidu.com/item/%E8%92%82%E5%A7%86%C2%B7%E4%BC%AF%E7%BA%B3%E6%96%AF-%E6%9D%8E" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/LS3_4919_%28cropped%29.jpg/330px-LS3_4919_%28cropped%29.jpg" alt="Tim Berners-Lee" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>Tim Berners-Lee · 百度百科</span>
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
        <span>Tim Berners-Lee 个人主页（W3C）</span>
      </a>
      <a href="https://home.cern/" target="_blank" class="inline-flex items-center gap-2 hover:text-primary-600">
        <span class="w-8 h-8 rounded-full overflow-hidden bg-slate-200 flex items-center justify-center">
          <i class="fas fa-atom text-slate-500 dark:text-slate-400 text-xs"></i>
        </span>
        <span>CERN 官网</span>
      </a>
    </div>
  </div>

  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-slate-100 border-4 border-slate-300 rounded-full"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-xl text-slate-500 dark:text-slate-400">2004</span>
      <span class="font-medium text-slate-700 dark:text-slate-300">Markdown 发布</span>
    </div>
    <p class="text-sm text-slate-500 dark:text-slate-400">John Gruber 为简化 HTML 书写创造了 Markdown，成为 AI 输出的默认格式。</p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://baike.baidu.com/item/%E7%BA%A6%E7%BF%B0%C2%B7%E6%A0%BC%E9%B2%81%E4%BC%AF" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/64/John_Gruber%2C_2009_%28cropped%29.jpg" alt="John Gruber" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>John Gruber · 百度百科</span>
      </a>
      <a href="https://en.wikipedia.org/wiki/John_Gruber" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 hover:text-primary-600">
        <i class="fas fa-globe text-[11px]"></i>
        <span>Wikipedia</span>
      </a>
    </div>
    <div class="mt-3 text-xs">
      <a href="https://daringfireball.net/projects/markdown/" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-500 dark:text-slate-400 hover:text-primary-600 hover:bg-primary-50 dark:bg-primary-900/30 border border-slate-100">
        <i class="fas fa-link text-xs"></i>
        <span>原始 Markdown 规范（Daring Fireball）</span>
      </a>
    </div>
  </div>

  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-white dark:bg-gray-800 border-4 border-blue-500 rounded-full"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-2xl text-slate-800">2008</span>
      <span class="font-bold text-blue-600">Chrome 与 V8 引擎革命</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400">Google 推出极速 V8 引擎，浏览器升级为“超级操作系统”。</p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://baike.baidu.com/item/%E6%8B%89%E6%96%AF%C2%B7%E5%B7%B4%E5%85%8B" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Lars_Bak.png" alt="Lars Bak" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>Lars Bak · 百度百科</span>
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
        <span class="text-xs text-slate-500 dark:text-slate-400">Chrome 浏览器</span>
      </a>
      <a href="https://v8.dev/" target="_blank" class="inline-flex items-center gap-2 hover:text-blue-600 text-xs text-slate-500 dark:text-slate-400">
        <i class="fas fa-bolt text-blue-500 text-xs"></i>
        <span>V8 引擎官方博客</span>
      </a>
    </div>
  </div>

  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-slate-100 border-4 border-slate-300 rounded-full"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-xl text-slate-500 dark:text-slate-400">2011-2014</span>
      <span class="font-medium text-slate-700 dark:text-slate-300">可视化与前端框架爆发</span>
    </div>
    <p class="text-sm text-slate-500 dark:text-slate-400">
      <strong>D3.js (2011)</strong> 让数据在网页上动起来；<br>
      <strong>Vue.js (2014)</strong> 让开发者像搭积木一样构建复杂应用。
    </p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://en.wikipedia.org/wiki/Mike_Bostock" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://avatars.githubusercontent.com/u/230541?v=4" alt="Mike Bostock" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>Mike Bostock · Wikipedia</span>
      </a>
      <a href="https://baike.baidu.com/item/%E5%B0%A4%E9%9B%A8%E6%BA%AA" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://avatars.githubusercontent.com/u/499550?v=4" alt="尤雨溪 (Evan You)" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>尤雨溪 · 百度百科</span>
      </a>
      <a href="https://en.wikipedia.org/wiki/Evan_You" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 hover:text-primary-600">
        <i class="fas fa-globe text-[11px]"></i>
        <span>Evan You · Wikipedia</span>
      </a>
    </div>
    <div class="mt-3 flex items-center gap-4">
      <a href="https://d3js.org/" target="_blank" class="inline-flex items-center gap-2 hover:opacity-80">
        <img src="https://d3js.org/logo.svg" alt="D3.js Logo" class="h-5 object-contain">
        <span class="text-xs text-slate-500 dark:text-slate-400">D3.js 官网</span>
      </a>
      <a href="https://vuejs.org/" target="_blank" class="inline-flex items-center gap-2 hover:opacity-80">
        <img src="https://vuejs.org/images/logo.png" alt="Vue.js Logo" class="h-5 object-contain">
        <span class="text-xs text-slate-500 dark:text-slate-400">Vue.js 官网</span>
      </a>
    </div>
  </div>

  <div class="relative pl-8">
    <div class="absolute -left-[10px] top-1 w-6 h-6 bg-white dark:bg-gray-800 border-4 border-purple-500 rounded-full animate-pulse"></div>
    <div class="flex items-baseline gap-3 mb-1">
      <span class="font-bold text-2xl text-slate-800">Now</span>
      <span class="font-bold text-purple-600">AI Coding 时代</span>
    </div>
    <p class="text-sm text-slate-600 dark:text-slate-400">无需手写 V8 或 Vue 语法，只需自然语言 Prompt，即可调动上述历史积淀生成科研工具。</p>
    <div class="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-600 dark:text-slate-400">
      <a href="https://baike.baidu.com/item/%E8%90%A8%E5%A7%86%C2%B7%E9%98%BF%E7%89%B9%E6%9B%BC" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Sam_Altman_TechCrunch_SF_2019_Day_2_Oct_3_%28cropped%29.jpg/330px-Sam_Altman_TechCrunch_SF_2019_Day_2_Oct_3_%28cropped%29.jpg" alt="Sam Altman" class="w-9 h-9 rounded-full object-cover ring-2 ring-white shadow" loading="lazy">
        <span>Sam Altman · 百度百科</span>
      </a>
      <a href="https://en.wikipedia.org/wiki/Sam_Altman" target="_blank" class="inline-flex items-center gap-2 px-2 py-1 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 hover:text-purple-600">
        <i class="fas fa-globe text-[11px]"></i>
        <span>Wikipedia</span>
      </a>
    </div>
  </div>
</div>

### 1.2 辨析：Markdown vs. HTML

<div class="not-prose grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
  <div class="glass-card p-6 rounded-xl flex flex-col h-full">
    <div class="mb-4">
      <span class="bg-slate-100 text-slate-600 dark:text-slate-400 px-2 py-1 rounded text-xs font-bold uppercase tracking-wider">Markdown</span>
      <div class="text-lg font-bold text-slate-900 dark:text-slate-100 mt-1">2004 年的极简主义</div>
    </div>
    <div class="flex-grow space-y-4 text-sm text-slate-600 dark:text-slate-400">
      <p><strong>你其实早就见过它</strong>：星号 <code>**重点**</code>、井号 <code># 标题</code> 都是标记。它是所有 AI 模型输出文本时的默认格式。</p>
      <div class="bg-red-50 text-red-700 p-3 rounded text-xs border border-red-100">
        <strong>局限</strong>：它是一张“数字纸张”。排序表格、图像放大、交互按钮都做不到。
      </div>
    </div>
  </div>

  <div class="glass-card p-6 rounded-xl flex flex-col h-full border border-primary-100 shadow-lg shadow-primary-500/5">
    <div class="mb-4">
      <span class="bg-primary-100 text-primary-600 px-2 py-1 rounded text-xs font-bold uppercase tracking-wider">HTML</span>
      <div class="text-lg font-bold text-slate-900 dark:text-slate-100 mt-1">全维度的数字容器</div>
    </div>
    <div class="flex-grow space-y-4 text-sm text-slate-600 dark:text-slate-400">
      <p><strong>本质</strong>：结构（Structure）、表现（Presentation）、行为（Behavior）的结合。AI 可以轻松生成 HTML，让浏览器立即把它变成可交互的软件。</p>
      <div class="bg-green-50 text-green-800 p-3 rounded text-xs border border-green-100">
        <strong>优势</strong>：信息从“二维纸面”跃升到“三维交互”，匹配人类视觉优势。
      </div>
    </div>
  </div>
</div>

<div class="not-prose mt-6 p-4 bg-slate-800 text-slate-200 rounded-lg text-center text-sm font-medium">
  结论：<span class="text-white">Markdown</span> 适合用来与 AI 对话（输入），<span class="text-white">HTML</span> 适合用来接收 AI 的成果（输出）。
</div>

## 可视化工具的谱系——寻找“中间地带”

在科研可视化的光谱上，我们拥有不同的工具。理解它们的边界，是选择正确工具的前提。

### 2.1 基础层：Markdown (草稿本)

<div class="not-prose relative pl-8 border-l-2 border-slate-200 dark:border-slate-700">
  <div class="absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-slate-300 border-2 border-white"></div>
  <p class="text-sm text-slate-500 dark:text-slate-400 mb-2">与 ChatGPT 对话时最常见的格式，也是目前 AI 的默认输出。</p>
  <div class="flex flex-wrap gap-2 text-sm">
    <span class="px-2 py-1 bg-slate-100 text-slate-600 dark:text-slate-400 rounded">纯文本</span>
    <span class="px-2 py-1 bg-slate-100 text-slate-600 dark:text-slate-400 rounded">格式简单</span>
    <span class="px-2 py-1 bg-red-50 text-red-600 rounded">局限：静态且线性</span>
  </div>
  <div class="mt-4 grid md:grid-cols-2 gap-4 text-xs">
    <div class="bg-slate-900 text-slate-100 rounded-lg p-3 font-mono">
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">原始格式（Markdown）</div>
      <pre><code># 免疫检查点阻断简介

**PD-1 抑制剂** 可以重新激活
被耗竭的 T 细胞。

- nivolumab
- pembrolizumab</code></pre>
    </div>
    <div class="bg-white dark:bg-gray-800 rounded-lg p-3 border border-slate-200 dark:border-slate-700 text-[13px] leading-relaxed">
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">渲染效果（在论文 / 网页中）</div>
      <div class="text-sm font-bold text-slate-900 dark:text-slate-100 mb-1">免疫检查点阻断简介</div>
      <p class="mb-1"><strong>PD-1 抑制剂</strong> 可以重新激活被耗竭的 T 细胞。</p>
      <ul class="list-disc pl-5 text-slate-600 dark:text-slate-400">
        <li>nivolumab</li>
        <li>pembrolizumab</li>
      </ul>
    </div>
  </div>
</div>

### 2.2 严谨层：Python / R (印刷机)

<div class="not-prose relative pl-8 border-l-2 border-slate-200 dark:border-slate-700">
  <div class="absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-slate-300 border-2 border-white"></div>
  <p class="text-sm text-slate-500 dark:text-slate-400 mb-2">发表 SCI 论文常用的绘图工具（Matplotlib, ggplot2）。</p>
  <div class="mb-2 text-sm text-slate-600 dark:text-slate-400 bg-slate-50 dark:bg-slate-900 p-2 rounded inline-block">
    <strong>历史背景</strong>：John Hunter (Matplotlib, 2003) / Hadley Wickham (ggplot2, 2005)
  </div>
  <div class="flex flex-wrap gap-2 text-sm mt-1">
    <span class="px-2 py-1 bg-slate-100 text-slate-600 dark:text-slate-400 rounded">静态高清</span>
    <span class="px-2 py-1 bg-slate-100 text-slate-600 dark:text-slate-400 rounded">精确控制</span>
    <span class="px-2 py-1 bg-red-50 text-red-600 rounded">局限：重且慢</span>
  </div>
  <div class="mt-4 grid md:grid-cols-2 gap-4 text-xs">
    <div class="bg-slate-900 text-slate-100 rounded-lg p-3 font-mono overflow-x-auto">
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">原始格式（Python / Matplotlib）</div>
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
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">渲染效果（论文中的静态图）</div>
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
      <p class="mt-2 text-[11px] text-slate-500 dark:text-slate-400 text-center">静态 PNG / PDF，被嵌入到文章中。</p>
    </div>
  </div>
</div>

### 2.3 核心层：HTML + JS (仪表盘)

<div class="not-prose relative pl-8 border-l-2 border-primary-500">
  <div class="absolute -left-[11px] top-0 w-5 h-5 rounded-full bg-primary-50 dark:bg-primary-900/30 border-4 border-primary-100 shadow-sm"></div>
  <p class="text-sm text-slate-500 dark:text-slate-400 mb-2">本课程的核心，也是常被忽视的“中间地带”。</p>
  <div class="mb-2 text-sm text-slate-600 dark:text-slate-400 bg-primary-50 dark:bg-primary-900/30 p-2 rounded inline-block border border-primary-100">
    <strong>历史背景</strong>：Mike Bostock (D3.js, 2011) —— 开启“数据驱动文档”时代。
  </div>
  <ul class="list-none space-y-2 mt-2">
    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-slate-300">
      <i class="fas fa-chevron-down text-primary-500 text-xs"></i> <strong>折叠</strong>：保持主界面清爽。
    </li>
    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-slate-300">
      <i class="fas fa-filter text-primary-500 text-xs"></i> <strong>筛选</strong>：瞬间找到关注的数据。
    </li>
    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-slate-300">
      <i class="fas fa-mouse-pointer text-primary-500 text-xs"></i> <strong>响应</strong>：悬停显示数值，框选放大。
    </li>
  </ul>
  <p class="text-sm font-bold text-primary-700 mt-2">价值：它是思考的容器，提供最佳的探索性数据分析 (EDA) 体验。</p>
  <div class="mt-4 grid md:grid-cols-2 gap-4 text-xs">
    <div class="bg-slate-900 text-slate-100 rounded-lg p-3 font-mono overflow-x-auto">
      <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">原始格式（HTML + JS 仪表盘片段）</div>
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
        <div class="text-[10px] uppercase tracking-wider text-slate-400 mb-1">渲染效果（炫彩交互仪表盘）</div>
        <div class="flex gap-2">
          <button class="px-2 py-1 text-[11px] rounded bg-gradient-to-r from-indigo-500 to-cyan-400 text-white shadow" onclick="renderDashboardDemo(true)">刷新模拟数据</button>
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
          <span class="inline-flex items-center gap-1 text-indigo-600"><i class="fas fa-magic text-xs"></i> 渐变高亮</span>
          <span class="inline-flex items-center gap-1 text-emerald-600"><i class="fas fa-filter text-xs"></i> 筛选突出 CR/PR</span>
        </div>
      </div>
    </div>
  </div>
</div>

## 实战——全流程的交互式重构

理论必须服务于实践。以下是 5 个可以立刻落地的场景，每个都配有 **操作步骤** 与 **可直接复制的 Prompt**。

<div class="not-prose space-y-16">
### 3.1 阅读的重构：从线性文本到交互式 App

<div class="glass-card p-8 rounded-2xl relative overflow-hidden">
<div class="absolute top-0 right-0 w-24 h-24 bg-blue-50 rounded-bl-full -z-10"></div>

<div class="bg-primary-50 dark:bg-primary-900/30 rounded-lg p-5 mb-6 text-sm text-primary-800 leading-relaxed">
<strong>核心思路</strong>：我们平常阅读的文献，大多是行间距很窄、版心拥挤的 PDF，图片经常跨页、来回翻找，既不护眼也不利于专注。<br>
与其被动接受排版，不如<strong>把文献“拆开重组”</strong>：如果有对应的网页版本，可以右键查看<strong>网页源代码</strong>，把这段 HTML 源码交给 AI，请它帮我们重排成一个“适合自己阅读”的 HTML 阅读器。<br>
源代码里天然包含了图片的 URL、标题结构等信息，因此经过一次性转换，我们就能得到一个<strong>字体更大、留白更充足、图文在同一视野内</strong>的阅读页面。<br>
即使没有网页源码，或者你就是习惯从 PDF 中复制文字，也可以让 AI 按照“知识点罗列 + 增大行距 + 重要句加粗”的方式重新排版，减少信息密度、突出重点，从而极大提升长文献阅读的舒适度和效率。
</div>

<div class="mb-6 text-xs text-slate-500 dark:text-slate-400 flex flex-wrap gap-3 items-center">
<span class="font-semibold text-slate-600 dark:text-slate-400 flex items-center gap-1"><i class="fas fa-compass text-primary-500"></i> 推荐 SOTA 示例：</span>
<a href="https://distill.pub/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-primary-100 hover:bg-primary-50 dark:bg-primary-900/30 hover:text-primary-700">
<i class="fas fa-file-alt text-[10px]"></i><span>Distill.pub（交互式论文）</span>
</a>
<a href="https://observablehq.com/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-primary-100 hover:bg-primary-50 dark:bg-primary-900/30 hover:text-primary-700">
<i class="fas fa-chart-line text-[10px]"></i><span>Observable（交互数据笔记本）</span>
</a>
</div>

<div class="grid md:grid-cols-2 gap-8 mb-8">
<div>
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide">操作步骤</h4>
<ol class="space-y-3 text-sm text-slate-600 dark:text-slate-400">
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">1</span>
<span>打开论文网页（HTML版），右键点击空白处，选择<strong>“查看网页源代码”</strong> (View Source)。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">2</span>
<span>按 <code>Ctrl+A</code> 全选，<code>Ctrl+C</code> 复制。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">3</span>
<span>打开 Gemini/ChatGPT，输入右侧的 Prompt。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">4</span>
<span>等待 AI 回复“请粘贴代码”后，粘贴你复制的源码。</span>
</li>
</ol>
</div>
<div class="flex flex-col">
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide flex justify-between items-center">
AI Prompt (直接复制)
<button class="text-primary-600 hover:text-primary-800 text-xs font-normal" onclick="copyToClipboard('prompt-3-1')"><i class="fas fa-copy mr-1"></i> Copy</button>
</h4>
<div class="bg-slate-800 p-4 rounded-lg text-xs font-mono text-green-400 overflow-x-auto flex-grow leading-relaxed" id="prompt-3-1">
你是一名资深的前端工程师和生物医学专家。
任务：请将我提供的论文 HTML 源码重构为一个单文件 HTML。
要求：
1. **排版**：使用 Tailwind CSS，风格为学术极简，大字体，护眼背景色。
2. **交互目录**：在左侧生成悬浮目录 (TOC)，点击可跳转。
3. **图文对照**：识别源码中的 `&lt;img&gt;` 标签，保留原图链接。将 Figure 图片移动到正文引用处（如 "Fig 1"）的侧边，实现图文并茂。
4. **术语解释**：识别文中 5 个关键医学缩写（如肿瘤标志物、基因名），为其添加鼠标悬停显示的 Tooltip 解释。
请先回复“准备好了，请粘贴 HTML 源码”，我再发送代码。
</div>
</div>
</div>

<!-- Live Demo 3.1 -->
<div class="mt-6 demo-browser-mockup bg-white dark:bg-gray-800 shadow-lg border border-slate-200 dark:border-slate-700">
<div class="p-6 border-b border-slate-100">
<div class="flex items-center gap-2 text-xs text-slate-400 font-bold uppercase tracking-widest mb-2">
<span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span> 效果预览
</div>
<h4 class="font-serif text-xl text-slate-800 font-bold mb-2">免疫检查点阻断（示例）</h4>
<p class="font-serif text-lg leading-relaxed text-slate-600 dark:text-slate-400">
近期研究显示，<span class="cursor-help border-b-2 border-dotted border-primary-500 relative group text-primary-700 font-medium">
PD-1
<span class="invisible group-hover:visible opacity-0 group-hover:opacity-100 transition-all duration-200 absolute bottom-full left-1/2 -translate-x-1/2 bg-slate-800 text-white text-xs p-3 rounded-lg w-64 mb-2 z-10 shadow-xl text-left leading-snug">
<strong>程序性死亡受体 1</strong><br>
肿瘤细胞通过与 T 细胞上的 PD-1 结合来逃避免疫系统的攻击。
<svg class="absolute text-slate-800 h-2 w-full left-0 top-full" x="0px" y="0px" viewBox="0 0 255 255"><polygon class="fill-current" points="0,0 127.5,127.5 255,0"/></svg>
</span>
</span> 抑制剂可以重新激活耗竭的 T 细胞，显著改善转移性黑色素瘤的预后。点击 
<button onclick="toggleModal()" class="text-primary-600 font-bold hover:underline bg-primary-50 dark:bg-primary-900/30 px-1 rounded">图 1</button> 查看示意。
</p>
</div>

<!-- Fake Modal -->
<div id="fig1-modal" class="hidden absolute inset-0 bg-white dark:bg-gray-800/95 backdrop-blur flex items-center justify-center z-20 p-4 transition-opacity">
<div class="text-center max-w-sm">
<div class="bg-slate-100 rounded-lg p-8 mb-4 border-2 border-dashed border-slate-300">
<i class="fas fa-image text-4xl text-slate-300 mb-2"></i>
<p class="text-slate-400 font-bold">示意图占位</p>
</div>
<p class="text-sm text-slate-600 dark:text-slate-400 font-medium">图 1：阻断 PD-1 信号可恢复肿瘤微环境中 T 细胞功能。</p>
<button onclick="toggleModal()" class="mt-4 px-4 py-2 bg-slate-800 text-white rounded-lg text-sm hover:bg-slate-700 transition-colors">关闭</button>
</div>
</div>
</div>

<!-- Bonus: Gemini Tool -->
<div class="glass-card p-8 rounded-2xl mt-8 border-l-4 border-purple-500 relative overflow-hidden">
<div class="absolute -right-10 -top-10 w-40 h-40 bg-purple-100 rounded-full blur-3xl -z-10"></div>
<h3 class="text-xl font-bold text-slate-900 dark:text-slate-100 mb-2 flex items-center gap-2">
<i class="fas fa-magic text-purple-500"></i>
✨ Bonus: Gemini 驱动的学术翻译官
</h3>
<p class="text-sm text-slate-600 dark:text-slate-400 mb-4">
不确定某段文字的含义？粘贴在这里，让 Gemini 为你生成通俗易懂的中文解释。
</p>
<textarea id="gemini-input" class="w-full p-4 rounded-xl bg-white dark:bg-gray-800/50 border border-slate-200 dark:border-slate-700 text-sm font-serif mb-4 focus:ring-2 focus:ring-purple-500 outline-none transition-all" rows="4" placeholder="在此粘贴晦涩的英文学术摘要..."></textarea>
<button onclick="callGemini()" class="px-6 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-lg font-medium transition-colors flex items-center gap-2 shadow-lg shadow-purple-500/20">
<i class="fas fa-sparkles"></i> 一键降维解读
</button>
<div id="gemini-output" class="mt-6 hidden">
<div class="p-4 bg-purple-50 rounded-xl border border-purple-100 text-slate-700 dark:text-slate-300 text-sm leading-relaxed"></div>
</div>
<div id="gemini-loading" class="mt-6 hidden">
<div class="flex items-center gap-2 text-purple-500 text-sm font-medium animate-pulse">
<i class="fas fa-circle-notch fa-spin"></i> 正在解析逻辑...
</div>
</div>
</div>

<!-- 3.1 Prompt 选型与结构拆解 -->
<div class="mt-8 grid md:grid-cols-3 gap-4 text-xs text-slate-600 dark:text-slate-400">
<div class="bg-white dark:bg-gray-800/80 border border-slate-100 rounded-xl p-4">
<h4 class="font-bold text-slate-800 mb-2 flex items-center gap-2 text-sm">
<span class="w-1.5 h-4 bg-primary-50 dark:bg-primary-900/300 rounded-full"></span>
不同任务选哪个 Prompt？
</h4>
<ul class="space-y-1.5">
<li>· <span class="font-semibold text-slate-800">基础排版</span>（单篇论文重排、首尝试）：使用「1. AI 论文网页化 Prompt (基础版)」。</li>
<li>· <span class="font-semibold text-slate-800">深入重构</span>（需要目录、术语工具提示、图文并茂）：使用「2. 文献重构改进版 (主要使用)」或「13. 文献重构——改进」。</li>
<li>· <span class="font-semibold text-slate-800">科普/公众号改写</span>：使用「23. 文献重构（公众号）」或「24. AI文章重构」。</li>
<li>· <span class="font-semibold text-slate-800">Gemini 专用版本</span>：使用「22. 文献重构(gemeni3版本)」。</li>
</ul>
</div>

<div class="bg-white dark:bg-gray-800/80 border border-slate-100 rounded-xl p-4">
<h4 class="font-bold text-slate-800 mb-2 flex items-center gap-2 text-sm">
<span class="w-1.5 h-4 bg-emerald-500 rounded-full"></span>
一键直达 Notion 里的 Prompt
</h4>
<p class="mb-2">以下链接会在新标签打开对应行，方便复制与二次修改：</p>
<div class="space-y-1.5">
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-80a8-9123-eea881d6e654" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-primary-50 dark:bg-primary-900/30 text-primary-700 hover:bg-primary-100">
<i class="fas fa-link text-[10px]"></i>
<span>1. 基础版 · 论文网页化</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-80f5-90ba-d7ff952bd71c" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>2. 文献重构改进版（主要使用）</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2a66ff12-2f6b-8051-be51-da86b0e4b598" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>13. 文献重构——改进</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2b36ff12-2f6b-802f-87c3-e7fd0f3e3909" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>23. 文献重构（公众号）</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2b76ff12-2f6b-809f-a21e-ec7922db6063" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>24. AI文章重构</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2b26ff12-2f6b-8095-937a-e97cff0bd133" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-link text-[10px]"></i>
<span>22. 文献重构（Gemini 3 版本）</span>
</a>
</div>
</div>

<div class="bg-slate-900 text-slate-50 rounded-xl p-4">
<h4 class="font-bold mb-2 flex items-center gap-2 text-sm">
<span class="w-1.5 h-4 bg-amber-400 rounded-full"></span>
Prompt 解剖：文献重构类的共同结构
</h4>
<ol class="space-y-1.5 list-decimal list-inside text-[11px] leading-relaxed">
<li><span class="font-semibold text-white">系统角色设定</span>：如“前端工程师 + 医学专家”，确保 AI 既懂排版又懂领域知识。</li>
<li><span class="font-semibold text-white">输入说明</span>：告诉 AI 将收到的是 HTML 源码、Markdown 文本还是纯文本段落。</li>
<li><span class="font-semibold text-white">输出结构</span>：明确需要「单文件 HTML」「TOC 目录」「图文对照」「术语 Tooltip」等模块。</li>
<li><span class="font-semibold text-white">约束与安全</span>：强调不要虚构数据、不要改动图表原意，只做重排与解释补充。</li>
<li><span class="font-semibold text-white">交互与风格</span>：指定字体、配色、留白、是否适配移动端，形成可复用的“视觉模板”。</li>
</ol>
</div>
</div>
</div>

### 3.2 演示的重构：从静态 PPT 到交互式 Slides

<div class="glass-card p-8 rounded-2xl relative overflow-hidden">
<div class="absolute top-0 right-0 w-24 h-24 bg-orange-50 rounded-bl-full -z-10"></div>

<div class="bg-orange-50 rounded-lg p-5 mb-6 text-sm text-orange-800 leading-relaxed">
<strong>核心思路</strong>：传统 PPT 汇报往往存在几个痛点：文件体积大、版本混乱（final_v3_real_final.pptx）、动画效果无法跨平台复现，还不便于嵌入可交互图表。<br>
基于 <strong>Reveal.js</strong> 的 HTML 幻灯片，本质上是一个网页：一份 <code>index.html</code> 就可以在任何现代浏览器中播放，不依赖特定软件，更适合通过 Git / 网盘长期保存和共享。<br>
在这个模式下，你只需要用文字给 AI 提供<strong>大纲 + 关键内容模块</strong>（比如“代码示例”“交互式结果图”等），AI 就能自动写出包含切换动画、代码高亮、Plotly 图表占位符的完整演示文稿。<br>
对于 Journal Club 或组会，这意味着你可以从“修 PPT 的美工工作”中解放出来，把时间真正花在梳理逻辑和筛选重点图表上，同时又能获得更现代、更适合线上分享的展示效果。
</div>

<div class="grid md:grid-cols-2 gap-8 mb-8">
<div>
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide">操作步骤</h4>
<ol class="space-y-3 text-sm text-slate-600 dark:text-slate-400">
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">1</span>
<span>准备好你的汇报大纲（简单的 Markdown 列表）。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">2</span>
<span>发送右侧 Prompt 给 AI。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">3</span>
<span>将 AI 生成的代码保存为 <code>presentation.html</code>。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">4</span>
<span>双击打开，按空格键翻页。</span>
</li>
</ol>
</div>
<div class="flex flex-col">
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide flex justify-between items-center">
AI Prompt (直接复制)
<button class="text-primary-600 hover:text-primary-800 text-xs font-normal" onclick="copyToClipboard('prompt-3-2')"><i class="fas fa-copy mr-1"></i> Copy</button>
</h4>
<div class="bg-slate-800 p-4 rounded-lg text-xs font-mono text-green-400 overflow-x-auto flex-grow leading-relaxed" id="prompt-3-2">
我需要做一个学术汇报（Journal Club）。
请基于 Reveal.js 框架，为我生成一个单文件 HTML 演示文稿。
主题：[在此填入主题，如：单细胞测序在肺癌中的应用]
大纲内容：
1. [背景：...]
2. [方法：...]
3. [结果：...]
要求：
- 使用 'white' 主题。
- 在“方法”部分，请嵌入一段 Python 代码示例，并启用语法高亮。
- 在“结果”部分，请预留一个可交互的柱状图位置（使用 Plotly.js）。
- 确保所有 JS/CSS 均通过 CDN 引入，无需本地下载。
</div>
</div>
</div>

<div class="mt-4 mb-10 text-xs text-slate-500 dark:text-slate-400 flex flex-wrap gap-3 items-center">
<span class="font-semibold text-slate-600 dark:text-slate-400 flex items-center gap-1"><i class="fas fa-compass text-primary-500"></i> 推荐 SOTA 工具：</span>
<a href="https://revealjs.com/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fas fa-laptop text-[10px]"></i><span>Reveal.js 官方文档</span>
</a>
<a href="https://marp.app/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fas fa-sliders-h text-[10px]"></i><span>Marp（Markdown 幻灯片）</span>
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
实战练习：让 AI 帮你“读代码”
</h3>
<div class="grid md:grid-cols-2 gap-6 text-sm text-slate-600 dark:text-slate-400">
<div class="space-y-3">
<p>在本讲义中，你已经看到了多个 HTML + JS 小应用（如 Reveal 幻灯片、GCS 计算器）。建议同学们<strong>反向利用这些示例</strong>，用专门的「代码阅读 Prompt」请 AI 把代码翻译成人类友好的教程。</p>
<ol class="space-y-2 text-xs md:text-sm">
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-[11px]">1</span>
<span>从本讲义或自己项目中，复制一段前端代码（组件 / 小工具均可）。</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-[11px]">2</span>
<span>在 AI 工具中先发送「代码阅读类 Prompt」，等待它回复“请粘贴代码”。</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-[11px]">3</span>
<span>粘贴代码，要求 AI 按「模块划分 / 数据流 / 交互逻辑」三个维度解释，并给出可以直接改造的建议。</span>
</li>
</ol>
</div>
<div class="space-y-3 text-xs md:text-sm">
<div>
<h4 class="font-bold text-slate-800 mb-2 text-sm flex items-center gap-2">
<span class="w-1.5 h-4 bg-sky-500 rounded-full"></span>
推荐使用的代码相关 Prompt
</h4>
<div class="space-y-1.5">
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-805e-804a-eb6c5d2d74af" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-900 text-slate-50 hover:bg-slate-800">
<i class="fas fa-book-open text-[10px]"></i>
<span>7. 新版——代码阅读</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-8040-9c27-efb436a50a4a" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-book-open text-[10px]"></i>
<span>4. 代码解读生成 Prompt</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-80cf-94ec-caaa3a28bb24" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-robot text-[10px]"></i>
<span>3. AI 研究工程师 Coding Prompt</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2786ff12-2f6b-805f-8234-e85c775fdd78" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-laptop-code text-[10px]"></i>
<span>12. 前端工程师</span>
</a>
</div>
</div>
<p class="text-[11px] text-slate-500 dark:text-slate-400 leading-relaxed">建议：先用「代码阅读类 Prompt」理解现有 demo，再用「前端工程师 / AI 研究工程师」Prompt 让 AI 帮你从零生成一个属于自己的小工具（如新的评分量表、实验记录器等）。</p>
</div>
</div>
</div>

### 3.3 概念的重构：从静态图示到动态模型

<div class="glass-card p-8 rounded-2xl relative overflow-hidden">
<div class="absolute top-0 right-0 w-24 h-24 bg-emerald-50 rounded-bl-full -z-10"></div>

<div class="bg-emerald-50 rounded-lg p-5 mb-6 text-sm text-emerald-800 leading-relaxed">
<strong>核心思路</strong>：在科研训练中，我们经常需要画“流程图”“信号通路图”或“诊断决策树”。用 PowerPoint 或手动画图，不仅费时费力，而且一旦修改实验流程，整张图几乎等于推倒重来。<br>
<strong>Mermaid.js</strong> 提供了一种“用文字画图”的思路：你只需要用接近自然语言的方式描述节点和箭头关系（谁指向谁、在哪个阶段发生分支），AI 就可以帮你生成标准的 Mermaid 代码，浏览器再把它渲染成矢量图。<br>
好处在于，这张图的“真相”不在图片里，而在背后的文本逻辑中：当你的实验流程调整时，只需修改几行文字，图像随之自动更新，不再依赖手工对齐和排版。<br>
对于复杂概念（如多步信号转导、临床分层路径等），这种“文字即模型”的方式尤其适合在组会或课堂上快速迭代和讨论。
</div>

<div class="mb-6 text-xs text-slate-500 dark:text-slate-400 flex flex-wrap gap-3 items-center">
<span class="font-semibold text-slate-600 dark:text-slate-400 flex items-center gap-1"><i class="fas fa-compass text-emerald-500"></i> 推荐 SOTA 资源：</span>
<a href="https://mermaid.js.org/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-emerald-100 hover:bg-emerald-50 hover:text-emerald-700">
<i class="fas fa-project-diagram text-[10px]"></i><span>Mermaid.js 官方文档</span>
</a>
<a href="https://mermaid.live/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-emerald-100 hover:bg-emerald-50 hover:text-emerald-700">
<i class="fas fa-pen-nib text-[10px]"></i><span>Mermaid Live Editor</span>
</a>
</div>

<div class="grid md:grid-cols-2 gap-8 mb-8">
<div>
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide">操作步骤</h4>
<ol class="space-y-3 text-sm text-slate-600 dark:text-slate-400">
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">1</span>
<span>梳理你要展示的逻辑（如信号通路、诊断流程）。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">2</span>
<span>发送 Prompt 给 AI。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">3</span>
<span>AI 会生成一段 HTML，其中包含 Mermaid 代码。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">4</span>
<span>打开 HTML，图表自动绘制。修改逻辑只需改文字，无需重画。</span>
</li>
</ol>
</div>
<div class="flex flex-col">
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide flex justify-between items-center">
AI Prompt (直接复制)
<button class="text-primary-600 hover:text-primary-800 text-xs font-normal" onclick="copyToClipboard('prompt-3-3')"><i class="fas fa-copy mr-1"></i> Copy</button>
</h4>
<div class="bg-slate-800 p-4 rounded-lg text-xs font-mono text-green-400 overflow-x-auto flex-grow leading-relaxed" id="prompt-3-3">
请帮我生成一个单文件 HTML，使用 Mermaid.js 绘制一个流程图。
逻辑内容：[Wet Lab: 样本采集 -> RNA提取 -> 质控 -> 建库测序] -> [Dry Lab: 序列比对 -> 差异表达分析 -> 通路富集]
要求：
1. 引入 mermaid.min.js CDN。
2. 图表样式美观，节点使用圆角矩形。
3. 区分 'Wet Lab' 和 'Dry Lab' 两个 Subgraph（子图），并填充不同颜色。
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
subgraph Wet_Lab ["🧪 湿实验室：样本制备"]
A[样本采集] --> B[裂解细胞]
B --> C[RNA 提取]
C --> D{"质控：RIN > 7 ?"}
D -- 否 --> E[丢弃样本]
D -- 是 --> F[建库]
F --> G["测序 (Illumina)"]
end

subgraph Dry_Lab ["💻 干实验室：生信分析"]
G --> H["原始序列 (FASTQ)"]
H --> I["质量评估 (FastQC)"]
I --> J["比对 (STAR/HISAT2)"]
J --> K[计数矩阵]
K --> L["差异表达 (DESeq2)"]
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

### 3.4 逻辑的重构：从被动查询到专属工具定制

<div class="glass-card p-8 rounded-2xl relative overflow-hidden border border-slate-100 shadow-xl shadow-slate-200/40">
<div class="absolute top-0 right-0 w-24 h-24 bg-indigo-50 rounded-bl-full -z-10"></div>

<div class="bg-indigo-50 rounded-lg p-5 mb-6 text-sm text-indigo-800 leading-relaxed">
<strong>核心思路</strong>：在临床和科研中，我们每天都在做各种“如果…则…”的判断：评分量表（GCS、CHA<sub>2</sub>DS<sub>2</sub>-VASc）、分期分级、用药剂量调整等。传统做法要么是纸质表格，要么是在脑中硬记规则，既容易出错，也不便于团队共享。<br>
通过 <strong>Vue.js</strong> 这样的响应式框架，我们可以让 AI 帮忙把这些规则“固化”为一个个小工具：输入选项一变，分数和风险提示就自动更新；当总分超过某个阈值时，界面背景变红、弹出提醒。<br>
更重要的是，这些小工具都是<strong>单文件 HTML</strong>，可以离线保存到手机或平板，在查房、门诊或会议现场随时打开使用；规则更新时，只需修改一处逻辑，所有人都能立即获得同一版本的决策支持。<br>
长远来看，这种方式帮助每位医生和科研人员，逐步沉淀出一套“专属于自己课题/学科”的微型工具库，而不仅仅是零散的截图和笔记。
</div>

<div class="mb-6 text-xs text-slate-500 dark:text-slate-400 flex flex-wrap gap-3 items-center">
<span class="font-semibold text-slate-600 dark:text-slate-400 flex items-center gap-1"><i class="fas fa-compass text-indigo-500"></i> 推荐 SOTA 生态：</span>
<a href="https://vuejs.org/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fab fa-vuejs text-[10px]"></i><span>Vue.js 官方文档</span>
</a>
<a href="https://vuetifyjs.com/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fas fa-layer-group text-[10px]"></i><span>Vuetify（Material 组件库）</span>
</a>
<a href="https://mdcalc.com/" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-white dark:bg-gray-800 border border-indigo-100 hover:bg-indigo-50 hover:text-indigo-700">
<i class="fas fa-stethoscope text-[10px]"></i><span>MDCalc（临床评分工具参考）</span>
</a>
</div>

<div class="grid md:grid-cols-2 gap-8 mb-8">
<div>
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide">操作步骤</h4>
<ol class="space-y-3 text-sm text-slate-600 dark:text-slate-400">
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">1</span>
<span>明确你的计算逻辑（如：A+B=C，如果 C>10 则报警）。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">2</span>
<span>发送 Prompt 给 AI。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">3</span>
<span>AI 会生成包含计算逻辑的单文件 HTML。</span>
</li>
<li class="flex gap-3">
<span class="flex-shrink-0 w-6 h-6 rounded-full bg-slate-200 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold text-xs">4</span>
<span>保存到手机或电脑，随时离线使用。</span>
</li>
</ol>
</div>
<div class="flex flex-col">
<h4 class="font-bold text-slate-700 dark:text-slate-300 mb-3 text-sm uppercase tracking-wide flex justify-between items-center">
AI Prompt (直接复制)
<button class="text-primary-600 hover:text-primary-800 text-xs font-normal" onclick="copyToClipboard('prompt-3-4')"><i class="fas fa-copy mr-1"></i> Copy</button>
</h4>
<div class="bg-slate-800 p-4 rounded-lg text-xs font-mono text-green-400 overflow-x-auto flex-grow leading-relaxed" id="prompt-3-4">
你是一名资深前端工程师。请为我生成一个单文件 HTML 小程序。
功能：GCS (格拉斯哥昏迷评分) 计算器。
逻辑：
- 睁眼反应 (4分)、语言反应 (5分)、运动反应 (6分)。
- 总分 = 三项之和。
界面要求：
- 使用 Vue.js (CDN) 实现响应式逻辑。
- 界面风格模仿 iOS，大按钮，适合触屏。
- 视觉反馈：当总分 <= 8 时，结果区域背景变红，并显示文字“提示：需气管插管”。
</div>
</div>
</div>

<!-- Live Demo 3.4 -->
<div class="mt-8 max-w-xs mx-auto bg-white dark:bg-gray-800 rounded-3xl shadow-2xl border border-slate-100 overflow-hidden transform transition-transform hover:scale-105">
<!-- Header -->
<div class="bg-slate-50 dark:bg-slate-900 p-4 border-b border-slate-100 flex justify-between items-center">
<div class="text-xs font-bold text-slate-400">9:41</div>
<div class="text-sm font-bold text-slate-800">GCS 计算器</div>
<div class="flex gap-1">
<div class="w-4 h-2 bg-slate-300 rounded-sm"></div>
<div class="w-1 h-2 bg-slate-300 rounded-sm"></div>
</div>
</div>

<!-- App Body -->
<div class="p-5 space-y-4">
<div>
<label class="text-xs font-bold text-slate-400 uppercase mb-1 block">睁眼反应</label>
<select id="eye" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-sm outline-none focus:border-indigo-500" onchange="calcGCS()">
<option value="4">4 - 自主</option>
<option value="3">3 - 呼唤</option>
<option value="2">2 - 疼痛</option>
<option value="1">1 - 无反应</option>
</select>
</div>
<div>
<label class="text-xs font-bold text-slate-400 uppercase mb-1 block">语言反应</label>
<select id="verbal" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-sm outline-none focus:border-indigo-500" onchange="calcGCS()">
<option value="5">5 - 定向</option>
<option value="4">4 - 迷惑</option>
<option value="3">3 - 不当言语</option>
<option value="2">2 - 模糊声</option>
<option value="1">1 - 无反应</option>
</select>
</div>
<div>
<label class="text-xs font-bold text-slate-400 uppercase mb-1 block">运动反应</label>
<select id="motor" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-sm outline-none focus:border-indigo-500" onchange="calcGCS()">
<option value="6">6 - 遵嘱</option>
<option value="5">5 - 定位痛</option>
<option value="4">4 - 回缩</option>
<option value="3">3 - 弯曲</option>
<option value="2">2 - 伸展</option>
<option value="1">1 - 无反应</option>
</select>
</div>

<!-- Result -->
<div id="gcs-result-box" class="mt-6 p-4 rounded-xl bg-emerald-100 text-emerald-900 transition-all duration-300">
<div class="text-center">
<span class="text-xs font-bold opacity-60 uppercase">总分</span>
<div class="text-4xl font-bold my-1" id="gcs-score">15</div>
<div class="text-xs font-bold" id="gcs-status">正常</div>
</div>
</div>
</div>
</div>
</div>

### 3.5 知识的重构：从教材到多步知识卡片流水线

<div class="glass-card p-8 rounded-2xl relative overflow-hidden border border-emerald-100 shadow-xl shadow-emerald-100/40">
<div class="absolute top-0 right-0 w-24 h-24 bg-emerald-50 rounded-bl-full -z-10"></div>

<div class="grid md:grid-cols-2 gap-8 items-start">
<div class="space-y-4 text-sm text-slate-600 dark:text-slate-400">
<div class="bg-emerald-50 rounded-lg p-5 leading-relaxed">
<strong>核心思路</strong>：与其一遍遍从头读厚厚的教材，不如把知识拆成可复习、可追踪的「闭合卡片」。借助一组互相衔接的 Prompt，我们可以做一条流水线：<br>
<span class="font-mono text-emerald-700 text-xs md:text-sm">书籍图片 / PDF → Markdown 文本 → 结构化知识提炼 → ANKI / USMLE 知识卡片</span><br>
每一步都由专门的 System Prompt 接手，既减少机械重复，又尽量保留原文的严谨性。
</div>
<h4 class="font-bold text-slate-800 text-sm uppercase tracking-wide">操作步骤（建议 workflow）</h4>
<ol class="space-y-2 text-xs md:text-sm">
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-[11px]">1</span>
<span>使用 <strong>20. 书籍图像转化为markdown</strong>：将教材扫描页或题库截图转为干净的 Markdown 文本。</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-[11px]">2</span>
<span>使用 <strong>文献重构类 Prompt</strong>（如「2. 文献重构改进版」「13. 文献重构——改进」）整理结构：提炼章节层级、标出重点与高频考点。</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-[11px]">3</span>
<span>把整理后的内容交给 <strong>USMLE / ANKI 系列 Prompt</strong>（5 / 6 / 8 / 21 / 17-19），生成分层的闭合卡片 JSON 或直接可导入的文本。</span>
</li>
<li class="flex gap-2">
<span class="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-[11px]">4</span>
<span>用 <strong>10. USMLE导师</strong> 或其他「导师类 Prompt」定期抽查这些卡片：生成周度复习计划、模拟口试问答。</span>
</li>
</ol>
</div>

<div class="space-y-4 text-xs md:text-sm">
<div>
<h4 class="font-bold text-slate-800 mb-2 text-sm flex items-center gap-2">
<span class="w-1.5 h-4 bg-emerald-500 rounded-full"></span>
推荐使用的 Prompt 组合（可点击打开）
</h4>
<div class="space-y-1.5">
<a href="https://rune-gem-5ee.notion.site/2aa6ff12-2f6b-80ec-9102-fcd34f7a01eb" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-emerald-50 text-emerald-800 hover:bg-emerald-100">
<i class="fas fa-image text-[10px]"></i>
<span>20. 书籍图像转化为markdown</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2716ff12-2f6b-80f5-90ba-d7ff952bd71c" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-file-alt text-[10px]"></i>
<span>2. 文献重构改进版 (主要使用)</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2a36ff12-2f6b-800d-a8c3-ca88e40f0ba3" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-sitemap text-[10px]"></i>
<span>17-19. ANKI 进一步优化系列</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2ab6ff12-2f6b-80a1-bed8-fd6e2b323d3d" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-900 text-slate-50 hover:bg-slate-800">
<i class="fas fa-clone text-[10px]"></i>
<span>21. ANKI_USMLE_精华版（正式使用）</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2786ff12-2f6b-802a-a819-fbe5bd3da611" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-microchip text-[10px]"></i>
<span>11. ANKI工程师</span>
</a>
<a href="https://rune-gem-5ee.notion.site/2776ff12-2f6b-80a7-b738-c4021ccd8a1c" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100">
<i class="fas fa-user-graduate text-[10px]"></i>
<span>10. USMLE导师</span>
</a>
</div>
</div>

<!-- Mini Anki Card Demo -->
<div class="mt-4 bg-slate-900 text-slate-50 rounded-xl p-4">
<div class="flex items-center justify-between mb-2 text-[11px] uppercase tracking-wide text-slate-400">
<span>ANKI Preview</span>
<button onclick="toggleAnkiDemo()" class="px-2 py-1 rounded bg-slate-800 text-[11px] hover:bg-slate-700">
<span id="anki-toggle-label">显示答案</span>
</button>
</div>
<div class="border border-slate-700 rounded-lg p-3 text-xs leading-relaxed">
<div id="anki-front">
<span class="font-semibold text-emerald-300">Q.</span>
一名 24 岁男性因高热、咳嗽入院，考虑细菌性肺炎。请列出经验性静脉抗生素选择时需要优先考虑的三个要素。
</div>
<div id="anki-back" class="hidden">
<span class="font-semibold text-emerald-300">A.</span>
① 覆盖常见病原体谱（如肺炎链球菌、流感嗜血杆菌等)；<br>
② 结合本院耐药监测数据与当地流行病学；<br>
③ 根据患者肾功能、过敏史等个体情况调整剂量与具体药物。
</div>
</div>
<p class="mt-2 text-[10px] text-slate-400">提示：用上面的 ANKI/USMLE Prompt，可以把整章节内容批量转化为类似风格的闭合卡片。</p>
</div>
</div>
</div>
</div>
</div>

## 附录：我的 Prompt 仓库（AI Studio）

<div class="not-prose glass-card rounded-2xl p-6">
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch">
    <div class="prose prose-slate max-w-none text-sm">
      <p>下方小窗口实时引用我在 Notion 中维护的 <strong>Prompts List</strong> 表格，用来集中存放本课程中用到的 System Prompt 和场景 Prompt。</p>
      <ul class="text-sm text-slate-600 dark:text-slate-400 list-disc pl-5 space-y-1">
        <li><span class="font-medium">html / code / knowledge / agent</span> 等标签，对应讲义中的主线：文献重构、代码阅读、知识卡片（USMLE / ANKI）、以及多步骤智能体。</li>
        <li>阅读讲义时，可以在表格中按标签筛选，并把适合自己的 Prompt 复制到 AI 工具中反复打磨。</li>
        <li>讲义后续新增案例时，只需在 Notion 中补充行，即可自动出现在这里，形成一个持续演化的 Prompt 库。</li>
      </ul>
      <div class="text-sm font-semibold text-slate-800 mt-4 flex items-center gap-2">
        <span class="inline-flex w-1.5 h-4 bg-slate-900 rounded-full"></span>
        建议配置的一组 “AI 团队”
      </div>
      <ul class="text-xs text-slate-600 dark:text-slate-400 list-disc pl-5 space-y-1">
        <li><strong>学术导师（长期陪跑）</strong>：<a href="https://rune-gem-5ee.notion.site/2736ff12-2f6b-80db-9ed9-d1cef1dd8b1e" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">9. AI教授指导</a>。</li>
        <li><strong>考试教练（USMLE/执业）</strong>：<a href="https://rune-gem-5ee.notion.site/2776ff12-2f6b-80a7-b738-c4021ccd8a1c" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">10. USMLE导师</a> + <a href="https://rune-gem-5ee.notion.site/2ab6ff12-2f6b-80a1-bed8-fd6e2b323d3d" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">21. ANKI_USMLE_精华版</a>。</li>
        <li><strong>前端工程师（可视化助手）</strong>：<a href="https://rune-gem-5ee.notion.site/2786ff12-2f6b-805f-8234-e85c775fdd78" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">12. 前端工程师</a>，把想法变成 HTML 小工具。</li>
        <li><strong>知识工程师（卡片工厂）</strong>：<a href="https://rune-gem-5ee.notion.site/2786ff12-2f6b-802a-a819-fbe5bd3da611" target="_blank" class="text-primary-600 hover:text-primary-800 underline-offset-2 hover:underline">11. ANKI工程师</a>，负责从文本批量生成结构化卡片。</li>
      </ul>
      <p class="mt-3 text-xs text-slate-500 dark:text-slate-400">提示：如果内嵌窗口因浏览器或网络设置无法加载，请点击右侧「在 Notion 中打开」按钮。</p>
    </div>
    <div class="relative">
      <div class="flex items-center justify-between mb-2 text-xs text-slate-500 dark:text-slate-400">
        <span class="inline-flex items-center gap-1">
          <i class="fas fa-table text-slate-400"></i>
          <span>Table · My Prompt For AI Studio</span>
        </span>
        <a href="https://rune-gem-5ee.notion.site/Table-My-Prompt-For-AI-Studio-2716ff122f6b806fae7dc5f95183fa25?pvs=74" target="_blank" class="inline-flex items-center gap-1 text-primary-600 hover:text-primary-800">
          <span>在 Notion 中打开</span>
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

## 结语：成为你知识产品的“首席产品经理”

回顾科学发展的历程，每一次工具的革新都带来了认知效率的飞跃。从手抄本到印刷术，从静态 PDF 到今天的交互式 HTML。在 AI 时代，**自然语言就是编程语言**。

<div class="not-prose inline-flex flex-col md:flex-row items-center gap-4 bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg border border-slate-100">
  <div class="flex items-center gap-2">
    <span class="w-8 h-8 rounded-full bg-slate-100 text-slate-600 dark:text-slate-400 flex items-center justify-center font-bold">1</span>
    <span class="font-bold text-slate-800">Ask (提问)</span>
  </div>
  <i class="fas fa-arrow-right text-slate-300 hidden md:block"></i>
  <i class="fas fa-arrow-down text-slate-300 md:hidden"></i>
  <div class="flex items-center gap-2">
    <span class="w-8 h-8 rounded-full bg-primary-100 text-primary-600 flex items-center justify-center font-bold">2</span>
    <span class="font-bold text-primary-700">Wrap (封装)</span>
  </div>
  <i class="fas fa-arrow-right text-slate-300 hidden md:block"></i>
  <i class="fas fa-arrow-down text-slate-300 md:hidden"></i>
  <div class="flex items-center gap-2">
    <span class="w-8 h-8 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center font-bold">3</span>
    <span class="font-bold text-emerald-700">View (浏览)</span>
  </div>
</div>

<p class="mt-12 text-xl font-bold text-primary-600 animate-pulse text-center">
欢迎来到科研可视化的新纪元。
</p>

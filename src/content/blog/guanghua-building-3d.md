---
title: "用一张照片，做一个可以在网页里转动的复旦光华楼"
description: "从单张参考照片估计建筑比例，用程序化几何重建光华楼，再把建模指令压缩后交给 Three.js / WebGL 在浏览器中重建，最后以内嵌 iframe 的方式部署到 Astro 博客。"
pubDate: 2026-09-05
---

前几天我想做一件很具体的小事：**把每天都很熟悉的复旦光华楼，从一张照片变成一个可以在浏览器里拖着转、放大缩小的 3D 模型。**

结果比我预想中有意思。它并不是“让 AI 把图片变成 3D”这么一句话就能概括，而更像一次很小的逆向工程：先读建筑的结构，再把结构写成参数化几何，最后才是 WebGL 渲染和网页部署。

先直接玩模型。鼠标拖动可以旋转，滚轮缩放；手机上可以单指旋转、双指缩放。

<div class="not-prose my-10">
  <div class="overflow-hidden rounded-2xl border border-slate-200 bg-slate-950 shadow-xl dark:border-slate-700">
    <iframe
      src="/interactive/guanghua-building.html"
      title="复旦大学光华楼可交互 3D 模型"
      loading="lazy"
      allow="fullscreen"
      allowfullscreen
      style="display:block;width:100%;height:min(72vh,720px);min-height:520px;border:0;"
    ></iframe>
  </div>
  <div class="mt-3 flex items-center justify-between gap-4 text-sm text-slate-500 dark:text-slate-400">
    <span>Photo-guided reconstruction · 非测绘 / BIM 模型</span>
    <a href="/interactive/guanghua-building.html" target="_blank" rel="noopener" class="font-medium text-indigo-600 hover:text-indigo-500 dark:text-indigo-400">单独全屏打开 ↗</a>
  </div>
</div>

## 第一步不是建模，而是把建筑拆开

单张照片不可能恢复一个建筑的真实三维信息。背面长什么样、楼体到底有多深、照片的焦距是多少，都没有唯一答案。所以这里做的不是测绘，而是 **photo-guided reconstruction：尽量让可见部分、比例关系和整体轮廓与参考照片一致，照片看不到的部分做合理补全。**

我先把照片里的东西拆成几个最重要的体块：低层裙房、左右两座塔楼、中间竖向大厅、半高处的连接体、塔顶格栅、入口台阶，以及只用于提供尺度感的树和前广场。

这一步比“细节做得多不多”重要得多。只要双塔宽高比、间距、裙房高度和中央连接体的位置错了，后面加再多窗户也不像光华楼。

## 第二步：用参数化几何，而不是手工一点点拉模型

模型主体是 Python 程序生成的。最基本的元素其实非常朴素：`box()`、`beam()`、`cylinder()` 和少量不规则树冠。建筑的大部分构件——墙体、石材立柱、玻璃窗、窗框、层间横梁——都可以归结为带位置和尺寸的长方体。

例如塔楼立面并不是贴一张“窗户纹理”，而是真的按楼层和开间循环生成窗、竖梃和横梁：

```python
for row in range(n_floors):
    z = z0 + row * floor_height
    for col in range(n_bays):
        x = tower_center - opening / 2 + (col + 0.5) * bay_width
        box("tower / glazing", glass_material,
            (x, facade_y, z + floor_height * 0.57),
            (bay_width - 0.11, 0.095, floor_height - 0.60))
```

这样做的好处是，一旦视角从正面转到斜侧，窗格、塔角石柱、塔顶结构仍然是真正的三维几何，而不是一张平面贴图露馅。

最终版本大约有 **115,832 个三角形、158,352 个顶点和 121 个命名对象**。对一个网页里的建筑小品来说已经足够细，但还没有重到必须做复杂的 LOD。

## 第三步：直接导出 GLB

建模脚本最后直接写出 glTF 2.0 的二进制格式 `.glb`。我把建模阶段使用的 Z-up 坐标转换为 glTF 常用的 Y-up 坐标，然后把 mesh、material、accessor 和 binary buffer 打包进一个文件。

这一步很关键，因为 **GLB 是浏览器 3D 展示非常合适的中间格式**：Blender 能导入，Three.js 能直接读取，文件又比 OBJ 这类“几何和材质分家”的格式好管理。

原始模型约 5.2 MB。最开始我做了一个完全离线的单文件 HTML：把 GLB、参考照片和渲染代码全部转成 Base64 塞进 HTML，所以那个文件大约 7.2 MB——优点是下载一个文件就能运行，缺点也很明显：放博客里太笨重。

## 第四步：博客版不直接传 5 MB 的三角形

原始 GLB 约 5.2 MB。它把最终三角形、法线和索引全部写死，适合 Blender 和通用 3D 软件，但对这个模型来说有一点浪费：建筑本来就是由大量重复的 box、beam、cylinder 生成的。

所以博客版换了一个思路：**不传“结果网格”，而传“建模指令”。** 我把生成器执行时的 5,206 条 primitive command 记录下来，例如：

```text
["b", material_id, center, size]       # box
["m", material_id, start, end, width] # beam
["c", material_id, start, end, radius]# cylinder
```

这份指令 JSON 原始约 560 KB，gzip 后只有大约 **56 KB**，再转成 Base64 也只有约 **75 KB**。HTML 打开后先解压 JSON，然后在浏览器里重新生成几何。建筑主体的 4,550 个 box 不是创建 4,550 次 draw call，而是按材质合并成 `InstancedMesh`。

核心逻辑类似这样：

```js
const DATA_URLS = [
  '/interactive/guanghua-data/gh_model_part_00.txt',
  '/interactive/guanghua-data/gh_model_part_01.txt',
  '/interactive/guanghua-data/gh_model_part_02.txt',
  '/interactive/guanghua-data/gh_model_part_03.txt',
];

const b64 = (await Promise.all(
  DATA_URLS.map(url => fetch(url).then(r => r.text()))
)).join('');

const raw = Uint8Array.from(atob(b64), c => c.charCodeAt(0));
const ds = new DecompressionStream('gzip');
const json = JSON.parse(new TextDecoder().decode(
  await new Response(new Blob([raw]).stream().pipeThrough(ds)).arrayBuffer()
));

const mesh = new THREE.InstancedMesh(unitCube, material, matrices.length);
matrices.forEach((matrix, i) => mesh.setMatrixAt(i, matrix));
scene.add(mesh);
```

这样最终的交互 viewer 只有大约 **88 KB**，而且建筑几何仍来自同一套参数化建模定义。树冠这类非关键景观在网页端换成了更轻量的实例化低多边形几何，换取更低的 draw call 和更稳定的手机性能。

之后就是常规 Three.js：`PerspectiveCamera` 负责透视相机，`OrbitControls` 负责拖拽 / 缩放，`HemisphereLight + DirectionalLight` 提供基础建筑光照，再加三个预设机位、自动旋转和夜景开关。

这里我刻意没有做复杂 UI。对博客来说，交互模型首先应该是文章内容，而不是一个独立的“3D 软件”。

## 第五步：在 Astro 文章里只放一个 iframe

真正嵌入博客反而是最简单的一步。把独立 viewer 放在 `public/interactive/guanghua-building.html`，压缩后的建模指令则拆成几个很小的静态数据分片，放在 `public/interactive/guanghua-data/` 下。这样部署时不需要再携带约 5.2 MB 的 GLB，文章里只写：

```html
<iframe
  src="/interactive/guanghua-building.html"
  title="复旦大学光华楼可交互 3D 模型"
  allow="fullscreen"
  style="width:100%;height:720px;border:0"
></iframe>
```

我比较喜欢这种结构，而不是把 Three.js 代码直接塞进文章页面。原因很简单：**文章和 3D 应用解耦。** 博客负责排版、SEO 和文字；viewer 自己负责 WebGL、输入事件和全屏。以后想换渲染器、换模型、甚至改成 WebGPU，都不用动文章系统。

## 现在这个模型还缺什么？

最大的限制不是渲染，而是输入信息。只有一张正面照片时，背面、进深和屋顶细节本质上都只能推断。如果以后真想把它做成更接近数字孪生的版本，我会优先增加侧面 / 背面照片、卫星图或平面尺寸，再考虑 PBR 材质、真实玻璃、环境贴图这些“锦上添花”的东西。

但作为一个从照片到参数化几何、再到浏览器实时渲染的小实验，我已经很满意它现在的形态：**它不是一张光华楼的图片，而是一个可以直接嵌进网页、让读者自己转动观察的空间对象。**

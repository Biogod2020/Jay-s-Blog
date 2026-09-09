# Markdown → 微信公众号草稿箱

这个仓库可以把 `src/content/blog/*.md` 作为唯一内容源，并自动把选中的 Markdown 文章同步到微信公众号草稿箱。

## 工作方式

流程是：

1. 读取 Astro Markdown front matter 和正文。
2. Markdown 转换为微信公众号可接受的内联样式 HTML。
3. 删除公众号正文不支持的 `script`、`iframe`、`video` 等交互元素。
4. 将正文图片上传到微信图文消息图片接口并替换 URL；SVG 会先自动栅格化为 PNG。
5. 将封面上传为永久图片素材，取得 `thumb_media_id`；SVG 封面同样自动转为 PNG。
6. 调用 `draft/add` 创建草稿。

博客现有的 GitHub Pages 部署 workflow 不受影响。

## 文章配置

普通博客文章仍然是 Markdown。需要自动同步到微信草稿箱时，在 front matter 增加：

```yaml
---
title: "示例标题"
description: "示例摘要"
pubDate: 2026-09-09
heroImage: "/images/example-cover.svg"
wechat:
  draft: true
  author: "复旦动物园"
  openComment: true
---
```

最少只需要：

```yaml
wechat:
  draft: true
```

封面选择顺序：

1. `wechat.cover`
2. `heroImage`
3. 正文第一张图片

可选字段：

```yaml
wechat:
  draft: true
  title: "公众号专用标题"
  author: "复旦动物园"
  digest: "公众号专用摘要"
  cover: "/images/wechat-cover.jpg"
  sourceUrl: "https://jiahaoblog.com/blog/example/"
  openComment: true
  onlyFansCanComment: false
```

## GitHub Secrets

不要把 AppSecret 写进 Markdown、Python、workflow 或任何 commit。

在仓库进入：

`Settings → Secrets and variables → Actions → New repository secret`

创建：

- `WECHAT_APP_ID`
- `WECHAT_APP_SECRET`

如果 AppSecret 曾经出现在聊天记录、日志或其他非密钥存储位置，建议先在微信公众平台重置，再把新值写入 GitHub Secret。

## 固定 IP / self-hosted runner

`.github/workflows/wechat-draft.yml` 默认使用：

```yaml
runs-on: [self-hosted, linux]
```

原因是微信 API 适合从固定公网出口 IP 的服务器调用。建议把一台 Linux 服务器注册为该仓库的 GitHub self-hosted runner，然后把服务器公网 IP 加入微信公众号后台的 API IP 白名单。

GitHub 中进入：

`Settings → Actions → Runners → New self-hosted runner`

按 GitHub 给出的命令在服务器上安装并启动 runner。

然后在微信公众号后台将这台服务器的公网出口 IP 加入 API IP 白名单。

SVG 转 PNG 使用 CairoSVG。如果你的精简 Linux 镜像没有 Cairo 运行库，在 Debian/Ubuntu 上安装：

```bash
sudo apt-get update
sudo apt-get install -y libcairo2
```

## 自动同步

当 `main` 分支的 `src/content/blog/**/*.md` 发生新增或修改时，workflow 会检查发生变化的文章。只有包含：

```yaml
wechat:
  draft: true
```

的文件会被发送到微信草稿箱。

注意：当前实现采用“创建新草稿”语义。如果同一篇文章再次修改并 push，会再生成一个新草稿，而不是覆盖旧草稿。这是有意设计，避免 CI 在没有可靠状态映射时误改公众号中人工编辑过的草稿。

## 手动重新生成某篇草稿

GitHub：

`Actions → Sync Markdown to WeChat Drafts → Run workflow`

输入例如：

```text
src/content/blog/compressed-modernity-medical-training.md
```

手动模式会强制生成草稿，不要求 `wechat.draft: true`。

## 当前支持范围

- Markdown 标题、段落、引用、列表、表格、代码块、链接
- Markdown 和普通 HTML `<img>` 图片
- 正文 JPG / PNG；SVG 自动转 PNG
- 封面 JPG / PNG / GIF；SVG 自动转 PNG
- 自动摘要
- 自动“阅读原文”链接到 `https://jiahaoblog.com/blog/<slug>/`

不会把博客里的 JavaScript、Mermaid 运行时、iframe、Three.js/WebGL 等互动组件直接复制到公众号正文。公众号版本会保留可静态表达的正文；复杂互动内容应通过“阅读原文”回到博客。

## 本地/服务器手动测试

```bash
python -m pip install -r scripts/wechat/requirements.txt
export WECHAT_APP_ID='...'
export WECHAT_APP_SECRET='...'
python scripts/wechat/publish.py --file src/content/blog/compressed-modernity-medical-training.md --force
```

成功时终端会打印微信返回的草稿 `media_id`。

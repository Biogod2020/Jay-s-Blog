#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import mimetypes
import os
import re
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import frontmatter
import markdown
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
API = "https://api.weixin.qq.com"
BLOG_BASE_URL = os.getenv("BLOG_BASE_URL", "https://jiahaoblog.com").rstrip("/")
AUTHOR_DEFAULT = os.getenv("WECHAT_AUTHOR", "复旦动物园")

TAG_STYLES = {
    "p": "margin:16px 0;line-height:1.9;font-size:16px;color:#222;letter-spacing:.02em;",
    "h1": "margin:34px 0 16px;font-size:24px;line-height:1.45;font-weight:700;color:#111;",
    "h2": "margin:32px 0 14px;font-size:21px;line-height:1.5;font-weight:700;color:#111;",
    "h3": "margin:28px 0 12px;font-size:18px;line-height:1.5;font-weight:700;color:#222;",
    "blockquote": "margin:20px 0;padding:12px 16px;border-left:3px solid #999;background:#f7f7f7;color:#555;line-height:1.8;",
    "pre": "margin:18px 0;padding:14px;overflow-x:auto;background:#f6f8fa;border-radius:8px;font-size:13px;line-height:1.6;white-space:pre-wrap;word-break:break-word;",
    "code": "font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:#f3f4f6;padding:2px 4px;border-radius:4px;",
    "img": "display:block;max-width:100%;height:auto;margin:20px auto;",
    "a": "color:#576b95;text-decoration:none;",
    "ul": "margin:14px 0;padding-left:1.4em;line-height:1.85;",
    "ol": "margin:14px 0;padding-left:1.4em;line-height:1.85;",
    "li": "margin:6px 0;",
    "table": "width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;",
    "th": "border:1px solid #ddd;padding:8px;background:#f6f6f6;text-align:left;",
    "td": "border:1px solid #ddd;padding:8px;vertical-align:top;",
    "hr": "border:0;border-top:1px solid #e5e5e5;margin:28px 0;",
}


def api_json(resp: requests.Response) -> dict:
    try:
        data = resp.json()
    except Exception as exc:
        raise RuntimeError(f"Non-JSON response from WeChat: HTTP {resp.status_code}") from exc
    if resp.status_code >= 400 or data.get("errcode", 0) not in (0, None):
        raise RuntimeError(f"WeChat API error: {data}")
    return data


def get_token(session: requests.Session) -> str:
    app_id = os.environ.get("WECHAT_APP_ID")
    secret = os.environ.get("WECHAT_APP_SECRET")
    if not app_id or not secret:
        raise RuntimeError("WECHAT_APP_ID and WECHAT_APP_SECRET must be set")
    resp = session.get(
        f"{API}/cgi-bin/token",
        params={"grant_type": "client_credential", "appid": app_id, "secret": secret},
        timeout=30,
    )
    return api_json(resp)["access_token"]


def guess_suffix(content_type: str | None, fallback: str = ".jpg") -> str:
    if content_type:
        suffix = mimetypes.guess_extension(content_type.split(";", 1)[0].strip())
        if suffix:
            return ".jpg" if suffix == ".jpe" else suffix
    return fallback


def materialize_image(ref: str, post_path: Path, session: requests.Session) -> tuple[Path, bool]:
    ref = ref.strip()
    if ref.startswith("data:image/"):
        header, payload = ref.split(",", 1)
        mime = header.split(";", 1)[0].split(":", 1)[1]
        raw = base64.b64decode(payload)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=guess_suffix(mime))
        tmp.write(raw)
        tmp.close()
        return Path(tmp.name), True

    if ref.startswith("http://") or ref.startswith("https://"):
        resp = session.get(ref, timeout=45)
        resp.raise_for_status()
        suffix = Path(urlparse(ref).path).suffix or guess_suffix(resp.headers.get("content-type"))
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix or ".jpg")
        tmp.write(resp.content)
        tmp.close()
        return Path(tmp.name), True

    if ref.startswith("/"):
        candidate = ROOT / "public" / ref.lstrip("/")
    else:
        candidate = (post_path.parent / ref).resolve()
        if not candidate.exists():
            candidate = (ROOT / "public" / ref).resolve()
    if not candidate.exists():
        raise FileNotFoundError(f"Image not found: {ref} (resolved to {candidate})")
    return candidate, False


def upload_body_image(token: str, image_ref: str, post_path: Path, session: requests.Session) -> str:
    path, temporary = materialize_image(image_ref, post_path, session)
    try:
        mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
        if mime not in {"image/jpeg", "image/png"}:
            raise RuntimeError(f"Body image must be JPG/PNG for WeChat uploadimg: {image_ref}")
        with path.open("rb") as fh:
            resp = session.post(
                f"{API}/cgi-bin/media/uploadimg",
                params={"access_token": token},
                files={"media": (path.name, fh, mime)},
                timeout=60,
            )
        return api_json(resp)["url"]
    finally:
        if temporary:
            path.unlink(missing_ok=True)


def upload_cover(token: str, image_ref: str, post_path: Path, session: requests.Session) -> str:
    path, temporary = materialize_image(image_ref, post_path, session)
    try:
        mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
        if mime not in {"image/jpeg", "image/png", "image/gif"}:
            raise RuntimeError(f"Cover must be JPG/PNG/GIF: {image_ref}")
        with path.open("rb") as fh:
            resp = session.post(
                f"{API}/cgi-bin/material/add_material",
                params={"access_token": token, "type": "image"},
                files={"media": (path.name, fh, mime)},
                timeout=60,
            )
        return api_json(resp)["media_id"]
    finally:
        if temporary:
            path.unlink(missing_ok=True)


def markdown_to_wechat_html(text: str) -> str:
    html = markdown.markdown(
        text,
        extensions=["extra", "sane_lists"],
        output_format="html5",
    )
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all(["script", "style", "iframe", "video", "audio", "canvas"]):
        tag.decompose()

    for tag_name, style in TAG_STYLES.items():
        for tag in soup.find_all(tag_name):
            existing = tag.get("style", "")
            tag["style"] = f"{style}{existing}"

    wrapper = soup.new_tag("section")
    wrapper["style"] = "max-width:100%;margin:0 auto;word-break:break-word;"
    for child in list(soup.contents):
        wrapper.append(child.extract())
    return str(wrapper)


def first_image_ref(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    img = soup.find("img", src=True)
    return img.get("src") if img else None


def rewrite_body_images(html: str, token: str, post_path: Path, session: requests.Session) -> str:
    soup = BeautifulSoup(html, "html.parser")
    cache: dict[str, str] = {}
    for img in soup.find_all("img", src=True):
        src = img["src"]
        if "mmbiz.qpic.cn" in src or "mmbiz.qlogo.cn" in src:
            continue
        if src not in cache:
            cache[src] = upload_body_image(token, src, post_path, session)
        img["src"] = cache[src]
    return str(soup)


def default_source_url(post_path: Path) -> str:
    slug = post_path.stem
    return f"{BLOG_BASE_URL}/blog/{slug}/"


def publish_one(post_path: Path, force: bool = False) -> str | None:
    post_path = post_path.resolve()
    if not post_path.exists():
        raise FileNotFoundError(post_path)

    post = frontmatter.load(post_path)
    cfg = post.metadata.get("wechat") or {}
    if not isinstance(cfg, dict):
        raise RuntimeError(f"wechat front matter must be an object: {post_path}")
    if not force and cfg.get("draft") is not True:
        print(f"skip {post_path}: wechat.draft is not true")
        return None

    title = str(cfg.get("title") or post.metadata.get("title") or "").strip()
    if not title:
        raise RuntimeError(f"Missing title: {post_path}")
    if len(title) > 64:
        raise RuntimeError(f"WeChat title is too long ({len(title)} > 64): {title}")

    author = str(cfg.get("author") or AUTHOR_DEFAULT).strip()
    if len(author) > 16:
        raise RuntimeError(f"WeChat author is too long ({len(author)} > 16): {author}")

    description = str(cfg.get("digest") or post.metadata.get("description") or "").strip()
    digest = re.sub(r"\s+", " ", description)[:120]

    raw_html = markdown_to_wechat_html(post.content)
    cover_ref = cfg.get("cover") or post.metadata.get("heroImage") or first_image_ref(raw_html)
    if not cover_ref:
        raise RuntimeError(
            f"No cover image for {post_path}. Add wechat.cover, heroImage, or at least one body image."
        )

    with requests.Session() as session:
        token = get_token(session)
        thumb_media_id = upload_cover(token, str(cover_ref), post_path, session)
        content = rewrite_body_images(raw_html, token, post_path, session)

        payload = {
            "articles": [
                {
                    "article_type": "news",
                    "title": title,
                    "author": author,
                    "digest": digest,
                    "content": content,
                    "content_source_url": str(cfg.get("sourceUrl") or default_source_url(post_path)),
                    "thumb_media_id": thumb_media_id,
                    "need_open_comment": 1 if cfg.get("openComment", True) else 0,
                    "only_fans_can_comment": 1 if cfg.get("onlyFansCanComment", False) else 0,
                }
            ]
        }
        resp = session.post(
            f"{API}/cgi-bin/draft/add",
            params={"access_token": token},
            json=payload,
            timeout=60,
        )
        data = api_json(resp)
        media_id = data["media_id"]
        print(f"created WeChat draft: {post_path.relative_to(ROOT)} -> {media_id}")
        return media_id


def changed_posts(base: str, head: str) -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AM", base, head, "--", "src/content/blog/*.md"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [ROOT / line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish Astro Markdown posts to WeChat draft box")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="One Markdown file, relative to repository root")
    group.add_argument("--changed", nargs=2, metavar=("BASE", "HEAD"), help="Publish changed opted-in posts")
    parser.add_argument("--force", action="store_true", help="Ignore wechat.draft opt-in for --file")
    args = parser.parse_args()

    if args.file:
        publish_one(ROOT / args.file, force=args.force)
        return

    posts = changed_posts(args.changed[0], args.changed[1])
    if not posts:
        print("No changed Markdown posts found")
        return
    for post in posts:
        publish_one(post, force=False)


if __name__ == "__main__":
    main()

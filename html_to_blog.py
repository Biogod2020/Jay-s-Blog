#!/usr/bin/env python3
"""
HTML to Astro Blog Converter

Converts raw HTML documents to Astro-compatible Markdown blog posts.
Handles metadata extraction, content transformation, and asset management.
"""

import os
import re
import argparse
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup
import shutil
import urllib.request

def extract_metadata(soup):
    """Extract title and description from HTML."""
    # Try to get title from <title> tag first
    title = None
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text().strip()
    
    # Fallback to h1
    if not title:
        h1 = soup.find('h1')
        if h1:
            title = h1.get_text().strip()
    
    # Get description from lead paragraph or meta tag
    description = None
    
    # Try meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc and meta_desc.get('content'):
        description = meta_desc['content']
    
    # Fallback to first lead paragraph
    if not description:
        lead = soup.find('p', class_='lead')
        if not lead:
            lead = soup.find(class_='lead')
        if lead:
            description = lead.get_text().strip()[:200] + "..."
    
    # Final fallback
    if not description:
        first_p = soup.find('main')
        if first_p:
            p = first_p.find('p')
            if p:
                description = p.get_text().strip()[:200] + "..."
    
    return title, description

def extract_external_scripts(soup):
    """Extract external script URLs from head."""
    external_scripts = []
    local_scripts = []
    
    for script in soup.find_all('script', src=True):
        src = script['src']
        if src.startswith('http'):
            external_scripts.append(src)
        elif src.startswith('/'):
            local_scripts.append(src)
    
    return external_scripts, local_scripts

def extract_local_styles(soup):
    """Extract local stylesheet links from head."""
    local_styles = []
    
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href', '')
        if href.startswith('/'):
            local_styles.append(href)
    
    return local_styles

def process_images(soup, output_image_dir, image_url_prefix):
    """
    Find all images, copy/download them to output directory,
    and update src paths.
    """
    os.makedirs(output_image_dir, exist_ok=True)
    
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if not src:
            continue
        
        # Skip data URLs and SVG
        if src.startswith('data:') or '.svg' in src:
            continue
        
        # Handle external URLs
        if src.startswith('http'):
            try:
                filename = os.path.basename(src.split('?')[0])
                if not filename or len(filename) > 100:
                    filename = f"img_{hash(src) % 10000}.jpg"
                
                dest_path = os.path.join(output_image_dir, filename)
                
                if not os.path.exists(dest_path):
                    print(f"  Downloading: {src[:60]}...")
                    urllib.request.urlretrieve(src, dest_path)
                
                img['src'] = f"{image_url_prefix}/{filename}"
            except Exception as e:
                print(f"  Warning: Failed to download {src}: {e}")
        
        # Handle local paths
        elif os.path.exists(src):
            filename = os.path.basename(src)
            dest_path = os.path.join(output_image_dir, filename)
            
            if not os.path.exists(dest_path):
                shutil.copy2(src, dest_path)
            
            img['src'] = f"{image_url_prefix}/{filename}"

def extract_body_content(soup):
    """Extract the main content body, removing head/scripts."""
    # Remove head tag
    head = soup.find('head')
    if head:
        head.decompose()
    
    # Remove standalone script tags (keep inline scripts in HTML)
    for script in soup.find_all('script'):
        # Only remove script tags with src or those that are just config
        if script.get('src') or 'MathJax' in str(script) or 'tailwind' in str(script):
            script.decompose()
    
    # Get body content
    body = soup.find('body')
    if body:
        # Remove body tag but keep content
        content = ''.join(str(child) for child in body.children)
    else:
        content = str(soup)
    
    return content.strip()

def generate_frontmatter(title, description, pub_date, external_scripts=None, local_scripts=None, local_styles=None):
    """Generate YAML frontmatter."""
    lines = [
        '---',
        f'title: "{title}"',
        f'description: "{description}"',
        f'pubDate: {pub_date}',
    ]
    
    if external_scripts:
        lines.append('externalScripts:')
        for script in external_scripts:
            lines.append(f'  - "{script}"')
    
    if local_scripts:
        lines.append('localScripts:')
        for script in local_scripts:
            lines.append(f'  - "{script}"')
    
    if local_styles:
        lines.append('localStyles:')
        for style in local_styles:
            lines.append(f'  - "{style}"')
    
    lines.append('---')
    
    return '\n'.join(lines)

def convert_html_to_blog(
    input_html_path,
    output_md_path,
    output_image_dir,
    image_url_prefix,
    pub_date=None
):
    """Main conversion function."""
    print(f"Converting: {input_html_path}")
    
    # Read HTML file
    with open(input_html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract metadata
    title, description = extract_metadata(soup)
    print(f"  Title: {title}")
    print(f"  Description: {description[:50]}...")
    
    # Extract scripts and styles
    external_scripts, local_scripts = extract_external_scripts(soup)
    local_styles = extract_local_styles(soup)
    
    # Process images
    print("  Processing images...")
    process_images(soup, output_image_dir, image_url_prefix)
    
    # Extract body content
    body_content = extract_body_content(soup)
    
    # Generate frontmatter
    if pub_date is None:
        pub_date = datetime.now().strftime('%Y-%m-%d')
    
    frontmatter = generate_frontmatter(
        title=title,
        description=description,
        pub_date=pub_date,
        # Note: We keep MathJax and Tailwind in the layout, not per-post
        external_scripts=None,
        local_scripts=None,
        local_styles=None
    )
    
    # Combine and write output
    output_content = f"{frontmatter}\n\n{body_content}\n"
    
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"  Output: {output_md_path}")
    print("  Done!")

def main():
    parser = argparse.ArgumentParser(description='Convert HTML to Astro blog post')
    parser.add_argument('input', help='Input HTML file path')
    parser.add_argument('-o', '--output', help='Output Markdown file path')
    parser.add_argument('-i', '--images', help='Output image directory')
    parser.add_argument('-p', '--prefix', help='Image URL prefix', default='/images')
    parser.add_argument('-d', '--date', help='Publication date (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    # Derive output paths if not specified
    input_path = Path(args.input)
    base_name = input_path.stem.lower().replace(' ', '-')
    
    # Simple slug generation
    slug = 'dipole-to-ecg'  # Default for this specific file
    
    if args.output:
        output_md = args.output
    else:
        output_md = f"src/content/blog/{slug}.md"
    
    if args.images:
        output_images = args.images
    else:
        output_images = f"public/images/{slug}"
    
    image_prefix = f"/images/{slug}"
    
    convert_html_to_blog(
        input_html_path=args.input,
        output_md_path=output_md,
        output_image_dir=output_images,
        image_url_prefix=image_prefix,
        pub_date=args.date
    )

if __name__ == '__main__':
    main()

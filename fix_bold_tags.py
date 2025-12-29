#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
脚本功能：将HTML文件中错误使用的Markdown加粗语法 ** ** 替换为正确的HTML标签 <b></b>
作者：Antigravity
日期：2025-12-29
"""

import re
import sys
from pathlib import Path


def fix_bold_syntax(file_path):
    """
    读取HTML文件，将 **文本** 格式替换为 <b>文本</b>
    
    参数:
        file_path: HTML文件路径
    
    返回:
        替换的数量
    """
    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 备份原文件
    backup_path = file_path.with_suffix('.html.bak')
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ 已创建备份文件: {backup_path}")
    
    # 使用正则表达式替换 **文本** 为 <b>文本</b>
    # 这个正则表达式会匹配 ** 和 ** 之间的非星号内容
    pattern = r'\*\*([^*]+?)\*\*'
    replacement = r'<b>\1</b>'
    
    # 执行替换并统计次数
    new_content, count = re.subn(pattern, replacement, content)
    
    if count > 0:
        # 写入修改后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ 成功替换了 {count} 处 ** ** 为 <b></b>")
        
        # 显示所有替换的内容
        print("\n替换详情:")
        matches = re.findall(pattern, content)
        for i, match in enumerate(matches, 1):
            print(f"  {i}. **{match}** → <b>{match}</b>")
    else:
        print("✓ 未发现需要替换的 ** ** 语法")
    
    return count


def main():
    # 文件路径
    file_path = Path("/Users/jay/LocalProjects/Jay-s-Blog/raw/从偶极子到心电图.html")
    
    # 检查文件是否存在
    if not file_path.exists():
        print(f"✗ 错误: 文件不存在 - {file_path}")
        sys.exit(1)
    
    print(f"开始处理文件: {file_path}")
    print("=" * 60)
    
    # 执行修复
    count = fix_bold_syntax(file_path)
    
    print("=" * 60)
    if count > 0:
        print(f"✓ 处理完成! 共修复 {count} 处错误")
        print(f"✓ 原文件已备份为: {file_path.with_suffix('.html.bak')}")
    else:
        print("✓ 文件检查完成，无需修复")


if __name__ == "__main__":
    main()

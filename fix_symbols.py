#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复HTML文件中的数学符号格式错误
"""

import re

file_path = "/Users/jay/LocalProjects/Jay-s-Blog/raw/从偶极子到心电图.html"

# 读取文件
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 备份
with open(file_path + '.symbol_bak2', 'w', encoding='utf-8') as f:
    f.write(content)
print("✓ 已创建备份")

# 修复符号格式错误
fixes = []

# 1. 修复 \\(+,- \\) 为 \\(+, -\\)
old1 = r'\(+,- \)'
new1 = r'\(+, -\)'
count1 = content.count(old1)
if count1 > 0:
    content = content.replace(old1, new1)
    fixes.append(f"修复符号格式: {old1} → {new1} (共{count1}处)")

# 2. 检查并修复可能的其他符号间距问题
# 例如 \(-q\) 和 \(+q\) 应该保持一致
patterns_to_check = [
    (r'\(-q\)', '负电荷表示'),
    (r'\(+q\)', '正电荷表示'),
    (r'\(Na\^+\)', '钠离子'),
    (r'\(Ca\^{2\+}\)', '钙离子'),
]

for pattern, desc in patterns_to_check:
    if re.search(pattern.replace('\\', '\\\\'), content):
        fixes.append(f"✓ {desc}格式正确: {pattern}")

# 写入修改后的内容
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n修复完成！共进行了 {len(fixes)} 项检查/修复：")
for fix in fixes:
    print(f"  {fix}")

# 验证修复
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    line173 = lines[172]
    if '+, -' in line173:
        print("\n✅ 验证成功：第173行符号格式已修正")
    else:
        print("\n⚠️  警告：第173行可能未正确修复")

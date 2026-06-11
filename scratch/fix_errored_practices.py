import os
import re
import io
import sys
import contextlib
import json

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

practice_dir = "/Users/hojin9/dev/jinysite/datas/src/practice"
folders = [d for d in os.listdir(practice_dir) if os.path.isdir(os.path.join(practice_dir, d)) and d not in ['midterm', 'final', 'wrapup']]

def strip_exec_results(content):
    lines = content.split('\n')
    new_lines = []
    skipping = False
    for line in lines:
        if re.match(r'^\s*>\s*\*\*💻\s*\[실행\s*결과\]\*\*', line):
            skipping = True
            continue
        if skipping:
            if line.strip().startswith('>') or line.strip() == '':
                continue
            else:
                skipping = False
        new_lines.append(line)
    return '\n'.join(new_lines)

def mock_display(*args, **kwargs):
    for arg in args:
        print(arg)

def execute_blocks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'(```python\n(.*?)\n```)', re.DOTALL)
    matches = list(pattern.finditer(content))
    if not matches:
        return

    env_globals = {
        'pd': pd,
        'sns': sns,
        'plt': plt,
        'display': mock_display,
        '__builtins__': __builtins__
    }

    new_content = ""
    last_end = 0

    base_dir = os.path.dirname(file_path)
    img_dir = os.path.join(base_dir, 'img')
    os.makedirs(img_dir, exist_ok=True)

    block_idx = 1
    for match in matches:
        full_block = match.group(1)
        code = match.group(2)
        start = match.start()
        end = match.end()

        new_content += content[last_end:end]

        f_out = io.StringIO()
        svg_filename = f"exec_step_{block_idx}.svg"
        svg_path = os.path.join(img_dir, svg_filename)

        svg_created = False
        def mock_show(*args, **kwargs):
            nonlocal svg_created
            if plt.get_fignums():
                plt.savefig(svg_path, format='svg', bbox_inches='tight')
                svg_created = True
                plt.close("all")
        env_globals['plt'].show = mock_show
        
        with contextlib.redirect_stdout(f_out):
            try:
                original_cwd = os.getcwd()
                os.chdir(base_dir)
                try:
                    exec(code, env_globals)
                finally:
                    os.chdir(original_cwd)
                if plt.get_fignums():
                    plt.savefig(svg_path, format='svg', bbox_inches='tight')
                    svg_created = True
                    plt.close("all")
            except Exception as e:
                print(f"Error: {e}")

        output_text = f_out.getvalue()
        
        result_md = ""
        has_text = bool(output_text.strip())
        has_img = svg_created

        if has_text or has_img:
            result_md += "\n\n> **💻 [실행 결과]**\n"
            if has_text:
                result_md += f"> ```text\n"
                for line in output_text.strip().split('\n'):
                    result_md += f"> {line}\n"
                result_md += f"> ```\n"
            if has_img:
                result_md += f"> ![실행 결과 시각화](img/{svg_filename})\n"
        
        new_content += result_md
        last_end = end
        block_idx += 1

    new_content += content[last_end:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Executed and embedded: {file_path}")

    # Regenerate practice.ipynb to keep in sync
    regenerate_ipynb(file_path, new_content)

def regenerate_ipynb(file_path, new_content):
    base_dir = os.path.dirname(file_path)
    clean_md = new_content
    if clean_md.startswith('---'):
        parts = clean_md.split('---', 2)
        if len(parts) >= 3:
            clean_md = parts[2].strip()
            
    # Remove 실행 결과 blockquotes for the notebook
    clean_md = strip_exec_results(clean_md)
    
    cells = []
    pattern = re.compile(r'```python\n(.*?)\n```', re.DOTALL)
    last_end = 0
    for match in pattern.finditer(clean_md):
        md_part = clean_md[last_end:match.start()].strip()
        if md_part:
            cells.append({
                "cell_type": "markdown",
                "source": [line + '\n' for line in md_part.split('\n')]
            })
        
        code_part = match.group(1).strip()
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [line + '\n' for line in code_part.split('\n')]
        })
        last_end = match.end()
    
    tail_part = clean_md[last_end:].strip()
    if tail_part:
        cells.append({
            "cell_type": "markdown",
            "source": [line + '\n' for line in tail_part.split('\n')]
        })
    
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    
    ipynb_path = os.path.join(base_dir, "practice.ipynb")
    with open(ipynb_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    print(f"Regenerated notebook: {ipynb_path}")

print("=== Phase 3: Detecting errors, stripping, and re-executing ===")
errored_count = 0
for folder in sorted(folders):
    idx_path = os.path.join(practice_dir, folder, "index.md")
    if not os.path.exists(idx_path):
        continue
        
    with open(idx_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if there is an Error inside a code block inside a blockquote
    # Quick regex or search: find if "Error:" is in the file
    # Especially if it is preceded by "💻 [실행 결과]" block
    if '💻 [실행 결과]' in content:
        # Check if the block has Error:
        exec_blocks = re.findall(r'> \*\*💻 \[실행 결과\]\*\*(.*?)(?=\n\n|\Z)', content, re.DOTALL)
        has_error = False
        for block in exec_blocks:
            if 'Error:' in block or 'Errno' in block:
                has_error = True
                break
                
        if has_error:
            print(f"Found error in: {folder}")
            stripped = strip_exec_results(content)
            with open(idx_path, "w", encoding="utf-8") as f:
                f.write(stripped)
            execute_blocks(idx_path)
            errored_count += 1

print(f"\nFixed {errored_count} errored practices.")

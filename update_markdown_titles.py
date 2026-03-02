import os
import re

base_dir = r"d:\site\jinydev\datas\src\python"

for root, dirs, files in os.walk(base_dir):
    if root == base_dir:
        continue
    
    for file in files:
        if file.endswith("index.md"):
            folder_name = os.path.basename(root)
            match = re.match(r"^(\d{2})_", folder_name)
            if not match:
                continue
            
            new_num = match.group(1)
            
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            title_match = re.search(r'title:\s*"(\d{2})\.', content)
            if not title_match:
                continue
            
            old_num = title_match.group(1)
            
            if old_num != new_num:
                content = content.replace(f'title: "{old_num}.', f'title: "{new_num}.')
                content = content.replace(f'# {old_num}.', f'# {new_num}.')
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated {folder_name}/index.md: {old_num} -> {new_num}")

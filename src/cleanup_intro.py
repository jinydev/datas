import os
import re

base_dir = r"d:\site\jinydev\datas\src\intro"

# Iterate over L2 dirs in intro
l2_entries = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.')]

for l2_entry in l2_entries:
    l2_abs = os.path.join(base_dir, l2_entry)
    
    # parse l2_num (e.g. 1_01_why -> 1)
    # wait! l2 is 1_01_why -> l2_num is 1. Wait, l2_num is the second number!
    m2 = re.match(r'^1_(\d+)_', l2_entry)
    if not m2: continue
    l2_num = int(m2.group(1))
    
    # get all L3 entries
    l3_entries = []
    for l3 in os.listdir(l2_abs):
        if l3 != "img" and not l3.startswith('.'):
            l3_entries.append(l3)
    
    # Sort L3 to maintain original order (since even messy numbers preserved order)
    # They have deep names like 1_01_01_01_01_overview, but they are alphabetically sorted fine.
    # Wait, 1_01_...01_overview comes before 1_01_...02_existence. So sort works.
    l3_entries.sort()
    
    count = 1
    for l3_entry in l3_entries:
        l3_abs = os.path.join(l2_abs, l3_entry)
        
        # strip all leading numbers and underscores
        clean_name = re.sub(r'^[\d_]+', '', l3_entry)
        
        if os.path.isdir(l3_abs):
            new_l3 = f"1_{l2_num:02d}_{count:02d}_{clean_name}"
            new_l3_abs = os.path.join(l2_abs, new_l3)
            if l3_abs != new_l3_abs:
                os.rename(l3_abs, new_l3_abs)
                print(f"Renamed {l3_entry} to {new_l3}")
                
            # Update markdown
            md_path = os.path.join(new_l3_abs, "index.md")
            if os.path.exists(md_path):
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Update title: e.g. title: "1.1.1 Overview"
                # Strip existing prefix
                new_prefix = f"1.{l2_num}.{count}"
                content = re.sub(r'title:\s*"[\d\.]+[\s]+', f'title: "{new_prefix} ', content)
                content = re.sub(r'#\s*[\d\.]+\s+', f'# {new_prefix} ', content)
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            count += 1
        elif l3_entry.endswith(".md") and l3_entry != "index.md":
            new_l3 = f"1_{l2_num:02d}_{count:02d}_{clean_name}"
            new_l3_abs = os.path.join(l2_abs, new_l3)
            if l3_abs != new_l3_abs:
                os.rename(l3_abs, new_l3_abs)
                print(f"Renamed {l3_entry} to {new_l3}")
            
            # Update markdown
            if os.path.exists(new_l3_abs):
                with open(new_l3_abs, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_prefix = f"1.{l2_num}.{count}"
                content = re.sub(r'title:\s*"[\d\.]+[\s]+', f'title: "{new_prefix} ', content)
                content = re.sub(r'#\s*[\d\.]+\s+', f'# {new_prefix} ', content)
                with open(new_l3_abs, 'w', encoding='utf-8') as f:
                    f.write(content)
            count += 1

print("Intro folder L3 entries cleaned up successfully.")

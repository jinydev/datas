import os
import re

base_dir = r"d:\site\jinydev\datas\src\intro"

fixes = [
    ("1_01_01_why_data_analysis", "1_01_why_data_analysis", "1.1"),
    ("1_01_02_industry_applications", "1_02_industry_applications", "1.2"),
    ("1_01_03_insight_and_conclusion", "1_03_insight_and_conclusion", "1.3")
]

for old_name, new_name, proper_num in fixes:
    old_abs = os.path.join(base_dir, old_name)
    new_abs = os.path.join(base_dir, new_name)
    
    if os.path.exists(old_abs):
        os.rename(old_abs, new_abs)
        print(f"Renamed {old_name} -> {new_name}")
        
    if os.path.exists(new_abs):
        # Update L2 index.md
        l2_idx = os.path.join(new_abs, "index.md")
        if os.path.exists(l2_idx):
            with open(l2_idx, 'r', encoding='utf-8') as f:
                content = f.read()
            # replace 1.1 with proper_num in title
            content = re.sub(r'title:\s*"1\.1\s+', f'title: "{proper_num} ', content)
            content = re.sub(r'#\s*1\.1\s+', f'# {proper_num} ', content)
            with open(l2_idx, 'w', encoding='utf-8') as f:
                f.write(content)
        
        # Also need to update L3 dirs inside!
        # wait! L3 dirs like `01_overview` became `1_01_01_overview`. 
        # But wait! If they were inside `1_01_02_industry_applications`, they were `1_01_XX_...` where `1_01` is actually wrong!
        # It should be `1_02_XX_...`!!
        # Let's fix L3 dirs inside `new_abs`
        for l3_entry in os.listdir(new_abs):
            l3_abs = os.path.join(new_abs, l3_entry)
            if os.path.isdir(l3_abs) and l3_entry != "img":
                # l3_entry is like `1_01_01_...`
                # we want to change `1_01_` to `1_02_` for industry_applications
                prefix_to_replace = "1_01_"
                proper_prefix = proper_num.replace('.', '_') + "_"  # e.g., "1_2_" -> wait, no! "1_02_"
                proper_prefix = f"1_{int(proper_num.split('.')[1]):02d}_"
                
                if l3_entry.startswith(prefix_to_replace) and proper_prefix != prefix_to_replace:
                    new_l3 = l3_entry.replace(prefix_to_replace, proper_prefix, 1)
                    new_l3_abs = os.path.join(new_abs, new_l3)
                    os.rename(l3_abs, new_l3_abs)
                    
                    # Update L3 index.md
                    l3_idx = os.path.join(new_l3_abs, "index.md")
                    if os.path.exists(l3_idx):
                        with open(l3_idx, 'r', encoding='utf-8') as f:
                            l3_content = f.read()
                        # L3 title had "1.1.X" where X is l3_num. We want to update to "{proper_num}.X"
                        # But wait, it might still just say "1.1."
                        l3_content = re.sub(r'title:\s*"1\.1\.', f'title: "{proper_num}.', l3_content)
                        l3_content = re.sub(r'#\s*1\.1\.', f'# {proper_num}.', l3_content)
                        with open(l3_idx, 'w', encoding='utf-8') as f:
                            f.write(l3_content)
                elif l3_entry.startswith(proper_prefix): # if it's 1.1, prefix already 1_01_
                    # just update L3 markdown files just in case
                    l3_idx = os.path.join(l3_abs, "index.md")
                    if os.path.exists(l3_idx):
                        with open(l3_idx, 'r', encoding='utf-8') as f:
                            l3_content = f.read()
                        # Nothing to change for 1.1!
                        pass
        
        print(f"Updated markdowns in {new_name}")

print("Fix applied.")

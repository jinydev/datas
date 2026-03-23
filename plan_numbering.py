import os

directories = [
    "04_array_creation",
    "05_array_operations",
    "06_indexing_slicing",
    "07_shape_memory",
    "08_concat_split",
    "09_random_exercises"
]

base_dir = r"d:\site\jinydev\datas\src\numpy"

for d_idx, d_name in enumerate(directories):
    chap_num = d_idx + 4 # 04 -> 4, 05 -> 5
    print(f"\n=== CHAPTER {chap_num}: {d_name} ===")
    
    dir_path = os.path.join(base_dir, d_name)
    subdirs = sorted([s for s in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, s))])
    
    for s_idx, subdir in enumerate(subdirs):
        sec_num = s_idx + 1
        md_file = os.path.join(dir_path, subdir, "index.md")
        if not os.path.exists(md_file):
            continue
            
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        h1_count = 0
        h2_count = 0
        h2_lines = []
        
        for line in lines:
            line_stripped = line.strip()
            # Ignore python comments that happen to start with #
            if line_stripped.startswith("# ") and not line_stripped.startswith("# 4.") and not line_stripped.startswith("# 출력") and not line_stripped.startswith("# 배열") and not "결과" in line_stripped:
                h1_count += 1
            if line_stripped.startswith("## ") and not line_stripped.startswith("## 출력"):
                h2_count += 1
                h2_lines.append(line_stripped)
                
        if h2_count > 0:
            print(f"  FILE: {subdir}/index.md  (Target H1: {chap_num}.{sec_num}) | H2 count: {h2_count}")
            for hl in h2_lines:
                print(f"    {hl}")

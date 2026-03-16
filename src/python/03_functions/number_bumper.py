import os
import re

base_dir = r"d:\site\jinydev\datas\src\python\03_functions"

# Mapping of file paths to the old and new numbers they should have
# 04 -> 05
# 05 -> 06
# 06 -> 07
# 07 -> 08
# 08 -> 09

bump_targets = {
    "05_advanced_parameters/index.md": ("3.3.4", "3.3.5"),
    "06_variable_scope/index.md": ("3.3.5", "3.3.6"),
    "07_lambda_and_recursion/index.md": ("3.3.6", "3.3.7"),
    "08_built_in_functions/index.md": ("3.3.7", "3.3.8"),
    "09_math_module/index.md": ("3.3.8", "3.3.9")
}

for rel_path, (old_num, new_num) in bump_targets.items():
    full_path = os.path.join(base_dir, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace only the first 3 occurrences to be safe: 
        # Title in YAML, H1 header, and maybe one other ref.
        # It's safest to simply replace old_num with new_num globally for these simple files.
        updated_content = content.replace(old_num, new_num)
        
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"Bumped numbers in {rel_path} : {old_num} -> {new_num}")
    else:
        print(f"Skipped {rel_path} (File not found)")

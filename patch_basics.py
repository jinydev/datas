import os
import shutil

# 1. Update index.md
idx_path = r"d:\site\jinydev\datas\src\python\index.md"
with open(idx_path, "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("01_python_basics", "01_basic")
with open(idx_path, "w", encoding="utf-8") as f:
    f.write(content)

# 2. Copy images
src_images = [
    r"C:\Users\infoh\.gemini\antigravity\brain\0fdaa599-d729-4590-a6a1-831855edd234\python_functions_illustration_1772305046613.png",
    r"C:\Users\infoh\.gemini\antigravity\brain\0fdaa599-d729-4590-a6a1-831855edd234\python_dictionary_illustration_1772305061825.png"
]

dest_dir = r"d:\site\jinydev\datas\src\assets\images\concept"
os.makedirs(dest_dir, exist_ok=True)

for img in src_images:
    if os.path.exists(img):
        if "functions" in img: dest_name = "04_functions.png"
        elif "dictionary" in img: dest_name = "05_dictionary.png"
        else: dest_name = os.path.basename(img)
        shutil.copy(img, os.path.join(dest_dir, dest_name))

print("Patch complete.")

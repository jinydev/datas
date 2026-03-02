import os
import shutil

src_images = [
    r"C:\Users\infoh\.gemini\antigravity\brain\0fdaa599-d729-4590-a6a1-831855edd234\oop_class_instance_concept_1772303548010.png",
    r"C:\Users\infoh\.gemini\antigravity\brain\0fdaa599-d729-4590-a6a1-831855edd234\oop_inheritance_concept_1772303561992.png",
    r"C:\Users\infoh\.gemini\antigravity\brain\0fdaa599-d729-4590-a6a1-831855edd234\oop_abstraction_concept_1772303578157.png"
]

dest_dir = r"d:\site\jinydev\datas\src\assets\images\oop"
os.makedirs(dest_dir, exist_ok=True)

for img in src_images:
    if os.path.exists(img):
        # Rename slightly for easier markdown usage
        if "class_instance" in img: dest_name = "01_class_instance.png"
        elif "inheritance" in img: dest_name = "02_inheritance.png"
        elif "abstraction" in img: dest_name = "03_abstraction.png"
        else: dest_name = os.path.basename(img)
        
        shutil.copy(img, os.path.join(dest_dir, dest_name))

print("Images copied to assets/images/oop successfully.")

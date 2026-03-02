import os
import shutil

base_dir = r"d:\site\jinydev\datas\src\python"

# 1. Rename existing folders to make room for Section 03
os.rename(os.path.join(base_dir, "05_data_analysis_packages"), os.path.join(base_dir, "06_data_analysis_packages"))
os.rename(os.path.join(base_dir, "04_oop"), os.path.join(base_dir, "05_oop"))
os.rename(os.path.join(base_dir, "03_data_structures"), os.path.join(base_dir, "04_data_structures"))

# 2. Rename 02_control_flow_functions to 02_control_flow
os.rename(os.path.join(base_dir, "02_control_flow_functions"), os.path.join(base_dir, "02_control_flow"))

# 3. Create 03_functions
os.makedirs(os.path.join(base_dir, "03_functions"), exist_ok=True)

# 4. Move 11_user_defined_functions from 02_control_flow to 03_functions
src = os.path.join(base_dir, "02_control_flow", "11_user_defined_functions")
dst = os.path.join(base_dir, "03_functions", "11_user_defined_functions")
shutil.move(src, dst)

print("Folder split complete!")

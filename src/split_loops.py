import os
import shutil

base_dir = r"d:\site\jinydev\datas\src\python\02_control_flow"

# Move exceptions safely
old_ex = os.path.join(base_dir, "04_exceptions")
new_ex = os.path.join(base_dir, "05_exceptions")
if os.path.exists(old_ex):
    os.rename(old_ex, new_ex)

# Create new loop directories
for_loop_dir = os.path.join(base_dir, "03_for_loop")
while_loop_dir = os.path.join(base_dir, "04_while_loop")

os.makedirs(os.path.join(for_loop_dir, "img"), exist_ok=True)
os.makedirs(os.path.join(while_loop_dir, "img"), exist_ok=True)

# Copy SVG
old_svg = os.path.join(base_dir, "03_for_while_loops", "img", "loops_anim.svg")
if os.path.exists(old_svg):
    shutil.copy2(old_svg, os.path.join(for_loop_dir, "img", "loops_anim.svg"))
    shutil.copy2(old_svg, os.path.join(while_loop_dir, "img", "loops_anim.svg"))

# Also handle old index shift if necessary, but we'll run master_rebuild.py later.

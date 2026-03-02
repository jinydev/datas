import os
import shutil

src_pandas = r"d:\site\jinydev\datas\src\pandas"
src_mathplotlib = r"d:\site\jinydev\datas\src\mathplotlib"

# Folders to move to mathplotlib
viz_folders = [
    "01_visualization_intro",
    "02_simple_line_plot",
    "03_figure_subplot",
    "04_gridspec_layout",
    "33_pydataset_intro",
    "34_pydataset_install",
    "35_pydataset_import",
    "36_seaborn_graph",
    "39_scatter_plot",
    "40_line_plot",
    "41_bar_plot",
    "42_box_plot",
    "43_histogram",
    "44_pie_chart",
    "45_violin_plot",
    "46_correlation_viz"
]

import glob

def migrate():
    # Ensure target exists
    if not os.path.exists(src_mathplotlib):
        os.makedirs(src_mathplotlib)

    # 1. Move to mathplotlib and re-index
    print("Moving visualization folders to mathplotlib...")
    for i, folder in enumerate(viz_folders):
        old_path = os.path.join(src_pandas, folder)
        new_prefix = f"{(i+1):02d}"
        new_name = new_prefix + folder[2:] # Keep the original name part, just change prefix
        new_path = os.path.join(src_mathplotlib, new_name)
        
        if os.path.exists(old_path):
            print(f"Moving {old_path} -> {new_path}")
            shutil.move(old_path, new_path)
            
            # also update layout inside index.md of the moved folder
            md_path = os.path.join(new_path, "index.md")
            if os.path.exists(md_path):
                with open(md_path, "r", encoding="utf-8") as f:
                    content = f.read()
                content = content.replace("layout: pandas", "layout: mathplotlib")
                # Fix navigation links if they were pointing to pandas
                # Actually, navigation isn't hardcoded in the md usually, just the layout
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(content)
        else:
            print(f"Warning: {old_path} not found.")

    # 2. Re-index remaining folders in pandas
    print("Re-indexing remaining pandas folders...")
    remaining_folders = sorted([f for f in os.listdir(src_pandas) if os.path.isdir(os.path.join(src_pandas, f))])
    
    for i, folder in enumerate(remaining_folders):
        old_path = os.path.join(src_pandas, folder)
        new_prefix = f"{(i+1):02d}"
        new_name = new_prefix + folder[2:]
        new_path = os.path.join(src_pandas, new_name)
        
        if old_path != new_path:
            print(f"Renaming {old_path} -> {new_path}")
            os.rename(old_path, new_path)

if __name__ == "__main__":
    migrate()

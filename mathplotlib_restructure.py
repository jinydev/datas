import os
import shutil

base_dir = r"d:\site\jinydev\datas\src\mathplotlib"

section_mapping = {
    "01_matplotlib_basics": ["01_visualization_intro", "02_simple_line_plot", "03_figure_subplot", "04_gridspec_layout"],
    "02_seaborn_dataset": ["05_pydataset_intro", "06_pydataset_install", "07_pydataset_import", "08_seaborn_graph"],
    "03_basic_charts": ["09_scatter_plot", "10_line_plot", "11_bar_plot"],
    "04_distribution_charts": ["12_box_plot", "13_histogram", "14_pie_chart"],
    "05_advanced_charts": ["15_violin_plot", "16_correlation_viz"]
}

for sec, items in section_mapping.items():
    sec_path = os.path.join(base_dir, sec)
    if not os.path.exists(sec_path):
        os.makedirs(sec_path)
    
    for item in items:
        src_path = os.path.join(base_dir, item)
        dest_path = os.path.join(sec_path, item)
        
        # move folder
        if os.path.exists(src_path) and os.path.isdir(src_path):
            shutil.move(src_path, dest_path)
            print(f"Moved {item} to {sec}")

print("Done physically restructuring Mathplotlib folders!")

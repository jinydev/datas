import os
import shutil

base_dir = r"d:\site\jinydev\datas\src\numpy"
yaml_path = r"d:\site\jinydev\datas\src\_data\numpy.yml"
index_path = r"d:\site\jinydev\datas\src\numpy\index.md"

section_mapping = {
    "01_numpy_basics": ["01_numpy_intro", "02_ndarray"],
    "02_array_creation": ["03_array_creation", "04_arange", "05_reshape", "06_linspace", "07_arange_vs_linspace", 
                          "08_zeros", "09_ones", "10_eye", "11_full", "12_empty", "13_like_functions"],
    "03_array_operations": ["14_scalar_operations", "15_array_operations", "16_ufunc", "22_broadcasting_intro", 
                            "23_scalar_broadcasting", "24_2d_broadcasting", "25_newaxis"],
    "04_indexing_slicing": ["17_1d_slicing", "18_2d_slicing", "19_3d_slicing", "26_1d_indexing", "27_2d_indexing", "28_advanced_indexing"],
    "05_shape_memory": ["20_reshape_advanced", "21_copy_view"],
    "06_concat_split": ["29_array_concat_intro", "30_vstack", "31_hstack", "32_column_row_stack", "33_concatenate_stack", 
                        "34_column_stack_vs_hstack", "35_row_stack_vs_vstack", "36_npc_column_stack", "37_npr", 
                        "38_1d_concat_methods", "39_1d_concat_summary", "40_split", "41_hsplit_vsplit", "42_array_split"],
    "07_random_exercises": ["43_random", "44_exercises"]
}

# Read content
with open(yaml_path, "r", encoding="utf-8") as f:
    yaml_content = f.read()

with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

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
        
        # replace in config
        old_url = f"/numpy/{item}/"
        new_url = f"/numpy/{sec}/{item}/"
        
        yaml_content = yaml_content.replace(old_url, new_url)
        index_content = index_content.replace(old_url, new_url)

with open(yaml_path, "w", encoding="utf-8") as f:
    f.write(yaml_content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Done restructuring NumPy folders!")

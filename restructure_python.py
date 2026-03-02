import os
import shutil

base_dir = r"d:\site\jinydev\datas\src\python"
data_yaml = r"d:\site\jinydev\datas\src\_data\python.yml"
index_md = r"d:\site\jinydev\datas\src\python\index.md"

sections = {
    "01_python_basics": [
        "01_comments_constants", "02_variables_assignment", "03_variable_naming", 
        "04_data_types_operators", "05_various_operators", "06_built_in_functions", 
        "07_math_module"
    ],
    "02_data_analysis_packages": [
        "08_pandas_visualization", "09_matplotlib_seaborn", "10_toy_data_dataframe"
    ],
    "03_control_flow_functions": [
        "11_if_statement", "12_match_statement", "13_for_while_loops", "14_user_defined_functions"
    ],
    "04_data_structures": [
        "15_list", "16_dictionary", "17_tuple", "18_set", "19_immutable_hash_id"
    ],
    "05_oop": [
        "20_class_object"
    ]
}

print("1. Moving folders...")
for section_folder, item_folders in sections.items():
    section_path = os.path.join(base_dir, section_folder)
    os.makedirs(section_path, exist_ok=True)
    
    for item in item_folders:
        src = os.path.join(base_dir, item)
        dst = os.path.join(section_path, item)
        if os.path.exists(src) and not os.path.exists(dst):
            print(f"Moving {item} to {section_folder}/")
            shutil.move(src, dst)

print("2. Updating index.md...")
with open(index_md, "r", encoding="utf-8") as f:
    md_content = f.read()

for section_folder, item_folders in sections.items():
    for item in item_folders:
        md_content = md_content.replace(f"(./{item}/)", f"(./{section_folder}/{item}/)")

with open(index_md, "w", encoding="utf-8") as f:
    f.write(md_content)

print("3. Updating python.yml...")
with open(data_yaml, "r", encoding="utf-8") as f:
    yaml_content = f.read()

for section_folder, item_folders in sections.items():
    for item in item_folders:
        yaml_content = yaml_content.replace(f"'/python/{item}/'", f"'/python/{section_folder}/{item}/'")

with open(data_yaml, "w", encoding="utf-8") as f:
    f.write(yaml_content)

print("Done.")

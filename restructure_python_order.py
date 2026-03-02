import os
import shutil
import re

base_dir = r"d:\site\jinydev\datas\src\python"
data_yaml = r"d:\site\jinydev\datas\src\_data\python.yml"
index_md = r"d:\site\jinydev\datas\src\python\index.md"

renames = [
    # Section 03 -> 02 (Control Flow)
    (r"03_control_flow_functions\11_if_statement", r"02_control_flow_functions\08_if_statement"),
    (r"03_control_flow_functions\12_match_statement", r"02_control_flow_functions\09_match_statement"),
    (r"03_control_flow_functions\13_for_while_loops", r"02_control_flow_functions\10_for_while_loops"),
    (r"03_control_flow_functions\14_user_defined_functions", r"02_control_flow_functions\11_user_defined_functions"),

    # Section 04 -> 03 (Data Structures)
    (r"04_data_structures\15_list", r"03_data_structures\12_list"),
    (r"04_data_structures\16_dictionary", r"03_data_structures\13_dictionary"),
    (r"04_data_structures\17_tuple", r"03_data_structures\14_tuple"),
    (r"04_data_structures\18_set", r"03_data_structures\15_set"),
    (r"04_data_structures\19_immutable_hash_id", r"03_data_structures\16_immutable_hash_id"),

    # Section 05 -> 04 (OOP)
    (r"05_oop\20_class_object", r"04_oop\17_class_object"),

    # Section 02 -> 05 (Data Analysis Packages - moved to end)
    (r"02_data_analysis_packages\08_pandas_visualization", r"05_data_analysis_packages\18_pandas_visualization"),
    (r"02_data_analysis_packages\09_matplotlib_seaborn", r"05_data_analysis_packages\19_matplotlib_seaborn"),
    (r"02_data_analysis_packages\10_toy_data_dataframe", r"05_data_analysis_packages\20_toy_data_dataframe")
]

# Create new section directories first
for new_sec in ["02_control_flow_functions", "03_data_structures", "04_oop", "05_data_analysis_packages"]:
    os.makedirs(os.path.join(base_dir, new_sec), exist_ok=True)

# Move item folders
for old_rel, new_rel in renames:
    old_tgt = os.path.join(base_dir, old_rel)
    new_tgt = os.path.join(base_dir, new_rel)
    if os.path.exists(old_tgt):
        shutil.move(old_tgt, new_tgt)

# Remove empty old section directories
for old_sec in ["02_data_analysis_packages", "03_control_flow_functions", "04_data_structures", "05_oop"]:
    sec_path = os.path.join(base_dir, old_sec)
    if os.path.exists(sec_path) and not os.listdir(sec_path):
        os.rmdir(sec_path)

print("Folders moved successfully.")

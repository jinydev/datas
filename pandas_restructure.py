import os
import shutil

base_dir = r"d:\site\jinydev\datas\src\pandas"
yaml_path = r"d:\site\jinydev\datas\src\_data\pandas.yml"
index_path = r"d:\site\jinydev\datas\src\pandas\index.md"

section_mapping = {
    "01_pandas_basics": ["01_pandas_intro", "02_series_intro", "03_dataframe_intro"],
    "02_series_dataframe_creation": ["04_series_creation", "05_series_functions", "06_dataframe_constructor", "07_df_from_matrix", "08_df_from_dict", "09_df_from_series", "10_df_from_dict_list", "11_df_from_series_dict", "12_df_dtypes", "13_date_range", "14_df_with_dates"],
    "03_data_selection": ["15_column_selection", "16_conditional_selection", "17_row_selection_loc", "18_row_selection_loc_i", "19_col_selection_loc", "20_col_selection_loc_i", "21_row_col_selection", "22_iloc_selection"],
    "04_data_modification": ["23_df_info_modify", "24_df_extract_assign", "25_df_modify_assign", "26_df_conditional_search", "27_df_sorting", "28_df_various_modifications"],
    "05_file_io": ["29_csv_excel_io", "30_internet_data"]
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
        old_url = f"/pandas/{item}/"
        new_url = f"/pandas/{sec}/{item}/"
        
        yaml_content = yaml_content.replace(old_url, new_url)
        index_content = index_content.replace(old_url, new_url)

with open(yaml_path, "w", encoding="utf-8") as f:
    f.write(yaml_content)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Done restructuring Pandas folders!")

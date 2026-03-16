import os

base_dir = r"d:\site\jinydev\datas\src\python\03_functions"

# The mappings from old to new. Must be done in reverse order to avoid overwriting!
rename_map = [
    ("08_math_module", "09_math_module"),
    ("07_built_in_functions", "08_built_in_functions"),
    ("06_lambda_and_recursion", "07_lambda_and_recursion"),
    ("05_variable_scope", "06_variable_scope"),
    ("04_advanced_parameters", "05_advanced_parameters")
]

for old, new in rename_map:
    old_path = os.path.join(base_dir, old)
    new_path = os.path.join(base_dir, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old} -> {new}")
    else:
        print(f"Warning: {old} not found.")

# Create the new slot
os.makedirs(os.path.join(base_dir, "04_function_call_flow", "img"), exist_ok=True)
print("Created: 04_function_call_flow")

import os

base_dir = r"d:\site\jinydev\datas\src\python"
data_pkg_dir = os.path.join(base_dir, "06_data_analysis_packages")

os.rename(os.path.join(data_pkg_dir, "20_toy_data_dataframe"), os.path.join(data_pkg_dir, "22_toy_data_dataframe"))
os.rename(os.path.join(data_pkg_dir, "19_matplotlib_seaborn"), os.path.join(data_pkg_dir, "21_matplotlib_seaborn"))
os.rename(os.path.join(data_pkg_dir, "18_pandas_visualization"), os.path.join(data_pkg_dir, "20_pandas_visualization"))

oop_dir = os.path.join(base_dir, "05_oop")
os.rename(os.path.join(oop_dir, "17_class_object"), os.path.join(oop_dir, "17_class_instance"))

os.makedirs(os.path.join(oop_dir, "18_inheritance_polymorphism"), exist_ok=True)
os.makedirs(os.path.join(oop_dir, "19_abstraction_interface"), exist_ok=True)

print("OOP expansion folders created and Data Analysis folders shifted successfully.")

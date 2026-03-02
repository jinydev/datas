import os
import shutil
import re

base_src = r"d:\site\jinydev\datas\src"
python_packages_dir = os.path.join(base_src, "python", "06_data_analysis_packages")
mathplotlib_dir = os.path.join(base_src, "mathplotlib")
ml_dir = os.path.join(base_src, "python", "09_machine_learning")

# 1. Move directories
target_packages_dir = os.path.join(mathplotlib_dir, "00_data_analysis_packages")
if os.path.exists(python_packages_dir):
    try:
        shutil.move(python_packages_dir, target_packages_dir)
        print("Moved 06_data_analysis_packages to mathplotlib/00_data_analysis_packages")
    except Exception as e:
        print(f"Error moving directory: {e}")

# 2. Delete ML directory
if os.path.exists(ml_dir):
    try:
        shutil.rmtree(ml_dir)
        print("Deleted 09_machine_learning")
    except Exception as e:
        print(f"Error deleting directory: {e}")

# 3. Update python/index.md
python_idx = os.path.join(base_src, "python", "index.md")
if os.path.exists(python_idx):
    with open(python_idx, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove SECTION 06. 데이터 분석 패키지 준비 section
    content = re.sub(r'## SECTION 06\. 데이터 분석 패키지 준비.*', '', content, flags=re.DOTALL)
    
    # Also remove from learning objectives in python/index.md
    content = re.sub(r'- \*\*분석 패키지 입문\*\*.*?$', '', content, flags=re.MULTILINE)
    
    with open(python_idx, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")
    print("Updated python/index.md")

# 4. Update mathplotlib/index.md
math_idx = os.path.join(mathplotlib_dir, "index.md")
if os.path.exists(math_idx):
    with open(math_idx, 'r', encoding='utf-8') as f:
        m_content = f.read()
    
    # Insert new SECTION 00
    section_00 = """## SECTION 00. 데이터 분석 패키지 시작하기 {#section-00}
- [01. 패키지 판다스와 시각화 라이브러리 설치](/mathplotlib/00_data_analysis_packages/20_pandas_visualization/)
- [02. 패키지 matplotlib, seaborn, pydataset 개요와 설치](/mathplotlib/00_data_analysis_packages/21_matplotlib_seaborn/)
- [03. 토이 데이터와 데이터프레임 활용](/mathplotlib/00_data_analysis_packages/22_toy_data_dataframe/)

"""
    
    # Find "## SECTION 01" and insert before
    idx = m_content.find("## SECTION 01")
    if idx != -1:
        new_m_content = m_content[:idx] + section_00 + m_content[idx:]
        with open(math_idx, 'w', encoding='utf-8') as f:
            f.write(new_m_content)
        print("Updated mathplotlib/index.md")

print("Done")

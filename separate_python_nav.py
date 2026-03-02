import os
import glob
import codecs

src_dir = r"d:\site\jinydev\datas\src"
basic_yml_path = os.path.join(src_dir, "_data", "basic.yml")
python_yml_path = os.path.join(src_dir, "_data", "python.yml")

# 1. Split basic.yml
with codecs.open(basic_yml_path, 'r', 'utf-8') as f:
    lines = f.readlines()

basic_lines = []
python_lines = ["main:\n"]
in_python = False

for line in lines:
    if "title: '2. 파이썬 기초 (Python)'" in line:
        in_python = True
        
    if in_python:
        python_lines.append(line)
    else:
        basic_lines.append(line)

with codecs.open(basic_yml_path, 'w', 'utf-8') as f:
    f.writelines(basic_lines)
    
with codecs.open(python_yml_path, 'w', 'utf-8') as f:
    f.writelines(python_lines)
print("Split basic.yml into basic.yml and python.yml.")

# 2. Duplicate layout templates
basic_layout_path = os.path.join(src_dir, "_layouts", "basic.html")
python_layout_path = os.path.join(src_dir, "_layouts", "python.html")

with codecs.open(basic_layout_path, 'r', 'utf-8') as f:
    layout_content = f.read()
    
# basic.html has {% include nav_basic.html %} -> we want {% include nav_python.html %}
python_layout_content = layout_content.replace("{% include nav_basic.html %}", "{% include nav_python.html %}")

with codecs.open(python_layout_path, 'w', 'utf-8') as f:
    f.write(python_layout_content)
print("Created _layouts/python.html.")

# 3. Duplicate include templates
nav_basic_path = os.path.join(src_dir, "_includes", "nav_basic.html")
nav_python_path = os.path.join(src_dir, "_includes", "nav_python.html")

with codecs.open(nav_basic_path, 'r', 'utf-8') as f:
    nav_content = f.read()

# nav_basic.html has site.data.basic.main -> site.data.python.main
python_nav_content = nav_content.replace("site.data.basic.main", "site.data.python.main")

with codecs.open(nav_python_path, 'w', 'utf-8') as f:
    f.write(python_nav_content)
print("Created _includes/nav_python.html.")

# 4. Modify all python markdown files to use layout: python
python_md_files = glob.glob(os.path.join(src_dir, "python", "**", "*.md"), recursive=True)

for md_file in python_md_files:
    with codecs.open(md_file, 'r', 'utf-8') as f:
        md_content = f.read()
    
    # Simple replacement assuming frontmatter starts immediately
    if "layout: basic" in md_content:
        md_content = md_content.replace("layout: basic", "layout: python")
        with codecs.open(md_file, 'w', 'utf-8') as f:
            f.write(md_content)
        print(f"Updated layout in {md_file}")

print("Done.")

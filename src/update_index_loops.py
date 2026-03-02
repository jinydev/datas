import os
import re

index_path = r"d:\site\jinydev\datas\src\python\index.md"

with open(index_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace block in the markdown section 02 (Control Flow)
old_block = """  - [3.2.3 반복문 for와 while](02_control_flow/03_for_while_loops/)
  - [3.2.4 예외 처리](02_control_flow/04_exceptions/)"""

new_block = """  - [3.2.3 반복문 for](02_control_flow/03_for_loop/)
  - [3.2.4 반복문 while](02_control_flow/04_while_loop/)
  - [3.2.5 예외 처리](02_control_flow/05_exceptions/)"""

if old_block in text:
    text = text.replace(old_block, new_block)
else:
    # Just in case we already modified it or it's formatted slightly differently, let's use a regex fallback
    text = re.sub(r"- \[3\.2\.3.*?03_for_while_loops/\)", "- [3.2.3 반복문 for](02_control_flow/03_for_loop/)\n  - [3.2.4 반복문 while](02_control_flow/04_while_loop/)", text)
    text = re.sub(r"- \[3\.2\.4.*?04_exceptions/\)", "- [3.2.5 예외 처리](02_control_flow/05_exceptions/)", text)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Index updated successfully.")

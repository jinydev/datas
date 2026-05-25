import os
import glob
import re
import io
import sys
import contextlib

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def mock_display(*args, **kwargs):
    for arg in args:
        print(arg)

# We will patch plt.show() inside the exec environment
plt_show_original = plt.show

def execute_blocks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find python blocks. We capture the block including the backticks.
    pattern = re.compile(r'(```python\n(.*?)\n```)', re.DOTALL)
    
    matches = list(pattern.finditer(content))
    if not matches:
        return

    # Globals for this file execution
    env_globals = {
        'pd': pd,
        'sns': sns,
        'plt': plt,
        'display': mock_display,
        '__builtins__': __builtins__
    }

    # Execute a setup block if needed
    # But seaborn and plt might need to be re-imported locally if the user code has `import seaborn as sns`
    # Python's exec will just override them in the dictionary, which is fine.

    new_content = ""
    last_end = 0

    base_dir = os.path.dirname(file_path)
    img_dir = os.path.join(base_dir, 'img')
    os.makedirs(img_dir, exist_ok=True)

    block_idx = 1
    for match in matches:
        full_block = match.group(1)
        code = match.group(2)
        start = match.start()
        end = match.end()

        # Append text before this block
        new_content += content[last_end:end]

        # Prepare to capture output
        f_out = io.StringIO()
        svg_filename = f"exec_step_{block_idx}.svg"
        svg_path = os.path.join(img_dir, svg_filename)

        # Patch plt.show to save fig instead
        svg_created = False
        def mock_show(*args, **kwargs):
            nonlocal svg_created
            if plt.get_fignums():
                plt.savefig(svg_path, format='svg', bbox_inches='tight')
                svg_created = True
                plt.close("all")
        
        # Inject our mock
        env_globals['plt'].show = mock_show

        with contextlib.redirect_stdout(f_out):
            try:
                exec(code, env_globals)
                # If the code creates a figure but forgets to call plt.show(), we should check and save it anyway.
                # Actually, many seaborn functions create plots without calling show(). 
                # Let's save if there's an active figure after block execution.
                if plt.get_fignums():
                    plt.savefig(svg_path, format='svg', bbox_inches='tight')
                    svg_created = True
                    plt.close("all")
            except Exception as e:
                print(f"Error: {e}")

        output_text = f_out.getvalue()
        
        # Build the result markdown
        result_md = ""
        has_text = bool(output_text.strip())
        has_img = svg_created

        if has_text or has_img:
            result_md += "\n\n> **💻 [실행 결과]**\n"
            if has_text:
                result_md += f"> ```text\n"
                for line in output_text.strip().split('\n'):
                    result_md += f"> {line}\n"
                result_md += f"> ```\n"
            if has_img:
                # Need to use the relative path for the markdown link
                result_md += f"> ![실행 결과 시각화](img/{svg_filename})\n"
        
        new_content += result_md
        last_end = end
        block_idx += 1

    new_content += content[last_end:]

    # Save the updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Processed: {file_path}")

def main():
    practice_dir = "/Users/hojin9/dev/jinysite/datas/src/practice"
    files = glob.glob(os.path.join(practice_dir, "*", "index.md"))
    
    # Sort files to execute them in order 
    files.sort()
    
    for file_path in files:
        # Avoid processing if already processed (check for 💻 [실행 결과])
        with open(file_path, 'r', encoding='utf-8') as f:
            if '💻 [실행 결과]' in f.read():
                print(f"Skipping already processed: {file_path}")
                continue
                
        print(f"Running: {file_path}")
        execute_blocks(file_path)

if __name__ == "__main__":
    main()

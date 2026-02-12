import os
import shutil
import re

base_path = '/Users/hojin8/docs/070.강의/c01.빅데이터분석/[(파이썬으로 배우는 데이터분석 입문) 코드와 콘텐츠]'

def reorganize():
    # List all files in the base directory
    files = [f for f in os.listdir(base_path) if f.endswith('.md') and f.startswith('ch')]
    
    for md_file in files:
        print(f"Processing {md_file}...")
        
        # Define paths
        old_md_path = os.path.join(base_path, md_file)
        folder_name = os.path.splitext(md_file)[0]
        new_folder_path = os.path.join(base_path, folder_name)
        new_img_dir = os.path.join(new_folder_path, 'img')
        new_md_path = os.path.join(new_folder_path, md_file)
        
        # Create directories
        os.makedirs(new_img_dir, exist_ok=True)
        
        # Read markdown content
        with open(old_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all image links: ![...](images/filename)
        # Regex to capture the alt text and the image path
        # Assuming the current format is ![Slide X](images/filename.png)
        # We want to change it to ![Slide X](img/filename.png) and move the file.
        
        def replace_link_and_move_image(match):
            alt_text = match.group(1)
            old_rel_path = match.group(2) # e.g. images/filename.png
            
            # Extract filename
            img_filename = os.path.basename(old_rel_path)
            
            # Paths for moving
            old_img_path = os.path.join(base_path, old_rel_path)
            new_img_path = os.path.join(new_img_dir, img_filename)
            
            if os.path.exists(old_img_path):
                # Move the image
                shutil.move(old_img_path, new_img_path)
                print(f"Moved {img_filename} to {new_img_dir}")
            else:
                # Check if it was already moved (e.g. run script twice)
                if not os.path.exists(new_img_path):
                    print(f"Warning: Image {old_rel_path} not found.")
            
            # Return new link
            return f"![{alt_text}](img/{img_filename})"

        # Update content
        # Pattern matches ![alt](images/...)
        pattern = r'!\[(.*?)\]\((images/.*?)\)'
        new_content = re.sub(pattern, replace_link_and_move_image, content)
        
        # Write new markdown file
        with open(new_md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Created {new_md_path}")
        
        # Remove old markdown file
        os.remove(old_md_path)
        print(f"Removed {old_md_path}")

if __name__ == "__main__":
    reorganize()

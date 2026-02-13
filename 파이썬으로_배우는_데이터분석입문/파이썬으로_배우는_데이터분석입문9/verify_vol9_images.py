
import re
import os
import urllib.parse
import unicodedata

markdown_file = "파이썬으로_배우는_데이터분석입문9.md"
img_dir = "img"

def normalize_str(s):
    return unicodedata.normalize('NFC', s)

def main():
    if not os.path.exists(img_dir):
        print(f"Error: Directory {img_dir} does not exist.")
        return

    # Get list of actual files in img dir, normalized
    actual_files = {normalize_str(f) for f in os.listdir(img_dir)}
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all image links: ![...](img/filename)
    # Regex captures the filename part after img/
    matches = re.findall(r'!\[.*?\]\((?:img|%s)/(.*?)\)' % img_dir, content)
    
    missing_files = []
    
    print(f"Found {len(matches)} image references in markdown.")
    
    for filename in matches:
        # Unquote URL just in case (though usually simple filenames)
        filename_decoded = urllib.parse.unquote(filename)
        filename_norm = normalize_str(filename_decoded)
        
        if filename_norm not in actual_files:
            missing_files.append(filename_decoded)

    if missing_files:
        print(f"Found {len(missing_files)} missing images:")
        for f in missing_files:
            print(f" - {f}")
    else:
        print("All image references are valid.")

if __name__ == "__main__":
    main()

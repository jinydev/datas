import os
import re
import shutil

csv_dir = "/Users/hojin9/dev/jinysite/datas/src/practice/csv_data"
practice_dir = "/Users/hojin9/dev/jinysite/datas/src/practice"

if not os.path.exists(csv_dir):
    print("csv_data directory does not exist.")
    exit(0)

# Get all directories in src/practice/
folders = [d for d in os.listdir(practice_dir) if os.path.isdir(os.path.join(practice_dir, d)) and d not in ['csv_data', 'midterm', 'final', 'wrapup']]

# Map folders by their number prefix
folder_by_num = {}
for folder in folders:
    num_match = re.match(r'^(\d+)_', folder)
    if num_match:
        folder_by_num[int(num_match.group(1))] = folder

csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
moved_count = 0
unmapped = []

for csv_file in csv_files:
    # Try to find number suffix
    suffix_match = re.search(r'_(\d+)\.csv$', csv_file)
    target_folder = None
    
    if suffix_match:
        num = int(suffix_match.group(1))
        if num in folder_by_num:
            target_folder = folder_by_num[num]
    else:
        # Fallback to name matching
        name_clean = re.sub(r'[\-_]', ' ', csv_file.replace('.csv', '')).lower()
        words = name_clean.split()
        
        best_match = None
        best_overlap = 0
        for folder in folders:
            folder_clean = re.sub(r'[\-_]', ' ', folder).lower()
            overlap = 0
            for w in words:
                # Stemming check or simple containment
                if w in folder_clean or w[:-1] in folder_clean if len(w) > 3 else False:
                    overlap += 1
            if overlap > best_overlap:
                best_overlap = overlap
                best_match = folder
        
        if best_overlap > 0:
            target_folder = best_match

    if target_folder:
        src_path = os.path.join(csv_dir, csv_file)
        dest_path = os.path.join(practice_dir, target_folder, csv_file)
        shutil.move(src_path, dest_path)
        print(f"Moved: {csv_file} -> {target_folder}/")
        moved_count += 1
    else:
        unmapped.append(csv_file)

print(f"Moved {moved_count} files.")
if unmapped:
    print(f"Failed to map files: {unmapped}")
else:
    # Check if directory is empty and delete it
    if len(os.listdir(csv_dir)) == 0:
        os.rmdir(csv_dir)
        print("csv_data directory is empty and has been deleted.")
    else:
        print(f"csv_data is not empty: {os.listdir(csv_dir)}")

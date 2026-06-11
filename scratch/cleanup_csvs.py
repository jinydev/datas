import os
import re

practice_dir = "/Users/hojin9/dev/jinysite/datas/src/practice"

# 1. First, perform the 9 special renames/moves to ensure correct files are in place
special_moves = [
    ("src/practice/31_netflix/netflix_titles.csv", "src/practice/31_netflix/netflix.csv"),
    ("src/practice/32_spotify/spotify_songs.csv", "src/practice/32_spotify/spotify.csv"),
    ("src/practice/33_airbnb/airbnb_listings.csv", "src/practice/33_airbnb/airbnb.csv"),
    ("src/practice/186_geothermal_heat_recovery/mall_customers.csv", "src/practice/34_customer_segmentation/customer_segmentation.csv"),
    ("src/practice/35_retail_sales/retail_store_sales.csv", "src/practice/35_retail_sales/retail_sales.csv"),
    ("src/practice/36_fifa_world_cup/fifa_world_cup_matches.csv", "src/practice/36_fifa_world_cup/fifa_world_cup.csv"),
    ("src/practice/37_covid19/covid_vaccination_vs_cases.csv", "src/practice/37_covid19/covid19.csv"),
    ("src/practice/39_food_delivery/food_delivery_orders.csv", "src/practice/39_food_delivery/food_delivery.csv"),
    ("src/practice/183_smart_thermostat_control/pokemon_stats.csv", "src/practice/40_pokemon/pokemon.csv"),
]

print("=== Phase 1: Special Renames and Moves ===")
for src_rel, dest_rel in special_moves:
    src = os.path.join("/Users/hojin9/dev/jinysite/datas", src_rel)
    dest = os.path.join("/Users/hojin9/dev/jinysite/datas", dest_rel)
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        # If destination already exists, remove it first
        if os.path.exists(dest):
            os.remove(dest)
        os.rename(src, dest)
        print(f"Renamed/Moved: {src_rel} -> {dest_rel}")
    else:
        print(f"Source not found (already moved?): {src_rel}")

# 2. Phase 2: Scan all practice directories, parse index.md, and delete non-referenced CSVs
print("\n=== Phase 2: Scanning and cleaning up unnecessary CSVs ===")

folders = [d for d in os.listdir(practice_dir) if os.path.isdir(os.path.join(practice_dir, d)) and d not in ['midterm', 'final', 'wrapup']]

deleted_count = 0
kept_count = 0

for folder in sorted(folders):
    folder_path = os.path.join(practice_dir, folder)
    idx_path = os.path.join(folder_path, "index.md")
    
    if not os.path.exists(idx_path):
        continue
        
    with open(idx_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Search for read_csv patterns
    read_csv_patterns = [
        r"pd\.read_csv\(['\"](.*?)['\"]\)",
        r"read_csv\(['\"](.*?)['\"]\)"
    ]
    matches = []
    for pattern in read_csv_patterns:
        matches.extend(re.findall(pattern, content))
        
    # We want to resolve the basenames of the read CSVs
    active_csvs = set()
    for m in matches:
        active_csvs.add(os.path.basename(m))
        
    # Find all CSV files currently in this directory
    csvs_in_dir = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    if active_csvs:
        for csv_file in csvs_in_dir:
            if csv_file in active_csvs:
                kept_count += 1
            else:
                file_to_del = os.path.join(folder_path, csv_file)
                os.remove(file_to_del)
                print(f"Deleted unnecessary CSV: {folder}/{csv_file} (Not referenced in code)")
                deleted_count += 1
    else:
        # If no read_csv was found in index.md, we keep the CSV files just in case
        kept_count += len(csvs_in_dir)

print(f"\nPhase 2 Complete. Kept {kept_count} active CSV files, deleted {deleted_count} unnecessary CSV files.")

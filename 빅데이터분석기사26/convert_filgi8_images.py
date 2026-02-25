
import os
from PIL import Image

def convert_png_to_jpg(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):
            png_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, os.path.splitext(filename)[0] + ".jpg")
            
            try:
                with Image.open(png_path) as img:
                    rgb_img = img.convert('RGB')
                    rgb_img.save(jpg_path)
                print(f"Converted {filename} to {os.path.basename(jpg_path)}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    img_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26/빅데이터분석기사26_필기8/img"
    convert_png_to_jpg(img_dir)


import os
from PIL import Image

def convert_images_to_png(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    # Create a new filename for the converted image
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_converted.png"
                    new_filepath = os.path.join(directory, new_filename)
                    
                    # Save as PNG
                    img.save(new_filepath, "PNG")
                    print(f"Converted {filename} to {new_filename}")
                    
                    # Optionally remove the original file if you want, or just keep both
                    # os.remove(filepath) 
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

image_dir = "temp_images_86_90"
convert_images_to_png(image_dir)

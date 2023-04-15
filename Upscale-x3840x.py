#! /bin/bash
#! pip install pillow

import os
import sys
from PIL import Image

input_folder = "."

def upscale_image(input_folder, max_size=3840):
    try:
        with Image.open(image_path) as img:
            width, height = img.size

            if width <= max_size and height <= max_size:
                return

            if width > height:
                new_width = max_size
                new_height = int((new_width * height) / width)
            else:
                new_height = max_size
                new_width = int((new_height * width) / height)

            new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
            new_img.save(image_path)

            print(f"Upscaled image: {image_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

if len(sys.argv) < 2:
    print("Usage: python upscale_images.py <folder_path>")
    sys.exit(1)

folder_path = sys.argv[1]

if not os.path.isdir(folder_path):
    print(f"Folder not found: {folder_path}")
    sys.exit(1)

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            file_path = os.path.join(root, filename)
            upscale_image(input_folder)

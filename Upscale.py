

from PIL import Image
import os
import glob

def resize_image(img, max_size=3840):
    width, height = img.size
    aspect_ratio = float(width) / float(height)

    if width > height:
        new_width = max_size
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = max_size
        new_width = int(new_height * aspect_ratio)

    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    return img

input_dir = 'input_folder'
output_dir = 'output_folder'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file in glob.glob(f"{input_dir}/*.*"):
    img = Image.open(file)
    resized_img = resize_image(img)
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(file))[0] + '.jpg')
    resized_img.save(output_file, 'JPEG', quality=88)

print("Images successfully converted and resized.")

import os
from PIL import Image

def resize_image(image, new_width, new_height):
    image = image.resize((new_width, new_height))
    return image

# Get the path to the directory containing the images
image_dir = "/Users/akshay.khanna/Documents/tech_book_covers"

# Get a list of all the files in the directory
image_files = os.listdir(image_dir)

# Create a new directory to store the resized images
resized_image_dir = "/Users/akshay.khanna/Documents/tech_audio_book_covers"
if not os.path.exists(resized_image_dir):
    os.makedirs(resized_image_dir)

# Resize each image and save it to the new directory
for image_file in image_files:
    image = Image.open(os.path.join(image_dir, image_file))
    resized_image = resize_image(image, new_width=3000, new_height=3000)
    resized_image.save(os.path.join(resized_image_dir, image_file))
from PIL import Image
import shutil
import os
import sys
import random

root = os.getcwd()
print("You're currently in this folder:")
print(root)

print("Your origin folder is:")
image_folder = root + "\\imagestobeproccesed\\"

destination_folder = root + "\\placeimagesinhere\\"

print(image_folder)

print("Files present:")
for root, dirs, files in os.walk(image_folder):  
    for filename in files:
        print(filename)
        full_path = image_folder + filename
        new_file = filename[-3:] + str(random.randint(1,999)) + "." + filename[-3:]
        shutil.move(full_path, (destination_folder + new_file))
    break

print("Finished moving and renaming files.")

moved_image = destination_folder + new_file

print("Now checking for jpg and converting if not.")

for root,dirs, files in os.walk(destination_folder):
    for filename in files:
        if filename[-3:] != "jpg":
            print("Converting", filename, "to jpg.")
            im = Image.open(destination_folder + filename)
            png_filename = filename[:-3] + "jpg"
            print(png_filename)
            im.mode
            rgb_im = im.convert('RGB')
            rgb_im.save(destination_folder + png_filename, 'JPEG', quality=95)
            os.remove(destination_folder + filename)
            print(".png converted to .jpg and original .png removed.")

print("Everything done! Press enter to exit.")
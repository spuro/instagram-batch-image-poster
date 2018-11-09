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
        new_file = filename[-3:] + str(random.randint(1,999999)) + "." + filename[-3:]
        shutil.move(full_path, (destination_folder + new_file))
    else:
        print("No files in " + image_folder)
        
print("Finished moving and renaming files.")

try:
    moved_image = destination_folder + new_file
except NameError as e:
        print(e)
        print("Whatever")

print("Now checking for jpg and converting if not.")

#fixes possible error "OSError: image file is truncated"
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

for root, dirs, files in os.walk(destination_folder):
    for filename in files:
        rules = [filename[-3:] != "jpg",
                 filename[-3:] != "JPG"]
        if all(rules):
            print("Converting", filename, "to jpg.")
            im = Image.open(destination_folder + filename)
            png_filename = filename[:-3] + "jpg"
            print(png_filename)
            im.mode
            rgb_im = im.convert('RGB')  
            rgb_im.save(destination_folder + png_filename, 'JPEG', quality=95)
            os.remove(destination_folder + filename)
            print(".png converted to .jpg and original .png removed.")

#Since the posting bot requires images with an aspect ratio of 1:1:
##This chunk adds white borders around each image to make it 1:1 without any cropping.
for root, dirs, files in os.walk(destination_folder):
    for filename in files:
        print(filename)
        im = Image.open(destination_folder + filename, "r")
        height = im.height
        width = im.width
        if width != height:
            print("Resizing and adding white background to: " + filename)
            print(filename + " dimensions: " + str(height) + " x " +  str(width))
            if width > height:
                print(filename + "'s width is larger than its height.")
                
                bg = Image.new('RGB', (width, width), (255, 255, 255))
                bigside = width if width > height else height
                centre = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))
                print(centre)
                bg.paste(im, centre)
                bg.save(destination_folder + "cropped_" + filename)
                os.remove(destination_folder + filename)
                
            else:
                print(filename + "'s height is larger than its width.")

                bg = Image.new('RGB', (height, height), (255, 255, 255))
                bigside = width if width > height else height
                centre = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))
                print(centre)
                bg.paste(im, centre)
                bg.save(destination_folder + "cropped_" + filename)
                os.remove(destination_folder + filename)
        else:
            print("This image is already square.")



input("Everything done! Press enter to exit.")

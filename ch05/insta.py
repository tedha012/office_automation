import time
import os
from PIL import Image
import sys

print("Process Strat.")

start_time = time.time()

directory = sys.argv[1]

background_color = sys.argv[2]

out_dir = "squared_images"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

input_files = os.listdir(directory)

for filename in input_files:
    name, exp = filename.strip().split(".")
    if exp not in "JPG jpg JPEG jpeg PNG png BMP bmp":
        continue

    image = Image.open(directory + "/" + filename)

    Xdim, Ydim = image.size

    if Xdim > Ydim:
        new_size = Xdim
        x_offset = 0
        y_offset = int((Xdim - Ydim) / 2)
    else:
        new_size = Ydim
        x_offset = int((Ydim - Xdim) / 2)
        y_offset = 0

    new_image = Image.new("RGBA", (new_size, new_size), background_color)

    new_image.paste(image, (x_offset, y_offset))

    new_image.save(out_dir + "/" + name + ".png")

    image.close()
    new_image.close()

print("Process Done")

end_time = time.time()
print("The Job Took : " + str(end_time - start_time) + " secondes.")

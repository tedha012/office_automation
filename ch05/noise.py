import time
import os
import numpy as np
from PIL import Image

# Start message
print("Process Start")

# record start time
start_time = time.time()

# image files numbers
NUM_SAMPLES = 1000

# making a directory
out_dir = "random_image"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# making a random image files in a directory
for i in range(NUM_SAMPLES):
    name = str(time.time())[-7:] + ".png"
    # 100 ~ 400 random 2 int numbers
    Xdim, Ydim = np.random.randint(100, 400, size=2)
    image = np.random.randint(256, size=(Xdim, Ydim, 3)).astype("uint8")
    result = Image.fromarray(image)
    result.save(out_dir + "/" + name)
    result.close()

print("Process Done")

end_time = time.time()
print("The Job Took" + str(end_time - start_time) + "secondes.")

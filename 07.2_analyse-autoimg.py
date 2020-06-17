# open image file using PIL
# plot image using matplotlib
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# open the input image as numpy array
img = np.array(Image.open("car.png"), dtype = np.uint8)

# get pixel brightness level

min=np.min(img)
max=np.max(img)
print(min, max)

# show image
plt.title("car.png", fontsize=10)  # set title and fontsize
plt.imshow(img)                    # set image to show
plt.show()                         # enable show image
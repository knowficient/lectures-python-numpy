# convert colour image into grayscale using manual numpy matrix conversion
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# GrayScale Method 1: Function RGB to Gray Level
# luminance (E'y) in Rec.ITU-R BT.601-7l
# Gray = 0.299*r + 0.587*g + 0.114*b
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# Open the input image as numpy array
img = np.array(Image.open("car.png"), dtype = np.uint8)

# Convert RGB to Grayscale
grayfloat = rgb2gray(img)

#convert array into uint8 instead of float
imgy = Image.fromarray(grayfloat.astype(np.uint8))
imgy.save('car-op-gray.png')


# Set plot size in inch
plt.figure(figsize=(10, 5), dpi=140)

# Plot gray image before improving contrast
plt.subplot(121)
plt.axis('off')
plt.title('Original', fontsize=10)
plt.imshow(img)

# Plot image with color map gray and data value min to max
plt.subplot(122)
plt.axis('off')
plt.title('Gray', fontsize=10)
plt.imshow(imgy, cmap = plt.get_cmap(name = 'gray'), vmin=0, vmax=255)

# Show the plot
plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=0.9)
plt.show()

# improve grayscale contrast using look up table of numpy array
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# open the input image as numpy array
gray = np.array(Image.open("car-op-gray.png"), dtype = np.uint8)
# get brightness level
gmin=np.min(gray)
gmax=np.max(gray)
print(gmin, gmax)

# make a Look-Up Table to translate image values
lut=np.zeros(256,dtype=np.uint8) #[0 0 0 .. 256th 0]
lut[gmin:gmax+1]=np.linspace(start=0,stop=255,num=(gmax-gmin)+1,endpoint=True,dtype=np.uint8)

# apply Look-Up Table and save resulting image
impcontrast = lut[gray]
impc = Image.fromarray(impcontrast)
impc.save('car-op-impcon-gray.png')

# set plot size in inch
plt.figure(figsize=(10, 5), dpi=140)

# plot gray image before improving contrast
plt.subplot(121)
plt.axis('off')
plt.title('Bad Contrast', fontsize=10)
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# plot gray image after improving contrast
plt.subplot(122)
plt.axis('off')
plt.title('Improved Contrast', fontsize=10)
plt.imshow(impcontrast, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show the plot
plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=0.9)
plt.show()
'''
 * Python program to use contours to count the objects in an image.
 *
 * usage: python Contours.py <filename> <threshold>
'''
import skimage
import skimage.filters
import skimage.measure
import sys

import matplotlib.pyplot as plt

# read command-line arguments
filename = sys.argv[1]
t = float(sys.argv[2])

# read original image
image = skimage.io.imread(fname=filename, as_gray=True)

blurred = skimage.filters.gaussian(image, sigma=2.5)
binary = blurred > t

# find contours
contours = skimage.measure.find_contours(
    binary, level=.5)

# print table of contours and sizes
print(f"Found {len(contours)} objects.")
for (i, c) in enumerate(contours):
    print(f"\tSize of contour {i}: {len(c)}")

# draw contours over original image
fig, ax = plt.subplots()
ax.imshow(image, cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

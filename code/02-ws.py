"""
 * Python program to create an image containing a single, white square.
 * The image is saved in two formats: bmp and jpg.
 *
 * usage: python 02-ws.py <dim>
"""
import skimage.io
import sys
import numpy as np

dim = int(sys.argv[1])

img = np.zeros((dim, dim, 3), dtype="uint8")
img.fill(255)

skimage.io.imsave(fname="data/02-ws.bmp", arr=img)
skimage.io.imsave(fname="data/02-ws.jpg", arr=img)

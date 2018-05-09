'''
 * Python program to create an image containing a single, white square.
 * The image is saved in two formats: bmp and jpg.
 *
 * usage: python ws.py <dim>
'''

import cv2, sys, numpy as np

dim = int(sys.argv[1])

img = np.zeros((dim, dim, 3), dtype="uint8")
img.fill(255)

cv2.imwrite("ws.bmp", img)
cv2.imwrite("ws.jpg", img)

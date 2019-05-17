'''
 * Python program to use contours to crop the objects in an image.
 *
 * usage: python ContourCrop.py <filename> <threshold>
'''
import cv2, sys, numpy as np

# read command-line arguments
filename = sys.argv[1]
t = int(sys.argv[2])

# read original image
image = cv2.imread(filename = filename)

# create binary image
gray = cv2.cvtColor(src = image, code = cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(src = gray, 
    ksize = (5, 5), 
    sigmaX = 0)

(t, binary) = cv2.threshold(src = blur, 
    thresh = t, 
    maxval = 255, 
    type = cv2.THRESH_BINARY)

# find contours
(_, contours, _) = cv2.findContours(image = binary, 
    mode = cv2.RETR_EXTERNAL, 
    method = cv2.CHAIN_APPROX_SIMPLE)

# create all-black mask image
mask = np.zeros(shape = image.shape, dtype = "uint8")

# draw white rectangles for each object's bounding box
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)

    cv2.rectangle(img = mask, 
        pt1 = (x, y), 
        pt2 = (x + w, y + h), 
        color = (255, 255, 255), 
        thickness = -1)
        
# apply mask to the original image
image = cv2.bitwise_and(src1 = image, src2 = mask)

# display masked image
cv2.namedWindow(winname = "output", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "output", mat = image)
cv2.waitKey(delay = 0)

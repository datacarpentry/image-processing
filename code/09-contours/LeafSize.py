'''
 * Python script to measure the size of an object, based on
 * the size of a reference object in the image.
 *
 * usage: python LeafSize.py <filename> <threshold>
'''
import cv2, sys

# read command-line arguments
filename = sys.argv[1]
t = int(sys.argv[2])

# read image as grayscale
image = cv2.imread(filename = filename, flags = cv2.IMREAD_GRAYSCALE)

# blur and threshold
blur = cv2.GaussianBlur(src = image,
    ksize = (5, 5),
    sigmaX = 0)

(t, binary) = cv2.threshold(src = blur,
    thresh = t,
    maxval = 255,
    type = cv2.THRESH_BINARY_INV)

# find contours
(_, contours, _) = cv2.findContours(image = binary, 
    mode = cv2.RETR_EXTERNAL,
    method = cv2.CHAIN_APPROX_SIMPLE)

# determine average length of contours
avg = 0
for c in contours:
    avg += len(c)
    
avg /= len(contours)

# save index of largest contour
largestIdx = -1
largestSize = -1

# find size of the reference square
for i, c in enumerate(contours):
    # keep track of largest one
    if len(c) > largestSize:
        largestSize = len(c)
        largestIdx = i

    # now only look at the larger contours
    if len(c) > avg / 10:
        # get approximating polygon
        epsilon = 0.1 * cv2.arcLength(curve = c, closed = True)

        approx = cv2.approxPolyDP(curve = c,
            epsilon = epsilon,
            closed = True)

        # the one with four vertices should be the reference
        if len(approx) == 4:
            # save bounding rectangle info
            x, y, w, h = cv2.boundingRect(c)

# calculate cm per pixels scale
scaleX = 2.54 / w
scaleY = 2.54 / h

# get bounding box for the largest contour
x, y, w, h = cv2.boundingRect(contours[largestIdx])

# calculate height and width of the leaf
height = h * scaleY
width = w * scaleX

# print results
print('%0.2f cm wide x %0.2f cm tall' % (width, height))


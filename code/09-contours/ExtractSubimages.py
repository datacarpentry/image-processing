'''
 * Python program to use contours to extract the objects in an image.
'''
import cv2, sys

# read command-line arguments
filename = sys.argv[1]
t = int(sys.argv[2])

# read original image
image = cv2.imread(filename = filename)

# create binary image
gray = cv2.cvtColor(src = image, code = cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(srck = gray, 
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

# use the contours to extract each image, into a new sub-image
for (i, c) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(c)
    # WRITE YOUR CODE HERE!
    # use slicing and the (x, y, w, h) values of the bounding
    # box to create a subimage based on this contour
    
    # WRITE YOUR CODE HERE!
    # save the subimage as sub-x.jpg, where x is the number
    # of this contour. HINT: try "sub-{0}".format(i) to 
    # create the filename

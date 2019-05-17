'''
 * Python script to practice simple thresholding.
 *
 * usage: python ThresholdPractice.py <filename> <kernel-size> <threshold>
'''
import cv2, sys

# get filename, kernel size, and threshold value from command line
filename = sys.argv[1]
k = int(sys.argv[2])
t = int(sys.argv[3])

# read and display the original image
image = cv2.imread(filename = filename)
cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original", mat = image)
cv2.waitKey(delay = 0)

# blur and grayscale before thresholding
blur = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(src = blur, 
    ksize = (k, k), 
    sigmax = 0)

# perform inverse binary thresholding 
# MODIFY CODE HERE!
(t, maskLayer) = cv2.threshold(src = blur, 
    thresh = t, 
    maxval = 255, 
    type = cv2.THRESH_BINARY_INV)

# make a mask suitable for color images
mask = cv2.merge(mv = [maskLayer, maskLayer, maskLayer])

# display the mask image
cv2.namedWindow(winname = "mask", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "mask", mat = mask)
cv2.waitKey(delay = 0)

# use the mask to select the "interesting" part of the image
sel = cv2.bitwise_and(src1 = img, src2 = mask)

# display the result
cv2.namedWindow(winname = "selected", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "selected", mat = sel)
cv2.waitKey(delay = 0)

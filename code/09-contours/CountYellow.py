'''
 * Python program to count the number of yellow dots in an image.
 *
 * usage: python CountYellow.py <filename> <kernel-size> <threshold>
'''
import cv2, sys, math, numpy as np

'''
 * Compute distance between two colors, as a 3D Euclidean distance.
'''
def colorDistance(kCol, uCol):
    # compute sum of square of differences between each channel 
    d = (kCol[0] - uCol[0])**2 + (kCol[1] - uCol[1])**2 + \
        (kCol[2] - uCol[2])**2
        
    # square root of sum is the Euclidean distance between the
    # two colors
    return math.sqrt(d)

'''
 * Main program starts here.
'''

# read and save command-line arguments
filename = sys.argv[1]
k = int(sys.argv[2])
t = int(sys.argv[3])

# read image, convert to grayscale, blur, and threshold to
# make binary image
image = cv2.imread(filename = filename)

gray = cv2.cvtColor(src = image, code = cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(src = gray, 
    ksize = (k, k), 
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

# create reference colors
YELLOW = (0, 255, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

# number of yellow dots
yellowCount = 0

# for each contour...
for c in contours:
    
    # ... only work with contours associated with actual dots
    if len(c) > avg / 2:
        
        # find centroid of shape
        M = cv2.moments(array = c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
        # find average color for 9 pixel kernel around centroid
        b = image[cy - 4 : cy + 5, cx - 4 : cx + 5, 0]
        g = image[cy - 4 : cy + 5, cx - 4 : cx + 5, 1]
        r = image[cy - 4 : cy + 5, cx - 4 : cx + 5, 2]
        
        bAvg = np.mean(b)
        gAvg = np.mean(g)
        rAvg = np.mean(r)
        
        # find distances to known reference colors
        dist = []
        dist.append(colorDistance(YELLOW, (bAvg, gAvg, rAvg)))
        dist.append(colorDistance(BLUE, (bAvg, gAvg, rAvg)))
        dist.append(colorDistance(GREEN, (bAvg, gAvg, rAvg)))
        
        # which one is closest?
        minDist = min(dist)
        # if it was yellow, count the shape
        if dist.index(minDist) == 0:
            yellowCount += 1

print("Yellow dots:", yellowCount)

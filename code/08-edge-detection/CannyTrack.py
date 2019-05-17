'''
 * Python script to demonstrate Canny edge detection
 * with trackbars to adjust the thresholds. 
 *
 * usage: python CannyTrack.py <filename>
'''
import cv2, sys

'''
 * Function to perform Canny edge detection and display the
 * result. 
'''
def cannyEdge():
    global image, minT, maxT
    edge = cv2.Canny(image = image, 
        threshold1 = minT, 
        threshold2 = maxT)

    cv2.imshow(winname = "edges", mat = edge)

'''
 * Callback function for minimum threshold trackbar.
''' 
def adjustMinT(v):
    global minT
    minT = v
    cannyEdge()

'''
 * Callback function for maximum threshold trackbar.
'''
def adjustMaxT(v):
    global maxT
    maxT = v
    cannyEdge()
    

'''
 * Main program begins here. 
'''
# read command-line filename argument
filename = sys.argv[1]

# load original image as grayscale
image = cv2.imread(filename = filename, flags = cv2.IMREAD_GRAYSCALE)

# set up display window with trackbars for minimum and maximum threshold
# values
cv2.namedWindow(winname = "edges", flags = cv2.WINDOW_NORMAL)

minT = 30
maxT = 150

# cv2.createTrackbar() does not support named parameters
cv2.createTrackbar("minT", "edges", minT, 255, adjustMinT)
cv2.createTrackbar("maxT", "edges", maxT, 255, adjustMaxT)

# perform Canny edge detection and display result
cannyEdge()
cv2.waitKey(delay = 0)


edge = cv2.Canny(image = image, 
    threshold1 = minT, 
    threshold2 = maxT)
cv2.imwrite('beads-out.jpg', edge)

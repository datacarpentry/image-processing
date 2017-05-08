'''
 * Python script to demonstrate Canny edge detection.
 *
 * usage: python CannyEdge.py <filename>
'''
import cv2, sys

'''
 * Function to perform Canny edge detection and display the
 * result. 
'''
def cannyEdge():
    global img, minT, maxT
    edge = cv2.Canny(img, minT, maxT)
    cv2.imshow("edges", edge)

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
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# set up display window with trackbars for minimum and maximum threshold
# values
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
minT = 30
maxT = 150
cv2.createTrackbar("minT", "edges", minT, 255, adjustMinT)
cv2.createTrackbar("maxT", "edges", maxT, 255, adjustMaxT)

# perform Canny edge detection and display result
cannyEdge()
cv2.waitKey(0)

'''
* Python script to ignore low intensity pixels in an image.
*
* usage: python HighIntensity.py <filename>
'''
import cv2, sys

# read input image, based on filename parameter
img = cv2.imread(sys.argv[1])
	
# display original image
cv2.namedWindow("original img", cv2.WINDOW_NORMAL)
cv2.imshow("original img", img)
cv2.waitKey(0)

# keep only high-intensity pixels
img[img < 128] = 0
		
# display modified image
cv2.namedWindow("modified img", cv2.WINDOW_NORMAL)
cv2.imshow("modified img", img)
cv2.waitKey(0)

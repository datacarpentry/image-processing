'''
* Python script to ignore low intensity pixels in an image.
*
* usage: python HighIntensity.py <filename>
'''
import cv2, sys

# read input image, based on filename parameter
image = cv2.imread(filename = sys.argv[1])
	
# display original image
cv2.namedWindow(winname = "original image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original image", mat = image)
cv2.waitKey(delay = 0)

# keep only high-intensity pixels
image[image < 128] = 0
		
# display modified image
cv2.namedWindow(winname = "modified image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "modified image", mat = image)
cv2.waitKey(delay = 0)

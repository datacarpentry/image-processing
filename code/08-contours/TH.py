import cv2, sys

def adjustThreshold(t):
    (t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY)
    cv2.imshow("image", binary)

filename = sys.argv[1]

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.createTrackbar("T", "image", 200, 255, adjustThreshold)

adjustThreshold(200)
cv2.waitKey(0)
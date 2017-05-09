#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:10:19 2017

@author: mark
"""

import cv2, sys, math, numpy as np

def colorDistance(kCol, uCol):
    d = (kCol[0] - uCol[0]) * (kCol[0] - uCol[0]) + \
        (kCol[1] - uCol[1]) * (kCol[1] - uCol[1]) + \
        (kCol[2] - uCol[2]) * (kCol[2] - uCol[2])
    return math.sqrt(d)

filename = sys.argv[1]
k = int(sys.argv[2])
t = int(sys.argv[3])

img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (k, k), 0)
(t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)

(_, contours, hierarchy) = cv2.findContours(binary, cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

#cmin = float("inf")
#cmax = -float("inf")
avg = 0
for c in contours:
    n = len(c)
#    if n < cmin:
#        cmin = n
#    if n > cmax:
#        cmax = n
    avg += n
    
avg /= len(contours)

#print("Number of contours:", len(contours))
#print("Largest:", cmax)
#print("Smallest:", cmin)
#print("Average:", avg)

yellow = (0, 255, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

yellowCount = 0

for c in contours:
    if len(c) > avg / 2:
        # find centroid of shape
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        
        # average color for 9 pixel kernel around centroid
        b = img[cy - 4 : cy + 4, cx - 4 : cx + 4, 0]
        g = img[cy - 4 : cy + 4, cx - 4 : cx + 4, 1]
        r = img[cy - 4 : cy + 4, cx - 4 : cx + 4, 2]
        
        bAvg = np.mean(b)
        gAvg = np.mean(g)
        rAvg = np.mean(r)
        
        # find distances to known colors
        dist = []
        dist.append(colorDistance(yellow, (bAvg, gAvg, rAvg)))
        dist.append(colorDistance(blue, (bAvg, gAvg, rAvg)))
        dist.append(colorDistance(green, (bAvg, gAvg, rAvg)))
        
        # which one is closest?
        minDist = min(dist)
        # if it was yellow, count the shape
        if dist.index(minDist) == 0:
            yellowCount += 1
        #cv2.drawContours(img, [c], -1, (0, 0, 255), 3)
        #cv2.circle(img, (cx, cy), 4, (0, 0, 255), -1)

print("Yellow dots:", yellowCount)
'''
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
'''
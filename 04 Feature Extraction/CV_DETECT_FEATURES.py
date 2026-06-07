import cv2
import numpy as np
import sys

import pip

filename = '04 Feature Extraction/R.jpg'
img = cv2.imread(filename)
# -------------- Harris -------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 5, 17, 0.04)
img[dst>0.01 * dst.max()] = [0, 255, 255]
#while (True):
cv2.imshow('Haris corners', img)
cv2.waitKey(0)

# -------------- SIFT --------------------

img = cv2.imread(filename)
img2 = img    
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT.create()
keypoints, descriptor = sift.detectAndCompute(gray,None)

img2 = cv2.drawKeypoints(image=img, outImage=img2, keypoints =
keypoints, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
color = (51, 163, 236))
cv2.imshow('sift_keypoints', img2)
cv2.waitKey(0)


# -------------- SURF --------------------

img = cv2.imread(filename)
img2 = img    
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#surf = cv2.xfeatures2d.SURF.create(400)
#keypoints, descriptor = surf.detectAndCompute(gray,None)
orb = cv2.ORB_create(nfeatures=400)
keypoints, descriptor = orb.detectAndCompute(gray,None)

img_with_keypoints = cv2.drawKeypoints(img, keypoints, None, (255, 0, 0), 4)

#cv2.imshow('SURF_keypoints', img_with_keypoints)
cv2.imshow('ORB_keypoints', img_with_keypoints)
cv2.waitKey(0)

cv2.destroyAllWindows()
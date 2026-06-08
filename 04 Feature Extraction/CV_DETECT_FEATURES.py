import cv2
import numpy as np

filename = '04 Feature Extraction/R.jpg'
img = cv2.imread(filename)

# -------------- Harris -------------------

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

copy = cv2.cornerHarris(gray, 5, 17, 0.04)

img[ copy > copy.max() * 0.01 ] = [0, 255, 255]

cv2.imshow('Haris corners', img)

# -------------- SIFT --------------------

img2 = img 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT.create()

keypoints, descriptor = sift.detectAndCompute(gray,None)

img2 = cv2.drawKeypoints(image=img, outImage=img2, keypoints = keypoints, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color = (0, 255, 255))

cv2.imshow('sift_keypoints', img2)

cv2.waitKey(0)

cv2.destroyAllWindows()
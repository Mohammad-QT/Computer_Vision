import cv2 
import numpy as np

filename = '01 Image Basics & Pixel Manipulation/P1.jpg'

image_colored = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)
image_grayscale = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

image = np.zeros((614, 1228, 3), dtype=np.uint8)

image[0:50,:] = [255,0,0]
image[50:100,:] = [0,255,0]
image[100:150,:] = [0,0,255]

image_colored[50:150, 50:150] = [0, 0, 255] 
roi = image_grayscale[200:300, 200:300]
image_colored[200:300, 200:300] = roi[:,:,None]

cv2.namedWindow("imageCreated", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Colored",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Grayscale",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("ROI",cv2.WINDOW_AUTOSIZE)

cv2.imshow("ROI", roi)
cv2.imshow('Colored', image_colored)
cv2.imshow('Grayscale', image_grayscale)
cv2.imshow('imageCreated', image)

print (image.shape)
print (image.size)
print (image.dtype)

cv2.waitKey(0)

pressed = cv2.waitKey(0)

if pressed == ord('s'):
    cv2.imwrite('Colored image', image_colored)
    cv2.imwrite('Grayscale image', image_grayscale)
    
elif pressed == ord('q'):
    cv2.destroyAllWindows()
import cv2
import numpy as np
from scipy import ndimage

filename = '03 Spatial Filtering & Edge Detection/Test_Image.jpg'

POS_clicked = [0,0]
clicked = False
global var_P1
global var_P2

def nothing(x):
    pass
def onMouse(event, x, y, flags, param):
    global POS_clicked
    global clicked
    if event == cv2.EVENT_MOUSEMOVE:
        POS_clicked = [x,y]
        print (image[y,x])
        
        clicked = True
        print (POS_clicked)
    

global image
global NewImage
#image = cv2.imread('Test_Image.jpg', cv2.IMREAD_ANYCOLOR)
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)


cv2.namedWindow("MAIN",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("EDGE",cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('P1', 'EDGE', 0, 255, nothing)
cv2.createTrackbar('P2', 'EDGE', 0, 255, nothing)

cv2.setMouseCallback("MAIN", onMouse)
#cv2.setMouseCallback("dst", onMouse)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or unable to read.")
else:
    # Display the image in a window named "Image Display"
    cv2.imshow('MAIN', image)

    #### Gaussian Blured
    blurred = cv2.GaussianBlur(image, (11,11), 0)
    g_hpf = image - blurred

    BlurredMedian = cv2.medianBlur(image, 5)
    BluredLaplacian = image;
    cv2.Laplacian(image, 0, BluredLaplacian, 5)
    normalizedInverseAlpha = (1.0 / 255) * (255 - image)
    Image_BluredLaplacian = BluredLaplacian * normalizedInverseAlpha

    cv2.imshow("Blured",blurred)
    cv2.imshow("BlurredMedian",BlurredMedian)
    cv2.imshow("BluredLaplacian",BluredLaplacian)
    cv2.imshow("Image_BluredLaplacian",Image_BluredLaplacian)

    # Loop to continuously read trackbar values and update edge detection
    while True:
        var_P1 = cv2.getTrackbarPos('P1', 'EDGE')
        var_P2 = cv2.getTrackbarPos('P2', 'EDGE')
        
        IMAGE_EDGE = cv2.Canny(image, var_P1, var_P2)
        cv2.imshow('EDGE', IMAGE_EDGE)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if (clicked == True):
        print (POS_clicked)
    
    # Close all the image windows
    cv2.destroyAllWindows()

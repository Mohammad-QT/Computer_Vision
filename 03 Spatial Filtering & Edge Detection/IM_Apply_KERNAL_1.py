import cv2
import numpy as np
from scipy import ndimage

filename = '03 Spatial Filtering & Edge Detection/Test_Image.jpg'

POS_clicked = [0,0]
clicked = False

def onMouse(event, x, y, flags, param):
    global POS_clicked
    global clicked

    if event == cv2.EVENT_MOUSEMOVE:
        POS_clicked = [x,y]

        print (image[y,x])
        print (dst[y,x])

        clicked = True

        print (POS_clicked)
    

global image
global NewImage

#image = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

kernel_3x3 = np.array([[-1, -1, -1], 
                       [-1, 8, -1], 
                       [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1], 
                       [-1,  1,  2,  1, -1],
                       [-1,  2,  4,  2, -1],
                       [-1,  1,  2,  1, -1],
                       [-1, -1, -1, -1, -1]])

kernel = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])


cv2.namedWindow("MAIN",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("3x3",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("5x5",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Blured",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("g_hpf",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("dst",cv2.WINDOW_AUTOSIZE)

#cv2.setMouseCallback("MAIN", onMouse)
cv2.setMouseCallback("dst", onMouse)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or unable to read.")
else:
    # Display the image in a window named "Image Display"
    cv2.imshow('MAIN', image)

    k3 = ndimage.convolve(image, kernel_3x3)
    k5 = ndimage.convolve(image, kernel_5x5)

    blurred = cv2.GaussianBlur(image, (11,11), 0)

    g_hpf = image - blurred

    dst = image
    cv2.filter2D(image, -1, kernel, dst)
    
    cv2.imshow("3x3", k3)
    cv2.imshow("5x5", k5)
    cv2.imshow("Blured",blurred)
    cv2.imshow("g_hpf",g_hpf)
    cv2.imshow("dst",dst)

    if (clicked == True):
        print (POS_clicked)

    # Wait for a key press indefinitely until a key is pressed
    # Press 'q' to close all windows
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close all the image windows
    cv2.destroyAllWindows()

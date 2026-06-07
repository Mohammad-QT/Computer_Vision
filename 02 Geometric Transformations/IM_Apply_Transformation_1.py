import cv2
import numpy as np
from scipy import ndimage

image = cv2.imread('02 Geometric Transformations/Test_Image.jpg', cv2.IMREAD_ANYCOLOR)
#image = cv2.imread('02 Geometric Transformations/Test_Image.jpg', cv2.IMREAD_GRAYSCALE)


cv2.namedWindow("MAIN",cv2.WINDOW_AUTOSIZE)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or unable to read.")
else:
    # Display the image in a window named "Image Display"
    cv2.imshow('MAIN', image)

    ###### Scaling #####
    scale_half = cv2.resize(image, None, fx=0.5, fy=0.5)
    scale_double = cv2.resize(image, None, fx=2, fy=2)
    new_width = 600
    new_height = 500
    scale_200_200 = cv2.resize(image,(new_width,new_height))

    cv2.imshow("Half Size", scale_half)
    cv2.imshow("Double Size", scale_double)
    cv2.imshow("scale_200_200", scale_200_200)
    #### ------------------------------------------
    #### Rotation ######
    # Get image center
    (h, w) = image.shape[:2]

    center = (w // 2, h // 2)

    # Rotation matrices
    rotate_45 = cv2.getRotationMatrix2D(center, 45, 1)
    rotate_90 = cv2.getRotationMatrix2D(center, 90, 1)

    # Apply rotation
    rotated_45 = cv2.warpAffine(image, rotate_45, (w, h))
    rotated_90 = cv2.warpAffine(image, rotate_90, (w, h))

    cv2.imshow("Rotated 45", rotated_45)
    cv2.imshow("Rotated 90", rotated_90)
     #-------------------------------------------
    ### TRanslation ##########
    # Translation matrix
    tx = 100   # shift right
    ty = 50    # shift down

    translation_matrix = np.float32([
        [1, 0, tx],
        [0, 1, ty]])

    translated = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

    cv2.imshow("Translated Image", translated)

# Wait for a key press indefinitely until a key is pressed
cv2.waitKey(0)

    # Close all the image windows
cv2.destroyAllWindows()

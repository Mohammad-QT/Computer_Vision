import cv2
import numpy as np

# بناء صورة سوداء وهمية بأبعاد 800 عرض و 800 طول و 3 قنوات ألوان (RGB)
# هذا السطر رح يكون بديل لسطر cv2.imread
image = np.zeros((800, 800, 3), dtype=np.uint8)

cv2.namedWindow("MAIN", cv2.WINDOW_AUTOSIZE)
cv2.imshow('MAIN', image)

# Read the image from the specified file path
# Use forward slashes (/) for cross-platform compatibility in the file path

# image = cv2.imread('P1.jpg', cv2.IMREAD_ANYCOLOR)

# ----- CHANGE DATA INSIDE IAMGE -------------
# EXAMPLE 001

# Change a single pixel at Row 100, Column 100 to a specific color [Blue, Green, Red]
image[100,100] = [125,255,120]

# Change a BLOCK of pixels (Rows 100 to 120, Columns 100 to 120)
# We only target color channel '0' (Blue) and set it to 150.
# Start at 100, and go up to (but don't include) 120.
image[100:120, 100:120, 0] = 150

# Change a bigger block of pixels to a specific BGR color
image[300:420, 100:120] = [125,255,120]

# Take the entire image (all rows ':', all columns ':') 
# and set color channel '1' (Green) to 0. This removes all green from the image!
image[:,:,1] = 0;

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or unable to read.")
else:
    # Display the image in a window named "Image Display"
    cv2.imshow('MAIN', image)

    # CHANGE INAGE INSDIDE EXAMPLE 002
    print (image.item(150,120,0) )
    image[150,120,0] = 250
    print (image.item(150,120,0) )

    # APPLY MY REGION OF INTEREST
    
    # STEP A: "Copy"
    # Grab a chunk of the image from Rows 300-400 and Columns 500-700. 
    # Save this chunk into a new variable called 'my_roi'.
    my_roi = image[300:400, 500:700]

    # STEP B: "Modify"
    # Turn every single pixel in this copied chunk completely white (255 is the max value).
    my_roi[:,:] = 255

    # STEP C: "Paste"
    # Take our modified white chunk and paste it back onto the original image 
    # in a completely different location (Rows 150-250, Columns 300-500).
    image[150:250, 300:500] = my_roi

    # Show the modified image in a window called 'Image NEW'
    cv2.imshow('Image NEW', image)

    # PRINT PARAMETERS FOR IMAGE
    print (image.shape)
    print (image.size)
    print (image.dtype)

    # Wait forever (0) until the user presses ANY key on the keyboard
    cv2.waitKey(0)

    # Once a key is pressed, close the graphical windows so the program can end cleanly
    cv2.destroyAllWindows()
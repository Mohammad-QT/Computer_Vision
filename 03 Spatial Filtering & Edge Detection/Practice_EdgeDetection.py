import cv2
import numpy as np

filename = '03 Spatial Filtering & Edge Detection/Test_Image.jpg'
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

def nothing(x):
    pass

if image is None:
    print("Error: Image not found or unable to read.")
else:
    cv2.imshow("Original", image)

    # ==================== TASK 0 ====================
    # TODO: Apply Gaussian Blur with kernel size 5
    # Display in window named "Task 0 - Gaussian Blur"

    g_blurred = cv2.GaussianBlur(image, (5,5), 0)
    blurred = image - g_blurred
    
    cv2.imshow("Task 0 - Gaussian Blur", blurred)
    
    # ==================== TASK 1 ====================
    # TODO: Apply Median Blur with kernel size 5
    # Display in window named "Task 1 - Median Blur"
    # HINT: cv2.medianBlur(image, 5)
    
    blurred_median = cv2.medianBlur(image, 5)
    cv2.imshow("Task 1 - Median Blur", blurred_median)
    
    # ==================== TASK 2 ====================
    # TODO: Apply Laplacian edge detection with kernel size 3
    # Method: Create output image, then use cv2.Laplacian(image, 0, dst, 3) 
    # Display in window named "Task 2 - Laplacian"
    # HINT: dst = image.copy() first, then pass to Laplacian
    
    copy = image

    laplacian_blurred = cv2.Laplacian(image, 0 , copy , 3)

    normallizedInverseAlpha = 1.0/255 * (255-image)
    Image_laplacian_blurred = laplacian_blurred * normallizedInverseAlpha

    cv2.imshow("Task 2 - Laplacian", Image_laplacian_blurred)
    
    # ==================== TASK 3 ====================
    # TODO: Apply Laplacian with kernel size 7 (different from Task 2)
    # Display in window named "Task 3 - Laplacian Large Kernel"
    # What's the difference from kernel size 3?
    
    copy2 = image

    laplacian_blurred2 = cv2.Laplacian(image , 0 , copy2 , 7)

    normallizedInverseAlpha2 = 1.0/255 * (255-image)

    image_laplacian_blurred2 = laplacian_blurred2 * normallizedInverseAlpha2

    cv2.imshow("Task 3 - Laplacian Large Kernel", image_laplacian_blurred2)
    
    # ==================== TASK 4 ====================
    # TODO: Apply Canny edge detection with thresholds P1=50, P2=150
    # Display in window named "Task 4 - Canny 50-150"
    # HINT: cv2.Canny(image, 50, 150)
    
    canny_50_150 = cv2.Canny(image, 50, 150)

    cv2.imshow("Task 4 - Canny 50-150", canny_50_150)
    
    # ==================== TASK 5 ====================
    # TODO: Apply Canny edge detection with thresholds P1=100, P2=200
    # Display in window named "Task 5 - Canny 100-200"
    # Compare with Task 4 - what changes?
    
    canny_100_200 = cv2.Canny(image, 100, 200)

    cv2.imshow("Task 5 - Canny 100-200", canny_100_200)
    
    # ==================== TASK 6 (BONUS) ====================
    # TODO: Create interactive Canny with trackbars!
    # 1. Create a window named "Canny Interactive"
    # 2. Create trackbar 'P1' (0-255) and 'P2' (0-255)
    # 3. Create a loop that reads trackbar values every frame
    # 4. Apply Canny with those values and display
    # 5. Press 'q' to exit
    # HINT: Check IM_EDGE_DETECTION.py for the trackbar structure!
    
    cv2.namedWindow("Canny Interactive", cv2.WINDOW_AUTOSIZE)
    
    cv2.createTrackbar('P1', 'Canny Interactive', 0, 255, nothing)
    cv2.createTrackbar('P2', 'Canny Interactive', 0, 255, nothing)

    while True:

        var_P1 = cv2.getTrackbarPos('P1', 'Canny Interactive')
        var_P2 = cv2.getTrackbarPos('P2', 'Canny Interactive')
        
        image_edge = cv2.Canny(image, var_P1, var_P2)   

        cv2.imshow('Canny Interactive', image_edge)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Display all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

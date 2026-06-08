import cv2
import numpy as np
from scipy import ndimage

filename = '03 Spatial Filtering & Edge Detection/Test_Image.jpg'
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found or unable to read.")
else:
    cv2.imshow("Original", image)
    
    # ==================== TASK 1 ====================
    # TODO: Create a BLUR kernel (3x3) where all values are 1/9
    # This will average the pixels = smooth blur effect
    # Then apply it using ndimage.convolve()
    # Display in window named "Task 1 - Blur Kernel"
    # HINT: All 9 values should be 1/9 (about 0.111)
    
    kernel_3x3 = np.array([[1/9, 1/9, 1/9],
                           [1/9, 1/9, 1/9],
                           [1/9, 1/9, 1/9]])
    
    blurred_3x3 = ndimage.convolve(image, kernel_3x3)

    cv2.imshow("Task 1 - Blur Kernel", blurred_3x3)
    # ==================== TASK 2 ====================
    # TODO: Create an EDGE DETECTION kernel (3x3)
    # Use: [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    # Apply using ndimage.convolve()
    # Display in window named "Task 2 - Edge Kernel"
    
    kernel_edge = np.array([[-1,-1,-1],
                            [-1,8,-1],
                            [-1,-1,-1]])
    
    edge_3x3 = ndimage.convolve(image,kernel_edge)

    cv2.imshow("Task 2 - Edge Kernel", edge_3x3)
    
    # ==================== TASK 3 ====================
    # TODO: Apply Gaussian Blur with kernel size (5,5)
    # Display in window named "Task 3 - Gaussian Blur"
    # HINT: cv2.GaussianBlur(image, (5,5), 0)
    
    kernel_gaussian = cv2.GaussianBlur(image, (5,5), 0)

    cv2.imshow("Task 3 - Gaussian Blur", kernel_gaussian)

    edge_gaussian = image - kernel_gaussian

    cv2.imshow("Task 3 - Gaussian Blur (Edges)", edge_gaussian)
    
    # ==================== TASK 4 ====================
    # TODO: Apply Gaussian Blur with kernel size (15,15)
    # Display in window named "Task 4 - Strong Blur"
    # HINT: Larger kernel = stronger blur
    
    gaussian_strong = cv2.GaussianBlur(image, (15,15), 0)

    cv2.imshow("Task 4 - Strong Blur", gaussian_strong)
    
    # ==================== TASK 5 ====================
    # TODO: Create a high-pass filter (edges)
    # 1. Blur the image with Gaussian (any size you like)
    # 2. Subtract blurred from original: original - blurred
    # 3. Display in window named "Task 5 - High Pass Filter"
    # This should show edges!
    
    #oops i did it even before but gonna do it again for the sake of the task

    blurred = cv2.GaussianBlur(image, (11,11), 0)
    g_hpf = image - blurred
    cv2.imshow("Task 5 - High Pass Filter", g_hpf)
    
    # ==================== TASK 6 (BONUS) ====================
    # TODO: Create a SHARPENING kernel (3x3)
    # Use: [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    # Apply using ndimage.convolve()
    # Display in window named "Task 6 - Sharpen"
    # HINT: Higher center value = more sharpening
    
    kernel_3x3_sharpen = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]])
    
    sharpened = ndimage.convolve(image, kernel_3x3_sharpen)

    cv2.imshow("Task 6 - Sharpen", sharpened)
    
    # Display all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

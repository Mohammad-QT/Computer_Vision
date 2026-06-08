import cv2
import numpy as np

# Load image
image = cv2.imread('02 Geometric Transformations/Test_Image.jpg', cv2.IMREAD_ANYCOLOR)

if image is None:
    print("Error: Image not found or unable to read.")

else:
    (h, w) = image.shape[:2]
    
    cv2.imshow("Original", image)
    
    # ==================== TASK 1 ====================
    # TODO: Scale the image to 75% of its original size (use fx and fy)
    # Display in window named "Task 1 - Scale 75%"
    # HINT: fx=0.75, fy=0.75

    image_scaled_75 = cv2.resize(image,None, fx=0.75, fy=0.75)
    
    cv2.imshow("Task 1 - Scale 75%", image_scaled_75)
    
    # ==================== TASK 2 ====================
    # TODO: Scale the image to exact dimensions: 400x300
    # Display in window named "Task 2 - Exact Size"
    # HINT: Use cv2.resize(image, (400, 300))

    H = 400
    W = 300

    image_scaled_dimensions = cv2.resize(image,(H,W))

    cv2.imshow("Task 2 - Exact Size", image_scaled_dimensions)
    
    # ==================== TASK 3 ====================
    # TODO: Rotate the image 30 degrees
    # Display in window named "Task 3 - Rotate 30"
    # HINT: Use center = (w // 2, h // 2) and getRotationMatrix2D(center, 30, 1)
    
    h,w = image.shape[:2]

    center = w//2 , h//2

    rotate_30 = cv2.getRotationMatrix2D(center,30,1)
    rotated_30 = cv2.warpAffine(image, rotate_30, (w,h))

    cv2.imshow("Task 3 - Rotate 30", rotated_30)   

    # ==================== TASK 4 ====================
    # TODO: Rotate the image 180 degrees (flip it upside down)
    # Display in window named "Task 4 - Rotate 180"
    
    rotate_180 = cv2.getRotationMatrix2D(center,180,1)

    rotated_180 = cv2.warpAffine(image, rotate_180 , (w,h))
    
    cv2.imshow("Task 4 - Rotate 180", rotated_180)

    # ==================== TASK 5 ====================
    # TODO: Translate image 150 pixels to the RIGHT and 75 pixels DOWN
    # Display in window named "Task 5 - Translate"
    # HINT: tx=150, ty=75
    
    tx = 150 
    ty = 75

    T_Matrix = np.float32([
        [1,0,tx],
        [0,1,ty]
    ])

    Translated = cv2.warpAffine(image, T_Matrix, (w,h))

    cv2.imshow("Task 5 - Translate", Translated)
    
    # ==================== TASK 6 (BONUS) ====================
    # TODO: Combine transformations!
    # 1. First scale to 50% size
    # 2. Then rotate 45 degrees
    # 3. Display in window named "Task 6 - Combined"
    # TIP: Do scaling first, get new dimensions, then rotate
    
    combined_transformations = cv2.resize(image, None , fx=0.5 , fy=0.5)
    
    h,w = combined_transformations.shape[:2]
    center = w//2 , h//2 

    rotate_45 = cv2.getRotationMatrix2D(center,45,1)
    combined_transformations = cv2.warpAffine(combined_transformations, rotate_45 , (w,h))

    cv2.imshow("Task 6 - Combined", combined_transformations)

    # Display all windows
    cv2.waitKey(0)

    cv2.destroyAllWindows()

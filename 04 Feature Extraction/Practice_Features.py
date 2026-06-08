import cv2
import numpy as np

filename = '04 Feature Extraction/R.jpg'
img = cv2.imread(filename)

if img is None:
    print("Error: Image not found")
else:
    cv2.imshow("Original", img)
    
    # ==================== TASK 1 ====================
    # TODO: Apply Harris Corner Detection
    # 1. Convert gray to float32
    # 2. Use cv2.cornerHarris(gray, 5, 17, 0.04)
    # 3. Mark corners with threshold 0.01 * dst.max() in cyan [0, 255, 255]
    # Display in window named "Task 1 - Harris Corners"
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    copy = cv2.cornerHarris(gray, 5, 17, 0.04)

    img[ copy > copy.max()* 0.01] = [0,255,255]

    cv2.imshow("Task 1 - Harris Corners", img)
    
    # ==================== TASK 2 ====================
    # TODO: Try different Harris threshold
    # Use 0.02 * dst.max() instead (stricter = fewer corners)
    # Display in window named "Task 2 - Harris Strict"
    # Compare with Task 1
    
    img [ copy > copy.max() * 0.02 ] = [0,255,255]
    cv2.imshow("Task 2 - Harris Strict", img)
    
    # ==================== TASK 3 ====================
    # TODO: Apply SIFT feature detection
    # 1. Create SIFT detector: sift = cv2.SIFT.create()
    # 2. Use detectAndCompute(): keypoints, descriptor = sift.detectAndCompute(gray, None)
    # 3. Draw keypoints using cv2.drawKeypoints()
    # 4. Display in window named "Task 3 - SIFT Keypoints"
    # HINT: Use flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color=(0, 255, 0)
    
  
    
    cv2.waitKey(0)

    cv2.destroyAllWindows()

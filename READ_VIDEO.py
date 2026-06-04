import cv2
import numpy as np

# Read the image from the specified file path
# Use forward slashes (/) for cross-platform compatibility in the file path
cameraCapture = cv2.VideoCapture(0)

cv2.waitKey(3000)
fps = 120 
size = ( int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)) , int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)) )

print (size)

success, frame = cameraCapture.read()

cv2.waitKey(5000)

if success:
    print('FRAME is captured')
while success:
    cv2.imshow("CAMERA",frame)
    success, frame = cameraCapture.read()
    ch = cv2.waitKey(20)
    if ch==32:
        break
cameraCapture.release()   
# Close all the image windows
cv2.destroyAllWindows()

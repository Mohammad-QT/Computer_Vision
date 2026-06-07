import cv2
import numpy as np

POS_clicked = [0,0]
clicked = False
def nothing():
    pass
def onMouse(event, x, y, flags, param):
    global POS_clicked
    global clicked
    if event == cv2.EVENT_MOUSEMOVE:
        POS_clicked = [x,y]
        clicked = True
    if event == cv2.EVENT_LBUTTONUP:
        clicked = False 
# Read the image from the specified file path
# Use forward slashes (/) for cross-platform compatibility in the file path
cv2.namedWindow("CAM",1)
cv2.setMouseCallback('CAM', onMouse)

cv2.createTrackbar('P1', 'CAM', 0, 255, nothing)
cv2.createTrackbar('P2', 'CAM', 0, 255, nothing)

CAP = cv2.VideoCapture('Vid.mp4')
fps = CAP.get(cv2.CAP_PROP_FPS)
#fps =  60
size = (
       int(CAP.get(cv2.CAP_PROP_FRAME_WIDTH)),
       int(CAP.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print (size)

videoWriter = cv2.VideoWriter(
'MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'),
fps, size)

success, frame = CAP.read()

while success:
    videoWriter.write(frame)
    cv2.imshow("CAM",frame)
    success, frame = CAP.read()
    ch = cv2.waitKey(10)
    print (ch)
    if ch==27:
        break
    if (ch==115):
        cv2.waitKey(0)
        cv2.imwrite('MY_Capture_Image.jpg',frame)
    if (clicked == True):
        print (POS_clicked)
        #clicked = False
        #print (frame[POS_clicked])
    if (ch == ord('e')):
        P1 = cv2.getTrackbarPos('P1', 'CAM')
        P2 = cv2.getTrackbarPos('P2', 'CAM')
        IMAGE_EDGE = cv2.Canny(frame,P1,P2)
        #IMAGE_EDGE = cv2.Canny(frame,100,150)
        cv2.imshow('IMAGE_EDGE',IMAGE_EDGE)
        cv2.waitKey(0)
    if (ch == ord('c')):
        P1 = cv2.getTrackbarPos('P1', 'CAM')
        P2 = cv2.getTrackbarPos('P2', 'CAM')
        #IMAGE_EDGE = cv2.Canny(frame,P1,P2)
        Frame_Contour = frame
        gray_frame = frame[:,:,1]
        ret, thresh = cv2.threshold(gray_frame, P1, P2, 0)
        contours, hierarchy = cv2.findContours(thresh,
        cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(Frame_Contour, contours, -1, (0,255,0), 2)

        cv2.imshow('thresh',thresh)
        cv2.imshow('Frame_Contour',Frame_Contour)
        cv2.waitKey(0)

CAP.release()
videoWriter.release()
# Close all the image windows
cv2.destroyAllWindows()

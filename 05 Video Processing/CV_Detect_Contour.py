import cv2
import numpy as np

filename = '05 Video Processing/Vid.mp4'

POS_clicked = [0,0]
clicked = False

def nothing(x):
    pass
def onMouse(event, x, y, flags, param):

    global POS_clicked
    global clicked

    if event == cv2.EVENT_MOUSEMOVE:
        POS_clicked = [x,y]
        clicked = True

    if event == cv2.EVENT_LBUTTONUP:
        clicked = False 


cv2.namedWindow("CAM",1)
cv2.setMouseCallback('CAM', onMouse)

cv2.createTrackbar('P1', 'CAM', 0, 255, nothing)
cv2.createTrackbar('P2', 'CAM', 0, 255, nothing)

CAP = cv2.VideoCapture(filename)
fps = CAP.get(cv2.CAP_PROP_FPS)
size = ( int(CAP.get(cv2.CAP_PROP_FRAME_WIDTH)) , int(CAP.get(cv2.CAP_PROP_FRAME_HEIGHT)) )

print (size)

videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)

success, frame = CAP.read()

while success:

    videoWriter.write(frame)

    cv2.imshow("CAM",frame)

    success, frame = CAP.read()

    ch = cv2.waitKey(100)

    print (ch)

    if ch==ord('q'):
        break

    if (ch==ord('s')):
        cv2.imwrite('05 Video Processing/MY_Capture_Image.jpg',frame)

    if (clicked == True):
        print (POS_clicked)
        
    if (ch == ord('e')):

        P1 = cv2.getTrackbarPos('P1', 'CAM')
        P2 = cv2.getTrackbarPos('P2', 'CAM')

        IMAGE_EDGE = cv2.Canny(frame,P1,P2)
        
        cv2.imshow('IMAGE_EDGE',IMAGE_EDGE)

        cv2.waitKey(0)

    if (ch == ord('c')):

        P1 = cv2.getTrackbarPos('P1', 'CAM')
        P2 = cv2.getTrackbarPos('P2', 'CAM')
        
        Frame_Contour = frame

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        ret, thresh = cv2.threshold(gray_frame, P1, P2, 0)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(Frame_Contour, contours, -1, (0,255,0), 2)

        cv2.imshow('thresh',thresh)
        cv2.imshow('Frame_Contour',Frame_Contour)

        cv2.waitKey(0) 

CAP.release()
videoWriter.release()
# Close all the image windows
cv2.destroyAllWindows()

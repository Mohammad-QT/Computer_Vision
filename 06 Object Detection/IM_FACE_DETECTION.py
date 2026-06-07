import cv2
import numpy as np
from scipy import ndimage

filename = '06 Object Detection/R.jpg'

#face_cascade = cv2.CascadeClassifier('C:/OpenCV_4_12/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('C:/OpenCV_4_12/opencv/sources/data/haarcascades/haarcascade_eye.xml')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    roi_gray = gray[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40,40))
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2)
        cv2.rectangle(roi_gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.namedWindow('Face Detected!!')
    cv2.imshow('Face Detected!!', img)
    cv2.imshow('ROI',roi_gray)

cv2.imwrite('./vikings.jpg', img)

cv2.waitKey(0)

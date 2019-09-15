
import os
ROOT_DIR = os.path.abspath(os.curdir)

import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier(ROOT_DIR + '\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(ROOT_DIR + '\\haarcascades\\haarcascade_eye.xml')
# smile_cascade = cv.CascadeClassifier(ROOT_DIR + '\\haarcascades\\haarcascade_smile.xml')
img = cv.imread('miguel.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    # smile = smile_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # for (ex,ey,ew,eh) in smile:
    #     cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,255),2)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
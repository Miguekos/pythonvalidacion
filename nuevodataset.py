import cv2
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('D:\\python\\FaceDetect\\Classifiers\\face.xml')
print (detector)
i=0
offset=100
import os
ROOT_DIR = os.path.abspath(os.curdir)
import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier(ROOT_DIR + '\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(ROOT_DIR + '\\haarcascades\\haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier(ROOT_DIR + '\\haarcascades\\haarcascade_smile.xml')
im = cv.imread('miguel.png')
name=input('Introduce tu id para guardar un registro: \n')
while True:
    # ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    print(gray)
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(120, 120), flags=cv2.CASCADE_SCALE_IMAGE)
    # faces=detector.detectMultiScale(image=gray, scaleFactor=1.2, minNeighbors=5, minSize=(120, 120))
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite("D:\\python\\FaceDetect\\dataSet\\face-"+name +'.'+ str(i) + ".jpg", gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        cv2.imshow('im',im[y:y+h,x:x+w])
        # cv.imshow('im',im)
        cv2.waitKey(100)
    if i>20:
        cam.release()
        cv2.destroyAllWindows()
        break
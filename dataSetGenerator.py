import cv2
from PIL import Image
from trainer import iniciar
# import argparse
import re
import cv2
import os
import io
import base64
import numpy as np
import sys

dirbase = (os.getcwd() + "\\")
print(dirbase)

# cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier(dirbase + 'Classifiers\\face.xml')
print (detector)

def indentificar(capcha, tipo, id):
    # print("imagen: %s" % capcha)
    print("tipo: %s" % tipo)
    print("id: %s" % id)
    if tipo == 1:
        im = stringToImage(capcha)
        print("de base 64 a imagen: %s" % im)
        gray = toRGB(im)
        print("Iagen en gris %s" % gray)
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        # print(gray)
        faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        name = str(id)
        print(name)
        offset=50
        i=0
        print(faces)
        # faces=detector.detectMultiScale(image=gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100))
        for(x,y,w,h) in faces:
            print(x)
            print(y)
            print(w)
            print(h)
            i=i+1
            print(cv2.imwrite(dirbase + "dataSet\\face-"+ name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset]))
            # cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        #     cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
        #     cv2.waitKey(100)
        # if i>20:
        #     # cam.release()
        #     cv2.destroyAllWindows()
        # # return ocrTexto
        # iniciar()
    elif tipo == 2:
        im = stringToImage(capcha)
        gray = toRGB(im)
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        # print(gray)
        faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        name = str(id)
        offset=50
        i=0
        print(faces)
        # faces=detector.detectMultiScale(image=gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100))
        for(x,y,w,h) in faces:
            print(x)
            print(y)
            print(w)
            print(h)
            i=i+1
            print(cv2.imwrite(dirbase + "selfie\\face-"+ name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset]))
            # cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        #     cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
        #     cv2.waitKey(100)
        # if i>20:
        #     # cam.release()
        #     cv2.destroyAllWindows()
        # # return ocrTexto
        # iniciar()
    else:
        return 'No se reconoce el tipo'

def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(imgdata))


def toRGB(image):
    # return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

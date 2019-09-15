import cv2,os
import numpy as np
from PIL import Image
import pickle
dirbase = (os.getcwd() + "\\")
recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer = cv2.createLBPHFaceRecognizer()
recognizer.read(dirbase + 'trainer\\trainer.yml')
# cascadePath = "Classifiers/face.xml"
cascadePath = dirbase + "Classifiers\\face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = dirbase + 'dataSet'
pathSelfie = dirbase + 'selfie'

# cam = cv2.VideoCapture(0)
# font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) #Creates a font
while True:
    image_paths = [os.path.join(path, f) for f in os.listdir(pathSelfie)]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        print(image_path)
    # ret, im =cam.read()
        image_pil = Image.open(image_path).convert('L')
        im = np.array(image_pil, 'uint8')
        # im = image_pil
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        # faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(120, 120), flags=cv2.CASCADE_SCALE_IMAGE)
        # for(x,y,w,h) in faces:
        #     nbr_predicted = 0
        #     nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        #     cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        #     print(nbr_predicted)
        #     if(nbr_predicted==1):
        #         nbr_predicted='Cesar'
        #     else:
        #         nbr_predicted='No se detecta'
        #         # cv2.cv.PutText(cv2.cv.fromarray(im),str(nbr_predicted)+"--"+str(conf), (x,y+h),font, 255) #Draw the text
        #         cv2.putText(im, str(nbr_predicted), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1, cv2.LINE_AA)
        #         cv2.imshow('im',im)
        #         cv2.waitKey(10)

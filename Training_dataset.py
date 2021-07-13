import cv2
import os
import numpy as np
from PIL import Image
recognizer=cv2.face.LBPHFaceRecognizer_create()
detector=cv2.CascadeClassifier('C:/Python/Python37/MINIPROJECT/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNP=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces=detector.detectMultiScale(imageNP)
        for (x,y,w,h) in faces:
            faceSamples.append(imageNP[y:y+h,x:x+w])
            Ids.append(Id)

    return faceSamples,Ids
faces,Ids=getImagesAndLabels('dataSet')
s=recognizer.train(faces,np.array(Ids))
print("successfully trained")
recognizer.write('trainer/trainer.yml')




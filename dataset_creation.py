import cv2
import os
def assure_path_exists(path):
    dir=os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
face_id=input("enter your rollno:")
image=cv2.VideoCapture(0)
detect=cv2.CascadeClassifier('C:/Python/Python37/MINIPROJECT/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
count=0
assure_path_exists("dataset/")
while(True):
    res,img=image.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=detect.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        count+=1
        cv2.imwrite("dataset/user." + str(face_id) +'.' + str(count) + ".jpg",gray[y:y+h,x:x+w])
        cv2.imshow("face recognition",img)
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break
    elif count>=20:
        print("Successfully captured")
        break
image.release()
cv2.destroyAllWindows()
import os
import numpy as np
import cv2


face_cas = cv2.CascadeClassifier('/home/sumit/imsge_processing/venv/include/Facial_Detection/data/haarcascades/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors= 5)
    cv2.imshow('frame', frame)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h ,
                        x:x+w ]

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.imwrite("img_my.png",roi_gray)
cap.release()
cv2.destroyAllWindows()



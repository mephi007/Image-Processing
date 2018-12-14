import numpy as np
import cv2

cap = cv2.VideoCapture(0)
def change_res(width , height):
    cap.set(3,width)
    cap.set(4,height)

change_res(230,150)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('GRAY' , gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def rescale(frame, percent):
    width = (int)(frame.shape[1]*percent/100)
    height =(int)(frame.shape[0]*percent/100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation= cv2.INTER_AREA)

while True:
    ret, frame = cap.read()
    frame1 = rescale(frame, percent=30)
    cv2.imshow('frame1', frame1)
    frame2 = rescale(frame, percent=150)
    cv2.imshow('frame2', frame2)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

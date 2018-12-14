import os
import numpy as np
import cv2

filename = 'video.avi'
frame_per_sec = 10.0
mres = '720p'

def change_res(cap,width,height):
    cap.set(3,width)
    cap.set(4,height)

Std_Dimension ={

    "480p" : (640, 480),
    "720p" : (1280, 720),
    "1080p" : (1920, 1080),
    "4k" : (3840, 2160),
}

def get_dims(cap , res = "1080p"):
    width,height = Std_Dimension["480p"]
    if res in Std_Dimension:
        width, height = Std_Dimension[res]

    change_res(cap, width, height)
    return width,height

VIDEO_TYPE = {
    "avi" : cv2.VideoWriter_fourcc(*'XVID'),
    "mp4" : cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename,ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0)
dims = get_dims(cap, mres)

video_type_cv2 = get_video_type(filename)

out = cv2.VideoWriter(filename, video_type_cv2, frame_per_sec, dims)

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('record', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
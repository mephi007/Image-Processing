import numpy
import cv2

img = cv2.imread('image.jpg', 0)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

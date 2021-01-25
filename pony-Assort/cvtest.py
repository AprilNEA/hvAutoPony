import numpy as np
import cv2 as cv

img = cv.imread("1.jpg")
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
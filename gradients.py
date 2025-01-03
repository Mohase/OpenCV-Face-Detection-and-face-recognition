import cv2 as cv
import numpy as np


img = cv.imread('Photos/cat.jpeg')
cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian
lap = cv.Laplacian(img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 1)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobelxy = cv.bitwise_or(sobelx, sobely)


cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('sobelxy', sobelxy)

# Canny (to compare to laplacian and sobel)
canny = cv.Canny(gray, 125, 175)
cv.imshow('canny',canny)

cv.waitKey(0)

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Catnada', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

ret, thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thres)

# Grab the edges with Canny
canny = cv.Canny(blur, 125, 175)  # Canny comes from the name of its inventor, Canny
cv.imshow('canny', canny)

    # To find countors, use cv.findContours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours on blank', blank)


cv.waitKey(0)

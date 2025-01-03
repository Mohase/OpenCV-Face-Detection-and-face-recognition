import cv2 as cv

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cats', img)

# To gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# threshold returns the given threshold (150)
# thresh returns the new image
cv.imshow('Simple thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple thresholded inverse', thresh_inv)

# Adaptive Thresholding
adaptive_threshold = (cv.adaptiveThreshold
                      (gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3))
cv.imshow('Adaptive thresholding', adaptive_threshold)



cv.waitKey(0)

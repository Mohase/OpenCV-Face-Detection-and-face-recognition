import cv2 as cv

img = cv.imread('Photos/cat.jpeg')
cv.imshow('cat', img)

# Average Blur
average = cv.blur(img, (3,3))
cv.imshow('average', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 25, 25)
cv.imshow('bilateral', bilateral)


cv.waitKey(0)

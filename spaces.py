import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)

plt.imshow(img)
plt.show()


# BGR
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BRG to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB in cv', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr', hsv_bgr)

plt.imshow(rgb)
plt.show()



#cv.waitKey(0)

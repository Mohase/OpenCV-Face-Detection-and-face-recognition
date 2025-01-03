import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('Photos/cat.jpeg')
cv.imshow('cat',img)

# Blank for mask
blank = np.zeros(img.shape[:2], dtype='uint8')


# Convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Circle for Mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', mask)

# Mask
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)


# Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], maskii,  [256], [0,256])
# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('number of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color Histogram
plt.figure()
plt.title('color histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixels')
colors = ('b', 'g', 'r')
for i, colour in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=colour)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)

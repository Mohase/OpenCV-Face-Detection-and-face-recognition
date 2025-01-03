import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # (width, height, number of color channels = 3)
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
# blank[200:300, 300:400] = 255,0,0
# cv.imshow('ColoredBlank', blank)


# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=-1)
cv.imshow('Rectangle tow lines', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=5)
cv.imshow('line', blank)

# 5. Write text
cv.putText(blank, 'MI Bomboclat', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('text', blank)

# img = cv.imread('Photos/cat.jpeg')
# cv.imshow('Cat', img)

cv.waitKey(0)

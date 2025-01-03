import cv2 as cv

img = cv.imread('Photos/cat.jpeg')
cv.imshow('catalonia', img)

# Converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)  # Ksize = kernel size. Should be odd (?)
cv.imshow('BLUR', blur)                             # bigger kernel -> more blur

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('CANNY', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilation', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Rsized', resized)

# Cropping
cropped = img[0:200, 0:300]
cv.imshow('Cropped', cropped)


cv.waitKey(0)

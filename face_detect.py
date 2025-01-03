import cv2 as cv

img = cv.imread('Photos/Puutin.jpeg')
cv.imshow('putin', img)
img_cat = cv.imread('Photos/Kissa.jpeg')
cv.imshow('kissa', img_cat)
realmadrid = cv.imread('Photos/reeal.jpeg')


# Grayscale, because haar cascade uses edges (does not use skin tone)
gray_putin = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray putin', gray_putin)

gray_reaal = cv.cvtColor(realmadrid, cv.COLOR_BGR2GRAY)
cv.imshow('gray real', gray_reaal)

# Read in the haar_face.xml file
# Done by creating a variable that uses cv.CascadeClassifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')


# Detecting face
# Create a variable
# This variable will be an instance of haar_cascade's cv.CascadeClassifier class
faces_rect = haar_cascade.detectMultiScale(gray_putin, scaleFactor=1.1, minNeighbors=3)
faces_rect_real = haar_cascade.detectMultiScale(gray_reaal, scaleFactor=1.1, minNeighbors=7)
print(f'number of faces found = {len(faces_rect)}')
print(f'number of faces found = {len(faces_rect_real)}')

# faces_rect is a collection of the rectangles coordinates that encompass the face
# Draw the rectangle
for (x,y,w,h) in faces_rect: # w = width, h = height
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 5 )
cv.imshow('detected face', img)

for (x,y,w,h) in faces_rect_real:
    cv.rectangle(realmadrid, (x,y), (x+w, y+h), (0,0,255), thickness=1)

cv.imshow('real faces', realmadrid)

cv.waitKey(0)

import cv2 as cv
import numpy as np

# (Read in haar_cascade file)
# Read in the face detection
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# The people
people = ['David Beckham', 'Cristiano Ronaldo', 'Jason Statham']


# Load in the saved lists
# features = np.load('features.npy')
# labels = np.load('labels.npy')

# Read in the recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# Load validation image (Jason Statham)
img = cv.imread('/Users//Desktop/images-1.jpeg')

# Turn to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Jason in Gray', gray)

# Detect the face in the image
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in face_rect:
    # Find the ROI
    face_roi = gray[y:y+h, x:x+w]

    # Predict i.e. finally try to recognize the face
    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    # Put the text on the image of the guess
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 1)

   # Outline the face
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('detected face', img)

cv.waitKey(0)

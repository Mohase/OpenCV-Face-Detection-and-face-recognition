import os
import cv2 as cv
import numpy as np

# Create a list of all the people in the images
people = ['David Beckham', 'Cristiano Ronaldo', 'Jason Statham']

# Make a variable for the base folder
DIR = '/Users//Desktop/Faces_celebs'

# Load the model CascadeClassifier

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Make variables for the features and labels
features = []
labels = []

# Make a function to iterate over the pictures of all the faces in all the folders


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

# Function call to create_train -> prepares data
create_train()
print('Training complete ---------')

# Convert features list and labels list into np.arrays for the training process
features = np.array(features, dtype='object')  # dtype='object' because  features contain complex data (images)
labels = np.array(labels)  # no dtype, because it is only **integers** or categorical

# Instantiate face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the face recognizer on the features list and the labels list
face_recognizer.train(features, labels)

# Save the data for efficiency and ease of transport
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)






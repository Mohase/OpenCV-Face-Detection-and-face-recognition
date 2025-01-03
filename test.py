import cv2 as cv

# Check OpenCV version
print("OpenCV Version:", cv.__version__)

# Verify the face module and LBPH recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
print("LBPHFaceRecognizer created successfully.")

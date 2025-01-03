import cv2 as cv

#img = cv.imread('Photos/cat.jpeg')

#cv.imshow('elGato', img)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('videoOfDog', frame)  # Shows frame by frame

    if cv.waitKey(20) & 0XFF == ord('d'):  # if the key d is pressed, stops
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)  # Waits for a key to be pressed. (0 = indefinitely)

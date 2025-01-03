import cv2 as cv

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.5):
    # Will work for: Images, Videos & Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Only works for Live video
    capture.set(3, width)
    capture.set(4, height)

# Video capture

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('videoOfDog', frame)  # Shows frame by frame
    cv.imshow('VideoOfDog Resized', frame_resized)  # Shows frame by frame of resized

    if cv.waitKey(20) & 0XFF == ord('d'):  # if the key d is pressed, stops
        break

capture.release()
cv.destroyAllWindows()

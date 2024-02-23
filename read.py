import cv2 as cv

# READING IMAGES
# img = cv.imread('photos/brian.jpg')

# cv.imshow('crew', img)

# cv.waitKey(0)

# READING VIDEOS
capture = cv.VideoCapture('videos/mashle1.mkv')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
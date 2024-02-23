import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. paint the image a certain color
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//3,blank.shape[0]//2), (0,0,255), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,255,0), thickness=-1)
cv.imshow('circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,2555), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Mithibe!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('text',blank)

# img = cv.imread('photos/me2.JPG')
# cv.imshow('image', img)

cv.waitKey(0)
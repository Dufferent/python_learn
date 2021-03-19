#!/usr/bin/python3

# opencv env

import cv2 as cv

capture = cv.VideoCapture("/dev/video0")
if not (capture.isOpened()):
    print ("cap open failed!")
    exit(-1)

while (1):
    ret,frame = capture.read()
    if not (frame is None):
        cv.imshow("cv",frame)
    key = cv.waitKey(30)
    if (key == 'a'):
        break

capture.release();
exit(0)



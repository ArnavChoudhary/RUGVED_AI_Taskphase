import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#img = cv.imread("/home/ubuntu/Desktop/Photos/pothole.jpg")
#cv.imshow('Pothole', img)
img1 = cv.imread("/home/ubuntu/Desktop/Photos/pothole2.jpg")
cv.imshow('Pothole2', img1)

roi = img1[197:570, 257:790]
cv.imshow('ROI', roi)

gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)
blur = cv.GaussianBlur(gray, (15,15), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)
blur1 = cv.medianBlur(blur, 19)
blur2 = cv.bilateralFilter(blur1, 10, 25, 25)
ret, thresh = cv.threshold(blur2, 97, 149, cv.THRESH_BINARY)
#cv.imshow('Thresh', thresh)

kernel = np.ones((5,5), np.uint8)
erode = cv.erode(thresh,kernel,iterations=1)
dilate = cv.dilate(erode,kernel,iterations=1)
contours, hierarchies = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank1 = np.zeros(roi.shape[:3], dtype='uint8')
canny = cv.Canny(dilate, 120, 175)
cv.imshow('Canny',canny)
cv.drawContours(blank1,contours,-1,(0,0,255), 1)
cv.imshow('Contours drawn', blank1)



cv.waitKey(0)

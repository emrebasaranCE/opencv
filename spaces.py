import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow("Cats", img)

# Displays as RGB image.
# plt.imshow(img)
# plt.show()


# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("Lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV --> BGR", hsv_bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow("LAB --> BGR", lab_bgr)
# plt.imshow(rgb)
# plt.show()


cv.waitKey(0)
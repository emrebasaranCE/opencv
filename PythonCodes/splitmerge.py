import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

b,g,r = cv.split(img)

cv.imshow("Bue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)

# Merged
merged = cv.merge([b,g,r])
cv.imshow("Merged image", merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Bue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)


cv.waitKey(0)
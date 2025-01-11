import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow("Cats", img)

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)


cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise and --> intersecting regions
bitwite_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwite_and)

# bitwise or --> non-intersecting and intersecting regions
bitwite_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwite_or)

# bitwise xor --> non-intersecting regions
bitwite_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwite_xor)

# bitwise not
bitwite_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT", bitwite_not)
bitwite_not_circle = cv.bitwise_not(circle)
cv.imshow("Bitwise NOT", bitwite_not_circle)

cv.waitKey(0)
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank/Black", blank)

# # 1. Paint the image a certain color
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow("Green", blank)

# blank[:] = 0, 255, 0
# cv.imshow("Green", blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=-1)
# cv.imshow("Rectangle", blank)

# 3. Draw a Circle
# cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=2)
# cv.imshow("Circle", blank)

# 4. Draw a Line
# cv.line(img=blank, pt1=(0, 0), pt2=(blank.shape[1]//2, blank.shape[0]//2), color=(255, 255, 0), thickness=3)
# cv.imshow("Line", blank)

# 5. Write Text
cv.putText(blank, text="Hello", org=(10, 225), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 255, 0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)

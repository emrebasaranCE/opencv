import cv2 as cv

### Reading Images ###
# file_path_to_image = "Resources/Photos/cat_large.jpg"
# img = cv.imread(file_path_to_image)

# cv.imshow("Cat", img)
# cv.waitKey(0)

### Reading Videos ###
capture = cv.VideoCapture("Resources/Videos/dog.mp4")

while(True):
    ## Frame is a one of the many images of the video.
    isTrue, frame = capture.read()

    # Here you simply show that frame. Which is changes every time.
    cv.imshow("Video", frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

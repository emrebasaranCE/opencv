import cv2 as cv

cap = cv.VideoCapture(0)


if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is read correctly
    if not ret:
        print("Error: Failed to capture image.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('Gray Person', gray)

    haar_cascade = cv.CascadeClassifier('D:/Opencv/FaceDetection/haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    # Display the resulting frame
    cv.imshow("Webcam", frame)

    # Break the loop when the 'q' key is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any OpenCV windows
cap.release()
cv.destroyAllWindows()
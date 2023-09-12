import cv2

cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)
capture = cv2.VideoCapture(r"videoSample.mp4", cv2.CAP_ANY)

while True:
    ret, frame = capture.read()

    if not ret:
        break

    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
import cv2

cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)
capture = cv2.VideoCapture(r"videoSample.mp4", cv2.CAP_ANY)
capture.set(3, 640)
capture.set(4, 480)

while True:
    ret, frame = capture.read()

    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', gray)

    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
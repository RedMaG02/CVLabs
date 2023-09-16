import cv2

cap = cv2.VideoCapture(2)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
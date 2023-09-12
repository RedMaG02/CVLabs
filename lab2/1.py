import cv2

def main():
    capture = cv2.VideoCapture(r"videoSample.mp4")

    while True:
        ret, frame = capture.read()

        if not ret:
            break

        frameHSV = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        cv2.imshow('frame', frameHSV)

        if cv2.waitKey(1) & 0xFF == 27:
            break


main()
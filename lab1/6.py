import cv2


def cross(img, color):
    h = img.shape[0]
    w = img.shape[1]

    upper_left = tuple(map(int, (w * 0.4, h * 0.47)))
    down_right = tuple(map(int, (w * (1 - 0.4), h * (1 - 0.47))))

    cv2.rectangle(img, upper_left, down_right, color, 1)

    upper_left = tuple(map(int, (w * 0.485, h * 0.3)))
    down_right = tuple(map(int, (w * (1 - 0.485), h * 0.47)))

    cv2.rectangle(img, upper_left, down_right, color, 1)

    upper_left = tuple(map(int, (w * 0.485, h * 0.53)))
    down_right = tuple(map(int, (w * (1 - 0.485), h * (1 - 0.3))))

    cv2.rectangle(img, upper_left, down_right, color, 1)



def main():
    capture = cv2.VideoCapture(r"videoSample.mp4")

    while True:
        ret, frame = capture.read()

        if not ret:
            break

        cross(frame, (0, 0, 255))
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break


main()

import cv2
import numpy

def cross(img, color):
    h = img.shape[0]
    w = img.shape[1]

    upper_left = tuple(map(int, (w * 0.4, h * 0.47)))
    down_right = tuple(map(int, (w * (1 - 0.4), h * (1 - 0.47))))

    cv2.rectangle(img, upper_left, down_right, color, -1)

    upper_left = tuple(map(int, (w * 0.485, h * 0.3)))
    down_right = tuple(map(int, (w * (1 - 0.485), h * 0.47)))

    cv2.rectangle(img, upper_left, down_right, color, -1)

    upper_left = tuple(map(int, (w * 0.485, h * 0.53)))
    down_right = tuple(map(int, (w * (1 - 0.485), h * (1 - 0.3))))

    cv2.rectangle(img, upper_left, down_right, color, -1)

def get_color(color):
    if color[0] >= (color[1] and color[2]):
        return (255, 0, 0)
    elif color[1] >= (color[0] and color[2]):
        return (0, 255, 0)
    else:
        return (0, 0, 255)

def main():
    capture = cv2.VideoCapture(r"videoSample.mp4")

    while True:
        ret, frame = capture.read()

        if not ret:
            break

        h = frame.shape[0]
        w = frame.shape[1]
        cross(frame, get_color(frame[numpy.int16(w / 2), numpy.int16(h / 2)]))
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break


main()
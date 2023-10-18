import cv2
import numpy as np

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

def le_pentagramm(img, line_length):
    h = img.shape[0]
    w = img.shape[1]
    center_x, center_y = w // 2, h // 2
    circle_radius = 100
    cv2.circle(img, (center_x, center_y), circle_radius, (0, 0, 255), thickness=3)

    star_outer_radius = circle_radius
    star_inner_radius = circle_radius // 2
    star_points = []
    for i in range(6):
        angle = i * 2 * np.pi / 6
        x = center_x + star_outer_radius * np.cos(angle)
        y = center_y + star_outer_radius * np.sin(angle)
        star_points.append((x, y))
        x = center_x + star_inner_radius * np.cos(angle + np.pi / 6)
        y = center_y + star_inner_radius * np.sin(angle + np.pi / 6)
        star_points.append((x, y))


    star_points = np.array(star_points, dtype=np.int32)

    for i in range(0, len(star_points), 2):
        cv2.line(img, tuple(star_points[i]), tuple(star_points[(i + 3) % len(star_points)]), (0, 0, 255), thickness=4)
        cv2.line(img, tuple(star_points[i + 1]), tuple(star_points[(i + 4) % len(star_points)]), (0, 0, 255),
                 thickness=4)

def get_color(color):
    if color[0] >= (color[1] and color[2]):
        return (255, 0, 0)
    elif color[1] >= (color[0] and color[2]):
        return (0, 255, 0)
    else:
        return (0, 0, 255)

def main():
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()

        if not ret:
            break

        h = frame.shape[0]
        w = frame.shape[1]
        #cross(frame, get_color(frame[np.int16(w / 2), np.int16(h / 2)]))
        le_pentagramm(frame, 30)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break


main()
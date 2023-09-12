import cv2

video = cv2.VideoCapture(r"videoSample.mp4", cv2.CAP_ANY)

w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter.fourcc(*'XVID')
video_writer = cv2.VideoWriter('videoSample.mov', fourcc, 60, (w, h))

while True:
    ret, frame = video.read()

    if not ret:
        break

    video_writer.write(frame)

video_writer.release()
video.release()

cv2.destroyAllWindows()
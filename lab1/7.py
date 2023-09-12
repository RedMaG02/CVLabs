import cv2

video = cv2.VideoCapture(0)

w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter.fourcc(*'XVID')
video_writer = cv2.VideoWriter('videoSample.mov', fourcc, 60, (w, h))

while True:
    ret, frame = video.read()

    if not ret:
        break

    video_writer.write(frame)
    if cv2.waitKey(10) & 0xFF == 27:
        video_writer.release()
        break

video.release()
cv2.destroyAllWindows()
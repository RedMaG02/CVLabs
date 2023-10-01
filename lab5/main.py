import cv2



capture = cv2.VideoCapture(r"videoSample.mp4")

prev_frame = None
this_frame = None
frame_diff = None

w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter.fourcc(*'XVID')
video_writer = cv2.VideoWriter('videoSample1.mov', fourcc, 60, (w, h))

while True:
    ret, frame = capture.read()


    if (prev_frame is None):
        prev_frame = frame.copy()
        prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        prev_frame = cv2.GaussianBlur(prev_frame, (7,7), 1)
        continue

    if not ret:
        break

    this_frame = frame.copy()
    this_frame = cv2.cvtColor(this_frame, cv2.COLOR_BGR2GRAY)
    this_frame = cv2.GaussianBlur(this_frame, (7, 7), 1)

    frame_diff = cv2.absdiff(prev_frame, this_frame)
    #print(frame_diff)
    ret, frame_diff = cv2.threshold(frame_diff, 127, 255, cv2.THRESH_BINARY)
    #print(frame_diff)
    prev_frame = this_frame

    contours, im2 = cv2.findContours(frame_diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    b = False
    if (contours is None):
        continue
    for con in contours:
        area = cv2.contourArea(con)
        print(area)
        if (area > 300):
            b = True

    #print(contours)

    #cv2.imshow("diff", frame_diff)
    if (b == True):
        video_writer.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        video_writer.release()
        break

video_writer.release()
import cv2

imgFlag1 = cv2.IMREAD_COLOR
imgFlag2 = cv2.IMREAD_GRAYSCALE
imgFlag3 = cv2.IMREAD_UNCHANGED

windowFlag1 = cv2.WINDOW_AUTOSIZE
windowFlag2 = cv2.WINDOW_NORMAL
windowFlag3 = cv2.WINDOW_KEEPRATIO

img1 = cv2.imread(r"sample.png", imgFlag1)
img2 = cv2.imread(r"sample.jpg", imgFlag2)
img3 = cv2.imread(r"sample.bmp", imgFlag3)

cv2.namedWindow("Img show", windowFlag3)
cv2.imshow("Img show", img3)
cv2.waitKey(0)

cv2.destroyAllWindows()
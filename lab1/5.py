import cv2

img = cv2.imread(r"sample.png", cv2.IMREAD_UNCHANGED)

cv2.imshow("orig", img)
cv2.imshow("hsv", cv2.cvtColor(img, cv2.COLOR_RGB2HSV))

cv2.waitKey(0)
cv2.destroyAllWindows()
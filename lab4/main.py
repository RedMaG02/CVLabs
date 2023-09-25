import cv2
import numpy as np
import MyGradientBorder as grad

def brd():
    img1 = cv2.imread(r"image.png")
    img_copy = img1.copy()
    grey_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    img_copy_list = grey_copy.tolist()

    for i in range(0, len(img_copy_list)):
        for j in range(0, len(img_copy_list[i])):
            if (type(img_copy_list[i][j]) != int):
                print("ne int")
                break


    gradient_matrix = grad.get_gradient_matrix(img_copy_list, grad.sobel_x, grad.sobel_y)
    gradient_matrix = grad.trim_matrix(gradient_matrix, len(grad.sobel_x)//2)
    gradient_length_matrix = grad.get_gradient_length_matrix(gradient_matrix)
    gradient_angle_matrix = grad.get_gradient_angle_matrix(gradient_matrix)
    hsv_matrix = grad.create_hsv(gradient_length_matrix, gradient_angle_matrix)
    numpy_array = np.array(hsv_matrix, dtype=np.uint8)
    hsv_image = cv2.cvtColor(numpy_array, cv2.COLOR_HSV2BGR)

    cv2.imshow("My", hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

brd()
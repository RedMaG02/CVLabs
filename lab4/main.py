import cv2
import numpy as np
import MyGradientBorder as grad
import my_gauss_patented as gauss

def brd():
    img1 = cv2.imread(r"image3.png")
    img_copy = img1.copy()
    grey_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    img_copy_list = grey_copy.tolist()

    #for i in range(0, len(img_copy_list)):
    #    for j in range(0, len(img_copy_list[i])):
    #        if (type(img_copy_list[i][j]) != int):
    #            print("ne int")
    #            break

    gauss_size = 11
    blurred = gauss.gaussian_blur(img_copy_list, gauss_size, 1)
    blurred = grad.trim_matrix(blurred, gauss_size//2)
    numpy_array_blurred_img = np.array(blurred, dtype=np.uint8)
    blurred_img = cv2.cvtColor(numpy_array_blurred_img, cv2.COLOR_GRAY2BGR)


    gradient_matrix = grad.get_gradient_matrix(blurred, grad.sobel_x, grad.sobel_y)
    gradient_matrix = grad.trim_matrix(gradient_matrix, len(grad.sobel_x)//2)
    gradient_length_matrix = grad.get_gradient_length_matrix(gradient_matrix)
    gradient_angle_matrix = grad.get_gradient_angle_matrix(gradient_matrix)

    #hsv_matrix = grad.create_hsv(gradient_length_matrix, gradient_angle_matrix)
    #numpy_array = np.array(hsv_matrix, dtype=np.uint8)
    #hsv_image = cv2.cvtColor(numpy_array, cv2.COLOR_HSV2BGR)
    #width, heigth= hsv_image.shape[1], hsv_image.shape[0]
    #resized_image = cv2.resize(hsv_image, (width * 1, heigth * 1))

    border_img_list = grad.destroy_nonmax(gradient_angle_matrix, gradient_length_matrix)
    border_img_list2 = grad.double_filtering(border_img_list, gradient_length_matrix, 30, 10) #Для вумен 30 10 ок коты 20 8 / 30 10
    numpy_array_border_img = np.array(border_img_list2, dtype=np.uint8)
    border_img = cv2.cvtColor(numpy_array_border_img, cv2.COLOR_GRAY2BGR)


    cv2.imshow("My", border_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

brd()
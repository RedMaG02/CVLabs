import cv2
import numpy as np
import my_gauss_patented as gauss

def fifty_shades_of_gray():
    img1 = cv2.imread(r"image.jpg")
    img_copy = img1.copy()
    grey_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    #height, width = grey_copy.shape
    img_copy_list = grey_copy.tolist()

    blurred_image_CV = cv2.GaussianBlur(grey_copy, (21, 21), 3)

    blur_matrix = gauss.gaussian_blur(img_copy_list, 21, 3)
    numpy_array = np.array(blur_matrix, dtype=np.uint8)
    blur_image = cv2.cvtColor(numpy_array, cv2.COLOR_GRAY2BGR)

    cv2.imshow("My", blur_image)
    cv2.imshow("Cringe CV", blurred_image_CV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def a_lot_shades_of_color():
    img1 = cv2.imread(r"image.jpg")
    img_copy = img1.copy()
    b, g, r = cv2.split(img_copy)

    blur_matrix_b = gauss.gaussian_blur(b, 15, 3)
    blur_matrix_g = gauss.gaussian_blur(g, 15, 3)
    blur_matrix_r = gauss.gaussian_blur(r, 15, 3)

    color_image = cv2.merge(([blur_matrix_b, blur_matrix_g, blur_matrix_r]))

    blurred_image_CV = cv2.GaussianBlur(img1, (15, 15), 3)

    cv2.imshow("My", color_image)
    cv2.imshow("CV", blurred_image_CV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

fifty_shades_of_gray()

import math
#numpy для клоунов, питон быстрый, если никуда не торопишься...

def my_gauss_func(x, y, size, sigma):
    a = b = size//2 + 1
    return (1/((2*math.pi) * pow(sigma, 2))) * math.exp( -(   (pow((x - a), 2)  + pow((y - b), 2))   / (2 * pow(sigma, 2)))  )

def matrix_norm(matrix):
    sum = 0
    for i in range(0, len(matrix)-1):
        for j in range(0, len(matrix[i])):
            sum += matrix[i][j]

    for i in range(0, len(matrix)-1):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = matrix[i][j]/sum

def fill_gauss_matrix(size, sigma):
    matrix = []
    for i in range(0, size - 1):
        matrix.append([])
        for j in range(0, size - 1):
            matrix[i].append(my_gauss_func(i, j, size, sigma))
    matrix_norm(matrix)

    return matrix


def gaussian_blur(img, gauss_matrix_size, sigma):
    height = len(img)
    width = len(img[0])
    x_start = gauss_matrix_size // 2
    x_end = height - gauss_matrix_size // 2
    y_start = gauss_matrix_size // 2
    y_end = width - gauss_matrix_size // 2

    gauss_matrix = fill_gauss_matrix(gauss_matrix_size, sigma)
    blur_matrix = img.copy()

    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            value = 0
            ii = 0
            for k in range(i - gauss_matrix_size // 2, i + gauss_matrix_size // 2):
                jj = 0
                for c in range(j - gauss_matrix_size // 2, j + gauss_matrix_size // 2):
                    value += img[k][c] * gauss_matrix[ii][jj]
                    jj += 1
                ii += 1
            blur_matrix[i][j] = value

    return blur_matrix
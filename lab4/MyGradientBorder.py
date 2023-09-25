import math
#НАМПАЯ НЕ БУДЕТ, Я НИКУДА НЕ ТОРОПЛЮСЬ!


sobel_x = [[-1, 0 , 1], [-2, 0, 2], [-1, 0, 1]]
sobel_y = [[-1, -2, -1], [0,0,0], [1,2,1]]

def get_gradient_matrix(matrix, g_x, g_y):
    g_x_size_2 = len(g_x)//2
    g_y_size_2 = len(g_y)//2
    result_matrix = matrix.copy()
    for i in range(g_x_size_2, len(matrix) - g_x_size_2 - 1):
        for j in range(g_y_size_2, len(matrix[i]) - g_y_size_2 - 1):
            value = [0,0]
            ii = 0
            for k in range(i - g_x_size_2, i + g_x_size_2):
                jj = 0
                for c in range(j - g_y_size_2, j + g_y_size_2):
                    value[0] += matrix[k][c] * g_x[ii][jj]
                    value[1] += matrix[k][c] * g_y[ii][jj]
                    jj += 1
                ii += 1
            result_matrix[i][j] = value
    return result_matrix

def trim_matrix(matrix, trim_size): #Очень глубоко, не каждый поймет...
    new_matrix = []
    ii = 0
    for i in range(trim_size, len(matrix) - trim_size - 1):
        new_matrix.append([])
        for j in range(trim_size, len(matrix[0]) - trim_size - 1):
            new_matrix[ii].append(matrix[i][j])
        ii += 1
    return new_matrix

def get_gradient_length_matrix(matrix):
    gradient_length = []
    for i in range(0, len(matrix)):
        gradient_length.append([])
        for j in range(0, len(matrix[i])):
            length = math.sqrt((matrix[i][j][0] * matrix[i][j][0]) + (matrix[i][j][1] * matrix[i][j][1]))
            gradient_length[i].append(length)
    return gradient_length

def get_gradient_angle_matrix(matrix):
    gradient_angle = []
    x_zero = 0
    y_zero = 0
    if (len(matrix) % 2 == 0):
    for i in range(0, len(matrix)):
        gradient_angle.append([])
        for j in range(0, len(matrix[i])):
            tan = math.tan(matrix[i][j][1]/matrix[i][j][0])
            if ((matrix[i][j][0] > 0 & matrix[i][j][1] < 0 & tan < -2.414) | (matrix[i][j][0] < 0 & matrix[i][j][1] < 0 & tan > 2.414)):
                gradient_angle[i].append(0)
            if (matrix[i][j][0] > 0 & matrix[i][j][1] < 0 & tan < -0.414):
                gradient_angle[i].append(1)

    return gradient_angle



def get_border(img):
    gradient_matrix = get_gradient_matrix(img, sobel_x, sobel_y)
    gradient_matrix = trim_matrix(gradient_matrix, len(sobel_x)//2)
    gradient_length_matrix = get_gradient_length_matrix(gradient_matrix)
    gradient_angle_matrix = get_gradient_angle_matrix(gradient_matrix)
    nonmax_matrix = destroy_nonmax()
    border_filtered_matrix = border_filter(min_value, max_value)





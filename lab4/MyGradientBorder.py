import math
#НАМПАЯ НЕ БУДЕТ, Я НИКУДА НЕ ТОРОПЛЮСЬ!


sobel_x = [[-1, 0 , 1], [-2, 0, 2], [-1, 0, 1]]
sobel_y = [[-1, -2, -1], [0,0,0], [1,2,1]]

def get_gradient_matrix(matrix, g_x, g_y):
    g_x_size_2 = len(g_x)//2
    g_y_size_2 = len(g_y)//2
    result_matrix = []
    for i in range(0, len(matrix)):
        result_matrix.append(matrix[i].copy())

    for i in range(g_x_size_2, len(matrix) - g_x_size_2):
        for j in range(g_y_size_2, len(matrix[i]) - g_y_size_2 ):
            value = [0,0]
            ii = 0
            for k in range(i - g_x_size_2, i + g_x_size_2):
                jj = 0
                for c in range(j - g_y_size_2, j + g_y_size_2):
                    value[0] = value[0] + (matrix[k][c] * g_x[ii][jj])
                    value[1] = value[1] + (matrix[k][c] * g_y[ii][jj])
                    jj += 1
                ii += 1
            result_matrix[i][j] = value
    return result_matrix

def trim_matrix(matrix, trim_size): #Очень глубоко, не каждый поймет...
    new_matrix = []
    ii = 0
    for i in range(trim_size, len(matrix) - trim_size):
        new_matrix.append([])
        for j in range(trim_size, len(matrix[0]) - trim_size):
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
    for i in range(0, len(matrix)):
        gradient_angle.append([])
        for j in range(0, len(matrix[i])):
            tan = math.tan(matrix[i][j][1]/matrix[i][j][0])
            x = matrix[i][j][0]
            y = matrix[i][j][1]
            if ((x > 0 and y < 0 and tan < -2.414) or (x < 0 and y < 0 & tan > 2.414)):
                gradient_angle[i].append(0)
            if (x > 0 & y < 0 & tan < -0.414):
                gradient_angle[i].append(1)
            if ((x >0 & y < 0 & tan > -0.414) | (x > 0 & y > 0 & tan < 0.414)):
                gradient_angle[i].append(2)
            if (x > 0 & y > 0 & tan < 2.414):
                gradient_angle[i].append(3)
            if ((x > 0 & y > 0 & tan > 2.414) | (x < 0 & y > 0 & tan < -2.414)):
                gradient_angle[i].append(4)
            if (x < 0 & y > 0 & tan < -0.414):
                gradient_angle[i].append(5)
            if ((x<0 & y>0 & tan > -0.414) | (x<0 & y<0 & tan < 0.414)):
                gradient_angle[i].append(6)
            if (x< 0 & y<0 & tan < 2.414):
                gradient_angle[i].append(7)

    return gradient_angle

def get_max_gradient_length(length_matrix):
    max = length_matrix[0][0]
    for i in range(0, len(length_matrix)):
        for j in range(0, len(length_matrix[i])):
            if (length_matrix[i][j] > max):
                max = length_matrix[i][j]
    return max

def get_min_gradient_length(length_matrix):
    min = length_matrix[0][0]
    for i in range(0, len(length_matrix)):
        for j in range(0, len(length_matrix[i])):
            if (length_matrix[i][j] < min):
                min = length_matrix[i][j]
    return min

def create_hsv(length, angle):
    hsv_matrix = []
    max_len = get_max_gradient_length(length)
    min_lem = get_min_gradient_length(length)
    s_m = 255/max_len
    h_m = 180 / 8
    v = 255
    for i in range(0, len(angle)):
        hsv_matrix.append([])
        for j in range(0, len(angle[i])):
            h = angle[i][j] * h_m
            s = length[i][j] * s_m
            hsv_matrix[i].append([h,s,v])

    return hsv_matrix

def get_border(img):
    gradient_matrix = get_gradient_matrix(img, sobel_x, sobel_y)
    gradient_matrix = trim_matrix(gradient_matrix, len(sobel_x)//2)
    gradient_length_matrix = get_gradient_length_matrix(gradient_matrix)
    gradient_angle_matrix = get_gradient_angle_matrix(gradient_matrix)
    #nonmax_matrix = destroy_nonmax()
    #border_filtered_matrix = border_filter(min_value, max_value)





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

    for i in range(g_x_size_2, len(matrix)  - g_x_size_2):
        for j in range(g_y_size_2, len(matrix[i])  - g_y_size_2 ):
            value = [0,0]
            ii = 0
            for k in range(i - g_x_size_2, i + g_x_size_2 + 1):
                jj = 0
                for c in range(j - g_y_size_2, j + g_y_size_2 + 1):
                    value[0] +=(matrix[k][c] * g_x[ii][jj])
                    value[1] +=(matrix[k][c] * g_y[ii][jj])
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
            if (matrix[i][j][0] == 0):
                matrix[i][j][0] = 0.0001

            tan = matrix[i][j][1]/matrix[i][j][0]
            #print(f"{matrix[i][j][0]}     :     {matrix[i][j][1]}")
            x = matrix[i][j][0]
            y = matrix[i][j][1]
            if ((x > 0 and y < 0 and tan < -2.414) or (x < 0 and y < 0 and tan > 2.414)):
                gradient_angle[i].append(0)
            elif (x > 0 and y < 0 and tan < -0.414):
                gradient_angle[i].append(1)
            elif ((x >0 and y < 0 and tan > -0.414) or (x > 0 and y > 0 and tan < 0.414)):
                gradient_angle[i].append(2)
            elif (x > 0 and y > 0 and tan < 2.414):
                gradient_angle[i].append(3)
            elif ((x > 0 and y > 0 and tan > 2.414) or (x < 0 and y > 0 and tan < -2.414)):
                gradient_angle[i].append(4)
            elif (x < 0 and y > 0 and tan < -0.414):
                gradient_angle[i].append(5)
            elif ((x<0 and y>0 and tan > -0.414) or (x<0 and y<0 and tan < 0.414)):
                gradient_angle[i].append(6)
            elif (x < 0 and y < 0 and tan < 2.414):
                gradient_angle[i].append(7)
            elif (x > 0):
                gradient_angle[i].append(2)
            elif (x < 0):
                gradient_angle[i].append(6)


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
    print(max_len)
    min_len = get_min_gradient_length(length)
    s_m = 255/max_len
    h_m = 180 / 8
    v = 255
    for i in range(0, len(length)):
        hsv_matrix.append([])
        for j in range(0, len(length[i])):
            h = angle[i][j] * h_m
            s = length[i][j] * s_m
            hsv_matrix[i].append([h,s,v])

    return hsv_matrix

def destroy_nonmax(angles, length):
    border_matrix = []
    ii = 0
    for i in range(1, len(angles) - 1):
        border_matrix.append([])
        for j in range(1, len(angles[i]) - 1):
            ang = angles[i][j]
            if (ang == 0 or ang == 4):
                if (length[i][j] > length[i - 1][j] and length[i][j] > length[i + 1][j]):
                    border_matrix[ii].append(255)
                else:
                    border_matrix[ii].append(0)
            elif(ang == 2 or ang == 6):
                if (length[i][j] > length[i][j - 1] and length[i][j] > length[i][j + 1]):
                    border_matrix[ii].append(255)
                else:
                    border_matrix[ii].append(0)
            elif(ang == 3 or ang == 7):
                if (length[i][j] > length[i + 1][j + 1] and length[i][j] > length[i - 1][j - 1]):
                    border_matrix[ii].append(255)
                else:
                    border_matrix[ii].append(0)
            elif (ang ==1 or ang == 5):
                if (length[i][j] > length[i - 1][j + 1] and length[i][j] > length[i + 1][j - 1]):
                    border_matrix[ii].append(255)
                else:
                    border_matrix[ii].append(0)
        ii += 1
    #angles = trim_matrix(angles, 1)
    #length = trim_matrix(length, 1)
    return border_matrix

def double_filtering(borders, lengths, low, high):
    lower_border = get_max_gradient_length(lengths) // low
    higher_border = get_max_gradient_length(lengths) // high
    ii = 1
    print(lengths)
    print(lower_border)
    print(higher_border)
    for i in range(0, len(borders)):
        jj = 1
        for j in range(0, len(borders[i])):
            if (borders[i][j] == 255 and lengths[ii][jj] >= higher_border):
                borders[i][j] = 255
            elif (borders[i][j] == 255 and lengths[ii][jj] <= lower_border):
                borders[i][j] = 0
            elif (borders[i][j] == 255 and lengths[ii][jj] > lower_border and lengths[ii][jj] < higher_border):
                borders[i][j] = 100
            jj += 1
        ii += 1
    #print(borders)
    for i in range(1, len(borders) - 1):
        for j in range(1, len(borders[i]) - 1):
            if (borders[i][j] == 100):
                b = False
                for k in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if (borders[k][c] == 255):
                            borders[i][j] = 255
                            b = True
                if (b == False):
                    borders[i][j] = 0
    return  borders



def get_border(img):
    gradient_matrix = get_gradient_matrix(img, sobel_x, sobel_y)
    gradient_matrix = trim_matrix(gradient_matrix, len(sobel_x)//2)
    gradient_length_matrix = get_gradient_length_matrix(gradient_matrix)
    gradient_angle_matrix = get_gradient_angle_matrix(gradient_matrix)
    #nonmax_matrix = destroy_nonmax()
    #border_filtered_matrix = border_filter(min_value, max_value)





import copy
import numpy as np


def absForList(list):
    temp = copy.deepcopy(list)
    for i in range(len(temp)):
        if temp[i] < 0:
            temp[i] = temp[i] * -1
    return temp

def maxModulDigitMatrix(list, mbMax):
    abs_list = copy.deepcopy(list)
    abs_mbMax = copy.deepcopy(mbMax)
    abs_list = absForList(abs_list)
    sum_list = sum(abs_list)
    if abs_mbMax < 0:
        abs_mbMax = abs_mbMax * -1

    s = sum_list - abs_mbMax

    if abs_mbMax >= s:
        return True

    return False


def isDetMatrixEqualsZero(matrix_A):
    if np.linalg.det(matrix_A) != 0:
        return False

    print("det = 0")
    return True


def isMaxOnDiagonal(matrix):
    len_matrix = len(matrix)
    for i in range(len_matrix):
        if not maxModulDigitMatrix(absForList(matrix[i]), matrix[i][i]):
            # print("Max is not on main diagonal!")
            return False
    return True


def testMatrix(matrix_A):
    if isMaxOnDiagonal(matrix_A) and not (isDetMatrixEqualsZero(matrix_A)):
        return True
    else:
        return False


def iterFormForA(matrix_A):
    matrix_C = copy.deepcopy(matrix_A)
    for i in range(len(matrix_A)):
        for j in range(len(matrix_A[i])):
            if matrix_A[i][j] == matrix_A[i][i]:
                matrix_C[i][j] = 0
            else:
                matrix_C[i][j] = -matrix_A[i][j] / matrix_A[i][i]
    return matrix_C


def iterFormForB(matrix_A, matrix_B):
    matrix_D = copy.deepcopy(matrix_B)

    for i in range(len(matrix_B)):
        if matrix_A[i][i] == 0:
            matrix_D[i] = 0
        else:
            matrix_D[i] = matrix_B[i] / matrix_A[i][i]

    return matrix_D


def transformMatrixForDiagonal(matrix_A, matrix_B):

    for i in range(len(matrix_A) - 1):
        for j in range(len(matrix_A)):
            if j > i:
                temp_a = copy.deepcopy(matrix_A)
                temp_b = copy.deepcopy(matrix_B)

                row_first = temp_a[i]
                row_second = temp_a[j]

                b_row_first = temp_b[i]
                b_row_second = temp_b[j]

                temp_a[i] = row_second
                temp_a[j] = row_first

                temp_b[i] = b_row_second
                temp_b[j] = b_row_first

                if isMaxOnDiagonal(temp_a):

                    matrix_A = temp_a
                    matrix_B = temp_b
                    return matrix_A, matrix_B

    print("Can't transform matrix")
    return False


def calculateIterations(matrix_C, matrix_D, x_matrix, input_e=0.0001):
    zero_matrix = copy.deepcopy(x_matrix)
    prevIterXMatrix = copy.deepcopy(matrix_D)
    e_matrix = copy.deepcopy(x_matrix)
    counter = 0

    e = 1

    while e >= input_e:
        counter += 1
        x_matrix = copy.deepcopy(zero_matrix)
        for i in range(len(matrix_C)):
            for j in range(len(x_matrix)):
                x_matrix[i] = x_matrix[i] + matrix_C[i][j] * prevIterXMatrix[j]
            x_matrix[i] += matrix_D[i]

            e_matrix[i] = abs(x_matrix[i] - prevIterXMatrix[i])

        e = max(absForList(e_matrix))
        prevIterXMatrix = copy.deepcopy(x_matrix)

    print("Number of iterations:", counter)
    print("E_matrix", e_matrix)
    return x_matrix

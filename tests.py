import matrix_generator as mat
import iteratin_method as f


def iterationFormTests():

    A_input = [[4, 1, -2],
               [1, -5, 1],
               [3, 1, -5]]

    B_input = [8, -10, 10]

    A_output = [[0, -0.25, 0.5],
                [0.2, 0, 0.2],
                [0.6, 0.2, 0]]

    B_output = [2, 2, -2]

    B_input = f.iterFormForB(A_input, B_input)
    A_input = f.iterFormForA(A_input)

    if A_input == A_output and B_input == B_output:
        return "iterationFormTests passed"
    else:
        return "iterationFormTests failed"


def simpleCaseTest():

    e = 0.000001

    A_input = [[4, 1, -2],
               [1, -5, 1],
               [3, 1, -5]]

    B_input = [8, -10, 10]

    x_matrix = mat.createMatrixTemplateB(3)

    X = [1.00000021, 2.00000001, -1.00000023]

    x_output = f.calculateIterations(f.iterFormForA(A_input), f.iterFormForB(A_input, B_input), x_matrix, e)
    for i in range(len(x_output)):
        x_output[i] = round(x_output[i], 8)

    if X == x_output:
        return "simpleCaseTest passed"
    else:
        return "simpleCaseTest failed"

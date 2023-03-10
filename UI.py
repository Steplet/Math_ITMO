import file_reader as fr
import iteratin_method as f
import matrix_generator as m


def initUserInterface():
    print("Please choose option to run")
    print("1. Random matrix")
    print("2. Get matrix from file \"input_matrix.txt\"")
    print("3. Write matrix in terminal")
    raw_input_data = input()
    try:
        data = int(raw_input_data)
    except ValueError:
        print("Wrong input, please write a number of option\n")
        return False

    if data > 3 or data < 1:
        print("Wrong number of option!\n")
        return False

    if data == 1:

        while not (randomMatrix()):
            continue

    elif data == 2:

        matrixFromFile()

    elif data == 3:

        while not (terminalMatrix()):
            continue

    return True


def terminalMatrix():

    print("Write a matrix size")
    raw_size = input()
    try:
        size = int(raw_size)
    except ValueError:
        print("Wrong input, please write a matrix size\n")
        return False

    print("Write a matrix")
    raw_matrix = input()
    matrix = raw_matrix.split()
    if len(matrix) != (size * size) + size:
        print("Wrong len matrix")
        return False

    print("Write an E digit")
    raw_e = input()
    try:
        e = float(raw_e)
    except ValueError:
        print("Wrong input, please write an E digit\n")
        return False

    matrixA = fr.getMatrixA(matrix, size)
    matrixB = fr.getMatrixB(matrix, size)

    if f.testMatrix(matrixA):

        matrixC = f.iterFormForA(matrixA)
        matrixD = f.iterFormForB(matrixA, matrixB)
        matrixZero = m.createMatrixTemplateB(size)

        result = f.calculateIterations(matrixC, matrixD, matrixZero, e)

        print("Roots:", result)


    else:

        if not f.transformMatrixForDiagonal(matrixA, matrixB):
            print("Wrong matrix")

            return True

        new_matrixA, new_matrixB = f.transformMatrixForDiagonal(matrixA, matrixB)

        if f.testMatrix(new_matrixA):

            matrixC = f.iterFormForA(new_matrixA)

            matrixD = f.iterFormForB(new_matrixA, new_matrixB)

            matrixZero = m.createMatrixTemplateB(size)

            result = f.calculateIterations(matrixC, matrixD, matrixZero, e)

            print("Roots:", result)

        else:

            print("Wrong matrix")

            return True

    return True


def matrixFromFile():
    matrixData = fr.scanMatrixInfo()

    numderOfRows = fr.getNdigit(matrixData)

    matrixA = fr.getMatrixA(matrixData, numderOfRows)

    matrixB = fr.getMatrixB(matrixData, numderOfRows)

    e = fr.getEdigit(matrixData)

    if f.testMatrix(matrixA):

        matrixC = f.iterFormForA(matrixA)
        matrixD = f.iterFormForB(matrixA, matrixB)
        matrixZero = m.createMatrixTemplateB(numderOfRows)

        result = f.calculateIterations(matrixC, matrixD, matrixZero, e)

        print("Roots:", result)

    else:
        if not f.transformMatrixForDiagonal(matrixA, matrixB):

            print("Wrong matrix")
            return True
        new_matrixA, new_matrixB = f.transformMatrixForDiagonal(matrixA, matrixB)

        if f.testMatrix(new_matrixA):
            matrixC = f.iterFormForA(new_matrixA)
            matrixD = f.iterFormForB(new_matrixA, new_matrixB)
            matrixZero = m.createMatrixTemplateB(numderOfRows)

            result = f.calculateIterations(matrixC, matrixD, matrixZero, e)

            print("Roots:", result)
        else:
            print("Wrong matrix")
            return True

def randomMatrix():
    print("Write a matrix size")

    raw_input_size = input()

    try:
        size = int(raw_input_size)
    except ValueError:
        print("Wrong input, please write a matrix number\n")
        return False

    matrixA = m.randomMatrixA(size)

    matrixB = m.randomMatrixB(size)

    if f.testMatrix(matrixA):

        matrixC = f.iterFormForA(matrixA)
        matrixD = f.iterFormForB(matrixA, matrixB)
        matrixZero = m.createMatrixTemplateB(size)

        result = f.calculateIterations(matrixC, matrixD, matrixZero)

        print("Roots:", result)
        return True

    else:
        print("Wrong random matrix!")
        print(matrixA)
        print(matrixB)

        return True


import random
import iteratin_method as f


def createMatrixTemplateA(numberOfRows):
    temp = []
    for i in range(numberOfRows):
        row = []
        for j in range(numberOfRows):
            row.append(0)
        temp.append(row)
    return temp


def randomMatrixA(numberOfRows):
    temp = []
    for i in range(numberOfRows):
        row = []
        for j in range(numberOfRows):
            row.append(random.randint(-20, 20))
        temp.append(row)
        while not (f.maxModulDigitMatrix(temp[i], temp[i][i])):
            temp[i][i] = random.randint(max(f.absForList(temp[i])), max(f.absForList(temp[i])) * 2)

    return temp


def createMatrixTemplateB(numberOfRows):
    temp = []
    for i in range(numberOfRows):
        temp.append(0)
    return temp


def randomMatrixB(numberOfRows):
    temp = []
    for i in range(numberOfRows):
        temp.append(random.randint(-100, 200))

    return temp


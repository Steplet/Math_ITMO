import matrix_generator as m


def scanMatrixInfo():
    f = open('input_matrix.txt', 'r')
    text_array = f.read().split()

    return text_array


def getEdigit(info):
    e = float(info[-1])
    info.pop(-1)

    return e


def getNdigit(info):
    n = float(info[0])
    info.pop(0)

    return int(n)


def getMatrixA(info, n):
    A = []

    row = []
    for i in range(len(info)):

        if (i + 1) % (n + 1) == 0:
            continue
        else:
            if len(row) < n:
                row.append(float(info[i]))
                if len(row) == n:
                    A.append(row)
                    row = []

    return A


def getMatrixB(info, n):
    B = []

    for i in range(len(info)):

        if (i + 1) % (n + 1) == 0:
            B.append(float(info[i]))

    return B

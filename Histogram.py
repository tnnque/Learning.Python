x = input()
s = x.split()


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def plotMatrix(mat):
    for i in mat:
        for j in i:
            if j == 1:
                print('*', end= '')
            else:
                print(' ', end= '')
        print('')


def convertDictToMatrix(d):
    matrix = []
    max_value = 0
    # Tim max
    for key in d:
        value = d[key]
        if value >= max_value:
            max_value = value
    # Matran 0 1
    for i in d:
        x = []
        # if d[i] ==:
        for j in range(0, d[i]):
            x.append(1)

        for k in range(d[i], max_value):
            x.append(0)
        matrix.append(x)
    # return matrix
    # Rotate 90
    matrix2 = []
    # matrix2 = matrix.copy()
    for i in matrix:
        sup = []
        for j in i:
            if vi tri cua j >= max_value:
                sup.append(i[j])
            max_value = max_value - 1
        matrix2.append(sup)
    # for i in range(0, len(matrix)):


        # for j in range(0, len(matrix[i])):

            # matrix2[i][j] = matrix[j][i]
    return matrix2


h = histogram(x)
c = convertDictToMatrix(h)
# plotMatrix(c)
print(c)

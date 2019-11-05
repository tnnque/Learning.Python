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
        sup_matrix = []
        # if d[i] ==:
        for j in range(0, d[i]):
            sup_matrix.append(1)

        for k in range(d[i], max_value):
            sup_matrix.append(0)
        matrix.append(sup_matrix)
    # return matrix
    # Rotate 90
    matrix2 = []
    # for j in matrix:
    #     rev_j = reversed(j)
    sub_matrix2 = []
    #     for i in rev_j:
    #         sub_matrix2.append(i)
    a = 0
    for i in matrix:
        while matrix.index(i) <= a:
            last_i = next(i[-a])
            sub_matrix2.append(last_i)
            a = a + 1
        matrix2.append(sub_matrix2)

    # matrix2 = matrix.copy()

    # return matrix2


h = histogram(x)
c = convertDictToMatrix(h)
# plotMatrix(c)
print(c)
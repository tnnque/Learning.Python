x = input()
s = x.split()

def plot_matrix(R, C, matrix):
    for i in range(R):
        a = []
        for j in range(C):
            a.append(int())
        matrix.append(a)
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end=" ")
        print()
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    C = len(d)
    R = max(d[x])
    for y in d:
        print(y,d[y])
histogram(x)

def plot_img():

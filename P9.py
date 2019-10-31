import sys
for u in sys.stdin.readlines():
    n = u.split(" ")
    n = list(map(int, n))
    l = len(n)

    for k in range(l):
        n1 = n[k:]
        mini = n1[0]

        for i in n1:
            if i < mini:
                mini = i

        id = n.index(mini)
        temp = mini
        n[id] = n[k]
        n[k] = temp

    print(n)

    #Hiếu là tên Mực Râu đáng ghét xí xí
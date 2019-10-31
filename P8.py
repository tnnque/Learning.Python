
n = int(input())
i = 1
x = '*'
y = ' '
s = (2 * n) - 1

while i <= n:
    k = int((2 * i) - 1)
    l = int((s - k)/2)
    print(l*y, end ="")
    print(x*k)
    i = i + 1
import sys
for n in sys.stdin.readlines():
    i = 1
    s = 0
    while i <= int(n):
        if (i % 2) == 0:
            s = s - (1/i)

        else:
            s = s + (1/i)
        i = i + 1
    print(round(s, 2))
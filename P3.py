import sys
for n in sys.stdin.readlines():
    i = 1
    s = 1
    if n == 0:
        print(1)
    else:
        while i <= int(n):
            s = s * i
            i = i + 1
    print (round(s,2))
import sys
for n in sys.stdin.readlines():
    i = 1
    s1 = 0
    s2 = 0
    while i <= int(n):
        s1 = s1 + i
        s2 = s2 + 1/s1
        i = i + 1
    print (round(s2,3))
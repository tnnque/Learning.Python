#n = input()
import sys
for n in sys.stdin.readlines():
    i = 0
    s = 0
    while i <= int(n):
        s = s + (1/(2*i + 1))
        i = i + 1
    print (round(s,2))

import sys
for x in sys.stdin.readlines ():
    a, b = x.split(" ")
    a, b = int(a), int(b)
    i = 1
    s = 0
    while i <= b:
        s = s + pow(a, 2 * i)
        i = i + 1
    print (s)
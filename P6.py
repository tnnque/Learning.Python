#import sys
#for x in sys.stdin.readlines():
#    a, b, c, d = x.split(" ")
#    a, b, c, d = int(a), int(b), int(c), int(d)

#    minimum = min (a, b, c, d)
#    maximum = max (a, b, c, d)

#    print(minimum, end = " ")
#    print(maximum)

import sys
for x in sys.stdin.readlines():
    a, b, c, d = x.split(" ")
    a, b, c, d = int(a), int(b), int(c), int(d)
    qlist = [a, b, c, d]
    maxi = qlist[0]
    mini = qlist[0]

    for n in qlist:
        if n <= mini:
            mini = n

    for m in qlist:
        if m >= maxi:
            maxi = m

    print(mini, end = " ")
    print(maxi)

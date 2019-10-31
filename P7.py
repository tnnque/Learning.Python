import sys
for u in sys.stdin.readlines():
    n = int(u)
    i = 2
    s = 0
    check = 0
    if n == 1:
        print ("No")
    # if n == 2 or n == 3:
    #     print ("Yes")
    else:
        while i < n:
            if (n % i) == 0:
                check = 1
                print("No")
                break
            i = i + 1
        if check == 0:
            print("Yes")

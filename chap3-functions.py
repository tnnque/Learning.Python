#Exercise 3.1

# def right_justify (s):
#     a = ' '
#     b = 70 - len(s)
#
#     print(a * b + s)
#
# right_justify('monty')

#Exercise 3.2

# def do_twice (f,x):
#     f(x)
#     f(x)
#
# def print_spam() :
#     print('spam')
#
# def print_twice(y):
#     print(y)
#     print(y)
#
# # do_twice(print_twice,'spam')
#
# def do_four (g,z) :
#     do_twice(g,z)
#     do_twice(g,z)
# do_four(print_twice,'spam')

#Exercise 3.3

def do_twice (f):
    f()
    f()

def do_four (g) :
    do_twice(g)
    do_twice(g)

def print_row():
    a = ('+' + '-' * 4) * 2 + '+'
    print(a)

def print_col():
    b = ('|' + ' ' * 4) * 2 + '|'
    print(b)

grid = print_row() + do_four(print_col())
print(grid)
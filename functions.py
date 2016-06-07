# Note that defining functions directly in a python script/module is
# easy.  You do not need to put your own custom functions in separate
# files.

def myfunc1(a, b):
    c = a + b
    return c


a1 = 7
b1 = 3
c1 = myfunc1(a1, b1)

a2 = 'hello '
b2 = 'students'
c2 = myfunc1(a2, b2)

# Returning multiple values is easy:
def myfunc2(a, b):
    c = a + b
    d = a*b
    return c, d

c3, d3 = myfunc2(5.0, 3.0)

# Default values are easy; any variable that has a default can be
# considered optional:
def myfunc3(a=1, b=2):
    c = a+b
    return c

c4 = myfunc3()
c5 = myfunc3(a=2)
c6 = myfunc3(b=7)


def myfunc4(a, b=7):
    c = a+b
    return c

c7 = myfunc4(1)

def myfunc5(b, a=1):
    c = a+b
    return c

c8 = myfunc5(1,2)

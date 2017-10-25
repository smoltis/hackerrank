# example 1, composition
def f(x):
    return x + 2

def g(h, x):
    return h(x) * 2

print(g(f, 42))

# example 2, closure
def addx(x):
    def _(y):
        return x + y
    return _

add2 = addx(2)
add3 = addx(3)

print(add2(3), add3(2))

# example 3, currying
def f(x,y):
    return x * y

def f2(x):
    def _(y):
        return f(x, y)
    return _

print(f2(2))
print(f2(2)(3))

# scope is checked by LEGB rule => local, enclosing, global, built-in

#local functions (may contain imports, new instance per execution)
g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    inner()
outer()

# error
#outer.inner()

#closure (closing over variables from earlier scopes to prevent them from garbage collecting)
def outer():
    x = 3
    def inner(y):
        return x+y # can reference enclosing variables (LEGB)
    return inner # can return local function result
i = outer()
print(type(i))
print(i.__closure__) # all closures have dunder closure attribute

# function factory
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp
#from raise_to import raise_to
square = raise_to(2)
print(square.__closure__)
print(square(5))
cube = raise_to(3)
print(cube(3))

import platform

print(platform.python_version())

#conditional expression
result = True if 1 == 2 else False
print("That's ", result) 
print(type(result))

#lambdas Alonzo Church
# sorted(key=) accepts callable

scientists = ["one a", "two c", "three b"]
my_lambda = lambda name: name.split(" ")[-1]
sl = sorted(scientists, key=my_lambda)
print(sl)
print(callable(my_lambda))

#arbitrary number of arguments
def hypervolume(*lengths):
    i = iter(lengths)
    v=next(i)
    for length in i:
        v *= length
    return v
print(hypervolume(3,4,5))
#hypervolume()
#Stop Iter error when no arguments passed, fix it
def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v
print(hypervolume(3,4,5))
#print(hypervolume())

#arbitrary keyword arguments
def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))
    result = "<"+name
    for k,v in kwargs.items():
        result += ' {}="{}"'.format(k,v)
    result += ">"
    return result

tag('img', src="monet.jpg", alt="Sunrise by Calude Monet", border=1)    
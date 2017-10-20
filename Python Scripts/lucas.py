def fibon(stopval):
    yield 2
    a=2
    b=1
    while b<stopval:
        yield b
        a,b = b, a + b

for x in fibon(1000):
    print(x)
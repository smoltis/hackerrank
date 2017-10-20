from functools import lru_cache

#recursive with cache, dynamic programming
@lru_cache(100)
def fib(n):
    if n<2: return n
    return fib(n-1)+fib(n-2)

#generator
def fib_generator(n):
    i=0
    a, b = 0, 1
    while i<:
        yield b
        a, b = b, a+b
        i +=1

#iterative
def fib(n):
    '''
    > fib(2)
    1
    > fib(5)
    5
    > fib(7)
    13
    '''
    if n < 3:
        return 1
    a, b = 0, 1
    count = 1
        while count < n:
        count += 1
        a, b = b, a+b
    return b


print(fib(4))

#1 1 2 3 5
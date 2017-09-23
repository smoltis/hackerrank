def wrapper(f):
    def fun(t):
        # complete the function
        t = ["+91 {} {}".format(item[-10:-5],item[-5:]) for item in t]
        return f(t)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = ['07895462130','919875641230','9195969878']
    #l = [input() for _ in range(int(input()))]
    sort_phone(l)
#expected
#+91 78954 62130
#+91 91959 69878
#+91 98756 41230

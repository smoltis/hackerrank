import dis

def f(x):
    return x.g(lambda x: x.good, lambda x: x.member)

dis.dis(f)

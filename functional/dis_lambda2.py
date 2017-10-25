import dis

def l1(x):
    return x.good
def l2(x):
    return x.member

def f1(x):
    return x(l1, l2)

dis.dis(f1)
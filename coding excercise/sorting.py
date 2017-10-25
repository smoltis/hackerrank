def ginortS():
    # a-z A-Z odd even
    ref = list(map(chr, range(ord('a'), ord('z') + 1)))
    ref.extend(list(map(chr, range(ord('A'), ord('Z') + 1))))
    ref.extend(list(map(str, range(1, 10, 2))))
    ref.extend(list(map(str, range(0, 10, 2))))
    return dict(zip(ref, range(len(ref))))


def alpha_d(ch):
    import string
    st = string.ascii_letters+string.digits[1::2]+string.digits[::2]
    d = dict(zip(list(st), range(len(st))))
    return d.get(ch, 0)


s = input().strip()
mysortdic = ginortS()
print(*sorted(s, key=lambda i: mysortdic.get(str(i), 0)), sep="")
print(*sorted(s, key=lambda i: alpha_d(str(i))), sep="")

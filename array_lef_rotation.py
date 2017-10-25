
def array_left_rotation(a, n, k):
    # calc index and then swap parts
    if k == n:
        return a
    elif k < n:
        return a[k:] + a[:k]
    else:
        i = k%n
        return array_left_rotation(a, n, i)


if __name__ == "__main__":
    n = 5
    k = 6
    a = [1,2,3,4,5]
    #expected: 5 1 2 3 4
    answer = array_left_rotation(a, n, k)
    print(*answer, sep=' ')

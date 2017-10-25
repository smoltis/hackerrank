"""
Find all permutations of s within b, where s,b are arbitrary strings
"""

def permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


if __name__ == "__main__":
    s = 'xacxzaa'
    b = 'fxaazxacaaxzoecazxaxaz'
    counter = 0

    # example: xaazxac
    for p in permutations(s):
        if b.find(p) > -1:
            counter += 1
    print(counter)
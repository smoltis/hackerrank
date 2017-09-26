def swap_case(s):
    result = []
    for ch in list(s):
        result.append(ch.lower() if ch.isupper() else ch.upper())
    return "".join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
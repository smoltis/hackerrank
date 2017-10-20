if __name__=="__main__":
    mset = set("2 4 5 9".split())
    nset = set("2 4 11 12".split())
    symdiff = nset^mset

    final = sorted(map(int,symdiff))
    for item in final:
        print(item)
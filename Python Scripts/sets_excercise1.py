if __name__ == "__main__":
    #n, m = map(int,input().split())
    myarray = map(int,"1 5 3".split())
    A, B = map(int,"3 1".split()), map(int,"5 7".split())
    happiness = 0
    A = set(A)
    B = set(B)
    #reduce A
    redA = A - B
    redB = B - A
    
    for element in myarray:
        if element in redA:
            happiness += 1
        if element in redB:
            happiness -= 1
    print(happiness)
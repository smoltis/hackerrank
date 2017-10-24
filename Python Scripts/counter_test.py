from collections import Counter
import os

total = 0
try:
    with open(os.path.join(os.getcwd(),'counter_test.txt'),'r') as f:
        num_shoes = int(f.readline()) # 100
        sizes = Counter(f.readline().split())
        n_cusomers = int(f.readline()) # 1000
        for line in f.readlines():
            raw = line.split()
            size, price = raw[0], int(raw[1])
            if(sizes[size] > 0):
                sizes.subtract([size])
                total += price
    print(total) # 6378
except Exception as e:
    print(e)
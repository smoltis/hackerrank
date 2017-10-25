import sys
import os

def process_file(f):
    for line in f:
        print(line[::-1], end="")

if __name__ == '__main__':

    if len(sys.argv) == 1:
        process_file(sys.stdin)
    else:
        for path in sys.argv[1:]:
            try:
                with open(path,"r") as file:
                    process_file(file)
            except Exception as e:
                print("%s" % e, file = sys.stderr)
                continue


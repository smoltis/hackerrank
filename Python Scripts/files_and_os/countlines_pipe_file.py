"""
In Windows:

>type ..\algo.py | python ./countlines_pipe_file.py
19

python ./countlines_pipe_file.py ../algo.py
19
"""


import sys

if __name__ == "__main__":
    #no args, read pipe
    if len(sys.argv) == 1:
        try:
            print(len(sys.stdin.readlines()))
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(e)
    else:
        try:
            with open(sys.argv[1], 'r') as f:
                print(len(f.readlines()))
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(e)
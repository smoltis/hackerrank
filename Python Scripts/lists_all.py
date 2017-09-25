def list_ops(*args):
    mylist = []
    for item in args:
        command,*args = item
        if command == "insert":
            idx, value = args
            mylist.insert(int(idx),int(value))
        elif command == "append":
            mylist.append(int(args.pop()))
        elif command == "remove":
            mylist.remove(int(args.pop()))
        elif command == "pop":
            mylist.pop()
        elif command == "sort":
            mylist.sort()
        elif command == "reverse":
            mylist.reverse()
        elif command == "print":
            print(mylist)
        
if __name__ == '__main__':
    #N = int(input())
    #commands = [input().split() for i in range(N)]
    #list_ops(*commands)
    commands = [['insert', '0', '5'],
    ['insert', '1', '10'],
    ['insert', '0', '6'],
    ['print'],
    ['remove', '6'],
    ['append', '9'],
    ['append', '1'],
    ['sort'],
    ['print'],
    ['pop'],
    ['reverse']
    ,['print']]
    list_ops(*commands)    
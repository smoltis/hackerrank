"""
Print the sum of the elements of set  on a single line.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
"""
n = int(input())
s = set(map(int, input().split())) 
n_cmd = int(input())

for _ in range(n_cmd):
    action = input().split()
    if len(action) == 1:
        s.pop()
        continue
    cmd, num = action[0], int(action[1])
    if cmd == "remove":
        s.remove(num)
    elif cmd == "discard":
        s.discard(num)
print(sum(s))
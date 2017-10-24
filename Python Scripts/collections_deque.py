"""
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

The first line contains an integer N, the number of operations. 
The next N lines contains the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque d.

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
"""

from collections import deque

def deque_ops(command, value = None):
    try:
        if command == 'append':
            d.append(int(value))
        elif command == 'pop':
            d.pop()
        elif command == 'popleft':
            d.popleft()
        elif command == 'appendleft': 
            d.appendleft(value)
    except:
        pass

d = deque()
n = int(input())
for _ in range(n):
    raw = input().split()
    if len(raw) == 2:
        command, value = raw[0], raw[1]
    else:
        command = raw[0].strip()
    deque_ops(command, value)

print(*[item for item in d])
"""
Task

You are the manager of a supermarket. 
You have a list of  items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""

from collections import OrderedDict

n = int(input())

sales = OrderedDict()

for _ in range(n):
    row = input().split()
    item = ' '.join(row[:-1])
    price = int(row[-1])
    sales[item] = sales.get(item,0) + price

for item in sales.items():
    print(*item)
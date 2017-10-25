"""
Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

We delete the following characters from our two strings to turn them into anagrams of each other:

cde
abc

Remove d and e from cde to get c.
Remove a and b from abc to get c.
We must delete 4 characters to make both strings anagrams, so we print 4  on a new line.
"""
from collections import Counter
def number_needed(a, b):
    c = Counter(a) & Counter(b)
    return len(a)+len(b)-2*sum(c.values())

if __name__ == "__main__":
    a = 'cde'
    b = 'abc'
    print(number_needed(a, b))


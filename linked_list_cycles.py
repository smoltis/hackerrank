"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
visited = set()

def has_cycle(head):
    if head == None: return False
        
    if head.next != None:
        visited.add(head.data)
        if head.next.data in visited:
            return True
        else:
            has_cycle(head.next)
    return False
    
    


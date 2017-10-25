
class Node(object):    
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, value):
        if value <= self.data:
            if self.left == None: # == None
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data: 
            return True
        elif value < self.data:
            if self.left == None: 
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)

    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()
        print(self.data, end = ' ')
        if self.right != None:
            self.right.printInOrder()
    
    def printPreOrder(self):
        print(self.data, end = ' ')
        if self.left != None:
            self.left.printInOrder()
        if self.right != None:
            self.right.printInOrder()
    
    def printPostOrder(self):
        if self.left != None:
            self.left.printInOrder()
        if self.right != None:
            self.right.printInOrder()
        print(self.data, end = ' ')


def checkBST(n, min=-float('Inf'), max=float('Inf')):
    if not n:
        return True
    if n.data <= min or n.data >= max:
        return False
    return checkBST(n.left, min, n.data) and checkBST(n.right, n.data, max)

if __name__ == "__main__":
    
    tree = Node(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(8)

    print('Contains 8:', tree.contains(8)) #expected: True

    print('In-order traversal: ')
    tree.printInOrder()
    print()
    print('Pre-order traversal: ')
    tree.printPreOrder()
    print()
    print('Post order traversal: ')
    tree.printPostOrder() 

    # 2
    # 1 2 4 3 5 6 7
    no_bin_search_tree = Node(4)
    no_bin_search_tree.insert(1)
    no_bin_search_tree.insert(2)
    no_bin_search_tree.insert(3)
    no_bin_search_tree.insert(5)
    no_bin_search_tree.insert(6)
    no_bin_search_tree.insert(7)
    print(checkBST(no_bin_search_tree))

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


def checkBST(root):
    left_check = True
    right_check = True
    
    if root.left != None:
        if root.data <= root.left.data:
            left_check = False
        else:
            left_check = checkBST(root.left)
    
    if root.right != None:
        if root.data >= root.right.data:
            right_check = False
        else:
            right_check = checkBST(root.right)
            
    return left_check and right_check
 
if __name__ == "__main__":
    tree = Node(4)
    string = "1 2 3 5 6 7 8 9 10 11 12 13 14 15 16 16 18 19 20 21 22 23 24 25 26 27 28 29 30 31"
    for s in string.split():
        tree.insert(int(s))
    
    print(checkBST(tree))
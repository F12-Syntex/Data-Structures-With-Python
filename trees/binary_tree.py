class Node(object):
    def __init__(self, data) -> None:
        self.left : Node = None
        self.right : Node = None
        self.data = data

    def __str__(self) -> str:
        if self.left is not None and self.right is not None:
            return str(self.data) + " -> " + str(self.left) + " " + str(self.right)
        elif self.left is not None:
            return str(self.data) + " -> " + str(self.left)
        elif self.right is not None:
            return str(self.data) + " -> " + str(self.right)
        else:
            return str(self.data)
        
    def printPreOrder(self):
        print(str(self.data))
        if(self.left):
            self.left.printPreOrder()
        if(self.right):
             self.right.printPreOrder()



class BinaryTree(object):
    def __init__(self, data) -> None:
        self.root = Node(data)

    def __str__(self) -> str:
        return str(self.root)

bt = BinaryTree(3)
bt.root.left = Node(1)
bt.root.right = Node(2)
bt.root.printPreOrder()

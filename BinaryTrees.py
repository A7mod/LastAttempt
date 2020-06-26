class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

class BinaryTree(object):
    def __init__(self, root):     #defining constructor
        self.root = Node(root)

    def preorder_print(self, start, traversal):     #preorder traversal module
        """ ORDER : Root -> Left -> Right """
        if start:
            traversal += (str(start.value) + ".")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal    



#             1
#           /   \
#          2     3 
#        /  \   /  \
#       4    5 6    7

# Set up Tree

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


 
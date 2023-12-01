class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node


# ALTERNATIVELY, YOU CAN CONSTRUCT A BST WITHOUT ANY NODE TO START OFF WITH
# Note that the constructor only takes in self in this case
class BinarySearchTree:
    def __init__(self):
        self.root = None


## I combined the two methods to work in tandem
class BinarySearchTree:
    def __init__(self, value=None):
        if value is None:
            self.root = None
        else:
            self.root = Node(value)



# IF USING METHOD 1:
my_tree = BinarySearchTree()


# IF USING METHOD 2:
my_tree = BinarySearchTree(1)


# IF USING MY METHOD:
my_tree = BinarySearchTree()
# OR...
my_tree = BinarySearchTree(5)

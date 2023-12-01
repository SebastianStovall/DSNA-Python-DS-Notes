# PSUEDOCODE FOR INSERTING A NEW NODE INTO A BST:

# 1.) create new_node
# 1a.) if root is None...  root = new_node (return and be done)
# 2.) DETERMINE WHERE TO PLACE --->   if < go LEFT ... if > go RIGHT
# 2a.) temp = self.root (see line 10)

# 3.) each time you move left or right there are two possibilities:  1.) there is a node in that spot    2.) there isnt a node
# 3a.) our code is solely dependent if node is LESS or GREATER than curr node,  if new_node == temp: return False
# 4.) if there ISNT a node, just insert node there, else... repeat step 2 and 3

# Note: steps 2 and 3 should be happening in a while loop --->  temp = self.root
                                                                # while(temp):


# Implement the insert method for the BinarySearchTree class that inserts a new node with a given value into the binary search tree.

# The method should perform the following tasks:

# Create a new instance of the Node class using the provided value.

# If the binary search tree is empty (i.e., self.root is None), set the root attribute of the BinarySearchTree class to point to the new node and return True.

# If the binary search tree is not empty, initialize a temporary variable temp to point to the root node, and then perform the following steps in a loop until the new node is inserted:

# If the value of the new node is equal to the value of the current node (stored in temp), return False, indicating that duplicate values are not allowed in the tree.

# If the value of the new node is less than the value of the current node, check if the left child of the current node is None:

# If it is, set the left child of the current node to the new node and return True.

# If it is not, update temp to point to the left child and continue the loop.

# If the value of the new node is greater than the value of the current node, check if the right child of the current node is None:

# If it is, set the right child of the current node to the new node and return True.

# If it is not, update temp to point to the right child and continue the loop.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:   # if our tree is empty, just assign the root to be the new_node and return
            self.root = new_node
            return True

        temp = self.root # initialize a pointer at root so we dont overwrite the actual root value
        while(temp): # loop until we find where to place

            if value == temp.value: # if the value we are trying to insert already exists, return false
                return False

            elif value > temp.value:   # if the value we are looking at is greater than the value of the node we are pointing at...
                if temp.right is not None: # then check if where we are going to is occupied or not, if it IS, navigate to the right and go to next iteration of loop
                    temp = temp.right
                else:
                    temp.right = new_node # else... assign the null node to be the new_node and return
                    return True

            elif value < temp.value:      # same logic for 64 - 69, but reversed
                if temp.left is not None:
                    temp = temp.left
                else:
                    temp.left = new_node
                    return True




##########################################################
##   Test code below will print output to "User logs"   ##
##########################################################


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Insert to Empty Tree -----\n")
bst = BinarySearchTree()
result = bst.insert(5)
check(True, result, "Insert 5, should succeed:")
check(5, bst.root.value, "Root value after inserting 5:")
check(None, bst.root.left, "Root's left child after inserting 5:")
check(None, bst.root.right, "Root's right child after inserting 5:")

print("\n----- Test: Insert to Existing Tree -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result = bst.insert(3)
check(True, result, "Insert 3, should succeed:")
check(3, bst.root.left.left.value, "Root's left-left value after inserting 3:")
check(None, bst.root.left.left.left, "Root's left-left-left child after inserting 3:")
check(None, bst.root.left.left.right, "Root's left-left-right child after inserting 3:")

print("\n----- Test: Insert Duplicate Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
result = bst.insert(5)
check(False, result, "Insert 5 again, should fail:")
check(None, bst.root.left.left, "Root's left-left child after inserting 5 again:")
check(None, bst.root.left.right, "Root's left-right child after inserting 5 again:")

print("\n----- Test: Insert Greater Than Root -----\n")
bst = BinarySearchTree()
bst.insert(10)
result = bst.insert(15)
check(True, result, "Insert 15, should succeed:")
check(15, bst.root.right.value, "Root's right value after inserting 15:")
check(None, bst.root.right.left, "Root's right-left child after inserting 15:")
check(None, bst.root.right.right, "Root's right-right child after inserting 15:")

print("\n----- Test: Insert Less Than Root -----\n")
bst = BinarySearchTree()
bst.insert(10)
result = bst.insert(5)
check(True, result, "Insert 5, should succeed:")
check(5, bst.root.left.value, "Root's left value after inserting 5:")
check(None, bst.root.left.left, "Root's left-left child after inserting 5:")
check(None, bst.root.left.right, "Root's left-right child after inserting 5:")

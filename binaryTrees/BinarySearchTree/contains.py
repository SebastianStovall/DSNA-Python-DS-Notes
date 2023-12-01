# Implement the contains method for the BinarySearchTree class that checks if a node with a given value exists in the binary search tree.

# The method should perform the following tasks:

# Initialize a temporary variable temp to point to the root node of the binary search tree.

# Use a loop to traverse the binary search tree until the target value is found or the end of the tree is reached:

# If the target value is less than the value of the current node (stored in temp), update temp to point to the left child and continue the loop.

# If the target value is greater than the value of the current node, update temp to point to the right child and continue the loop.

# If the target value is equal to the value of the current node, return True, indicating that the target value exists in the tree.

# If the loop ends without finding the target value, return False, indicating that the target value does not exist in the tree.


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
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):   # here
        def check_tree(temp):
            if temp is None: # if temp root is None, return false
                return False

            if temp.value == value:  # if temp's value is the value we are trying to find, return True
                return True

            check_left = check_tree(temp.left)   # recursively check the left side of the tree
            check_right = check_tree(temp.right) # recursively check the right side of the tree
            return check_left or check_right # check if target was found on the left or right side of the tree

        return check_tree(self.root) # pass in self.root to be temp


    # ITERATIVE VERSION OF THE CONTAINS METHOD
    def containsIterativeVersion(self, value):
        temp = self.root
        while(temp is not None):   # basically just determine where you need to go by checking the temp's value and comparing it to the value your trying to find
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True   # if value matches temp.value, return True
        return False   # if at any point the root becomes None before you found the value your looking for, return False because the value does not exist in the tree




##########################################################
##   Test code below will print output to "User logs"   ##
##########################################################


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Contains on Empty Tree -----\n")
bst = BinarySearchTree()
result = bst.contains(5)
check(False, result, "Check if 5 exists in an empty tree:")

print("\n----- Test: Contains Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result = bst.contains(10)
check(True, result, "Check if 10 exists:")
result = bst.contains(5)
check(True, result, "Check if 5 exists:")
result = bst.contains(15)
check(True, result, "Check if 15 exists:")

print("\n----- Test: Contains Not Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
result = bst.contains(15)
check(False, result, "Check if 15 exists:")

print("\n----- Test: Contains with Duplicate Inserts -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(10)
result = bst.contains(10)
check(True, result, "Check if 10 exists with duplicate inserts:")

print("\n----- Test: Contains with Left and Right -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(1)
bst.insert(8)
bst.insert(12)
bst.insert(20)
result = bst.contains(1)
check(True, result, "Check if 1 exists:")
result = bst.contains(8)
check(True, result, "Check if 8 exists:")
result = bst.contains(12)
check(True, result, "Check if 12 exists:")
result = bst.contains(20)
check(True, result, "Check if 20 exists:")

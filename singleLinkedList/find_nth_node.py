# Implement the get method for the LinkedList class.
# The get method should take an integer index as a parameter and return a pointer to the node at the specified index in the linked list.
# If the index is out of bounds (less than 0 or greater than or equal to the length of the list), the method should return None.


# Keep in mind the following requirements:

# 1.) The method should handle the cases where the index is out of bounds.

# 2.) The method should start at the head of the list and traverse the list using the next attribute of the nodes.

# 3.) The method should stop traversing the list when it reaches the specified index and return the node at that position.

# 4.) If the index is out of bounds, the method should return None.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def find_nth_node(self,index):     # can also use this function to change the node's value once you find the node
        # if the node you want to find is EQUAL to the length of list "the null pointer" OR its out of bounds (less than or greater than list), return None"
        if index >= self.length or index < 0:
            return None

        temp = self.head        # <--- create a reference to the head that you can iterate through without actually re-assigning head pointer
        count = 0
        while(temp):
            if count == index:    # <--- if count = n, return the node
                return temp
            else:
                temp = temp.next   # <--- else, go to the next node and increase the counter
                count += 1



my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.find_nth_node(3).value)



"""
    EXPECTED OUTPUT:
    ----------------
    3

"""

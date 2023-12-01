# Implement the append method for the LinkedList class.
# The append method should add a new node with a given value to the end of the linked list, updating the tail attribute and the length attribute accordingly.

# Keep in mind the following requirements:

# 1.) The method should handle the cases where the list is empty and where the list already has one or more nodes.

# 2.) The method should create a new node with the given value and add it to the end of the list.

# 3.) The method should update the tail attribute of the LinkedList correctly.

# 4.) The method should update the length attribute of the LinkedList to reflect the addition of the new node.





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

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):           # <--------- HERE
        new_node = Node(value)
        if self.head is None:         # <---- if list is empty, have head and tail point to new node
            self.head = new_node
            self.tail = new_node
        else:                                   # <----- else, assign the tail's next pointer to be the new node, then shift over the tail pointer to be the new node
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1




my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2

    Linked List:
    1
    2

"""

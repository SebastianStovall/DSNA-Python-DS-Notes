# Implement the prepend method for the LinkedList class.

# The prepend method should add a new node with a given value to the beginning of the linked list, updating the head attribute and the length attribute accordingly.

# Keep in mind the following requirements:

# 1.) The method should handle the cases where the list is empty and where the list already has one or more nodes.

# 2.) The method should create a new node with the given value and add it to the beginning of the list.

# 3.) The method should update the head attribute of the LinkedList correctly.

# 4.) The method should update the length attribute of the LinkedList to reflect the addition of the new node.

# 5.) The method should return True if the operation is successful.


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

    # inserts a node to the beggining of a linked list
    def add_to_head(self,value):                                         # <------ here  ( this method was called prepend() in the DSNA video )
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True

        new_node.next = self.head               # <------ assign the new node's next value to be the head
        self.head = new_node                     # <------ assign the head pointer to the new node
        self.length += 1
        return True



my_linked_list = LinkedList(2)
my_linked_list.append(3)

print('Before prepend():')
print('----------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()


my_linked_list.add_to_head(1)


print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:

    Before prepend():
    ----------------
    Head: 2
    Tail: 3
    Length: 2

    Linked List:
    2
    3


    After prepend():
    ---------------
    Head: 1
    Tail: 3
    Length: 3

    Linked List:
    1
    2
    3

"""

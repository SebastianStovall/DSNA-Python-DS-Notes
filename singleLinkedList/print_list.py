# Implement a method print_list(self) that prints the linked list's elements, one per line.
# YOUR IMPLEMENTATION WILL BE A CLASS METHOD IN THE LINKED LIST CLASS...

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

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):                      # <-------------- HERE
        while(self.head != None):
            print(self.head.value)
            self.head = self.head.next

            # self.head = the node object
            # so... key into the node object then into the value key



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3

"""

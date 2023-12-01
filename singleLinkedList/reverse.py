# Implement the reverse method for the LinkedList class.
# The reverse method should reverse the order of the nodes in the linked list so that the head becomes the tail and the tail becomes the head.
# The method should not create any new nodes or modify the values of the nodes.
# The method should only update the next attribute of each node to point to the previous node in the list.


# Consider the following requirements while implementing the method:

# 1.) The method should handle edge cases, such as an empty list or a list with a single node.

# 2.) The method should utilize a temporary variable to swap the head and tail attributes of the LinkedList class.

# 3.) The method should use a loop to iterate through the nodes in the list and update the next attribute of each node.

# 4.) The method should not modify the length attribute of the LinkedList class.


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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head        ##   FIRST, SWAP THE HEAD AND TAIL POINTERS (TEMP = self.HEAD --->  self.HEAD = self.TAIL --->  self.TAIL = TEMP)
        self.head = self.tail   ##
        self.tail = temp        ##
        after = temp.next       ###  THEN, SET UP THE NECESSARY POINTERS FOR THE REVERSAL
        before = None           ###        after = what still needs to be reversed     before = what has already been reversed
        while(temp is not None):
            after = temp.next     # after represents the rest of the list we still need swapped (specifically the current head of the unreversed list)
            temp.next = before  # the temp head node than becomes part of the reversed list
            before = temp    # the reversed list's head comes up to the (now reversed) head
            temp = after   # the temp head used for reversal then goes to the next node that needs reversing




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1

"""

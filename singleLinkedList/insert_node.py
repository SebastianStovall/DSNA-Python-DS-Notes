# Implement the insert method for the LinkedList class.
# The insert method should take an integer index and a value as parameters and insert a new node with the given value at the specified index in the linked list.
# If the index is out of bounds, the method should return False. If the new node is successfully inserted, the method should return True.


# Keep in mind the following requirements:

# 1.) The method should handle edge cases, such as inserting a new node at the beginning or end of the list.

# 2.) The method should utilize the prepend, append, and get methods for handling these edge cases.

# 3.) The method should create a new node with the given value and insert it at the specified index.

# 4.) The method should update the next attribute of the previous node to point to the new node.

# 5.) The method should increment the length attribute of the LinkedList class.

# 6.) The method should return True if the new node is successfully inserted.

# 7.) If the index is out of bounds, the method should return False.


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

    def insert(self, index, value):           # <---- here

        # if placing at start
        if index == 0:
            self.prepend(value)
            return True

        # if placing at end
        if index == self.length:
            self.append(value)
            return True

        # check if node is in a valid range of the list
        node_at_index = self.get(index)
        if node_at_index == None:
            return False

        # if valid, create the new node to insert with
        new_node = Node(value)

        # determine where to insert node
        temp = self.head   # give a reference to the head so we can iterate through the list without reassigning the real head pointer
        count = 0
        while(temp):
            # find insertion point --- place right BEFORE the given index (index - 1)
            if count == (index - 1):
                rest_of_list = temp.next    # grab a reference to the rest of the list before assigning anything
                temp.next = new_node        # assign the head's next pointer to be the incoming node
                new_node.next = rest_of_list  # assign the incoming node's next value to be the rest of the list
                self.length += 1
                return True
            else:
                temp = temp.next
                count += 1


my_linked_list = LinkedList(1)
my_linked_list.append(3)


print('LL before insert():')
my_linked_list.print_list()

my_linked_list.insert(1,2)

print('\nLL after insert(2) in middle:')
my_linked_list.print_list()


my_linked_list.insert(0,0)

print('\nLL after insert(0) at beginning:')
my_linked_list.print_list()


my_linked_list.insert(4,4)

print('\nLL after insert(4) at end:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before insert():
    1
    3

    LL after insert(2) in middle:
    1
    2
    3

    LL after insert(0) at beginning:
    0
    1
    2
    3

    LL after insert(4) at end:
    0
    1
    2
    3
    4

"""

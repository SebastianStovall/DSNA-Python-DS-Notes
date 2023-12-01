# Implement the pop_first method for the LinkedList class.

# The pop_first method should remove the first node (the head) from the linked list, update the head attribute and the length attribute accordingly, and return the removed node.


# Keep in mind the following requirements:
# 1.) The method should handle the cases where the list is empty and where the list has one or more nodes.

# 2.) The method should save a reference to the current head node before updating the head attribute.

# 3.) The method should update the head attribute to the second node in the list.

# 4.) The method should disconnect the removed node from the list by setting its next attribute to None.

# 5.) The method should update the length attribute of the LinkedList to reflect the removal of the node.

# 6.) If the list becomes empty after removing the node, the method should set the tail attribute of the LinkedList to None.

# 7.) The method should return the removed node, or None if the list is empty.


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

    def remove_from_head(self):                # <----- here (remember to return THE node... not the node's value)
        if self.length == 0:
            return None

        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node

        popped_node = self.head                # <----- the node we want to return is the head, so store its value before reassigning the new head
        self.head = self.head.next             # <----- reassign head to be head.next
        self.length -= 1
        return popped_node




my_linked_list = LinkedList(2)
my_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_linked_list.remove_from_head().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.remove_from_head().value)
# (0) Items - Returns None
print(my_linked_list.remove_from_head())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""

# Your task is to implement the pop method for the LinkedList class.
# The pop method should remove the last node (tail) from the linked list and return the removed node. If the list is empty, the method should return None.
# After the last node is removed, the second-to-last node should become the new tail of the list.
# Additionally, if the list becomes empty after the pop operation, both the head and tail attributes should be set to None.


# Keep in mind the following requirements:
# 1.) The method should handle the cases where the list is empty, has only one node, or has multiple nodes.

# 2.) The method should update the tail attribute of the LinkedList correctly.

# 3.) The method should update the length attribute of the LinkedList to reflect the removal of the node.

# 4.) The method should either return the removed node or None if the list is empty.

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
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print(" -> ".join(values))

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

    def pop(self):                                                   # <-------- here (keep in mind need to return THE node... not the node's value)
        # if self.length == 0:
        if self.head is None or self.tail is None:                                                     # <-------- if the linked list is empty
            return None

        if self.length == 1:                                                                           # <-------- if the linked list has exactly 1 node
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node

        temp_head = self.head                             # <-------- if the linked list has 2 or more nodes    <--- ** use temp_head to AVOID REASSIGNING THE REAL HEAD **
        while(temp_head is not None):                                                                             # (if you do decide to use the REAL head, need its val stored in a variable before looping, then reassign it back before you return popped node)
            if temp_head.next.next == None:
                popped_node = temp_head.next
                self.tail = temp_head
                self.length -= 1
                return popped_node
            else:
                temp_head = temp_head.next


#             temp_head       temp_head.next     temp_head.next.next
# 1        -      2        -        3        -       None




##########################################################
##   Test code below will print output to "User logs"   ##
##########################################################

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Pop on linked list with one node -----\n")
linked_list = LinkedList(1)
linked_list.print_list()
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on linked list with multiple nodes -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
popped_node = linked_list.pop()
check(3, popped_node.value, "Value of popped node:")
check(1, linked_list.head.value, "Head of linked list:")
check(2, linked_list.tail.value, "Tail of linked list:")
check(2, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on empty linked list -----\n")
linked_list = LinkedList(1)
linked_list.head = None
linked_list.tail = None
linked_list.length = 0
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop all -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.print_list()
popped_node = linked_list.pop()
check(2, popped_node.value, "Value of popped node (first pop):")
check(1, linked_list.head.value, "Head of linked list (after first pop):")
check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
check(1, linked_list.length, "Length of linked list (after first pop):")
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node (second pop):")
check(None, linked_list.head, "Head of linked list (after second pop):")
check(None, linked_list.tail, "Tail of linked list (after second pop):")
check(0, linked_list.length, "Length of linked list (after second pop):")
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list (third pop):")
check(None, linked_list.head, "Head of linked list (after third pop):")
check(None, linked_list.tail, "Tail of linked list (after third pop):")
check(0, linked_list.length, "Length of linked list (after third pop):")

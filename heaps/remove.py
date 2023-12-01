# Here's what your remove method should do in detail:

# If the heap is empty, the remove method should return None.
# If the heap has only one element, the remove method should remove and return this element.

# If the heap has more than one element, the remove method should remove the root of the heap, place the last element in the heap at the root, and then call
# the _sink_down method to reorganize the heap, maintaining the max heap property.


# Here's what your _sink_down method needs to do in detail:

# The method takes an index as a parameter. This index is the position of the node in the heap that needs to be 'sunk down' to its appropriate position to maintain the max heap property.
# In each iteration of its main loop, the method identifies the maximum of the node at the provided index, its left child, and its right child. The indexes of the left and right children can be determined using the _left_child and _right_child methods, respectively.
# If the maximum value is found to be at the provided index, the method ends. Otherwise, the node at the provided index is swapped with the node with the maximum value. The _swap method can be used for this.
# The index of the node with the maximum value is then set as the provided index for the next iteration of the loop.
# The _sink_down method should aim for an efficient time complexity of O(log n), where n is the number of elements in the heap.


class MaxHeap:   # the code for a MinHeap is very similar, a lot of it is just changing signs around and switching a few variable names
    def __init__(self):
        self.heap = []

    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self, index):
        return 2 * index + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def swap_positions(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self.parent_index(current)]:
            self.swap_positions(current, self.parent_index(current))
            current = self.parent_index(current)

    def _sink_down(self, index):
        max_index = index  # track max_index to determine if we need to swap or not
        while(True):
            left_child_idx = self.left_child_index(index) # grab the left child index from the node/index we are currently looking at
            right_child_idx = self.right_child_index(index) # grab the right child index from the node/index we are currently looking at

            if left_child_idx < len(self.heap) and self.heap[left_child_idx] > self.heap[max_index]: # if the left child is in the heap, and the value at the left child is GREATER than than the node at max_index, reassign max_index to be the left child index (we will swap these two nodes and continue the loop)
                max_index = left_child_idx

            if right_child_idx < len(self.heap) and self.heap[right_child_idx] > self.heap[max_index]: # if the right child is in the heap, and the value at the right child is GREATER than the node at max_index, reassign max_index to be the right child index (we will swap these two nodes and continue the loop)
                max_index = right_child_idx

            if max_index != index:  # if the left child or right child was bigger, swap the two nodes and continue down the tree until we find where to place our node
                self.swap_positions(max_index, index)
                index = max_index
            else:
                return  # this indicates that the node at the index we were observing was correctly placed in the heap, and we can now return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:  # if only one element, pop and return its value
            return self.heap.pop()

        popped_val = self.heap[0]  # when removing from the heap, you ONLY REMOVE FROM THE TOP... here we are referencing the popped_val so we can return it later
        self.heap[0] = self.heap.pop()  # overwrite the top value with the last value in the heap (and also remove the last value since its now at index 0). This must be done to MAINTAIN HEAP STRUCTURE!
        self._sink_down(0) # use the helper method to determine where to properly place the overwritten top node
        return popped_val



myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""

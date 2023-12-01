# You are provided with a partial implementation of a MaxHeap class.
# The class includes a method for initialization, plus helper methods for getting the left child, the right child, and the parent of a node and swapping elements in the heap.

# Your task is to complete this class by implementing the insert method.

# This method should take an integer as input and add it to the heap. The insertion of a new element should preserve the Max Heap property, i.e.,
# for every node i other than the root,
# the value of node i is less than or equal to the value of its parent, with the maximum value at the root of the heap.
# Your insert method should be efficient, ideally achieving a time complexity of O(log n), where n is the number of elements in the heap. After inserting the new element at
# the end of the heap, you should appropriately restructure the heap to maintain the Max Heap property. This typically involves 'bubbling up'
# the inserted element to its correct position in the heap.
# Remember to handle edge cases, for example when the heap is empty or contains only one or two elements.


class MaxHeap:
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
        self.heap.append(value)    # insert the value into the heap
        current_index = len(self.heap) - 1   # start at the node/index you just inserted

        while(current_index > 0 and self.heap[current_index] > self.heap[self.parent_index(current_index)]): # while we havent reached the top of the heap AND heap[current] is greater than heap[parent]
            self.swap_positions(current_index, self.parent_index(current_index)) # swap the positions of heap[current] with heap[parent]
            current_index = self.parent_index(current_index) # assign current_index to be the parent index for the next iteration


            # 99
           # /  \
         # 72    61
        # /  \
       # 58  100  <--- insert the 100 to the heap (current node/index on first iteration)
    #    https://i.gyazo.com/917acc94c3a1471b46f2e285d552e759.png


myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)


myheap.insert(100)

print(myheap.heap)


myheap.insert(75)

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""

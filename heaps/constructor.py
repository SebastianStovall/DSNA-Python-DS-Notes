class MaxHeap:      # max heap = biggest value in root, smallest values in bottom, each node's children are less than the parent node
    def __init__(self):
        self.heap = []   # THE HEAP IS JUST AN ARRAY, but we REPRESENT it as a BINARY TREE, so I refer to elements as node's

    def left_child_index(self, index):   # equation to get the left child from the node we are currently looking at
        return 2 * index + 1

    def right_child_index(self, index):  # equation to get the right child from the node we are currently looking at
        return 2 * index + 2

    def parent_index(self, index):       # equation to get the parent node of the node we are currently looking at
        return (index - 1) // 2        #  // <-- is the same as Math.floor()

    def swap_positions(self, index1, index2):      # swaps positions of two nodes in our heap
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

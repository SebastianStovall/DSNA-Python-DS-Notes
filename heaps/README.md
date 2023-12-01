# Notes On Heaps
### 1. There are MinHeaps and MaxHeaps
* In a min heap, the smallest value is at the root, and the children of any given node are always bigger than the parent
* In a max heap, the biggest value is at the root, and the children of any given node are always smaller than the parent

<br/>

###  2. When inserting a value into a heap, you must always append/push the value since nodes are always attached left to right
* From there, we assign current to be the last node in the heap (current = len(heap) - 1), then move up the tree by checking parent values to determine where to place

<br />

### 3. When removing a value from a heap, we reassign the last value in the heap to be the root value (heap[0])... This is done to maintain heap structure
* From there, we deploy a helper function called sink_down() which moves down the tree by checking child values of the current node, and determining if swaps need to be made

<br/> <br/>

## When To Use A Heap / How To Identify When To Implement A Heap

* Keep an eye out for keywords like "smallest," "largest," "priority," or "top K" in the problem statement, as they often indicate a potential application for heaps.
* When solving problems that require selecting or removing elements with the highest or lowest priority.
* When the problem involves finding the k smallest/largest elements.
* When you are working with problems related to graphs and need to perform operations like Dijkstra's algorithm or Prim's algorithm.

* Let's consider a real-life scenario of managing tasks with varying priorities. We can model this as a TaskHeap class, where each task has a priority, and the heap structure helps efficiently manage the tasks based on their priority.
-----> https://i.gyazo.com/9ac4e04e4860d9f2102000c99adbf7f4.png

<br/> <br/> <br/>

# Heaps Big-O Analysis

* INSERT ---> O(log n)
* DELETION ---> O(log n)

<br/>

##### A binary search tree can't do what I heap can do in terms of time complexity for removal and insertion because worst-case-scenario, a BST can be very unbalanced -- O(n)
##### The only way a heap can work and be implemented is if it is balanced (nodes are always inserted left to right) -- O(log n)

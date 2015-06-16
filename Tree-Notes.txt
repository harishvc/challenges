#HEAP
* A heap is a tree with some special properties
* Basic requirements of a heap is that the value of the node must the >= or <= its children - <i>heap property</i>
  * min heap - value of node is <strong>less than or equal to</strong> value of children. Root of the heap has maximum value
  * max heap - value of node is <strong>greater than or equal to</strong> value of children.  Root of the heap has maximum value
* Leaves should be at h or h-1 level where h is the height of the tree (h > 0) - <b>complete binary tree</b>
* Maximun number of elements = 2^h+1 -1 . h is the height of the binary tree.
* Minimum number of nodes = 2^h . h is the height of the binary tree.

##BINARY HEAPS
* Each node can have up to two nodes
* <b>Parent of a node</b>: For a node at ith position, its parent is at  i-1//2 location
* <b>Child of a node</b>: For a node at ith position its childresn are at 2*i + 1 and 2*i + 2 locations

##Operations
* Heapify - After inserting an element in a heap, the heap may not satisfy the heap property. We'll have to change the location of
nodes to satisfy heap properties. This process is called heapify. Also referred to percolate down since we are moving from top to bottom.
* Deleting an element uses percolate down
* Inserting an element uses percolate up

##Complexity
* Time complexity for delete and insert is O(log n), for n elements the complexity is O(nlogn)
* If we start with the entire list theheap can be build in O(n)

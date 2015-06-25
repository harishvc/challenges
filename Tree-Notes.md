#HEAP
* A heap is a tree with some special properties
* Basic requirements of a heap is that the value of the node must the >= or <= its children - <i>heap property</i>
  * min heap - value of node is <strong>less than or equal to</strong> value of children. Root of the heap has maximum value
  * max heap - value of node is <strong>greater than or equal to</strong> value of children.  Root of the heap has maximum value
* Leaves should be at h or h-1 level where h is the height of the tree (h > 0) - <b>complete binary tree</b>
* Maximum number of elements = 2^h+1 -1 . h is the height of the binary tree.
* Minimum number of nodes = 2^h . h is the height of the binary tree.
* Binary Heap
  * Each node can have up to two nodes
  * <b>Parent of a node</b>: For a node at ith position, parent is at  i-1/2 location (math.floor)
  * <b>Child of a node</b>: For a node at ith position childrens are at 2*i + 1 and 2*i + 2 locations
* <b>Heapify</b>: After inserting an element in a heap, the heap may not satisfy the heap property. Location of nodes has to be changed to satisfy heap properties. 
    * Delete an element: Copy root node (max value if max heap) to temp variable, copy last node to root, pop ,reduce heap size and percolate down by checking with child node value
    * Insert an element: Insert new node at end, increase heap size and percolate up by checking with parent node value
* Complexity
  * Time complexity for delete and insert is O(log n), for n elements the complexity is O(nlogn)
  * Complexity to build a heap from array O(n) - If we start with the entire list the heap can be build in O(n)
* Heap Sort 
  * Two steps: Build heap & heapify
  * complexity: Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n))
* Online Reference
  * [Heap Sort In Python](http://www.geekviewpoint.com/python/sorting/heapsort)

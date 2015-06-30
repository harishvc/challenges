#HEAP
* Special properties of a heap are
  * Each node can have up to two child nodes
  * Value of the parent node must the >= or <= of child nodes
    * min heap - value of parent node is <strong>less than or equal to</strong> value of children. Root of the heap has maximum value
    * max heap - value of parent node is <strong>greater than or equal to</strong> value of children.  Root of the heap has maximum value
  * At level k (height, k > 0), there are a total of 2^k-1 nodes  
    * A leaf node at depth k (k > 0) can exist only if all nodes at depth k-1 exist 
    * Nodes at a partially filled level must be added from left to right
  * <strong>Binary Heap is a complete Binary tree where all levels except the lowest are completely full. </strong>
    * Maximum number of elements = 2^h+1 -1 . h is the height of the binary tree.
    * Minimum number of nodes = 2^h . h is the height of the binary tree.
* Heap Operations  
  * Parent of a node: For a node at ith position, parent is at  i-1//2 location  
  * Child of a node: For a node at ith position childrens are at 2*i + 1 and 2*i + 2 locations  
  * Delete: Only removing root node is permitted    
     * Copy root node (max value if max heap) to temp variable    
     * Copy last node to root  
     * Reduce heap size  
     * Pop (remove last element)  
     * Percolate down by comparing values  
  * Insert:   
     * Insert new node at end  
     * Increase heap size  
     * Percolate up by comparing values  
* <b>Heapify</b>: After inserting an element in a heap, the heap may not satisfy the heap property. 
  Location of nodes has to be changed to satisfy heap properties. Given a input (example:list) a heap can be built in linear time. 
* Complexity
  * Time complexity for delete and insert is O(log n), for n elements the complexity is O(nlogn)
  * Complexity to build a heap from array O(n) - If we start with the entire list the heap can be build in O(n)
* Heap Sort 
  * Two steps: Build heap & heapify
  * complexity: Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n))
* Online Reference
  * [Heap Sort In Python](http://www.geekviewpoint.com/python/sorting/heapsort)
  * [Heap Sort on Bogotobogo](http://www.bogotobogo.com/Algorithms/heapsort.php)
  * [Heaps &amp; Binary Search Tree @Univ of Washington](http://courses.cs.washington.edu/courses/cse373/02au/lectures/lecture11l.pdf)
  * [Heaps Tutorial @Univ of Toronto](http://www.cs.toronto.edu/~krueger/cscB63h/w07/lectures/tut02.txt)

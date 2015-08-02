
#TREES
* In computer science, a tree is a widely used abstract data type (ADT).
  A tree is a hierarchy (non-linear) data structure made up of nodes and edges where all nodes are connected without having any cycle
* Terminology  
    * <bold>Depth</bold> of a node is the length of the path from the <bold>root</bold> to the node
    * <bold>Height</bold> of a node is the length of the path from the node to the <bold>deepest</bold> node
    * <bold>Leaf</bold> is a node with no children.  
##BINARY TREES
* A tree is a binary tree if <bold>each node has zero,one or two child nodes</bold>
* #Nodes at level h is 2^h
* #Total nodes is 2^h+1 - 1
* <bold>Strict Binary Tree:</bold> Each node has <bold>exactly</bold>  <bold>2 child nodes</bold> or <bold>0</bold> child nodes 
* <bold>Full Binary Tree:</bold> Each node has <bold>exactly</bold> two child nodes
* <bold>Complete Binary Tree:<bold> All child nodes are height h or h-1      
* Depth First Traversal (DFT):  
	* Pre-order-Traversal: current node data ->left subtree -> right subtree
	* In-order-Traversal: <bold>Ascending order</bold> left subtree > current node data > right subtree
	* Post-order-Traversal:  left subtree > right subtree > current node data
* Breadth First Traversal (BFT): Visit nodes at each level starting with root.  
###BINARY SEARCH TREE (BST)
* left sub-tree elements are less than root
* right sub-tree elements are greater than root
* each node should satisfy this property
* <quote>The definition of BST is that it is a ordered set, thus duplicates are not allowed to be inserted. 
  This is usually due to more complex structures being built atop the BST. Depending on the desired behavior, 
  you may want to throw an exception, error or silently ignore when duplicates are inserted. However, depending 
  on your comparison function you can store duplicates on the left or right subtree, but remember to keep your 
  traversals and insertion sides consistent.</quote>
* Compare BST vs Dictionary
    * BST finds elements closest to (not necessarily equal to) some arbitrary key value
    * BST iterates through the contents in sorted order (in-order traversal)
    * BST are memory-efficient, reserve more memory than they need to.
    * BST allows you to do range searches efficiently. 
    * Dictionary provides constant lookup time  
##HEAP
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

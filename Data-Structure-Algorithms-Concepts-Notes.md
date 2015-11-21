# Data structures, algorithms and concepts

# Built-in Data Types (Primitive)
 * Lists
 * Sets
 * Tuples
 * Dictionary
 * Selecting the right data type    
   * Dictionary when you have a set of unique keys that map to values  
   * List if you have an ordered collection of items  
   * Set to store an unordered set of items and ignore deplicates  
 
# User Built-in Data Types (Abstract Data Types) 
  * Linked List
  * Stack
  * Queue
  * Tree
  * Graph
  
# LINKED LIST & LISTS
* Linked List advantages :notes:
  * Linked List is Dynamic data Structure, can grow and shrink during run time.
  * Insertion and deletion operations are from the beginning of the list in <strong>constant time</strong>
  * Efficient Memory Utilization - no need to pre-allocate memory
  * Faster access time and can be expanded in constant time without memory overhead
  * Linear data structures such as Stack,Queue can be easily implemeted using Linked list
* Linked List drawbacks :notes:
  * Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists.
  * Extra memory space for a pointer is required with each element of the list.
  * Reverse traversing is difficult
  * Memory is allocated to Linked List at run time if and only if there is space available in heap  
* Lists stores elements in successive order in memory.
  * Constant time for accessing an element at a specific index and adding new element at end

# STACK 
* Stack uses LIFO (Last in First Out) ordering
* Implementation can be using linked list or arrays. 
* Constant time to add and remove elements since no internal shifting around
* Does not offer constant time to access elements at position i unlike list/array
* Operations in constant time: push(), pop(), peek(), isEmpty(), size()  

# QUEUE 
* Queue uses FIFO (First in First Out) ordering
* Implementation can be using linked list or arrays. Linked Lists are preferred since access time can be kept constant. 
   All array elements need to get shifted after removing the first element.
* Constant time to add and remove elements since no internal shifting around
* Does not offer constant time to access elements at position i unlike list/array
* Operations in constant time: add(), remove(), peek(), isEmpty(), size()  

# TREES
* In computer science, a tree is a widely used abstract data type (ADT).
  A tree is a hierarchy (non-linear) data structure made up of nodes and edges where all nodes are connected without having any cycle
* A tree is a <strong>connected graph without the cycles</strong> - acyclic connected graph
* Terminology  
    * <strong>Depth</strong> of a node is the length of the path (#nodes) from the <strong>root</strong> to the node
       * Root node has a depth of zero
    * <strong>Height</strong> of a node is the length of the path (#nodes) from the node to the <strong>deepest</strong> node
       * Leaf nodes have height one
       * Height of a tree is height of the root  
    * <strong>Size</strong> of binary tree is size of left subtree + 1 + size of right subtree
    * <strong>Diameter/width</strong>The diameter of a tree (sometimes called the width) is the number of nodes on the 
      <strong>longest path</strong> between two leaves in the tree 
    * <strong>Leaf</strong> is a node with no children.

## TRIES (Prefix trees)
* Variation of n-ary tree in which characters are stored in each node. Each <strong>path down the tree</strong> may represent a word.
* A trie can check if a string is a valid prefix in O(K) time where K is the length of the string

## BINARY TREES
* A tree is a binary tree if <strong>each node has zero,one or two child nodes</strong>
* #Nodes at level h is 2^h
* #Total nodes is 2^h+1 - 1
* Definitions (there a subjective elements, ask for clarification)   
    * <strong>Fully balanced binary tree</strong> is defined as a tree such that the <strong>height</strong> of the two subtrees of 
     any node <strong>never differ by more than one</strong>.
    * <strong>Structurally symmetric binary tree</strong> is defined as a tree where if you draw a vertical line passing through 
     the root node then the left half should be the mirror image of the right half.
    * <strong>Structurally identical binary tree</strong> is defined as a tree where left and right sub-nodes have exactly the same number 
     of nodes, arranged in the exactly same way. It is <bold>not necessary that the value of each node should also be the same</bold>.
    * <strong>Complete Binary Tree:</strong> Each level is fully filled except perhaps for the last level.
      Last level is filled left to right. All child nodes are height h or h-1. Example <strong>Heap</strong>.       
    * <strong>Full Binary Tree:</strong> Each node has <strong>exactly 2 child nodes</strong> or <strong>0</strong> child nodes 
    * <strong>Perfect Binary Tree:</strong> <strong>Full and complete</strong>. Rare in real life and interviews.
* Depth First Traversal (DFT):  
	* Pre-order-Traversal: current node data ->left subtree -> right subtree
	* In-order-Traversal: <strong>Ascending order</strong> left subtree > current node data > right subtree
	* Post-order-Traversal:  left subtree > right subtree > current node data
* Breadth First Traversal (BFT): Visit nodes at each level starting with root.  

### BINARY SEARCH TREE (BST)
* BST is also known as an ordered binary tree. Here left sub-tree elements are less than root and right sub-tree 
  elements are greater than root. This property is satisfied at each node.
* The definition of BST can <strong>vary with respect to equality</strong>. Duplicates are not allowed by some definition. 
  In others, duplicate values will be on right or can be on eith side, <strong>clarify with your interviewer.</strong> 


### RED AND BLACK TREES
* Red and Black trees vs Dictionary :notes:
  * Simple memory management - simplifies error handling in concurrent code, less I/O hits, 
  * Consistent performance because rehashing (expanding the hash table's array) happens on some insertions.
    This is important in real-time systems where you want to provide bounds on how long each operation takes
  * Keys are sorted
  * Reference: http://www.quora.com/Why-would-anyone-like-to-use-a-red-black-tree-when-a-hash-table-can-do-the-job-perfectly 

## HEAP
* Heap is a <strong>complete binary search tree</strong>
* Special properties of a heap are
  * Each node can have up to two child nodes
  * Value of the parent node must the >= or <= of child nodes
    * min heap - value of parent node is <strong>less than or equal to</strong> value of children. Root of the heap has minimum value
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
     * <strong>Percolate down</strong> by comparing values  
  * Insert:   
     * Insert new node at end  
     * Increase heap size  
     * <strong>Percolate up</strong> by comparing values  
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

## Compare data structures
### BST vs Dictionary  :notes:
 * BST finds elements closest to (not necessarily equal to) some arbitrary key value
 * BST iterates through the contents in sorted order (in-order traversal)
 * BST are memory-efficient, reserve more memory than they need to
 * BST allows you to do range searches efficiently 
 * Dictionary provides constant lookup time   
 
### BST vs Heap :notes:  
  * Heap provides constant time lookup for min and max value
  * BST provides O(logn) time complexity for search,insert,delete & access
  * BST finds elements closest to (not necessarily equal to) some arbitrary key value
  * BST allows you to do range searches efficiently 

### Red & Black Trees vs Dictionaries  
   * Simple memory management - simplifies error handling in concurrent code, less I/O hits,    
   * Consistent performance because rehashing (expanding the hash table's array) happens on some insertions.  
     This is important in real-time systems where you want to provide bounds on how long each operation takes  
   * Keys are sorted  

# TIME COMPLEXITY
* Dictionary: O(1) for insert, delete and lookup 
* Linked List: O(1) insert/delete and O(n) lookup
* List: O(1) insert, O(n) delete, and O(n) lookup
* BST: O(logN) insert/delete/lookup/max/min
* Binary Heap: O(1) max/min, O(logN) insert/delete, O(n) lookup
* Reference
  * [Know Thy Complexities!](http://bigocheatsheet.com/)

# Graphs
* <strong>Connected Graph</strong> There is a path between every pair of vertex (nodes)
* <strong>Path</strong> in a graph is a finite or infinite sequence of edges which connect a sequence of vertices. 
  No <strong>vertices</strong> are repeated in a simple path.
* A cycle is a <strong>closed path</strong>. That is, we start and end at the same vertex and do not travel to any vertex twice  
* <strong>Acyclic graph</strong> is one without cycles (example: tree)
* <strong>Topological sort</strong> is ordering of the vertex in a directed acyclic graph (DAG), such that if there is a edge from vertex u to vertex v, 
   then v appears after u in the ordering
* Trail refer to a path where <strong>no edge</strong> is repeated
* Circuits refer to the <strong>closed trail</strong>, meaning we start and end at the same vertex



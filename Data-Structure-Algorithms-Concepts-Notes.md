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
  

# Sort Algorithms

| Algorithm | Best Time Complexity | Average Time Complexity| Worst Time Complexity | Space Complexity | Stable | Recursive/Iterative | Notes
| --- | --- | --- | --- | --- | --- | --- | --- |
|Insertion Sort| O(n)  | O(n^2) | O(n^2) | O(1) | Stable | Iterative | Ideal if n is small. Values sorted left -> right
|Bubble Sort|    O(n)  | O(n^2) | O(n^2) | O(1) | Stable | Iterative | Ideal if n is small. Values sorted right <- left
|Quick Sort | O(nlogn) | O(nlogn) | O(n^2) | O(1) | NOT stable | Recursive | Default sort
|Merge Sort | O(nlogn) | O(nlogn) | O(nlogn)| O(n) | Stable | Recursive | Ideal for parallel processing
|Heap Sort |  O(nlogn) | O(nlogn) | O(nlogn)| O(1) | NOT stable | Iterative | Ideal for max, min values


* Bubble Sort
   * Simple sort
   * STABLE (retains order of same values)
   * Ideal if list is **mostly sorted**  
   * Time Complexity: Best: O(n) , Average: O(n^2), Worst Case: O(n^2)  
   * Space Complexity: O(1)     
* Insertion Sort
   * Insertion sort is simple (no recursion)
   * **STABLE** (retains order of same values)
   * For small lists, insertion is generally faster than a comparably implemented quicksort or mergesort
   * In-place sorting
   * Ideal for input MOSTLY sorted!
   * Time Complexity: Best: O(n), Average: O(n^2), Worst Case: O(n^2)   
* Merge Sort
   * Divide and conquer
   * **STABLE** (retains order of same values)
   * EXTRA space is needed to hold two halves
   * Ideal for processing across multiple processors in parallel
   * Space Complexity: O(n)
   * Time Complexity: Best: O(nlogn), Average: O(nlogn), Worst Case: O(nlogn)      
* Quick Sort:
   * Divide and conquer
   * Inplace algorithm using a **pivot** (pivot value is the MEDIAN :boom:)
   * NO need for extra memory
   * NOT stable
   * **Need to know length of list**
   * Time Complexity: Average: O(nlogn), Worst Case: O(n^2)
* Heap Sort
   * Build a max or min heap
   * **Need NOT know length of list**  Ideal for input streams
   * NOT stable
   * You can **only delete the root node** 
     * swap last value in heap with the root node
     * reduce heap size and **percolate down (Heap Sort)**  
   * You can **only insert** at the end
     * **percolate up** values to retain heap properties  
   * Time Complexity: Best: O(nlogn), Average: O(nlogn), Worst Case: O(nlogn), logn is the height of the heap
* Counting Sort
   * NOT comparision based
   * Simple buckets, simple processing, memory overhead
   * Sorting integers. Buckets for each value (memory overhead), works well for sorting input with several repeated values in small range
* Radix Sort
   * NOT comparision based
   * Simple buckets, sophisticated processing (least significat bit to most significant bit), speed overhead 
     and still need additional static memory
   * Works well for a small input with small length 
* Bucket Sort
   * NOT comparision based
   * Sophisticated buckets, simple processing, requires dynamic memory, good in average



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
* Double Linked List
  * Traverse in both directions - start to end and as well as from end to start
    *  If we are at a node, then we can go to any node  
  * Requires more space per node because one extra field is required to keep track of previous node   
  * Insertion and deletion take more time than linear linked list   

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
    * <strong>Depth (AKA Level, Top Down)</strong> of a node is the length of the path (#nodes) from the <strong>root</strong> to the node  
       * **Root node has a depth of ONE** :boom:
       * Height of a tree is also referred as **maximum depth** :bulb:    
    * <strong>Height (AKA Max Depth, Bottom Up)</strong> of a node is #nodes on the **longest path** (#nodes) from the node to the **farthest leaf node**     
       * <strong>Leaf nodes have height ONE</strong> :boom:
       * Height of a tree is at the root 
       * Height of a tree == height at the root
       * Height of a tree is also referred as **maximum depth**  
    * <strong>Diameter (AKA Width)</strong>The diameter of a tree (sometimes called the width) is 
      <bold>max</bold>(diameter of left sub-tree,diameter of right sub-tree,longest path between two leaves going through the root). Diameter of a tree <strong>may not</strong> be throught the root.
    * <strong>Size</strong> of binary tree is size of left subtree + 1 + size of right subtree
    * <strong>Leaf</strong> is a node with no children.

## TRIES (Prefix trees)
* Variation of n-ary tree in which characters are stored in each node. Each <strong>path down the tree</strong> may represent a word.
* A trie can check if a string is a valid prefix in O(K) time where K is the length of the string

## BINARY TREES
* A tree is a binary tree if <strong>each node has zero,one or two child nodes</strong>
* #Nodes at level h is 2^(h-1)
  * height = 1, nodes at this height = 1
  * height = 2, nodes at this height = 2
  * height = 3, nodes at this height = 4 
* #Total nodes is (2^h) - 1
  * Node in a Binary Tree with height =1  is 1
  * Node in a Binary Tree with height =2  is 3
  * Node in a Binary Tree with height =3  is 7
  * Node in a Binary Tree with height =4  is 15
* Definitions (there a subjective elements, ask for clarification)   
    * <strong>Balanced Binary Tree</strong>
      * <strong>height</strong> of the two subtrees of any node <strong>never differ by more than one</strong>
    * <strong>Complete Binary Tree (example: Heap):</strong> 
      * Each level is fully filled except perhaps for the last level  
      * Last level is filled left to right  
      * All child nodes are height h or h-1          
    * <strong>Full Binary Tree (AKA: Proper Binary Tree, 2-tree or Strict Binary Tree):</strong> 
      * Each node has <strong>exactly 2 child nodes</strong> except leaf nodes.       
    * <strong>Perfect Binary Tree:</strong> 
      * <strong>Full and complete</strong>. Rare in real life and interviews.
    * <strong>Structurally symmetric binary tree</strong> is defined as a tree where if you draw a vertical line passing through 
     the root node then the left half should be the mirror image of the right half. <strong>Check for data and structure</strong>
    * <strong>Structurally identical binary tree</strong> is defined as a tree where left and right sub-nodes have exactly the same number 
     of nodes, arranged in the exactly same way. It is <bold>not necessary that the value of each node should also be the same</bold>.
* Depth First Traversal (DFT):  
	* Preorder   Traversal:  
      * current node data ->left subtree -> right subtree   
      * first node is the root and last node is the right most
      * **going down** from the parent node to child node(s)  
      * Examples: clone a tree, flip the nodes in a tree, LCA, build a tree, path from root, depth , height 
	* In-order   Traversal:  
      * left subtree -> current node data -> right subtree   
      * first node is the left most and last node is the right most. In a BST the values are **sorted**  
      * **looking upwards** starting from the leaf node(s) to parent nodes    
      * Examples: sorted values (only in BST), smallest value (only in BST)
	* Post-order Traversal:  
      * left subtree -> right subtree -> current node data   
      * first node is the left most and last node is the root
      * **looking upwards** starting from the leaf nodes to sub-tree to the parent subtree all the way to root 
      * Examples: check is tree is unival, largest value (only in BST) 
* Breadth First Traversal (BFT): 
    * Visit nodes at **each level** starting with root. Nodes are stored in a **queue** during traversal    

### BINARY SEARCH TREE (BST)
* BST is also known as an ordered binary tree. Here left sub-tree elements are less than root and right sub-tree 
  elements are greater than root. This property is satisfied at each node.
* The definition of BST can <strong>vary with respect to equality</strong>. Duplicates are not allowed by some definition. 
  In others, duplicate values will be on right or can be on eith side, <strong>clarify with your interviewer.</strong> 
* When a BST is created the first value becomes the root of the BST and next values go either on the right (>root) or left(<root). 
  So **picking the root values in BST plays a critical role in determining the height of the tree**.     
* BST offers O(log n) for best cases and O(n) for worst case (height of the tree == #nodes)  
* To **guarantee O(log n) complexity a BST should be fully balanced**  
* A **fully balanced binary tree** is defined as a tree such that the height of the two subtrees of any node **never differ by more than one**  


### RED AND BLACK TREES
* Red and Black trees vs Dictionary :notes:
  * Simple memory management - simplifies error handling in concurrent code, less I/O hits, 
  * Consistent performance because rehashing (expanding the hash table's array) happens on some insertions.
    This is important in real-time systems where you want to provide bounds on how long each operation takes
  * Keys are sorted
  * Reference: http://www.quora.com/Why-would-anyone-like-to-use-a-red-black-tree-when-a-hash-table-can-do-the-job-perfectly 

## HEAP
* Heap is a <strong>Complete Binary Tree</strong>
  * Each level is fully filled except perhaps for the last level
* Special properties of a heap are
  * Each node can have up to two child nodes
  * Value of the parent node must the >= or <= of child nodes
    * min heap - value of parent node is <strong>less than or equal to</strong> value of children. Root of the heap has minimum value
    * max heap - value of parent node is <strong>greater than or equal to</strong> value of children.  Root of the heap has maximum value
  * At level k (height, k > 0), there are a total of 2^k-1 nodes  
    * A leaf node at depth k (k > 0) can exist only if all nodes at depth k-1 exist 
    * Nodes at a partially filled level must be added from left to right  - **left complete binary tree since they are stored in an array**  
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


# GRAPH
* **Descendant** Given vertices _v_ and _w_, if _v_ lies on the **unique path** between _w_ and the **root**, then _w_ is a descendant of _v_        
* <strong>Path</strong> in a graph is a finite or infinite sequence of edges which connect a sequence of vertices. 
  No <strong>vertices</strong> are repeated in a simple path.
* <strong>Connected Graph</strong> There is a path between every pair of vertex (nodes)
* Trail refer to a path where <strong>no edge</strong> is repeated    
* Circuits refer to the <strong>closed trail</strong>, meaning we start and end at the same vertex    
* Strongly Connected Components (SSC) of a directed graph are **subsets of nodes** 
such that **each node within a subset can be reached from each other node**.   

## Adjacency List   
  * Hash of list or Hash of Linked List to store vertices and edges  
  * Space: O(n+e)  
  * Lookup if edges exists: O(v), max # of edges any vertex can have is #vertices-1  
  * Ideal for sparse graph   

## Adjacency Matrix    
  * 2 dimensional list to sore vertices and edges  
  * Space: O(n*m)  
  * Lookup if edge exists: O(1)  
  * Ideal where constant lookup time is needed and graph is dense  

## Cycle  
* A cycle is a <strong>closed path</strong>. That is, we can _visit a node for the second time before all its decendents have been visited_ 
* Cycle detection on a graph is different than a tree since **in a graph a node can have  multiple parents**      
* <strong>Acyclic graph</strong> is one without cycles (example: tree)  
* <strong>Topological sort</strong> is ordering of the vertex in a directed acyclic graph (DAG), such that if there is a edge from vertex u to 
  vertex v, then v appears after u in the ordering  


## Traversal  

### DFS   
  * Makes deep incursions into a graph, retreating only when it runs out of new nodes to visit   
  * Can end up taking a long and convoluted route to a vertex that is actually very close by    
  * If vertices are **deeper, time complexity is more**    
  * Applications: Finding Connected components, Topological sort

### BFS  
  * Visit vertices in **increasing order of their distance** from the starting point  
  * BFS **always provides the shortest path** between two connected vertices   
  * BFS is a **broader, shallower search** like the propagation of a wave upon water  
  * Queue is used for BFS implementation (Memory Constraints)  
  * Applications: Finding Shortest Path, Bipertiteness

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

## Fundamentals
* O(1): Constant
* O(log N): Logrithmic
* O(n): Linear
* O(n!): Factorial
* O(n)^2: Quadratic
* O(n)^3: Cubic
* O(2^n): Exponential base 2
* O(n^n): Exponential base n

## Data Structures
* Dictionary: O(1) for insert, delete and lookup 
* Linked List: O(1) insert/delete and O(n) lookup
* List: O(1) insert, O(n) delete, and O(n) lookup
* BST: O(logN) insert/delete/lookup/max/min
* Binary Heap: O(1) max/min, O(logN) insert/delete, O(n) lookup
* Reference
  * [Know Thy Complexities!](http://bigocheatsheet.com/)

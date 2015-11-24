Cracking the coding interview
=============================

Collection of interesting questions and solutions that involve data structures, algorithms and concepts. Solutions are in Python version 3.4.3

## Table of Contents
* [Python Standard Library](#python-standard-library) 
* [Data Structures, Algorithms &amp; Concepts](#data-structures-algorithms--concepts)
* [Brain Teasers (Basic)](#brain-teasers-basic)
* [Brain Teasers (Moderate)](#brain-teasers-moderate)
* [Lists &amp; Dictionaries](#lists--dictionaries)
* [Strings](#strings)
* [Permutations and Combinations](#permutations-and-combinations)
* [Linked Lists](#linked-lists)
* [Stacks](#stacks)
* [Queues](#queues)
* [Binary Trees](#binary-trees)
* [Binary Search Tree (BST)](#binary-search-tree-bst)
* [Heaps](#heaps)
* [GRAPHS](#graphs)
* [Sorting](#sorting)
* [Dynamic Programming](#dynamic-programming)
* [Design &amp; Algorithms](#design--algorithms)
* [Bitwise Operations](#bitwise-operations)
* [Online Resources](#algorithms-and-data-structures-resources)
* [Python Resources](#python-resources)
* [Interview Resources](#interview-resources)
* [Amazing Technical Discussions](#amazing-technical-discussions)

### Python Standard Library
1. [Python standard library reference (part 1/5)](https://github.com/harishvc/challenges/blob/master/python-intro.py)
2. [Dictionary, tuples, list and list comprehension, two dimensional list and file read (part 2/5)](https://github.com/harishvc/challenges/blob/master/python-intro2.py)
3. [Sort >>> lists, lists of lists and list of dictionaries (part 3/5)](https://github.com/harishvc/challenges/blob/master/python-intro3.py)
4. [Lambda >>> intro, sort variations (part 4/5)](https://github.com/harishvc/challenges/blob/master/lambda.py)
5. [Notes: Python 3.x (part 5/5)](https://github.com/harishvc/challenges/blob/master/python-intro4.py)
6. [Python interview questions and answers](http://www.ilian.io/python-interview-question-and-answers/)
 
### Data Structures, Algorithms &amp; Concepts
* [Notes: Data structures, algorithms, time complexity and concepts](https://github.com/harishvc/challenges/blob/master/Data-Structure-Algorithms-Concepts-Notes.md)  :thumbsup: :notes:

### Brain Teasers (Basic)
1. [Convert celsius to fahrenheit](https://github.com/harishvc/challenges/blob/master/celsius-fahrenheit.py)
2. [Find sum of all even numbers for a given range](https://github.com/harishvc/challenges/blob/master/sum-of-numbers.py) 
3. [Find pairs in an integer array whose sum is equal to a given value](https://github.com/harishvc/challenges/blob/master/find-integer-pairs-equal-to-sum.py) 
4. [Find factorial of n](https://github.com/harishvc/challenges/blob/master/factorial.py)
5. [Find square root of a number](https://github.com/harishvc/challenges/blob/master/find-square-root-without-using-sqrt-function.py)
6. [Find square root without using sqrt function](https://github.com/harishvc/challenges/blob/master/find-square-root-without-using-sqrt-function.py)
7. [Find power of a number](https://github.com/harishvc/challenges/blob/master/power.py) 
8. Fibonacci series    
   8.1 [Find the Fibonacci numbers between the given range](https://github.com/harishvc/challenges/blob/master/fibonacci.py)    
   8.2 [Find odd numbers in the Fibonacci series for a given range](https://github.com/harishvc/challenges/blob/master/fibonacci-find-even-odd.py)  

### Brain Teasers (Moderate)
1. Find the first n prime numbers
2. [How many trailing zeros are in n! (n factorial)](https://github.com/harishvc/challenges/blob/master/factorial-trailingzero.py) :memo: 
3. Reverse an integer  
4. Find the Greatest Common Divisior (GCD) of two positive integers
5. Check if two given strings are Isomorphic   
6. [Validate Sudoku](https://github.com/harishvc/challenges/blob/validate-sudoku.py) [TODO]    
7. Flatten a nested hash. Example {a:1, b:2, c:{d:3,e:4}} flattens to {a:1,b:2,c.d:3,c.e:4} :boom: :thumbsup:   
8. [Sort version numbers](https://github.com/harishvc/challenges/blob/master/sort-version-numbers.py) :memo: :boom:   
9. Matrix    
   9.1 Print the matrix from outside to inside (Spiral) :boom:   
   9.2 [Given a two dimentional matrix where rows and columns are sorted in increasing order. Design an efficient algorithm that decides whether a number X appears in A](https://github.com/harishvc/challenges/blob/master/two-dimensional-array-number-exist.py) :thumbsup:     
10. Duplicates  
   10.1 [Given a list of integers return a list of integers that only occurred once](https://github.com/harishvc/challenges/blob/master/find-distinct-elements-in-lists.py) :bulb: :memo:  
   10.2 Given a sorted list, remove the duplicates in place, return modified list and #unique values
11. Given a list and sum  
   11.1 Find all possible 2 numbers in the list that add up to the given sum    
   11.2 [Find all possible triplets in the list that add up to the given sum](https://github.com/harishvc/challenges/blob/master/find-three-numbers-that-add-to-a-given-input.py)     
   11.3 Find all possible quadruplets in the list that add up to the given sum
12. Rotated list   
   12.1 [Rotate a list to the right or left by n places](https://github.com/harishvc/challenges/blob/master/rotate-array.py)    
   12.2 Find minimum in a rotated soted list     
   12.3 [Search a target number in a rotated sorted list](https://github.com/harishvc/challenges/blob/master/binary-search-tree-search-sorted-rotated-list.py) :bulb:     
13. Time intervals  
   13.1 [Merge overlapping time intervals](https://github.com/harishvc/challenges/blob/master/merge-overlapping-intervals.py) :notes:   
   13.2 [Find #conflicting appointments](https://github.com/harishvc/challenges/blob/master/interval-scheduler.py) :memo:  
   13.3 [Find conflicting appointments](https://github.com/harishvc/challenges/blob/master/find-conflicting-appointments.py)  
14. Median  
   14.1 [Find median of a sorted list](https://github.com/harishvc/challenges/blob/master/find-median-sorted-list.py)  
   14.2 [Find median of two sorted list](https://github.com/harishvc/challenges/blob/master/find-median-of-two-sorted-lists.py) :bulb: :thumbsup: :rocket:  
   14.3 Find median of unsorted list  


### Lists & Dictionaries
1. [Randomize list elements](https://github.com/harishvc/challenges/blob/master/randomize-array-elements.py)
2. Find the majority element in linear time :boom:
3. [Given two numbers as list add them and return result as list](https://github.com/harishvc/challenges/blob/master/list-add-two-numbers.py )
4. [Say as you see - given an input string of integers print the output](https://github.com/harishvc/challenges/blob/master/say-as-you-see.py) :memo: 
5. [Find the intersection of two sorted lists](https://github.com/harishvc/challenges/blob/master/find-intersection-of-sorted-lists.py) :memo:
6. [Given two arrays of integers, find a pair of values (one from each array) such that
    you can swap so that both arrays sume to the same value](https://github.com/harishvc/challenges/blob/master/lists-swap-same-sum.py) [TODO]
 
### Strings
1. [Find #words in a sentance](https://github.com/harishvc/challenges/blob/master/string-words.py)
2. [Reverse a string recursively](https://github.com/harishvc/challenges/blob/master/reverse-string-recursiverly.py)
3. [Reverse all words in a sentance](https://github.com/harishvc/challenges/blob/master/reverse-sentance.py)
4. [Test if a string is a Palindrome. Ignore all non-alphanumeric characters](https://github.com/harishvc/challenges/blob/master/palindrome.py)
5. [Find most and least frequently used words in a sentance](https://github.com/harishvc/challenges/blob/master/sort-by-word-frequency.py)
6. [Find first occurance of substring](https://github.com/harishvc/challenges/blob/master/first-occurance-of-substring.py)
7. [Write a function which finds a closest pair of equal entries](https://github.com/harishvc/challenges/blob/master/closest-matching-pair.py) :memo: 
8. [Write a function that given an integer returns a formatted number string](https://github.com/harishvc/challenges/blob/master/format-integer.py) :memo: :bulb: :thumbsup:
9. Given two strings find if they are Anagrams (rearranging the letters of a word or phrase to produce a new word or phrase)
10. Given a long string seperated by space, find how many occurances of another small string 


### Permutations and Combinations
0. [Introduction to Permutation and Combination](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)
1. [Compute all permutations of a string](https://github.com/harishvc/challenges/blob/master/string-permutations.py)
2. [Find all possible combinations for a given string](https://github.com/harishvc/challenges/blob/master/string-combinations.py)
3. [Compute all possible string combinations that can be made my placing spaces (zero or one) between them](https://github.com/harishvc/challenges/blob/master/string-combinations-by-placing-spaces.py)
4. [Given an input string and pattern find the minimum window in the input string that will contain all the characters in the pattern](https://github.com/harishvc/challenges/blob/master/minimum-window-matching-pattern.py)
5. [Given a string containing only digits, restore it by returning all possible valid IP address combinations](https://github.com/harishvc/challenges/blob/master/find-ip-address-variations.py)
6. [Given a phone number provide possible letter mnemonics](https://github.com/harishvc/challenges/blob/master/phone-number-mnemonics.py)

### Linked Lists
1. [Linked Lists Introduction](https://github.com/harishvc/challenges/blob/master/linked-list-introduction.py)
2. [Find the nth node from the end of a linked list](https://github.com/harishvc/challenges/blob/master/find-nth-node-from-the-end-in-a-single-linked-list.py)
3. [Given a linked list detect if it contains a cycle. If so what is the cycle length and start node?](https://github.com/harishvc/challenges/blob/master/detect-cycles-in-linked-list.py)
4. [Reverse a linked list](https://github.com/harishvc/challenges/blob/master/linked-list-reverse.py) :thumbsup: :rocket:
5. [Check if a linked list is a Palindrome](https://github.com/harishvc/challenges/blob/master/check-if-linkedlist-is-a-palindrome.py)
6. [Find the middle element in a linked list](https://github.com/harishvc/challenges/blob/master/linked-list-middle-element.py) :bulb:
7. Find the node at which the intersection of two singly linked lists begins
8. Delete a node in the linked list

### Stacks
1. [Implement stack using list](https://github.com/harishvc/challenges/blob/master/stack-implement.py)
2. [Implement stack using linked list](https://github.com/harishvc/challenges/blob/master/stack-implementation-using-linked-lists.py)
3. [Implement stack using dynamic array](https://github.com/harishvc/challenges/blob/master/stack-implementation-using-dynamic-array.py)
4. [Implement stack using fixed size array](https://github.com/harishvc/challenges/blob/master/stack-implementation-using-fixed-sized-array.py)
5. [Implement stack with getMax() that operates in constant time](https://github.com/harishvc/challenges/blob/master/stack-with-maxvalue.py) :memo:
6. [Check if a string containing parenthesis'()' is balanced](https://github.com/harishvc/challenges/blob/master/stack-check-matching-parenthesis.py) :memo: 
7. [Check if a string containing parenthesis, square brackets and curly brackets is balanced](https://github.com/harishvc/challenges/blob/master/stack-check-matching-parenthesis-square-brackets-and-curly-brackets.py)
8. Implement stack using queue [TODO]
9. [Design an algorithm for computing the k-th largest element in a sequence of elements.
   It should run in O(n) expected time where n is the length of the sequence, which is not known in advnance.
   The value of K is known in advance. Your algorithm should print the k-th largest element after the sequence has ended.
   It should use O(k) additional storage](https://github.com/harishvc/challenges/blob/master/k-largest-element.py ) [TODO]

### Queues
1. [Implement queue using list](https://github.com/harishvc/challenges/blob/master/queue-implement.py)
2. [Implement queue using linked list](https://github.com/harishvc/challenges/blob/master/queue-implementation-using-linked-lists.py)
3. [Implement a queue using two stacks](https://github.com/harishvc/challenges/blob/master/implement-queue-using-two-stacks.py)
4. [Queue implementation using dynamic array](https://github.com/harishvc/challenges/blob/master/queue-implementation-using-dynamic-array.py)
5. [Queue implementation using fixed size array](https://github.com/harishvc/challenges/blob/master/queue-implementation-using-fixed-sized-array.py)
6. [Design an algorithm to sort a stack in descending order] (https://github.com/harishvc/challenges/blob/master/sort-stack-in-descending-order.py)
7. Given a screen with all pixels having one of two colors. When a random pixel is clicked, then that pixel & all the adjacent pixels with 
    same color should change the color to the second color  [TODO]
8. Implement blocking queue [TODO]
9. Implement non-blocking queue [TODO]
     
### Binary Trees
1.  [Traversal](https://github.com/harishvc/challenges/blob/master/binary-tree-introduction.py)  
  1.1 [Pre-order](https://github.com/harishvc/challenges/blob/master/binary-tree-traversal-pre-order.py)    
  1.2. [In-order](https://github.com/harishvc/challenges/blob/master/binary-tree-traversal-in-order.py)    
  1.3. [Post-order](https://github.com/harishvc/challenges/blob/master/binary-tree-traversal-post-order.py)    
  1.4. [Level-order](https://github.com/harishvc/challenges/blob/master/binary-tree-traversal-level-order.py)   
2. Essentials  
  2.1 [Find # of leaves, half nodes and nodes in a binary tree](https://github.com/harishvc/challenges/blob/master/binary-tree-leaves-nodes.py)  
  2.2 [Find the size of a binary tree](https://github.com/harishvc/challenges/blob/master/binary-tree-size.py)  
  2.3 [Find the height of the binary tree](https://github.com/harishvc/challenges/blob/master/binary-tree-height.py)  
  2.4 [Find maximum depth of a binary tree](https://github.com/harishvc/challenges/blob/master/binary-tree-max-depth.py)  
  2.5 [Find the depth (level) of a node and the path from the root](https://github.com/harishvc/challenges/blob/master/binary-tree-node-depth-path.py) :thumbsdown:  
  2.6 [Find the deepest node in binary tree](https://github.com/harishvc/challenges/blob/master/binary-tree-deepest-node.py)  
  2.7 [Find maximum diameter (width) and height of a binary tree](https://github.com/harishvc/challenges/blob/master/binary-tree-max-diameter-height.py) :thumbsup:  
  2.8 [Find all edge nodes (boundary/perimeter) in the binary tree](https://github.com/harishvc/challenges/blob/master/binary-tree-edge-nodes.py) :thumbsup:  
3. Path Sum  
  3.1 [Find the max value of the binary tree](https://github.com/harishvc/challenges/blob/master/binary-tree-max-value.py)  
  3.2 [Find level than has maximum sum](https://github.com/harishvc/challenges/blob/master/binary-tree-find-level-with-max-pathsum.py) :thumbsup:  
  3.3 [Given path sum check if the path exists](https://github.com/harishvc/challenges/blob/master/binary-tree-check-if-path-exists.py) :thumbsup:  
  3.4 Print all paths & path sum from root to leaf in a binary Tree :thumbsup:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3.4.1 [Iterative] (https://github.com/harishvc/challenges/blob/master/binary-tree-root-to-leaf-paths.py)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3.4.2 [Recursive] (https://github.com/harishvc/challenges/blob/master/binary-tree-root-to-leaf-paths-recursive.py)  
  3.5 [Find the sum of all root to leaf paths in a binary tree where a node has a binary digit value and each root to leaf path
       represents a binary number. Sum all such numbers.](https://github.com/harishvc/challenges/blob/master/binary-tree-sum-of-all-root-to-leaf-paths.py) :thumbsup:  :memo: :bulb:  
4. Moderate Difficulty  
  4.1  [Check if a binary tree is symmetric (mirror)](https://github.com/harishvc/challenges/blob/master/binary-tree-check-symmetric.py)  
  4.2  [Are two binary trees structurally identical?](https://github.com/harishvc/challenges/blob/master/binary-tree-structurally-identical.py) :thumbsup:  
  4.3  [Check if a binary tree is fully balanced](https://github.com/harishvc/challenges/blob/master/binary-tree-balanced.py) :thumbsup: :bulb:  
  4.4  [Given two binary trees T1 and T2, check if T2  is a subset of T1](https://github.com/harishvc/challenges/blob/master/binary-tree-subset.py) :bulb: :notes: :thumbsup:  
  4.5  [Find the ancestors of a node in a binary tree](https://github.com/harishvc/challenges/blob/master/binary-tree-ancestor.py) :thumbsup: :notes: :rocket:  
  4.6  Find the Lowest (nearest/first) Common Ancestor (LCA) of two nodes in a binary tree    
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.6.1 [Traverse down - parent node to child node](https://github.com/harishvc/challenges/blob/master/binary-tree-first-common-ancestor-of-two-nodes.py) :thumbsup: :notes: :rocket:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.6.2 [Traverse up - child node to parent node](https://github.com/harishvc/challenges/blob/master/binary-tree-first-common-ancestor-of-two-nodes-traverse-up.py)  
  4.7 Find the shortest path between two nodes in a binary tree :thumbsup: :notes: :rocket:    
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.7.1 [solution 1: Modify LCA](https://github.com/harishvc/challenges/blob/master/binary-tree-shortest-path.py)   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.7.2 [solution 2: Using root to node path](https://github.com/harishvc/challenges/blob/master/binary-tree-shortest-path2.py)  
  4.8 Given a binary tree where path are from parent node to child node, root and leaf can be excluded in the path  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.8.1 [Count # path that add up to a given value](https://github.com/harishvc/challenges/blob/master/binary-tree-count-path-sum.py) :bulb: :thumbsup:  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.8.2 [List all the path that add up to a given value](https://github.com/harishvc/challenges/blob/master/binary-tree-count-path-sum-with-path.py) :thumbsup:  
  4.9 Given a linked list, construct a balanced tree with the same in-order traversal

### Binary Search Tree (BST)  
1.  [Convert list to BST](https://github.com/harishvc/challenges/blob/master/binary-search-tree-create.py)     
2.  [Delete node from BST](https://github.com/harishvc/challenges/blob/master/binary-search-tree-delete-node.py) :thumbsup:     
3.  [Find max value of BST](https://github.com/harishvc/challenges/blob/master/binary-search-tree-max-value.py)     
4.  [Find min value of BST](https://github.com/harishvc/challenges/blob/master/binary-search-tree-min-value.py)     
5.  [Find if an element exists in BST](https://github.com/harishvc/challenges/blob/master/binary-search-tree-find-value.py)      
6.  [Check if valid BST](https://github.com/harishvc/challenges/blob/master/binary-search-tree-check.py) :thumbsup:  
7.  [In a BST find first value greater than K or given node K find the next node](https://github.com/harishvc/challenges/blob/master/binary-search-tree-first-value-greater-than-K.py) :memo:     
8.  [Find smallest K in a BST](https://github.com/harishvc/challenges/blob/master/binary-search-tree-smallestK.py) :thumbsup: :bulb:    
9.  [Given a BST find # nodes that lie in the given range](https://github.com/harishvc/challenges/blob/master/binary-search-tree-range.py) 
10. [Search in sorted list X for index i such that X[i] = i](https://github.com/harishvc/challenges/blob/master/binary-search-tree-find-index-i-equals-value.py) :bulb: :thumbsup:
11. [Given a sorted list create a BST with minimal height] (https://github.com/harishvc/challenges/blob/master/binary-search-tree-minimal-height.py) :thumbsup: :bulb:
12. [Find all possible combinations that can generate identical Binary Search Tree (BST)](https://github.com/harishvc/challenges/blob/master/binary-search-tree-input-variations.py) :bulb: :thumbsup: :memo: :art:
13. Find mean of a BST
14. Find depth of a binary search tree without using recursion

### Heaps  
1. [Heaps Introduction](https://github.com/harishvc/challenges/blob/master/heaps-introduction.py)  
2. [heapq Python library introduction](https://github.com/harishvc/challenges/blob/master/heapq-library.py)  
3. [Convert unsorted list to heap in linear time](https://github.com/harishvc/challenges/blob/master/convert-list-to-heap.py):memo:  
4. [Heap Sort](https://github.com/harishvc/challenges/blob/master/heapsort.py)  
5. [Find Kth maximum in an unsorted list](https://github.com/harishvc/challenges/blob/master/find-k-maximum.py)  
6. [Design an algorithm to compute the k elements closest to the median of an list](https://github.com/harishvc/challenges/blob/master/heap-k-elements-close-to-array-median.py)[TODO]
7. Running mean

### Graphs
1. [Directed Acyclic Graph (DAG) introduction](https://github.com/harishvc/challenges/blob/master/graph-dag-introduction.py) 
2. [Topological sort introduction](https://github.com/harishvc/challenges/blob/master/graph-topological-sort.py)
3. [Topological sort using DFS](https://github.com/harishvc/challenges/blob/master/graph-topological-sort-using-DFS.py) :bulb: :thumbsup: :notes: :rocket:
4. [In a directed graph given two nodes find out whether if a path exists](https://github.com/harishvc/challenges/blob/master/graph-check-if-path-exists.py)
5. [In a directed graph find path between two nodes](https://github.com/harishvc/challenges/blob/master/graph-find-path-between-nodes.py) :notes:

### Sorting
1. [Sort lists,lists of lists and list of dictionaries](https://github.com/harishvc/challenges/blob/master/python-intro3.py)
2. [Merge Sort &amp; Quick Sort](https://github.com/harishvc/challenges/blob/master/algorithms-sort.py)
3. [Sort a list of ones, twos and threes](https://github.com/harishvc/challenges/blob/master/sort-array-containing-zeros-ones-twos.py)
4. [Given two sorted list merge them] (https://github.com/harishvc/challenges/blob/master/sort-merge.py)

### Dynamic Programming
1. [Find the nth Fibonacci number](https://github.com/harishvc/challenges/blob/master/fibonacci-find-nth.py) 
2. [Longest Common Subsequence (LCS)](https://github.com/harishvc/challenges/blob/master/longest-common-subsequence.py) :boom: :thumbsup:  
   2.1 [Length of the LCS](https://github.com/harishvc/challenges/blob/master/longest-common-subsequence-length.py)  
   2.2 [Find a LCS](https://github.com/harishvc/challenges/blob/master/longest-common-subsequence-find-one.py)  
   2.3 [Find all the LCS](https://github.com/harishvc/challenges/blob/master/longest-common-subsequence-find-all.py) :rocket:   
3. Longest common substring
   3.1 Length of the longest common substring
   3.2 [Find the longest common substring](https://github.com/harishvc/challenges/blob/master/longest-common-substring.py)
4. Given two sequences find the longest palindrome
5. [Implement Unix diff command](https://github.com/harishvc/challenges/blob/master/unix-diff.py)
6. [Given stock prices during a time period find the maximum gain that can be made from one purchase followed by one sale of the stock](https://github.com/harishvc/challenges/blob/master/find-maximum-gain.py) :memo:
7. Given denominations and a total   
    a. [Find total #ways to reach a total](https://github.com/harishvc/challenges/blob/master/coin-change.py) :bulb: :boom:   
    b. Minimum # coins needs to reach the total   
    c. All possible combinations and the most optimal one   
8. Given an array of integers, write a functions that returns true if there is a triplet (a,b,c) that satisfies a^2 + b^2 = c^2 [TODO]

### Design &amp; Algorithms
1. [Design and implement Least Used Cache (LRU)](https://github.com/harishvc/challenges/blob/master/Design-and-implement-LRU.py) :bulb:
2. [Given a million points (x, y), give an O(n) solution to find the n points closest to (0, 0)](https://github.com/harishvc/challenges/blob/master/nearest-point.py)
3. [Implement T9](https://github.com/harishvc/challenges/blob/master/t9.py)
4. [How to find list of possible words from a letter matrix (Boggle)](https://github.com/harishvc/challenges/blob/master/boggle.py)
5. [Given a family tree, find oldest sisters of the given person, oldest sister in the family tree and the oldest ancestor](https://github.com/harishvc/challenges/blob/master/people-tree.py)
6. [Given a source word, target word and dictionary, transform the source word to target by changing/adding/removing 1 character at a time, 
    while all intermediate words being valid words in the dictionary. Return the transformation chain which has the smallest number of 
    intermediate words](https://github.com/harishvc/challenges/blob/master/transform-word.py) :memo:
7. [Design a command line alarm clock](https://github.com/harishvc/challenges/blob/master/alarm-clock.py)
8. [Design a data structure that provides insert, remove, contains and get random operations in O(1) time](https://github.com/harishvc/challenges/blob/master/design-data-structure-constant-time.py) :bulb: :rocket: :thumbsup:
9. Using OOP design a elevator  

### Bitwise Operations
1. [Introduction to bitwise operations](https://github.com/harishvc/challenges/blob/master/bitwise-operations.py)
2. [Bitwise addition](https://github.com/harishvc/challenges/blob/master/bit-operation-add.py)
3. [Bitwise subtraction](https://github.com/harishvc/challenges/blob/master/bit-operation-subtract.py)
4. [Given a number n, check whether the number is a power of 2](https://github.com/harishvc/challenges/blob/master/bit-operation-check-if-number-is-power-of-2.py)
5. [Given a number n, multiple the number by 2^k](https://github.com/harishvc/challenges/blob/master/bit-operation-multiply-number-by-power-of-2.py)
7. [Swap two variable values without additional space](https://github.com/harishvc/challenges/blob/master/swap-two-variable-values-without-additional-space.py)

### Algorithms and Data Structures Resources
* [Top 10 Algorithms for Coding Interview](http://www.programcreek.com/2012/11/top-10-algorithms-for-coding-interview/) :boom: :thumbsup:
* [Problem Solving with Algorithms and Data Structures](http://interactivepython.org/runestone/static/pythonds/index.html)
* Data Structure and Algorithmic Thinking with Python :boom: :thumbsup:  
   a. [Book@Amazon](http://www.amazon.com/dp/8192107590/ref=as_li_ss_til?tag=caree0ea-20&camp=213381&creative=390973&linkCode=as4&creativeASIN=819210754X&adid=1PJGG64MJE0JQ00FTD4E&&ref-refURL=http://careermonk.com/?qa=buy)  
   b. [GitHub Repository](https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython)   
* Cracking the Coding Interview (6th Edition) :boom: :thumbsup:  
   a. [Book@Amazon](http://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl)    
   b. [GitHub Repository](https://github.com/gaylemcd/CtCI-6th-Edition)   
   c. [Resources](http://www.crackingthecodinginterview.com/resources.html)    
* Tushar Roy :boom: :thumbsup:   
   a. [Interview Questions Wiki](https://github.com/mission-peace/interview/wiki)   
   b. [YouTube Playlist](https://www.youtube.com/user/tusharroy2525)   
* [The Hitchhiker’s Guide to the Programming Contests (PDF)](http://comscigate.com/Books/contests/icpc.pdf)
* [Two-phase commit protocol](http://en.wikipedia.org/wiki/Two-phase_commit_protocol)  
* [Juan Elices Leetcode blog ](http://jelices.blogspot.com/)  
* [Magic of XOR](http://www.cs.umd.edu/class/sum2003/cmsc311/Notes/BitOp/xor.html)
* [Know Thy Complexities!](http://bigocheatsheet.com/)

### Python Resources
* [Python Module of the Week](http://pymotw.com/2/contents.html)
* [dis – Python Bytecode Disassembler](https://pymotw.com/2/dis/)
* [Python debugger cheat sheat](http://www.cheatography.com/ralienpp/cheat-sheets/python-pdb/)
* [Python exception handling - try/except/else/finally](http://pythoncentral.io/catching-python-exceptions-the-try-except-else-keywords/)
* [Real-World Regular Expressions for Python](http://pythoncentral.io/real-world-regular-expressions-for-python/)
* [The Python Tutorial (version 3.4)](https://docs.python.org/3.4/tutorial/index.html)
* [Python Programming.Net](http://pythonprogramming.net/dashboard/)
* [Popular Python recipes @ ActiveState](http://code.activestate.com/recipes/langs/python/)
* [Object-oriented concepts in Python](http://zetcode.com/lang/python/oop)

### Interview Resources
* [Google interview questions - Product & Software Engineer](https://gist.github.com/amaxwell01/3728155)
* [How to avoid and outlive layoffs as a programmer?](http://www.coderust.com/blog/2014/07/20/avoid_outlive_programmer_layoffs/)
* [How do I prepare for a software engineering job interview? - Discussion on Quora](http://www.quora.com/How-do-I-prepare-for-a-software-engineering-job-interview)
* [Data Structure tutorials from Eternally Confuzzled](http://eternallyconfuzzled.com/Tutorials.aspx)
* [Andrei Simionescu GitHub Respository with code and numerous online resources](https://github.com/andreis/interview)
* [Recent interview questions@Career Cup](http://www.careercup.com/page)
* [Interview questions on reddit](https://www.reddit.com/r/cscareerquestions/comments/20ahfq/heres_a_pretty_big_list_of_programming_interview/)
* [JavaScript interview questions](http://rileyh.com/ui-developer-interview-questions-answers/)

### Amazing Technical Discussions
* [Why would anyone like to use a red black tree when a hash table can do the job perfectly?](http://www.quora.com/Why-would-anyone-like-to-use-a-red-black-tree-when-a-hash-table-can-do-the-job-perfectly)
* [Beating Binary Search @ LinkedIn Blogs - using interpolation search](http://data.linkedin.com/blog/2010/06/beating-binary-search) :bulb:

### GitHub Resources
* [List of emoji for git commits](https://gist.github.com/pocotan001/68f96bf86891db316f20)
* [Emoji cheat sheet](http://www.emoji-cheat-sheet.com/)
* [Github markup preview](http://github-markup.dfilimonov.com/)

#Write a function that returns values randomly, according to their weight

'''
SOURCE:
http://blog.gainlo.co/index.php/2016/11/11/uber-interview-question-weighted-random-numbers/

EXPLANATION:
Suppose we have 3 elements with their weights: A (1), B (1) and C (2). 
The function should return A with probability 25%, B with 25% and C with 50% based on the weights

SOLUTION 1:
input                lookup1                        lookup2
A->1,B->1,C->2       1->A,2->B,4->C                  X    1    2    4
                                                    [0]  [1]  [2]  [3]

n = # of elements
Time Complexity: O(log n) - binary search on lookup2
Space complexity: O(n)


SOLUTION 2:
input                lookup
A->1,B->1,C->2        X    A    B    C    C
                     [0]  [1]  [2]  [3]  [4]

m = sum of weights
Time Complexity: O(1)
Space complexity: O(m)
'''



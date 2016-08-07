#Question: Given BST find inorder successor of node N

'''
OBSERVATION:
1. In inorder traversal, next node value (successor) is > N
2. Successor is the smallest of the largest value > N 

REFERENCES:
1. https://discuss.leetcode.com/topic/25698/java-python-solution-o-h-time-and-o-1-space-iterative
2. http://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/
'''

import sys
sys.path.append("./mylib")
import BST

#Create BST
root = BST.BSTNode(4)
input = [3,2,1,5,10,7,6,9,12,15]
for x in input:
    BST.insert(root, BST.BSTNode(x))


def nextNode(node,target):
    result = None
    while node:
        #if value > target, can be successor!
        if node.data > target:
            result = node.data
            #IMPORTANT: find smallest of the largest!
            node = node.left
        else:
            #go right!
            node = node.right
    return result

target = 11
print("First value greater than ", target , " = ", nextNode(root,target))

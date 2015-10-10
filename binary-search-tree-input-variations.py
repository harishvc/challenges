'''
Question: Find all possible combinations that can generate identical Binary Search Tree (BST)

Algorithm:
1. Find all left nodes
2. Find all right nodes
3. Weave values from left nodes and right nodes to generate new lists 
   such that the relative positions are SAME . 
   Example:  3,1,2,4,5
   - 1 will be always before 2
   - 5 will be always after 4

TODO: 
1. Time complexity
2. Use Linked List
3. #variations: http://stackoverflow.com/questions/1701612/permutations-of-bst
'''

#Modified from https://github.com/gaylemcd/CtCI-6th-Edition/blob/master/Java/Ch%2004.%20Trees%20and%20Graphs/Q4_09_BST_Sequences/Question.java
def weave(l,r,result,prefix):
    #case 1: one of the list is empty
    if (len(l) == 0 or len(r) == 0):
        result += [prefix + l + r]     
        return
    #case 2: go left
    prefix.append(l.pop(0))
    weave(l,r,result,prefix)
    l.insert(0,prefix.pop())
    #case 3: go right
    prefix.append(r.pop(0))
    weave(l,r,result,prefix)
    r.insert(0,prefix.pop())
    
#Given a node, return all child nodes
def FindChildNodes(node,result):
    if node is None:
        return result
    result.append(node.data)
    FindChildNodes(node.left,result)
    FindChildNodes(node.right, result)
    
def FindCombinations(node):
    result = []
    lnodes = []
    rnodes = []    
    #get root
    prefix = [node.data]
    #get all left nodes of the root
    FindChildNodes(node.left, lnodes)
    #get all right nodes of the root
    FindChildNodes(node.right, rnodes)
    #find permutations
    weave(lnodes,rnodes,result,prefix)
    return result

import sys
sys.path.append("./mylib")
import BST

#Create BST
input = [3,1,2,4,5]
root = BST.BSTNode(input[0])
for x in range(1,len(input)):
    BST.insertNode(root, BST.BSTNode(input[x]))

print("BST permutations for input >>", input)
result = FindCombinations(root)
for c in result:
    print(c)


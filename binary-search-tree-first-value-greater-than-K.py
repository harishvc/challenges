'''
Question: In a BST find first value greater than K or given node K find the next node. Return 1 if None

Observation:
When root.data > K we have a greater value. We then need to traverse left to first the first greater value.
Since left node can be None, we need to store the greatest value found so far before traversing left
'''

import sys
sys.path.append("./mylib")
import BST

#Create BST
root = BST.BSTNode(4)
input = [3,2,1,5,10,7,6,9,12,15]
for x in input:
    BST.insertNode(root, BST.BSTNode(x))


def FirstGreatestValue(node,target,result):
    #End of recursion
    if(node is None):
        return result
    
    #Found value?
    if(node.data == target):
        return node.data
    if (node.data > target and result == 1):
        #First new value
        result = node.data
    elif( node.data > target and (node.data-target) < (result-target)):
       #found next new value!
       result = node.data
    
    #Next?   
    if(node.data < target):
        #go right
        return(FirstGreatestValue(node.right,target,result))
    else:
        #go left
        return(FirstGreatestValue(node.left,target,result))

target = 11
print("First value greater than ", target , " = ", FirstGreatestValue(root,target,1))
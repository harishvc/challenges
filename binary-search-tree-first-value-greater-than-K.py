'''
Question: In a BST find first value greater than K or given node K find the next node

Observation:
When root.data > K we have a greater value. We then need to traverse left to first the first greater value.
Since left node can be None, we need to store the greatest value found so far before traversing left
'''

import sys
sys.path.append("./mylib")
import BST

#Create BST
root = BST.BSTNode(4)
input = [3,2,1,5,10,7,6,9,15]
for x in input:
    BST.insertNode(root, BST.BSTNode(x))

def FirstGreaterValue(root,K,result):
    if(root is None):
        return result
    elif (root.data > K): #new result!
        result = FirstGreaterValue(root.left,K,root.data)
    elif (root.data <= K):
        result = FirstGreaterValue(root.right,K,result)
    return result
    
for K  in range(0,len(input)-1):
    print("First value greater than %d = %d" % (input[K],FirstGreaterValue(root,input[K],"None")))

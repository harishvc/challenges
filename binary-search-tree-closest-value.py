'''
Question: In a BST given target find a value close to the target
'''

import sys
sys.path.append("./mylib")
import BST

#Create BST
root = BST.BSTNode(4)
input = [3,2,1,5,10,7,6,9,12,15]
for x in input:
    BST.insertNode(root, BST.BSTNode(x))


#http://stackoverflow.com/questions/6209325/how-to-find-the-closest-element-to-a-given-key-value-in-a-binary-search-tree
def ClosestValue(node,target,result):
    #End?
    if(node is None):
        return result
    
    #Found new value?
    if(node.data == target):
        return node.data
    if(result is None or  abs(target-node.data) < abs(target-result)):
       #found new value!
       result = node.data
    
    #Next path?   
    if(node.data < target):
        #go right
        return(ClosestValue(node.right,target,result))
    else:
        #go left
        return(ClosestValue(node.left,target,result))

target = 11
print("Value close to ", target, " = ", ClosestValue(root,target,-1))


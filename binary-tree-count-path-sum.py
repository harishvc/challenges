'''
Question: Count # path that add up to a given value. 
Path are from parent node to child node, root and leaf can be excluded in the path
'''

import sys
sys.path.append("./mylib")
import Tree

def UpdatePathSumHash(PSH,sum,delta):
    newcount = PSH.get(sum,0) + delta
    PSH[sum] = newcount
    
def SumRoot2LeafPathsRecursive(node,sum,target,PSH):
     if(node is None):
         return 0
     
     sum += node.data  #running sum
     psum = sum - target #pathsum IMPORTANT!
     result = PSH.get(psum,0) #get #path that add up to a pathsum
     if (sum == target):
         result += 1
    
     #Increment 1 path to running sum
     UpdatePathSumHash(PSH,sum,1) 
     result += SumRoot2LeafPathsRecursive(node.getLeft(),sum,target,PSH)
     result += SumRoot2LeafPathsRecursive(node.getRight(),sum,target,PSH)
     #Decrement 1 path to running sum since path are from parent nodes to child nodes
     UpdatePathSumHash(PSH,sum,-1) 
     return result
 
     
#Build binary tree 
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)

PSH = {} #path sum hash
target = 7 #target value
countPaths = SumRoot2LeafPathsRecursive(root,0,target,PSH)
print("#paths that sum to %d = %d" % (target,countPaths))

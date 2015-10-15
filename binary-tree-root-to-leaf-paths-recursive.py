'''
Question: Print all paths & path sum from root to leaf (recursive)
'''

import sys
sys.path.append("./mylib")
import Tree

def SumRoot2LeafPathsRecursive(node,sum,path):
     if(node is None):
         return 0
     sum = sum + node.data  #sum of path
     path.append(node.data) #path
     #leaf
     if(node.getLeft() is None and node.getRight() is None):
         print("path=%s sum=%d" %(path,sum))
         path.pop()
         return sum-node.data 
     SumRoot2LeafPathsRecursive(node.getLeft(),sum,path)
     SumRoot2LeafPathsRecursive(node.getRight(),sum,path)
     path.pop() #Important
 
     
#Build binary tree 
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)


path = []
print("root to leaf path & sum:")
SumRoot2LeafPathsRecursive(root,0,path)
assert len(path) == 0, "Houston we have a problem!"

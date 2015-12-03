'''
Question: Print all paths & path sum from root to leaf (recursive)
'''

import sys
sys.path.append("./mylib")
import Tree
 

#Print all root to leaf path and sum
def Root2Leaf(node,path,sum):
    if (node is None):
        return
    sum += node.data
    path.append(node.data)    
    if(node.getRight() is None and node.getLeft() is None):
        print(path, sum)
        path.pop()
        return
    Root2Leaf(node.getLeft(),path,sum)
    Root2Leaf(node.getRight(),path,sum)
    path.pop() #pop non-leaf nodes while leaving


     
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
#SumRoot2LeafPathsRecursive(root,0,path)
Root2Leaf(root,path,0)
assert len(path) == 0, "Houston we have a problem!"

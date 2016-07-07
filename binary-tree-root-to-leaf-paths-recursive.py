'''
Question: Print all paths & path sum from root to leaf (recursive)
'''

import sys
sys.path.append("./mylib")
import Tree
 
#Solution 1
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

#Solution 2
#Modified post order traversal (EASY TO FOLLOW!)
def Root2Leaf2(node,path,sum):
    if node is None:
        return
    path.append(node.data)
    sum += node.data    
    Root2Leaf2(node.left,path,sum)
    Root2Leaf2(node.right,path,sum)
    #IMPORTANT: Path ends in a leaf, check if node is leaf    
    if(node.left is None and node.right is None):
        print(path,sum)
    path.pop()
    sum -= node.data


     
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
#Root2Leaf(root,path,0)
#assert len(path) == 0, "Houston we have a problem!"
Root2Leaf2(root,path,0)
assert len(path) == 0, "Houston we have a problem!"

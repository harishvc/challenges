'''
Question: Print all paths & path sum from root to leaf (recursive)
'''

import sys
sys.path.append("./mylib")
import Tree
 
#Modified post order traversal
def Root2Leaf2(node,path,sum):
    if node is None:
        return
    #step 1: update sum and path
    path.append(node.data)
    sum += node.data    
    #step 2: visit sub-tree on left
    Root2Leaf2(node.left,path,sum)
    #step 3: visit sub-tree on right
    Root2Leaf2(node.right,path,sum)
    #step 4: If you are here, you have visited all nodes in the left and right sub-tree!!!
    #check if node is leaf?    
    if(node.left is None and node.right is None):
        print(path,sum)
    #step 5: update sum and path (go up the tree to the parent node)
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

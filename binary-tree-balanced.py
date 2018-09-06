#Check if a binary tree is a fully balanced binary tree

'''
Fully balanced tree is defined as a tree such that the height of the two subtrees of any node never differ by more than one.
'''

import sys
sys.path.append("./mylib")
import Tree
import BinaryTreeTraversal

def isBalancedBinaryTree(node):
    return (isBalancedBinaryTreeWrapper(node) >= 0)

#Modified post order traversal      
#Integrate height 
def isBalancedBinaryTreeWrapper(node):
    if node is None:
        return 0
    lheight = isBalancedBinaryTreeWrapper(node.left)
    rheight = isBalancedBinaryTreeWrapper(node.right)
    #Kill if height of sub-trees > 1
    if abs(lheight-rheight) > 1:
        return -1
    #return height of sub-tree
    return max(lheight,rheight) + 1


root = Tree.BinaryTree(5)
root.insertLeft(2)
root.insertRight(10)
root.getLeft().insertLeft(1)
root.getLeft().insertRight(3)
root.getLeft().getLeft().insertLeft(25)
root.getLeft().getLeft().getLeft().insertLeft(60)

print("Is this tree balanced? %s" % (isBalancedBinaryTree(root)))
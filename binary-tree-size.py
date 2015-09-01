#Question: Find the size of the binary tree

#Size of binary tree is size of left subtree + 1 + size of right subtree

import sys
sys.path.append("./mylib")
import Tree

def TreeSize(root):
	if not root:
		return 0
	return TreeSize(root.left) + TreeSize(root.right) + 1 	

#Initialize Binary Tree
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)
#
#
print("Size of the binary tree =",TreeSize(root))
 

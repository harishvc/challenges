'''
Question: Find the height of the binary tree

Height is the number of nodes along the longest path from the root node down 
to the farthest leaf node

Leaf nodes have height 1
http://stackoverflow.com/questions/13322616/how-to-find-the-height-of-a-node-in-binary-tree-recursively/
'''

import sys
sys.path.append("./mylib")
import Tree

def height(root):
	if (root == None) :
		return 0
	x = height(root.left)
	y = height(root.right)
	z = max(x,y) + 1
	return z


root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)
root.getLeft().getLeft().insertLeft(8)
root.getLeft().getRight().insertRight(9)
root.getLeft().getRight().getRight().insertRight(10)
root.getLeft().getRight().getRight().getRight().insertRight(11)
print("height of node(%d) is %d" % (root.data,height(root)))
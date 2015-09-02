'''
Question: Find max diameter (width) and height of a binary tree

Diameter of a tree (sometimes called the width) is the number of nodes on the 
longest path between two leaves in the tree. 

Height is the number of nodes along the longest path from the root node down 
to the farthest leaf node.
'''


import sys
sys.path.append("./mylib")
import Tree
	
#source:http://www.careercup.com/question?id=1767700
def diameter_height(tree):	
	if tree is None: 
		return (0,0)
	ld, lh = diameter_height(tree.left)
	rd, rh = diameter_height(tree.right)
	d = max([ld, rd, lh+rh+1])
	h = max([lh+1, ld+1])
	return d, h	

root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
#root.getLeft().insertRight(5)
#root.getRight().insertLeft(6)
#root.getRight().insertRight(7)
#root.getLeft().getLeft().insertLeft(8)
#root.getLeft().getRight().insertRight(9)
#root.getLeft().getRight().getRight().insertRight(10)
#root.getLeft().getRight().getRight().getRight().insertRight(11)

d,h = diameter_height(root)
print("Diameter of tree = %d and max height=%d" % (d,h))

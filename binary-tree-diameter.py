#Question: Find diameter (width) of a binary tree

import sys
sys.path.append("./mylib")
import Tree

'''
Notes:
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree. 
http://www.geeksforgeeks.org/diameter-of-a-binary-tree/

The function Compute the "height" of a tree. Height is the number f nodes along 
the longest path from the root node down to the farthest leaf node.
'''
			
#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter06trees/TreeDiameter.py
def diameter(root):
	if (root == None): 
		return 0
	lHeight = height(root.left)
	rHeight = height(root.right)
	lDiameter = diameter(root.left)
	rDiameter = diameter(root.right)
	return max(lHeight + rHeight + 1, max(lDiameter, rDiameter))

# The function Compute the "height" of a tree. Height is the number f nodes along 
# the longest path from the root node down to the farthest leaf node.
def height(root):
	if (root == None) :
		return 0
	return 1 + max(height(root.left), height(root.right))


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
print("Diameter of tree = %s" % (diameter(root)))

'''
Question: Find max diameter (width) and height of a binary tree

Height is the number of nodes along the longest path from the node down 
to the farthest leaf node.

Diameter of a tree (sometimes called the width) is the number of nodes on the 
longest path between two leaves in the tree. 


Diameter of a binary tree T will be the largest of the following quantities:
1. Diameter of T’s left subtree
2. Diameter of T’s right subtree
3. Longest path between leaves that goes through the root of T 
   (this can be computed from the heights of the subtrees of T)
'''

import sys
sys.path.append("./mylib")
import Tree

#Reference: http://tech-queries.blogspot.com/2010/09/diameter-of-tree-in-on.html
#Solution 1:
#Time complexity: O(n^2) . height() is linear however it is called for every node that results in a complexity of O(n^2). 
#Time complexity can be reduced to O(n) if we calculate the height with diameter for each node (solution 2)
def diameter(root):
	if (root == None): 
		return 0
	lHeight = height(root.left)
	rHeight = height(root.right)
	lDiameter = diameter(root.left)
	rDiameter = diameter(root.right)
	return max(lHeight + rHeight + 1, max(lDiameter, rDiameter))
	
def height(root):
	if (root == None) :
		return 0
	x = height(root.left)
	y = height(root.right)
	z = max(x,y) + 1
	return z
	
#Reference 1: http://www.careercup.com/question?id=1767700
#Reference 2: https://crackinterviewtoday.wordpress.com/2010/03/11/diameter-of-a-binary-tree/
#Solution 2: Optimized to find max diameter and height
#Time complexity: O(n)
def diameter_height(tree):	
	if tree is None: 
		return (0,0)
	ld, lh = diameter_height(tree.left)   #Diameter of left subtree
	rd, rh = diameter_height(tree.right)  #Diameter of right subtree
	path = lh+rh+1  #Longest path between leaves that goes through the node (tree)
	d = max([ld, rd, path])
	h = max(lh,rh) + 1
	#print("Node(%d) diameter=%d height=%d" % (tree.data,d,h))
	return (d,h)	


root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
#root.getRight().insertLeft(6)
#root.getRight().insertRight(7)
#root.getLeft().getLeft().insertLeft(8)
#root.getLeft().getRight().insertRight(9)
#root.getLeft().getRight().getRight().insertRight(10)
#root.getLeft().getRight().getRight().getRight().insertRight(11)

print("Diameter of tree (time complexity O(n^2)) = %d" % diameter(root))
d,h = diameter_height(root)
print("Diameter of tree (time complexity O(n)) = %d and max height=%d" % (d,h))
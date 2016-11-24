#Question: Find max diameter (width, longest path) and height of a binary tree

'''
NOTES:
Diameter of a binary tree T will be the largest of the following quantities:
1. Diameter of T’s left subtree
2. Diameter of T’s right subtree
3. Longest path between leaves that goes through the root of T 
    - height of left subtrees + height of right subtree + 1
'''

import sys
sys.path.append("./mylib")
import Tree

#Solution 1:
#Reference: http://tech-queries.blogspot.com/2010/09/diameter-of-tree-in-on.html
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
	
#Solution 2: Optimized to find max diameter and height
#Reference 1: http://www.careercup.com/question?id=1767700
#Reference 2: https://crackinterviewtoday.wordpress.com/2010/03/11/diameter-of-a-binary-tree/
#Time complexity: O(n)
def diameter_height(tree):	
	if tree is None: 
		return (0,0)
	ld, lh = diameter_height(tree.left)   #Diameter of left subtree
	rd, rh = diameter_height(tree.right)  #Diameter of right subtree
	longest_path = lh+rh+1                #Longest path between leaves that goes through the node (tree)
	h = max(lh,rh) + 1
	d = max([ld, rd, longest_path])
	#print("Node(%d) height=%d diameter=%d" % (tree.data,h,d))
	return (d,h)	

'''
Example 1: diameter via root
                         1
                       /   \ 
                      2     3
                    /   \
                  4      5
 
 node[4]: height=1, diameter=1
 node[5]: height=1, diameter=1
 node[2]: height=2, diamter= max(1,1,1+1+1) = 3
 node[3]: height=1, diameter=1
 node[1]: height=max(2,1)+1 = 3, diameter=max(3,1,2+1+1) = 4
'''
#Example 1
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
d,h = diameter_height(root)
print("Diameter of tree 1 (time complexity O(n)) = %d and max height=%d" % (d,h))

'''
Example 2: diameter not via root
						  1
						/   
					   2	
					 /   \
				    4     5
				  /        \
				 6          7
				             \
				              8   
node[8]: height=1 , diameter=1 
node[7]: height=2 , diameter=2 
node[5]: height=3 , diameter=3 
node[6]: height=1 , diameter=1 
node[4]: height=1 , diameter=2 
node[2]: height=4 , diameter=max(2,3,2+3+1)=6 
node[1]: height=5 , diameter=max(6,0,4+0+1)=6 
'''
root = None
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getLeft().getLeft().insertLeft(6)
root.getLeft().getRight().insertRight(7)
root.getLeft().getRight().getRight().insertRight(8)
d,h = diameter_height(root)
print("Diameter of tree 2 (time complexity O(n)) = %d and max height=%d" % (d,h))

#Question: Find max depth of binary tree
#Depth of a node is the length of the path (#nodes) from the root to the node

import sys
sys.path.append("./mylib")
import Tree
from heapq_showtree import show_tree
 
def MaxDepthRecursive(root):
	if (root == None):
		return 0 
	return max(MaxDepthRecursive(root.right),MaxDepthRecursive(root.left)) + 1  	

#Source: http://jelices.blogspot.com/2014/05/leetcode-python-maximum-depth-of-binary.html
def MaxDepth(root):
	maxDepth = 0
	if root is None:
		return maxDepth
	nodes = []
	depth = []
	nodes.append(root) 
	depth.append(1) #root node at depth 1
	while nodes:  
		newNode =  nodes.pop()
		newDepth = depth.pop()
		maxDepth = max(maxDepth,newDepth)
		if(newNode.left is not None):
			nodes.append(newNode.left)   #Add new node to stack
			depth.append(newDepth + 1)   #Add height of new node in stack
		if(newNode.right is not None):
			nodes.append(newNode.right)  #Add new node to stack
			depth.append(newDepth + 1)   #Add height of new node in stack
	return maxDepth

root = Tree.BinaryTree(5)
root.insertLeft(9)
root.insertRight(15)
root.getLeft().insertLeft(2)
root.getLeft().insertRight(4)
root.getRight().insertLeft(3)
root.getRight().insertRight(7)
root.getLeft().getLeft().insertLeft(8)
root.getLeft().getRight().insertRight(9)
root.getLeft().getRight().getRight().insertRight(10)
root.getLeft().getRight().getRight().getRight().insertRight(11)

#Find max depth
print("Max depth of the binary tree (iterative) =",MaxDepth(root))
print("Max depth of the binary tree (recursive) =",MaxDepthRecursive(root))

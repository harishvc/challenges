#Question: Find the max value of the binary tree

import sys
sys.path.append("./mylib")
import Tree

#Find maximum value
def FindMax(root):
	global DefaultMax  #global variable since function is recursive   
	if not root:   #Handle null node
		return
	if (root.data > DefaultMax):
		DefaultMax = root.data
	FindMax(root.right)
	FindMax(root.left)	
	
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
result = []
#
#
#
DefaultMax = float("-infinity") #Storing max in a global variable since the function is recursive
FindMax(root)
print("Maximum value in the binary tree =",DefaultMax)
 

#BST Library: Add, Delete, isBST? max, min

import sys
sys.path.append("./mylib")
import BinaryTreeTraversal

class BSTNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

#Insert node to BST
def insert(node,Newnode):
	#condition 1: node is empty
	if node is None:
		node = Newnode
	#condition 2: new value < value at parent node	and parent has NO left node
	elif Newnode.data < node.data and node.left is None:
		node.left = Newnode
	#condition 3: new value < value at parent node	and parent has left node
	elif Newnode.data < node.data:
		insert(node.left,Newnode)
	#condition 4: new value >= value at parent node	and parent has NO right node
	#Handle DUPLICATE values. BST usually don't have DUPLICATE values by some definition
	elif Newnode.data >= node.data and node.right is None:
		node.right = Newnode
	#condition 5: new value > value at parent node and parent has right node
	else:
		insert(node.right,Newnode)

#Delete node from BST
def delete(node,Newnode):
	#case 1: Found node to delete
	if node.data == Newnode.data:
		#case 4: node to delete has left and right subtrees
		if node.right and node.left:
			#IMPORTANT: Find the smallest value in the right sub tree to replace the node for deletion
			pnode,snode = findSmallest(node,node.right)
			if pnode.left == snode:
				#pnode and snode are ALREADY connected
				#OBSERVATION: snode is a leaf or half node (cannot be a full node)
				pnode.left = snode.right
			else:
				#OBSERVATION: NO left node; pnode == node
				pnode.right = snode.right
			snode.left = node.left
			snode.right = node.right
			#clean up
			node.left  = None
			node.right = None
			#IMPORTANT: return snode
			return snode
		#case 5: node to delete has either left or right subtree or leaf	
		elif node.left:
			#clean up
			tmp = node.left
			node.left = None
			return tmp #promote left subtree
		else:
			#clean up
			tmp = node.right
			node.right = None
			return node.right  #promote right subtree; node == leaf
	#case 2: node to delete in left subtree
	elif Newnode.data < node.data and node.left:
		node.left = delete(node.left,Newnode)
	#case 3: node to delete in right subtree
	elif Newnode.data > node.data and node.right:
		node.right = delete(node.right,Newnode)
	else:
		print("Value outside BST")
		return node
	#IMPORTANT return node
	return node

#Find the node with smallest value in the subtree
def findSmallest(predecessor, successor):
	#Smallest value is in the left sub tree!
	if successor.left:
		return findSmallest(successor,successor.left)
	else:
		return predecessor,successor


#Is the tree a BST?
#Modify pre order traversal
def isBST(node):
	#condition 1: no node
	if node is None:
		return True
	#condition 2: left node with value > parent node
	elif node.left and node.left.data > node.data:
		return False
	#condition 3: right node with value < parent node
	elif node.right and node.right.data < node.data:
		return False
	#condition 4: leaf node
	else:
		return isBST(node.left) and isBST(node.right)

#Find Max
#Modify in order traversal to get the value of the furthest right node
def getMax(node):
	if node.right:
		return getMax(node.right)
	else:
		return node.data

#Find Min
#Modify post traversal to get the value of the furthest left node
def getMin(node):
	if node.left:
		return getMin(node.left)
	else:
		return node.data

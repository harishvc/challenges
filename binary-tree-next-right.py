#Given a full binary tree, populate the nextright pointers in each node

'''
OBSERVATION:
1. Modify pre order traversal to check for left and right nodes
2. if node has a left node set right sibling
3. if node has a right node set right sibling using PREVIOUSLY found value!  
4. Traversing using the nextright attribute is similar to LEVEL ORDER TRAVERSAL

REFERENCE: 
http://articles.leetcode.com/first-on-site-technical-interview
'''

class BinaryTree:
	def __init__(self, data):
		self.data = data  # root node
		self.left = None  # left child
		self.right = None  # right child
		self.nextright = None #right sibling

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right    

	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp

	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp

#IMPORTANT: nextright set on the root node!!!
def populateSibling(node):
    if node is None:
        return None
    if node.left:
        node.left.nextright = node.right
    #IMPORTANT: use the node.nextright  rather than node.left.left!       
    if node.right and node.nextright:
        node.right.nextright = node.nextright.left
    populateSibling(node.left)
    populateSibling(node.right)

#Traversing using the nextright attribute is similar to LEVEL ORDER TRAVERSAL
def LevelOrderTraversal(node):
	while node:
		print(node.data,end=" ")
		node = node.nextright

import sys
sys.path.append("./mylib")
#import Tree
import BinaryTreeTraversal

root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)

print("In order traversal >>")
BinaryTreeTraversal.inOrder(root)
print("")

#IMPORTANT: nextright set on the root node!!!
root.nextright = root.left
populateSibling(root)
print("Level order traversal")
LevelOrderTraversal(root)
print("")
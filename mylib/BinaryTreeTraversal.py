#Binary Tree Traversal Library

class BinaryTree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def insertRight(self,node):
		self.right = node

	def insertLeft(self,node):
		self.left = node

###
def preOrder(root):
	if root is None:
		return
	print(root.data,end=" ")
	preOrder(root.left)
	preOrder(root.right)
def preOrderIterative(root):
	seen = []
	if root is None:
		return seen
	seen.append(root)
	while seen:
		node = seen.pop()
		print(node.data)
		if node.right:
			seen.append(node.right)  #IMPORTANT!!!! 
		if node.left:
			seen.append(node.left)   #add left subtree at the end!!!!

###
def inOrder(root):
	if root is None:
		return
	inOrder(root.left)
	print(root.data,end=" ")
	inOrder(root.right)
def inOrderIterative(root):
	seen = []
	if root is None:
		return seen
	node = root
	while seen or node:
		if node:
			seen.append(node) 
			node = node.left
		else:
			node = seen.pop()
			print(node.data)
			node = node.right

###
def postOrder(root):
	if root is None:
		return
	postOrder(root.left)
	postOrder(root.right)
	print(root.data,end=" ")
def postOrderIterative(root):
	seen = []
	node = root
	visited = set() #keep track of nodes visited
	while seen or node:
		if node:
			seen.append(node) 
			node = node.left
		else:
			node = seen.pop()
			if node not in visited:
				visited.add(node)
				#IMPORTANT: Add node back to stack
				seen.append(node) 
				node = node.right
			else:
				#complete visting the left and right node
				print(node.data)
				#IMPORTANT: change node to None so next node can get processed
				node = None

###
import queue
def levelOrder(root):
	q = queue.Queue()
	result =  []
	depth = 0
	if root is None:
		return
	else:
		q.put(root)
		q.put(depth) #depth = 0 at root 
		currentDepth = 0
	while not q.empty():
		node = q.get()
		depth = q.get()
		if depth == currentDepth:
			result.append(node.data)
		else:
			print(result)
			del result[:] #
			result.append(node.data)
			currentDepth = depth
		if node.left:
			q.put(node.left)
			q.put(depth+1)
		if node.right:
			q.put(node.right)
			q.put(depth+1)
	print(result) #leaves/last level

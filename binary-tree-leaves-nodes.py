#Question: Find #leaves in a binary tree

import queue

#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter06trees/BinaryTree.py
class BinaryTree:
	def __init__(self, data):
		self.data = data  # root node
		self.left = None  # left child
		self.right = None  # right child
	# set data
	def setData(self, data):
		self.data = data
	# get data   
	def getData(self):
		return self.data	
	# get left child of a node
	def getLeft(self):
		return self.left
	# get right child of a node
	def getRight(self):
		return self.right
	# get left child of a node
	def setLeft(self, left):
		self.left = left
	# get right child of a node
	def setRight(self, right):
		self.right = right
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
			
#Using Python queue library for level order traversal
def levelOrder(root):
	if root is None: 
		return
	nleaves = 0 #number of leaves
	nfullnodes = 0 #number of full nodes
	nhalfnodes = 0 #number of half nodes
	q = queue.Queue()       
	q.put(root)
	n = None
	while not q.empty():
		n = q.get()  #dequeue FIFO
		#Is this node a leaf?
		if(n.left == None and n.right == None):
			nleaves += 1
		#Is this node a full node?
		if(n.left and n.right):
			nfullnodes += 1	
		#Is this node a half node?
		if ((n.left and not n.right) or (n.right and not n.left)):
			nhalfnodes += 1
		if n.left is not None:
			#print("traversing left ..",n.left.getData())
			q.put(n.left)
		if n.right is not None:
			#print("traversing right ..",n.right.getData())
			q.put(n.right)  
	return (nleaves,nfullnodes,nhalfnodes)		


######## Get Started!!!!!
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
# root.getRight().insertRight(7)
# root.getLeft().getLeft().insertLeft(8)
# root.getLeft().getRight().insertRight(9)
# root.getLeft().getRight().getRight().insertRight(10)
# root.getLeft().getRight().getRight().getRight().insertRight(11)

nleaves,nfullnodes,nhalfnodes= levelOrder(root)
print("#leaves = %d , #fullnodes = %d , #halfnodes = %d" % (nleaves,nfullnodes,nhalfnodes))

 
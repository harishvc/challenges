'''
Question: Check if a binary tree is symmetric. 
'''

'''Binary Tree Class and its methods'''
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

import queue
def levelOrder(root, result):
	q = queue.Queue()       
	q.put(root)
	n = None
	while not q.empty():
		n = q.get()  #dequeue FIFO
		#print(n.getData())
		result.append(n.getData())
		if n.left is not None:
			#print("traversing left ..",n.left.getData())
			q.put(n.left)
		if n.right is not None:
			#print("traversing right ..",n.right.getData())
			q.put(n.right)  
					
#Initialize Binary Tree
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(2)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(5)
root.getRight().insertRight(4)

#Traverse
result = []
levelOrder(root, result)
print("LevelOrder traversal: %s" % (result))

def CheckMirror(t1,t2):
	#condition1: both nodes are empty
	if (t1 is None and t2 is None):
			return True
	#condition 2: one of the nodes is empty
	elif( t1 is None or t2 is None):
			return False
	#condition 3: data does not match
	elif( t1.getData() != t2.getData()):
			return False
	#condition 4: check for subnodes	
	else:
		return CheckMirror(t1.getLeft(),t2.getRight()) and  CheckMirror(t1.getRight(),t2.getLeft())
	
print("Is the binary tree symmetrical? " , CheckMirror(root.getLeft(),root.getRight()))	 
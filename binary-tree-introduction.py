#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter06trees/BinaryTree.py

import queue

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

#
class Queue():
		def __init__(self, limit=15):
				self.que = []
				self.limit = limit
				self.front = None
				self.rear = None
				self.size = 0		   

		def isEmpty(self):
				return self.size <= 0

		def enQueue(self, item):
				if self.size >= self.limit:
						print('Queue Overflow!')
						return
				else:
						self.que.append(item)
						
				if self.front is None:  
						self.front = self.rear = 0
				else:
						self.rear = self.size
				self.size += 1
				#print('Queue after enQueue', self.que)
				
		def deQueue(self):
				#print ("que size ....", len(self.que))
				if self.size <= 0:
						print('Queue Underflow!')
						return 0
				else:
						#self.que.pop(0)
						self.size -= 1
						if self.size == 0:
								self.front = self.rear = None   
						else:
								self.rear = self.size - 1
						#print('Queue after deQueue', self.que)
						return self.que.pop(0)
						
# 		def queueRear(self):
# 				if self.rear is None:
# 						print("Sorry, the queue is empty!")
# 						raise IndexError
# 				return self.que[self.rear]
# 
# 		def queueFront(self):
# 				if self.front is None:
# 						print("Sorry, the queue is empty!")
# 						raise IndexError
# 				return self.que[self.front]
						
		def size(self):
				return self.size
			
				    
# Pre-order recursive traversal. The nodes' values are appended to the result list in traversal order
def preorderRecursive(root, result):
    if not root:
        return
    
    result.append(root.data)
    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)

# In-order recursive traversal. The nodes' values are appended to the result list in traversal order
def inorderRecursive(root, result):
	if not root:
		return

	inorderRecursive(root.left, result)
	result.append(root.data)
	inorderRecursive(root.right, result)

# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order
def postorderRecursive(root, result):
    if not root:
        return
    
    postorderRecursive(root.left, result)
    postorderRecursive(root.right, result)
    result.append(root.data)

# Pre-order iterative traversal. The nodes' values are appended to the result list in traversal order
def preorderIterative(root, result):
	if not root:
		return
	stack = []
	stack.append(root)
	while stack:
		node = stack.pop()
		result.append(node.data)
		if node.right: stack.append(node.right)
		if node.left: stack.append(node.left)	
		
# In-order iterative traversal. The nodes' values are appended to the result list in traversal order
def inorderIterative(root, result):
	if not root:
		return

	stack = []
	node = root
	while stack or node:
		if node:
			stack.append(node)
			node = node.left
		else:
			node = stack.pop()
			result.append(node.data)
			node = node.right

# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order
def postorderIterative(root, result):
    if not root:
        return

    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None

#Using Python queue library
def levelOrder2(root, result):
	if root is None: 
		return
    #q = Queue.Queue()
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

#Using list as queue. Inefficient
def levelOrder3(root,result):
	a = []
	a.append(root)
	while a :  #list not empty
		tmp = a.pop(0)
		result.append(tmp.data)
		if tmp.left is not None:
			a.append(tmp.left)
		if tmp.right is not None:
			a.append(tmp.right)

#Recursive. Using list as queue. Inefficient
def levelOrder4(a,result):
	#print (a)
	while a:
		#print ("aaa")
		tmp = a.pop(0)
		result.append(tmp.data)
		if tmp.left is not None:
			a.append(tmp.left)
		if tmp.right is not None:
			a.append(tmp.right)
		levelOrder4(a, result)	

#Implementation using start and end pointers in list as queue
def levelOrder1(root, result):
	global depth
	if root is None:
		return  
	q = Queue()
	q.enQueue(root)
	n = None
	while not q.isEmpty():
	  n = q.deQueue()  # dequeue FIFO
	  result.append(n.getData())
	  if n.left is not None:
	    q.enQueue(n.left)
	
	  if n.right is not None:
	    q.enQueue(n.right)	

#Find maximum value
def FindMax(root):
	global max     #Storing max in a global variable since the function is recursive
	if not root:   #Handle null node
		return
	if (root.data > max):
		max = root.data
	FindMax(root.right)
	FindMax(root.left)	
	
def TreeSize(root):
	if not root:
		return 0
	return TreeSize(root.left) + TreeSize(root.right) + 1 	
	
######## Get Started!!!!!
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)
result = []
#####
preorderRecursive(root, result)
print("PreOrder traversal (recursive): %s" % (result))
#####
del result[:]
preorderIterative(root, result)
print("PreOrder traversal (iterative): %s" % (result))
######
del result[:]
inorderRecursive(root, result)
print("InOrder traversal (recursive): %s" % (result))
######
del result[:]
inorderIterative(root, result)
print("InOrder traversal (iterative): %s" % (result))
######
del result[:]
postorderRecursive(root, result)
print("PostOrder traversal (recursive): %s" % (result))
######
del result[:]
postorderIterative(root, result)
print("PostOrder traversal (iterative): %s" % (result))
######
del result[:]
levelOrder2(root, result)
print("LevelOrder traversal (Python Library): %s" % (result))
######
del result[:]
levelOrder1(root, result)
print("LevelOrder traversal (Inhouse Library): %s" % (result))
######
del result[:]
levelOrder3(root, result)
print("LevelOrder traversal (using list): %s" % (result))
######
del result[:]
levelOrder4([root], result) #send root as list
print("LevelOrder traversal (using list, recursive): %s" % (result))
###########
#float max 
max = float("-infinity")
FindMax(root)
print("Maximum value in the binary tree =",max)
print("Size of the binary tree =",TreeSize(root))
 
#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter06trees/BinaryTree.py



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
		if node.right: stack.append(node.right) #right first - stack pop!
		if node.left:  stack.append(node.left)	
		
# In-order iterative traversal. The nodes' values are appended to the result list in traversal order
def inorderIterative(root, result):
	if not root:
		return
	stack = []
	node = root
	while stack or node:
		if node: #node first then stack
			stack.append(node)
			node = node.left   #Go all the way to the left!!!!
		else:
			node = stack.pop()
			result.append(node.data)
			node = node.right

# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order
def postorderIterative(root, result):
    if not root:
        return
    visited = set() #keep track  of visited nodes
    stack = []
    node = root
    while stack or node:
        if node: #node first then stack
            stack.append(node)
            node = node.left  #Go all the way to the left!!!!
        else:
            node = stack.pop()
            if node.right and not node.right in visited:  #single visit
                stack.append(node)
                node = node.right #Go all the way to the right!!!!
            else:
                visited.add(node)
                result.append(node.data)
                node = None #no right, so set to none to stop iteration


import queue
def levelOrder(root, result):
	if root is None: 
		return
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
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
				    

# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order
def postorderRecursive(root, result):
    if not root:
        return
    
    postorderRecursive(root.left, result)
    postorderRecursive(root.right, result)
    result.append(root.data)


# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order
def postorderIterative(root,result):
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
				result.append(node.data)
				#IMPORTANT: change node to None so next node can get processed
				node = None

'''
                     1
                   /  \ 
                  2     3 
                /  \   / \
               4    5  6  7

post order traversal = 4,5,2,6,7,3,1               
'''			
#Initialize Binary Tree
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)

#Traverse
result = []
#postorderRecursive(root, result)
#print("PostOrder traversal (recursive): %s" % (result))

#del result[::]
postorderIterative(root, result)
print("PostOrder traversal (Iterative): %s" % (result))

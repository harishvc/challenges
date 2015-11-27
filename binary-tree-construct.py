'''
Construct Binary tree from preorder and inorder traversal
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
	
#Construct Binary tree from pre-order and in-order traversal
#http://chaoren.is-programmer.com/posts/44859.html
def buildTree(preorder, inorder):
	if not inorder: return None # inorder is empty
	root = BinaryTree(preorder[0])
	rootPos = inorder.index(preorder[0])
	root.left = buildTree(preorder[1 : 1 + rootPos], inorder[ : rootPos])
	root.right = buildTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
	return root	
	
	
			
#Initialize Binary Tree
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)

#Traverse
print("Binary Tree 1")
preorder = []
preorderRecursive(root, preorder)
print("PreOrder traversal (recursive): %s" % (preorder))
inorder = []
inorderRecursive(root, inorder)
print("InOrder traversal (recursive): %s" % (inorder))
#
#Build Tree
print("Binary Tree 2")
root2 = buildTree(preorder,inorder)
preorder = []
preorderRecursive(root2, preorder)
print("PreOrder traversal (recursive): %s" % (preorder))
inorder = []
inorderRecursive(root2, inorder)
print("InOrder traversal (recursive): %s" % (inorder))

#Question: Find the deepest node in the binary tree


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

#Source: http://jelices.blogspot.com/2014/05/leetcode-python-maximum-depth-of-binary.html
def DeepestNode(root):
	if root == None:
		return 0
	nodeStack = [root]  #Store nodes in array
	depthStack = [1]    #Store depth of each level in array
	maxDepth = 0        #Default max depth
	DeepestNodeValue = float("-infinity")
	DeepestNodedDepth = 0
	#while len(nodeStack)>0:
	while nodeStack:	
		node = nodeStack.pop()
		depth = depthStack.pop()
		#maxDepth = max (maxDepth, depth)
		if depth > maxDepth:
			maxDepth = depth
			DeepestNodeValue = node.data
			DeepestNodedDepth = depth
		if node.left != None:
		 	nodeStack.append(node.left) #append left node
		 	depthStack.append(depth+1)  #append depth of left node
		if node.right != None:
			nodeStack.append(node.right) #append right node
			depthStack.append(depth+1)   #appaend right node depth
	return (DeepestNodeValue,DeepestNodedDepth,maxDepth)



######## Get Started!!!!!
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)
root.getLeft().getLeft().insertLeft(8)
root.getLeft().getRight().insertRight(9)
root.getLeft().getRight().getRight().insertRight(10)
root.getLeft().getRight().getRight().getRight().insertRight(11)

data,depth,maxdepth = DeepestNode(root)
print("deepest node=%d is at depth=%d, max depth of the tree=%d" % (data,depth,maxdepth))

 
#Question: Given two binary trees, return true if they are structurally identical


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
			
def areStructurullySameTrees(root1, root2):
	#Senario 1: Leaf node
	if (not root1.left) and (not root1.right) and (not root2.left) and \
		(not root2.right) and root1.data == root2.data:
		return True

    #Scenario 2: Missing any nodes? Same data?
	if (root1.data != root2.data) or (root1.left and not root2.left) or \
		(not root1.left and root2.left) or (root1.right and not root2.right) \
		or (not root1.right and root2.right): 
		return False
	
    #Scenario 3: Check left tree
	left = areStructurullySameTrees(root1.left, root2.left) if root1.left and root2.left else True
	
	#Scenario 4: Check right tree
	right = areStructurullySameTrees(root1.right, root2.right) if root1.right and root2.right else True
	
	return left and right

######## Get Started!!!!!
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)

root1 = BinaryTree(1)
root1.insertLeft(2)
root1.insertRight(3)

print ("(root,root) structurally identical? %s" % (areStructurullySameTrees(root,root)))
print ("(root,root1) structurally identical? %s" % (areStructurullySameTrees(root,root1)))

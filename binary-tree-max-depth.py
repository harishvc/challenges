#Question: Find max depth of binary tree and level than has maximum sum
from multiprocessing import Queue

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
def MaxDepthIterative(root):
	if root == None:
		return 0
	nodeStack = [root]  #Store nodes in array
	depthStack = [1]    #Store depth of each level in array
	maxDepth = 0        #Default max depth
	#while len(nodeStack)>0:
	while nodeStack:	
		node = nodeStack.pop()
		depth = depthStack.pop()
		maxDepth = max (maxDepth, depth)
		if node.left != None:
		 	nodeStack.append(node.left) #append left node
		 	depthStack.append(depth+1)  #append depth of left node
		if node.right != None:
			nodeStack.append(node.right) #append right node
			depthStack.append(depth+1)   #appaend right node depth
	return maxDepth
 
def MaxDepthRecursive(root):
	if (root == None):
		return 0 
	return max(MaxDepthRecursive(root.right),MaxDepthRecursive(root.left)) + 1  	

import queue
def FindLevelwithMaximumSum(root):
	if root is None:           #Validation
		return 0
	nodeStack = queue.Queue()  #Store nodes in a queue
	nodeStack.put(root)
	nodeStack.put("EOL")       #Add delimiter between levels  
	level=maxLevel=currentSum=maxSum= 0
	while not nodeStack.empty():	
		node = nodeStack.get()
		if (node == "EOL"):  #Level ended
			#End of level
			if (currentSum > maxSum):
				maxSum = currentSum
				maxLevel = level
			currentSum = 0
			if not nodeStack.empty():
				nodeStack.put("EOL")  #Magic!!!
				level += 1
		else:
			currentSum += node.data	
			if node.left != None:
				nodeStack.put(node.left) #append left node
			if node.right != None:
				nodeStack.put(node.right) #append right node
	return maxLevel

######## Get Started!!!!!
root = BinaryTree(5)
root.insertLeft(9)
root.insertRight(15)
root.getLeft().insertLeft(2)
root.getLeft().insertRight(4)
root.getRight().insertLeft(3)
root.getRight().insertRight(7)
root.getLeft().getLeft().insertLeft(8)
root.getLeft().getRight().insertRight(9)
root.getLeft().getRight().getRight().insertRight(10)
root.getLeft().getRight().getRight().getRight().insertRight(11)
print("Max depth of the binary tree (iterative) =",MaxDepthIterative(root))
print("Max depth of the binary tree (recursive) =",MaxDepthRecursive(root))
print("Level with maximum sum =",FindLevelwithMaximumSum(root))

 
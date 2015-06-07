#Question: Find diameter (width) of a binary tree

#Notes:
#The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree. 
#http://www.geeksforgeeks.org/diameter-of-a-binary-tree/

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
			
#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter06trees/TreeDiameter.py
def diameter(root):
	if (root == None): 
		return 0
	lHeight = height(root.left)
	rHeight = height(root.right)
	lDiameter = diameter(root.left)
	rDiameter = diameter(root.right)
	return max(lHeight + rHeight + 1, max(lDiameter, rDiameter))

# The function Compute the "height" of a tree. Height is the number f nodes along 
# the longest path from the root node down to the farthest leaf node.
def height(root):
	if (root == None) :
		return 0
	return 1 + max(height(root.left), height(root.right))


def printEdgeNodes(root, pType, cType):
   if root is None:
       return
   if pType == "root" or (pType == "left" and cType == "left") or (pType == "right" and cType == "right"):
        print (root.data)
   if root.left is None and root.right is None:
       print (root.data)
   if pType != cType and pType != "root":
       cType = "invalid"
   printEdgeNodes(root.left, cType, "left")

# def printEdgeNodes(root):
#     return printEdgeNodes(root, "root", "root")


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
print("Diameter of tree = %s" % (diameter(root)))
printEdgeNodes(root, "root", "root")

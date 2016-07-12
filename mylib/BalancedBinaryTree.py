#Balanced Binary Tree: Add, Delete, isBalanced?

class BalancedBinaryTree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def insertRight(self,node):
		self.right = node

	def insertLeft(self,node):
		self.left = node


def height(node):
	if node is None:
		return 0
	lheight = height(node.left)  + 1
	rheight = height(node.right) + 1
	print("height(%d): lheight=%d rheight=%d" % (node.data,lheight,rheight))
	return max(lheight,rheight)

def isBalancedBinaryTree(node):
	return (isBalancedBinaryTreeWrapper(node) >= 0)

#Modified post order traversal		
#Integrate height 
def isBalancedBinaryTreeWrapper(node):
	if node is None:
		return 0
	lheight = isBalancedBinaryTreeWrapper(node.left)
	rheight = isBalancedBinaryTreeWrapper(node.right)
	#Kill if height of sub-trees > 1
	if abs(lheight-rheight) > 1:
		return -1
	#return height of sub-tree
	return max(lheight,rheight) + 1

root = BalancedBinaryTree(1)
t2 = BalancedBinaryTree(2)
t3 = BalancedBinaryTree(3)
t4 = BalancedBinaryTree(4)
t5 = BalancedBinaryTree(5)
t6 = BalancedBinaryTree(6)
t7 = BalancedBinaryTree(7)
#
root.insertLeft(t2)
root.insertRight(t3)
t2.insertRight(t4)
t2.insertLeft(t7)

t4.insertLeft(t6)
t3.insertLeft(t5)

print(isBalancedBinaryTree(root))

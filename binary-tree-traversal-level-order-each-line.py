'''
Question: Print one tree level each line
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
			
#Add level for each node in the queue
#When levels change print node(s)				    
import queue
def LevelOrderPrintEachLevel(node):
	q = queue.Queue()
	q.put(node)
	level = 0 #current level
	q.put(level)
	lastPrintlevel = 0 #current print level
	result = []
	while (not q.empty()):
		new = q.get()      #get data
		newlevel = q.get() #get level
		#NEW LEVEL!!!
		if (newlevel != lastPrintlevel):
			print(result)
			del result[:]
			lastPrintlevel += 1
		result.append(new.data)
		if new.left is not None:
			q.put(new.left)
			q.put(newlevel +1)
		if new.right is not None:
			q.put(new.right)
			q.put(newlevel +1)
	print(result)  #child nodes

			
#Initialize Binary Tree
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)

#Traverse level by level
LevelOrderPrintEachLevel(root)

'''
Question: Print one tree levels each line
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
def LevelOrderPrintEachLevel(root):
	next_node = queue.Queue()   #[1,"END",2,3,"END",4,5,6,7,"END"]
	result = []                 #[1,"END",2,3,"END",4,5,6,7,"END"]
	depth = 1
	next_node.put(root)
	next_node.put("END")           #Delimited between levels
	while not next_node.empty():   #until queue is not empty
		node = next_node.get()
		if node != "END":
			result.append(node.data)
			if node.left:
				next_node.put(node.left)
			if node.right:
				next_node.put(node.right)
		else:
			if not next_node.empty():  #IMPORTANT! avoid infinite loop
				next_node.put("END")
			result.append("END")

	#print(result)  #[1,"END",2,3,"END",4,5,6,7,"END"]
	level_nodes = []
	for node_value in result:
		if node_value != "END":
			level_nodes.append(node_value)
		else:
			print(level_nodes)
			del level_nodes[::]


'''
                     1
                   /  \ 
                  2     3 
                /  \   / \
               4    5  6  7

level order traversal by depth -               
[1]
[2, 3]
[4, 5, 6, 7]
'''			

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

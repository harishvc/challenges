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
def LevelOrderPrintEachLevel(node):
	q = queue.Queue()
	current_depth = 0
	q.put(node)          #store node and depth
	q.put(current_depth) #store node and depth
	nodes_at_same_depth = []
	while not q.empty():
		new_node = q.get()  #get node and depth
		new_depth = q.get() #get node and depth
		if new_depth != current_depth:
			print(nodes_at_same_depth)
			del nodes_at_same_depth[:] #flush all values
			current_depth = new_depth #new depth
		nodes_at_same_depth.append(new_node.data)
		if new_node.left:
			q.put(new_node.left)
			q.put(current_depth+1)
		if new_node.right:
			q.put(new_node.right)
			q.put(current_depth+1)
	#print leaf nodes!
	print(nodes_at_same_depth)


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

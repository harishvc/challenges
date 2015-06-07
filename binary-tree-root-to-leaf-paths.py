#Question: Print all paths from root to leaf , given sum check if path exists

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


#Source: http://stackoverflow.com/questions/11045399/print-every-leaf-path-of-a-tree-without-recursive
class Stack(object): # just for reference
    def __init__(self):
        self.a = []

    def push(self, b):
        self.a.append(b)

    def peek(self):
        return self.a[-1]

    def pop(self):
        return self.a.pop()

    def isEmpty(self):
        return len(self.a) == 0

    def show(self):
        return self.a
       
def RLpaths(troot): # you should create your own Tree and supply the root
    current = troot
    s = Stack()
    s.push(current)
    s.push(str(current.data))
    s.push(current.data)

    while not s.isEmpty():
        pathsum = s.pop()
        path = s.pop()
        current = s.pop()

        if not current.left and not current.right:
            print('path: %s, pathsum: %d' % (path, pathsum))

        if current.right:
            rightstr = path + "->" + str(current.right.data)
            rightpathsum = pathsum * 10 + current.right.data
            s.push(current.right)
            s.push(rightstr)
            s.push(rightpathsum)

        if current.left:
            leftstr = path + "->" + str(current.left.data)
            leftpathsum = pathsum * 10 + current.left.data
            s.push(current.left)
            s.push(leftstr)
            s.push(leftpathsum)
 
def pathFinder(root, val, path, paths):
	if not root:
		return False    
	if not root.left and not root.right:
		if root.data == val:
			path.append(root.data)
			paths.append(path)
			#print(path)
			return True
		else:
			return False
	left = pathFinder(root.left, val - root.data, path + [root.data], paths)
	right = pathFinder(root.right, val - root.data, path + [root.data], paths)  
	return left or right
    #return paths
     	
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

print("Printing all paths from root to leaf")
RLpaths(root)

print ("Is 10 valid sum?",pathFinder(root,10,[],[]) )
print ("Is 15 valid sum?",pathFinder(root,15,[],[]) )
print ("Is 9 valid sum?",pathFinder(root,9,[],[]) )

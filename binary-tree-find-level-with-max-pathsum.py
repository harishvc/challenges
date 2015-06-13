#Question: Find level than has maximum sum

import sys
sys.path.append("./mylib")
import Tree

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

root = Tree.BinaryTree(5)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(2)
root.getLeft().insertRight(4)
root.getRight().insertLeft(3)
root.getRight().insertRight(7)
root.getLeft().getLeft().insertLeft(8)
root.getLeft().getRight().insertRight(9)
root.getLeft().getRight().getRight().insertRight(10)
root.getLeft().getRight().getRight().getRight().insertRight(11)
print("Level with maximum sum =",FindLevelwithMaximumSum(root))

 
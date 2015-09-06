'''
Question: Find level than has maximum sum

Algorithm:
1. Use queue to store nodes
2. Flag when nodes in a level have been processed by adding a delimiter in the queue
'''

import sys
sys.path.append("./mylib")
import Tree


import queue
def MaxSumLevel(root):
	maxsum = root.data #initialize root node has max sum
	maxlevel = 1 #initialize max level is at root
	sum = 0
	level = 2 
	nodes = queue.Queue()
	if (root.getLeft() is not None): nodes.put(root.getLeft())
	if (root.getRight() is not None): nodes.put(root.getRight())
	nodes.put("EOL") #end of level
	while not nodes.empty():
		nextNode = nodes.get()
		#"EOL" flags all nodes in a level has been processed
		#Add "EOL" to queue ONLY if there are elements in the queue!
		if (nextNode == "EOL" and not nodes.empty()):
			nodes.put("EOL")
		if (nextNode == "EOL" and sum > maxsum):
			maxsum = sum
			maxlevel = level
		if (nextNode == "EOL"):
			sum = 0 #reset sum
			level += 1
		else:				
			sum += nextNode.data
			if (nextNode.getLeft() is not None): nodes.put(nextNode.getLeft())
			if (nextNode.getRight() is not None): nodes.put(nextNode.getRight())
	return(maxsum,maxlevel)

root = Tree.BinaryTree(500)
root.insertLeft(2)
root.insertRight(30)
root.getLeft().insertLeft(2)
root.getLeft().insertRight(4)
root.getRight().insertLeft(3)
root.getRight().insertRight(7)
root.getLeft().getLeft().insertLeft(8)
root.getLeft().getRight().insertRight(9)
root.getLeft().getRight().getRight().insertRight(10)
root.getLeft().getRight().getRight().getRight().insertRight(110)
#print("Level with maximum sum =",FindLevelwithMaximumSum(root))

a,b = MaxSumLevel(root)
print("Level %d has maximum sum %d" % (b,a))
 
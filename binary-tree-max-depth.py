#Question: Find max depth of binary tree

import sys
sys.path.append("./mylib")
import Tree

#Source: http://jelices.blogspot.com/2014/05/leetcode-python-maximum-depth-of-binary.html
def MaxDepthIterative(root):
	if root == None:
		return 0
	nodeStack = [root]  #Store nodes in array
	depthStack = [1]    #Store depth of each level in array
	maxDepth = 0        #Default max depth
	while nodeStack:	
		node = nodeStack.pop()
		depth = depthStack.pop()
		maxDepth = max (maxDepth, depth)
		if node.left != None:
		 	nodeStack.append(node.left) #append left node
		 	depthStack.append(depth+1)  #append depth of left node
		if node.right != None:
			nodeStack.append(node.right) #append right node
			depthStack.append(depth+1)   #append right node depth
	return maxDepth
 
def MaxDepthRecursive(root):
	if (root == None):
		return 0 
	return max(MaxDepthRecursive(root.right),MaxDepthRecursive(root.left)) + 1  	


root = Tree.BinaryTree(5)
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
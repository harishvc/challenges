#Question: Find the deepest node in the binary tree

import sys
sys.path.append("./mylib")
import Tree

def MaxDepthNode(root):
	maxDepth = 0
	if root is None:
		return maxDepth
	nodes = []
	depth = []
	nodes.append(root) 
	depth.append(1) #root node at depth 1
	MaxDepthNode = None
	while nodes:  
		newNode =  nodes.pop()
		newDepth = depth.pop()
		if newDepth > maxDepth:
			maxDepth = newDepth
			MaxDepthNode = newNode.data
		if(newNode.left is not None):
			nodes.append(newNode.left)   #Add new node to stack
			depth.append(newDepth + 1)   #Add height of new node in stack
		if(newNode.right is not None):
			nodes.append(newNode.right)  #Add new node to stack
			depth.append(newDepth + 1)   #Add height of new node in stack
	return MaxDepthNode


root = Tree.BinaryTree(1)
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
print("deepest node=%d" % (MaxDepthNode(root)))
 

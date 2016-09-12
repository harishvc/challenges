#Construct binary tree from pre-order traversal with -1 representing None
#http://www.geeksforgeeks.org/serialize-deserialize-binary-tree/


import sys
sys.path.append("../mylib")
import Tree
import BinaryTreeTraversal

def myiterator(a):
	for i in a:
		yield i


def constructBinaryTree(node):
	if node != -1:
		root = Tree.BinaryTree(node)
		root.left = constructBinaryTree(next(nextNode))
		root.right = constructBinaryTree(next(nextNode))
		return root
	else:
		return None
 
a = [20,8,4,-1,-1,12,10,-1,-1,14,-1,-1,-1]
nextNode = myiterator(a)
root = constructBinaryTree(next(nextNode))


print("input >>>", a)
print("pre order traversal >>>")
BinaryTreeTraversal.preOrder(root)
print("")
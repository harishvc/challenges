#Find the max size of BST in a binary tree

'''
NOTES:
1. Modify post order traversal to find #BST
2. Each sub-tree will return back #of BST trees
'''
import sys
sys.path.append("./mylib")
import Tree
import BinaryTreeTraversal


#Modify post order traversal to find #BST
#Each sub-tree will return back #of BST trees
def postOrderBST(node):
	if node is None:
		return 0
	lcount = postOrderBST(node.left)
	rcount = postOrderBST(node.right)
	#print("checking ,,,", node.data)
	#case 1: BST tree!
	if node.left and node.data > node.left.data and node.right and node.data < node.right.data:
		#print("BST size", lcount + rcount +  1 )
		return lcount + rcount +  1
	#case 2: Leaf node
	elif node.left is None and node.right is None:
		#print("BST size", 1 )
		return 1
	#case 3: not BST, return max value 
	else:
		#print("BST size", max(lcount,rcount))
		return max(lcount,rcount)


root = Tree.BinaryTree(5)
root.insertLeft(2)
root.insertRight(0)
root.getLeft().insertLeft(1)
root.getLeft().insertRight(3)

print("Inorder traversal >>>")
BinaryTreeTraversal.inOrder(root)
print("")

print("Max size of BST=",postOrderBST(root))

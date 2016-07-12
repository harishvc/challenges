#Given a sorted list create a BST with minimal height

'''
NOTES:
1. TO build a balanced binary tree, root of the tree needs to the median of the sorted input
2. Left and right nodes of the root can be easily constructed from the values on the left and right of the median
'''

import sys
sys.path.append("./mylib")
import BST
import BinaryTreeTraversal
import BinaryTreeEssentials
import BalancedBinaryTree

def BalancedBST(a,start,end):
	#IMPORTANT: exit condition > (not == or <)
	if start > end:
		return None
	mid = start + (end-start)//2
	node = BST.BSTNode(a[mid])
	node.left = BalancedBST(a,start,mid-1)
	node.right = BalancedBST(a,mid+1,end)
	return node


a = [4,5,6,7,8]
root = BalancedBST(a,0,len(a)-1)

print("Input >>>", a)
print("In order traversal of new BST>>")
BinaryTreeTraversal.inOrder(root)
print("")
print("Height of new BST:", BinaryTreeEssentials.findHeight(root))
print("Is balanced?", BalancedBinaryTree.isBalancedBinaryTree(root))

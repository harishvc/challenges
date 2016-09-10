#Delete nodes outside the given range in BST
#http://www.geeksforgeeks.org/remove-bst-keys-outside-the-given-range/

import sys
sys.path.append("../mylib")
import BST
import BinaryTreeTraversal

#Pass the parent node around
#if node value > target_max remove the right sub-tree and
#if node value < target_min remove the left sub-tree
#Assumption: root node is in range!
def deleteNode(node,parent,target_min,target_max):
	if node is None:
		return 
	elif node.data < target_min:
		parent.left = node.right
		#cleanup(node)
		deleteNode(node.right,parent,target_min,target_max)
	elif node.data > target_max:
		parent.right = node.left
		#cleanup(node)
		deleteNode(node.left,parent,target_min,target_max)
	else:
		deleteNode(node.left,node,target_min,target_max)
		deleteNode(node.right,node,target_min,target_max)

#def cleanup(node):
	#remove all references

#Initialize BST
root = BST.BSTNode(6)
input = [-13,14,-8,13,7,15]
for x in input:
    BST.insert(root, BST.BSTNode(x))


print("pre order traversal >>>")
BinaryTreeTraversal.preOrder(root)
print("")

target_min = -10
target_max = 13
deleteNode(root,None,target_min,target_max)

print("pre order traversal after removing nodes outside range %d - %d >>>" % (target_min,target_max))
BinaryTreeTraversal.preOrder(root)
print("")





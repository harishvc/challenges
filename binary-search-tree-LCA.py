#Find the Lowest Common Ancestor (LCA) in a BST

import sys
sys.path.append("./mylib")
import BST
import BinaryTreeTraversal


def findLCA(node,node1,node2):
	#case 1: if value at root > node1 and node2, go left since LCA in the left subtree
	if node.data > node1.data and node.data > node2.data:
		return findLCA(node.left,node1,node2)
	#case 2: if value at root < node1 and node2, go right since LCA in the right subtree		
	elif node.data < node1.data and node.data < node2.data:
		return findLCA(node.right,node1,node2)
	#case 3: Found LCA! 
	#node1 and node2 can be on the left subtree, right subtree or either side
	return node.data

a = [3,2,1,6,5,4,7]
#Create BST
root = BST.BSTNode(a[0])
for i in range(1,len(a)):
        node = BST.BSTNode(a[i])
        BST.insert(root,node)

print("In order traversal >>")
BinaryTreeTraversal.inOrder(root)
print("")

node1 = BST.BSTNode(2)
node2 = BST.BSTNode(4)

print("LCA for nodes with values %d & %d = %d" % (node1.data,node2.data,findLCA(root,node1,node2)))
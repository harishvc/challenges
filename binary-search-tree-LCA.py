#Find the Lowest Common Ancestor (LCA) in a BST

import sys
sys.path.append("./mylib")
import BST
import BinaryTreeTraversal


#Solution 1: Recursive
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

#Solution 2: Iterative
def findLCA2(node,anode,bnode):
	while node:
		#case 1: nodes a and b on the left and right subtree
		if node.data >= anode.data and node.data <=bnode.data:
			return node.data
		#case 2: node a and b are on the left subtree
		elif node.data >= anode.data and node.data >= bnode.data:
			return node.data
		#case 3: node a and b are on the right subtree
		elif node.data <= anode.data and node.data <= bnode.data:
			return node.data
		#case 4: go left
		elif node.data >= anode.data and node.data >= bnode.data:
			node = node.left
		#case 5: go right
		else:
			node = node.right

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
print("LCA for nodes with values %d & %d = %d" % (node1.data,node2.data,findLCA2(root,node1,node2)))

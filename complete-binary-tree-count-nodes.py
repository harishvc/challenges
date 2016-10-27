#Find #nodes in a Complete Binary Tree (CBT)

'''
NOTES
1. In a CBT nodes are filled from left to right
2. If the depth of the left most node == depth of the right most node
   then #nodes is 2^h - 1 , h == height
3. if the depth of the left most node != depth of the right most node
	then find the height on the left sub tree and right sub-tree

REFERENCES
1. http://www.programcreek.com/2014/06/leetcode-count-complete-tree-nodes-java/
'''


#Solution 1: Count all the nodes. Time Complexity: O(n)


#Find depth of the left most node
def depthLeft(node):
	height = 0
	while node:
		node = node.left
		height += 1
	return height

#Find depth of the right most node
def depthRight(node):
	height = 0
	while node:
		node = node.right
		height += 1
	return height

#Solution 2: Find the depth of the left and right nodes to calculate # of nodes
#Time Complexity: O(h^2), h = height of tree
def nodesCBT(node):
	leftDepth = depthLeft(node)
	rightDepth = depthRight(node)
	if leftDepth == rightDepth:
		return 2**leftDepth -1
	else:
		#IMPORTANT: +1 to include root node of subtree
		return nodesCBT(node.left) + nodesCBT(node.right) + 1


import sys
sys.path.append("./mylib")
import Tree
import BinaryTreeTraversal


'''
             1  
            /  \
           2    3
          /  \  / \ 
         4    5 x  x
'''
#Initialize Complete Binary Tree
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
#root.getRight().insertLeft(6)
#root.getRight().insertRight(7)

print("In order traversal >>> ")
BinaryTreeTraversal.inOrder(root)
print("")

print("# nodes =", nodesCBT(root))

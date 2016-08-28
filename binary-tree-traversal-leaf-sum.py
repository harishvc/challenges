#Find sum of leaf nodes in a binary tree

#http://stackoverflow.com/questions/14392639/is-the-root-node-an-internal-node
#if there is one node, the root node and leaf node as same!
def leafSum(node):
	if node is None:
		print("node is None")
		return 0
	elif node.left is None and node.right is None:
		return node.data
	else:
		return leafSum(node.left) + leafSum(node.right)


'''
             1  
            /  \
           2    3
          /  \  / \ 
         4    5 6  7
'''

import sys
sys.path.append("./mylib")
import Tree

#Initialize Binary Tree
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)


print(leafSum(root))

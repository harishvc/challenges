#Serialize and Deserialize a Binary Tree using pre order traversal

'''
OBSERVATION:
1. Mark leaf and half nodes with "x" we can construct the tree back!
2. Space used by this technique depends on # of leaf and half nodes
3. This technique takes less space than generating tree from pre-order and in-order

REFERENCE:
http://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
'''


import sys
sys.path.append("./mylib")
import Tree
import BinaryTreeTraversal

#Mark leaf and half nodes with "x" we can construct the tree back!
def preOrderMark(node,all_nodes_with_making):
	if node is None:
		all_nodes_with_making.append("x")
	else:
		all_nodes_with_making.append(node.data)
		preOrderMark(node.left,all_nodes_with_making)
		preOrderMark(node.right,all_nodes_with_making)

#Reconstruct tree
def generateBinaryTree(n):
	node_value = next(n)
	if node_value != "x":
		node = Tree.BinaryTree(node_value)
		node.left = generateBinaryTree(n)
		node.right = generateBinaryTree(n)
		return node
	else:
		return None


'''
         input       input with markings "x"
           1          1
          /          /  \
         2          2    x
         \         / \ 
          3       x   3
                     /  \
                    x    x

pre-order = 1,2,3
pre-order with markings = 1-2-x-3-x-x-x
'''

#Build binary tree 
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.getLeft().insertRight(3)
print("pre order traversal of given tree >>>")
BinaryTreeTraversal.preOrder(root)
print("")


#step 1: Serialize
all_nodes_with_making = []
preOrderMark(root,all_nodes_with_making)
#step 2: turn results list to an iterator
n = iter(all_nodes_with_making)
#step 3: DeSerialize
root2 = generateBinaryTree(n)
print("pre order traversal of new tree >>>")
BinaryTreeTraversal.preOrder(root2)
print("")
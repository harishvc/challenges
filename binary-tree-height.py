#Question: Find the height (max depth) of the binary tree

'''
OBSERVATIONS:
- Height is the number of nodes along the longest path from the root node down to the farthest leaf node
- Height of a node = max(height of left sub-tree, right sub-tree) + 1
- Leaf node has height 1
  http://stackoverflow.com/questions/13322616/how-to-find-the-height-of-a-node-in-binary-tree-recursively/
'''

import sys
sys.path.append("./mylib")
import Tree

#max(height of left sub-tree, right sub-tree) + 1
def height(node):
	if node is None:
		return 0
	left_height = height(node.left)
	right_height = height(node.right)
	return max(left_height,right_height) + 1
	#tmp = max(left_height,right_height) + 1
	#print("node[%d] = %d" % (node.data,tmp))
	#return tmp



'''
                      1
                     /  \
                    2    3  
                  /   \
                 4     5
                /       \ 
               8         9
                          \
                           10
                            \
                            11

height@node[11] = 1
height@node[10] = 2
height@node[9]  = 3
height@node[5]  = 4
height@node[4]  = 2 
height@node[2]  = 5
height@node[3]  = 1
height@node[1]  = 6
'''
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getLeft().getLeft().insertLeft(8)
root.getLeft().getRight().insertRight(9)
root.getLeft().getRight().getRight().insertRight(10)
root.getLeft().getRight().getRight().getRight().insertRight(11)
print("height of tree = %d" % (height(root)))

#Find sum of all left left nodes

#Pass if node is on the left or right of the parent node
def leftLeafSum(node,left=None):
	if node is None:
		return 0
	elif node.left is None and node.right is None:
		#IMPORTANT: left leaf nodes!
		return node.data if left else 0
	else:
		return leftLeafSum(node.left,True)+leftLeafSum(node.right,False)

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


print(leftLeafSum(root))

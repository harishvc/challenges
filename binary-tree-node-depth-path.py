'''
Question: Find the depth (level) of a node and the path from the root
'''

import sys
sys.path.append("./mylib")
import Tree

def NodeDepthandPath(node,n1,depth,path):
	if (node is None):
		return 0 #IMPORTANT!!!	
	if (node.data == n1):
		path.append(node.data)
		return depth
	ldepth  = NodeDepthandPath(node.left, n1, depth+1,path)
	if (ldepth > 0):
		path.append(node.data)
		return ldepth
	rdepth  = NodeDepthandPath(node.right, n1, depth+1,path)
	if (rdepth > 0):
		path.append(node.data)
	return rdepth
	

root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)
root.getRight().getRight().insertRight(9)
root.getLeft().getRight().insertRight(10)
root.getRight().getRight().getRight().insertRight(11)

n1 = 11
n2 = 6

path1 = []
depth = NodeDepthandPath(root,n1,0,path1)
path1.reverse()
print("depth of node %d = %d and path from root = %s" % (n1,depth,path1))

path2 = []
depth = NodeDepthandPath(root,n2,0,path2)
path2.reverse()
print("depth of node %d = %d and path from root = %s" % (n2,depth,path2))

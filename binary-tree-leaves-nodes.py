#Question: Find number of leaves,half nodes and full nodes in a binary tree

import sys
sys.path.append("./mylib")
import Tree
        
        
fn = 0
hn = 0
leaf = 0
#Modified inorder recursive traversal using global variables
def inorderRecursive(root):
	global fn,hn,leaf
	if root is None:
		return
	if(root.getLeft() is not None and root.getRight() is not None):
		fn += 1
	elif (root.getLeft() is None and root.getRight() is None):
		leaf += 1
	else:
		hn += 1		
	if(root.getLeft() is not None):
		inorderRecursive(root.left)
	if(root.getRight() is not None):
		inorderRecursive(root.right)

#Modified inorder recursive traversal without using global variables
def inorderRecursive2(root,fn,hn,leaf):
	if(root.getLeft() is not None and root.getRight() is not None):
		fn += 1
	elif (root.getLeft() is None and root.getRight() is None):
		leaf += 1
	else:
		hn += 1		
	if(root.getLeft() is not None):
		fn,hn,leaf = inorderRecursive2(root.left,fn,hn,leaf)
	if(root.getRight() is not None):
		fn,hn,leaf = inorderRecursive2(root.right,fn,hn,leaf)
	return (fn,hn,leaf)


root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)
root.getLeft().getLeft().insertLeft(8)
root.getLeft().getRight().insertRight(9)
root.getLeft().getRight().getRight().insertRight(10)
root.getLeft().getRight().getRight().getRight().insertRight(11)

inorderRecursive(root)
print("#leaves = %d , #fullnodes = %d , #halfnodes = %d" % (leaf,fn,hn))

fn2,hn2,leaf2 =  inorderRecursive2(root,0,0,0)
print("#leaves = %d , #fullnodes = %d , #halfnodes = %d" % (leaf2,fn2,hn2))

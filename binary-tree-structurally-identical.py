#Question: Given two binary trees, return true if they are structurally identical

import sys
sys.path.append("./mylib")
import Tree
			
def CheckIdentical(t1,t2):
	#condition1: both nodes are empty
	if (t1 is None and t2 is None):
			return True
	#condition 2: one of the nodes is empty
	elif( t1 is None or t2 is None):
			return False
	#condition 3: data does not match
	elif( t1.getData() != t2.getData()):
			return False
	#condition 4: check for subnodes	
	else:
		return CheckIdentical(t1.getLeft(),t2.getLeft()) and  CheckIdentical(t1.getRight(),t2.getRight())



root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)

root1 = Tree.BinaryTree(1)
root1.insertLeft(2)
root1.insertRight(3)

print ("(root,root) structurally identical? %s" % (CheckIdentical(root,root)))
print ("(root,root1) structurally identical? %s" % (CheckIdentical(root,root1)))

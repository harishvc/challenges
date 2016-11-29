#Question: Given two binary trees, return true if they are structurally identical

'''
OBSERVATION:
* left and right sub-trees are arranged in the exactly same way (no value comparison)
'''

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
	else:
		return CheckIdentical(t1.getLeft(),t2.getLeft()) and  CheckIdentical(t1.getRight(),t2.getRight())


'''
           root                      root1
               1                       1   
             /   \                   /   \
            2     3                 4     5

'''
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)

root1 = Tree.BinaryTree(1)
root1.insertLeft(4)
root1.insertRight(5)

print ("(root,root1) structurally identical? %s" % (CheckIdentical(root,root1)))

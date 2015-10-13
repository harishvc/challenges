'''
Question: Given two binary trees T1 and T2, check if T2  is a subset of T1.

Conversation topics:
1. How large is the binary tree?
2. Are there duplicate values?
3. Memory constraints?
4. Space constraints?
'''

'''
Solution 1: 

Algorithm:
Step 1: Find pre-order and in-order path for T1
 - If DUPLICATES values then insert NULL if left or right node is not there 
Step 2: Find pre-order and in-order path for T2
 - If DUPLICATES values then insert NULL if left or right node is not there 
Step 3: Check if pre-order and in-order path of T1 is a subset of T2

Space Complexity: O(m+n),  m=#nodes in T1 & n=#nodes in T2
Time Complexity: O (m+n)
'''

'''
Solution 2: 

Algorithm: Recursively iterate T1 and value matches T2 (root) then check for subset
Important Factors: 
1. T2 is small than T1. 
2. #T2 nodes to keep track of end of T2
Time complexity: O(m+n) ..... O(m*n) if there are multiple nodes with similar values
'''

import sys
sys.path.append("./mylib")
import Tree
			
def CheckSubset(T1,T2,size):
	count = size
	if (T1 is None):
		return False
	if(T2 is None):
		return True
	#Modified CheckIndentical to handle small T2
	def CheckIdentical(t1,t2):
		nonlocal count #Python3
		#condition 1: both nodes are empty
		if (t1 is None and t2 is None):
			return True
		#condition 2: one of the nodes is empty
		elif( t1 is None or t2 is None):
			return False
		#condition 3: data does not match
		elif( t1.getData() != t2.getData()):
			return False
		#condition 4: check for sub-nodes	
		else:
			if(count > 0):
				count -=1
				if(CheckIdentical(t1.getLeft(),t2.getLeft())):
					return True
			if(count > 0):
				count -=1
				if(CheckIdentical(t1.getRight(),t2.getRight())):
					return True
			return False

	if (T1.getData() == T2.getData() and CheckIdentical(T1,T2)):
		return True
	count = size #reset size
	return (CheckSubset(T1.getLeft(),T2,size) or CheckSubset(T1.getRight(),T2,size))
	

root = Tree.BinaryTree(1)
root.insertLeft(1)
root.insertRight(3)
root.getLeft().insertLeft(2)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)

root1 = Tree.BinaryTree(1)
root1.insertLeft(2)

print ("(root,root1) structurally identical? %s" % (CheckSubset(root,root1,2)))

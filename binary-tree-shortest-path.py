'''
Question: Find the shortest path between two nodes in a binary tree

Algorithm: :bulb: :rocket:
1. Modify Lowest Common Ancestor (LCA) and gather path 
   1.1 Detailed explanation with picture http://codereview.stackexchange.com/questions/83567/finding-common-ancestor-in-a-binary-tree
2. Return left path + LCA + find right path
'''

import sys
sys.path.append("./mylib")
import Tree

#Source: http://codereview.stackexchange.com/questions/83567/finding-common-ancestor-in-a-binary-tree
#Modify LCA to capture the left and right path
#Iterate through the left and right path to construct the shortest path
def LCAModified(n1, n2, head):
	count = 0   # How many nodes in {n1, n2} have been visited so far?
	ancestor = False
	left_path = []
	right_path = []
	def traverse(node,left_path,right_path):
		nonlocal count, ancestor #Python3
		if node is None or ancestor is True: return
		count_at_entry = count
		if node.data == n1: 
			count += 1
		if node.data == n2: 
			count += 1
		traverse(node.getLeft(),left_path,right_path)
		traverse(node.getRight(),left_path,right_path)
		#left path: count_at_entry=0, count=1
		if(count_at_entry == 0 and count == 1):
			left_path.append(node.data)
		#right path: count_at_entry=1, count=2
		elif(count_at_entry == 1 and count == 2):
			right_path.append(node.data)
		#lcr: count_at_entry=0, count=2				
		if count_at_entry == 0 and count == 2 and ancestor is False:
			ancestor = True
			#lcr
			right_path.append(node.data)
	traverse(head,left_path,right_path)
	return FindShortestPath(left_path,right_path)

#TODO: Use linked list instead of list
def FindShortestPath(p1,p2):
	i = len(p1)-1
	j = len(p2)-1
	LCA = []
	while(p1[i] == p2[j] and i>=0 and j >=0):
		i -= 1
		j -= 1
	#left path
	left_path = p1[:i+1]
	#LCA
	if(i+1 <= len(p1)-1):
		LCA.append(p1[i+1])
	#right path
	right_path = p2[:j+1]
	right_path.reverse()
	return(left_path + LCA + right_path)


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


n1 = 2
n2 = 3
nodes = [[2,3],[6,11],[11,2]]
for input in nodes:
	print("Shortest path between nodes %d and %d = %s" % (input[0],input[1],LCAModified(input[0],input[1],root)))

'''
Question: Find the shortest path between two nodes in a binary tree

Solution 2:
Algorithm: http://stackoverflow.com/questions/2134583/looking-for-fast-algorithm-to-find-distance-between-two-nodes-in-binary-tree
1. Find depth of n1 and the path from root as p1
2. Find depth of n2 and the path from root as p2
3. Iterate through p1 and p2 until they are not equal

Notes: Store paths from root in a linked list with length instead of list
'''

import sys
sys.path.append("./mylib")
import Tree

#Given a node value find the depth (level) and path from root
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
	
#Prune paths to remove all ancestor nodes	
#Smallest path = left path + LCA + reverse(right path)
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

nodes = [[2,3],[6,11],[2,11]]
for input in nodes:
	path1 = []
	NodeDepthandPath(root,input[0],0,path1)
	path2 = []
	NodeDepthandPath(root,input[1],0,path2)
	result = FindShortestPath(path1,path2)
	print("Shortest path from %d to %d = %s" %(input[0],input[1],result))	
'''
Question: Find all possible combinations that can generate identical Binary Search Tree (BST)

Algorithm:
1.Using pre order traversal
  a. Find all nodes on the left subtree 
  b. Find all nodes on the right subtree
2. Weave values from left nodes and right nodes to generate new lists 
   such that the relative positions are SAME . 
   Example: 3,1,2,4,5  . Here 3 is root, 1,2 are values in the left sub-tree and 4,5 are values in the right sub-tree
   - 1 will be always before 2
   - 5 will be always after 4
'''


#combinations = m*n
# m = # of elements in a
# n - # elements in b
def merge(a,root,frontB,backB):
	for i in range(0,len(a)):
		frontA = a[0:i+1]
		backA = a[i+1:]
		print(root+frontA+frontB+backA+backB)


a = [1,2]    #left sub-tree values
b = [4,5,6]  #right sub-tree values
root = [3]   #root node


#merge values from right with left
for i in range(0,len(a)):
	merge(b,root,a[0:i+1],a[i+1:])

#merge values from left with right
for i in range(0,len(b)):
	merge(a,root,b[0:i+1],b[i+1:])


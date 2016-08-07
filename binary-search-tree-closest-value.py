'''
Question: In a BST given target find a value close to the target

REFERENCE:
1. http://stackoverflow.com/questions/6209325/how-to-find-the-closest-element-to-a-given-key-value-in-a-binary-search-tree
'''

import sys
sys.path.append("./mylib")
import BST

#Create BST
root = BST.BSTNode(4)
input = [3,2,1,5,10,7,6,9,12,15]
for x in input:
    BST.insert(root, BST.BSTNode(x))


def  ClosestValue(node,target,result):
	while node:
		#find closest node
		if node.data == target:
			return node.data
		elif abs(target-node.data) < abs(target-result):
			#new closest node
			result = node.data
		#go left or right?
		if node.data > target:
			node = node.left
		else:
			node = node.right
	return result

target = 8
print("Value close to ", target, " = ", ClosestValue(root,target,root.data))


'''
Question: Find the ancestors of a node in a binary tree

Algorithm: :bulb: :rocket:
1. Detailed explanation with picture http://codereview.stackexchange.com/questions/83567/finding-common-ancestor-in-a-binary-tree
2. Check count (nonlocal variable) at the entry and exit of the recursive function
3. Only ancestor nodes have the property where count is 0 on entry and 2 on exit!

Python3: nonlocal :notes:
The nonlocal statement causes the listed identifier to refer to previously 
bound variables in the nearest enclosing scope excluding globals

'''

import sys
sys.path.append("./mylib")
import Tree

#Source: http://codereview.stackexchange.com/questions/83567/finding-common-ancestor-in-a-binary-tree
def common_ancestor(n1, head):
	count = 0   # How many nodes in {n1, n2} have been visited so far?
	result = []
	def traverse(node):
		nonlocal count, result #Python3
		if node is None: return
		count_at_entry = count
		if node.data is n1: count += 1
		traverse(node.getLeft())
		traverse(node.getRight())
		if count_at_entry == 0 and count == 1 and n1 != node.data:
			result.append(node.data)
	traverse(head)
	return result


root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)


n1 = 4
print("Ancestors of nodes %d = %s" % (n1,common_ancestor(n1, root)))
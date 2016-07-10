'''
Question: Find the Lowest (nearest/first) Common Ancestor (LCA) of two nodes in a binary tree
          Each node had child, left and right node(s)  
           
Algorithm: :bulb: :rocket:
0. Traverse down from root to child - pre order traversal!
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
#Notes :notes:
#if we keeps track of how many of n1 and n2 have been visited so far on entry and and exit of each node
#Common ancestors of the two nodes have count = 0 on entry and count = 2 on exit
def common_ancestor(n1, n2, head):
	count = 0   # How many nodes in {n1, n2} have been visited so far?
	ancestor = None
	def traverse(node):
		nonlocal count, ancestor #Python3
		if node is None or ancestor is not None: return
		count_at_entry = count
		if node.data is n1: count += 1
		if node.data is n2: count += 1
		traverse(node.getLeft())
		traverse(node.getRight())
		if count_at_entry == 0 and count == 2 and ancestor is None:
			ancestor = node
	traverse(head)
	return ancestor.data


#Solution 2 (modified solution 1)
#Taking advantage of recursion
def findLCA(node,v1,v2,count,result):
    if node is None:
        return count,result
    count_entry = count
    if(node.data == v1): count += 1
    if(node.data == v2): count +=  1
    count,result = findLCA(node.left,v1,v2,count,result)
    count,result = findLCA(node.right,v1,v2,count,result)
    if(count_entry == 0 and count == 2 and result is None):
        #print(node.data)
        result = node.data
    return count,result


root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)


n1 = 4
n2 = 6
print("Nearest common ancestor to nodes %d and %d = %s" % (n1,n2,common_ancestor(n1, n2, root)))

a,b = findLCA(root,n1,n2,0,None)
print("LCA(6,4)=",b)

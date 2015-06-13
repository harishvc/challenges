#Question: Find number of leaves,half nodes and full nodes in a binary tree

import sys
sys.path.append("./mylib")
import Tree
import queue

def levelOrder(root):
	if root is None: 
		return
	nleaves = 0 #number of leaves
	nfullnodes = 0 #number of full nodes
	nhalfnodes = 0 #number of half nodes
	q = queue.Queue()       
	q.put(root)
	n = None
	while not q.empty():
		n = q.get()  #dequeue FIFO
		#Is this node a leaf?
		if(n.left == None and n.right == None):
			nleaves += 1
		#Is this node a full node?
		if(n.left and n.right):
			nfullnodes += 1	
		#Is this node a half node?
		if ((n.left and not n.right) or (n.right and not n.left)):
			nhalfnodes += 1
		if n.left is not None:
			#print("traversing left ..",n.left.getData())
			q.put(n.left)
		if n.right is not None:
			#print("traversing right ..",n.right.getData())
			q.put(n.right)  
	return (nleaves,nfullnodes,nhalfnodes)		

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
nleaves,nfullnodes,nhalfnodes= levelOrder(root)
print("#leaves = %d , #fullnodes = %d , #halfnodes = %d" % (nleaves,nfullnodes,nhalfnodes))

 
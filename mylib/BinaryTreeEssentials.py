#Binary Tree Essentials

#find height of the tree - length of the longest path from the leaf to the root, #nodes
def findHeight(node):
	if node is None:
		return 0
	lheight = findHeight(node.left)
	rheight = findHeight(node.right)
	return max(lheight,rheight) + 1

#Maximum(Diameter of left sub­tree, Diam­e­ter of right sub­tree, Longest path between two nodes which passes through the node)
#Naive solution: O(n^2) (since we are calculating the height seperately)
def findDiameter1(node):
	if node is None:
		return 0
	dleftTree = findDiameter1(node.left)
	drightTree = findDiameter1(node.right)
	LongestPath = findHeight(node.left) + findHeight(node.right) + 1
	return max( dleftTree, drightTree,LongestPath)

#Optimized solution to find diameter and height together
def findDiameter2(node):
	if node is None:
		return 0,0
	dleftTree, hleftTree = findDiameter2(node.left)
	drightTree,hrightTree = findDiameter2(node.right)
	LongestPath = hleftTree + hrightTree + 1
	return  max(dleftTree, drightTree,LongestPath),  max(hleftTree,hrightTree)+1

#Find max value in a Binary Tree
def findMax(node,nmax):
	if node is None:
		return nmax
	if nmax is None:
		nmax = node.data
	elif node.data > nmax:
		nmax = node.data
	lmax = findMax(node.left,nmax)
	rmax = findMax(node.right,nmax)
	#print("node=%d lmax=%d rmax=%d" % (nmax,lmax,rmax))
	return max(nmax,lmax,rmax)


def isLeaf(node):
    if (node.getLeft() is None and  node.getRight() is None):
        return True
    else:
        return False


#Find all path and sum
#Modified post order traversal
def findPathSum(node,path,psum):
	if node is None:
		return
	path.append(node.data)
	psum += node.data
	findPathSum(node.left,path,psum)
	findPathSum(node.right,path,psum)
	#Important: Path ends in a leaf!
	if node.left is None and node.right is None:
		print(path, psum)
	#Important: pop and remove value on the way back!
	path.pop()
	psum -= node.data

#Clone tree
#Modified pre order traversal
def cloneBT(node):
	if node is None:
		return
	newNode = BinaryTree(node.data)
	newNode.left = cloneBT(node.left)
	newNode.right = cloneBT(node.right)
	return newNode 

#Deepest node: Level order traversal

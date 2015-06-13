#Question: Given two binary trees, return true if they are structurally identical

import sys
sys.path.append("./mylib")
import Tree
			
def areStructurullySameTrees(root1, root2):
	#Senario 1: Leaf node
	if (not root1.left) and (not root1.right) and (not root2.left) and \
		(not root2.right) and root1.data == root2.data:
		return True

    #Scenario 2: Missing any nodes? Same data?
	if (root1.data != root2.data) or (root1.left and not root2.left) or \
		(not root1.left and root2.left) or (root1.right and not root2.right) \
		or (not root1.right and root2.right): 
		return False
	
    #Scenario 3: Check left tree
	left = areStructurullySameTrees(root1.left, root2.left) if root1.left and root2.left else True
	
	#Scenario 4: Check right tree
	right = areStructurullySameTrees(root1.right, root2.right) if root1.right and root2.right else True
	
	return left and right

root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)

root1 = Tree.BinaryTree(1)
root1.insertLeft(2)
root1.insertRight(3)

print ("(root,root) structurally identical? %s" % (areStructurullySameTrees(root,root)))
print ("(root,root1) structurally identical? %s" % (areStructurullySameTrees(root,root1)))

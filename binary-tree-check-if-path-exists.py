#Question: Given path sum check if the path exists

import sys
sys.path.append("./mylib")
import Tree
        
def pathFinder(root, val, path, paths):
	if not root:
		return False    
	if not root.left and not root.right:
		if root.data == val:
			path.append(root.data)
			paths.append(path)
			return True
		else:
			return False
	left = pathFinder(root.left, val - root.data, path + [root.data], paths)
	right = pathFinder(root.right, val - root.data, path + [root.data], paths)  
	return left or right
     	
######## Get Started!!!!!
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
print ("Is 10 valid sum?",pathFinder(root,10,[],[]) )
print ("Is 15 valid sum?",pathFinder(root,15,[],[]) )
print ("Is 9 valid sum?",pathFinder(root,9,[],[]) )

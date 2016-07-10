#Question: Delete a node from Binary Search Tree(BST)


import sys
sys.path.append("./mylib")
import BinaryTreeTraversal 
import BST

a = [3,2,1,5,5,4,7]
#Create BST
root = BST.BSTNode(a[0])
for i in range(1,len(a)):
	node = BST.BSTNode(a[i])
	BST.insert(root,node)



print("Tree in-order traversal:")
BinaryTreeTraversal.inOrder(root)

#Time Complexity: O(logn), since only branch of a tree is processed
#Delete node from BST
print("\ndeleting node.data=", 3)
root = BST.delete(root,BST.BSTNode(3))

print("Tree in-order traversal:")
BinaryTreeTraversal.inOrder(root)
print("")


#Largest Kth value  in BST

import sys
sys.path.append("./mylib")
import BST
import BinaryTreeTraversal

a = [3,2,1,6,5,4,7]
#Create BST
root = BST.BSTNode(a[0])
for i in range(1,len(a)):
        node = BST.BSTNode(a[i])
        BST.insert(root,node)

#reverse inorder
def rinorder(node,k,result):
	if node is None:
		return
	#go right - largest value is on the right	
	rinorder(node.right,k,result)
	if len(result) < k:
		result.append(node.data)
	if len(result) == k:
		return
	#go left - next largest value is on the left node of the right most node	
	rinorder(node.left,k,result)


print("In order traversal >>")
BinaryTreeTraversal.inOrder(root)
print("")

k= 4
result=[]
rinorder(root,k,result)
#print(result)
print("%dth largest value=%d" %(k,result[-1]))

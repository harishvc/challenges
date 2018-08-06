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

#Reverse in order traversal to get values in descending order
#solution #1
def largestK(node,K):
    if node and K > 0:
        K = largestK(node.right,K)
        if K > 0:
            print(node.data)
            K = K- 1
        K = largestK(node.left,K)
        #Important: return K
        return K
    else:
        #Important: return K
        return K

#solution #2
def largek(node,results,k):
    if node and len(results) <k:
        if node.right:
            largek(node.right,results,k)
        results.append(node.data)
        largek(node.left,results,k)

print("In order traversal >>")
BinaryTreeTraversal.inOrder(root)
print("")


k= 2
#solution #1
print(k, "largest:")
# largestK(root,k)

#solution #2
results = []
size = 0
largek(root,results,k)
print(results[k-1])
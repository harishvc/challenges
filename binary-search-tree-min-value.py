'''
Question: Find min value of Binary Search Tree(BST)

Min value is the left most leaf
'''

class BinarySearchTree:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)


#Ascending order of elements
def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data,end=" ")
    inOrderTraversal(root.right)
    

def minValue(node):
    if node.left:
        return minValue(node.left)
    else:
        return node.data        
 
        
input = [12,5,17,3,7,13,19,1,9,14,20,8,11,18]
root = BinarySearchTree(input[0])
#Create BST
for x in input[1:]:
    insertNode(root,BinarySearchTree(x))

#Print tree
print("Inorder traversal of BST >>> ",end="")
inOrderTraversal(root)
print("")

print("Max value =", minValue(root))


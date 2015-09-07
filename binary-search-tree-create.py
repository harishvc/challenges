'''
Question: Convert a list into Binary Search Tree(BST)

Time Complexity: O(nlogn), log n for each insert
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
    
    
input = [15,10,20,21,8,12,7,19,11,17,14,16,18]
root = BinarySearchTree(input[0])

#Create BST
for x in input[1:]:
    insertNode(root,BinarySearchTree(x))

#Print tree
print("Inorder traversal of BST >>> ",end="")
inOrderTraversal(root)
print("")


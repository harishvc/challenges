'''
Question: Delete a node from Binary Search Tree(BST)

Time Complexity: O(logn), since only branch of a tree is processed
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
#Source: http://stackoverflow.com/questions/11392773/deletion-in-binary-search-tree-with-parent-pointers
#Reference: https://www.youtube.com/watch?v=gcULXE7ViZw
def delete(x,T):
    #Condition 1: Value does not exist in the tree
    if T is None:
        print('Element Not Found')
    #Condition 2: Value is less, go right    
    elif x<T.data:
        T.left = delete(x,T.left)
    #Condition 3: Value is more, go left    
    elif x>T.data:
        delete(x,T.right)
    #Condition 4: Found node to delete and node is full node    
    elif T.left and T.right:
        TempNode = findMinNode(T.right)
        T.data = TempNode.data
        T.right = delete(TempNode.data,T.right)
    #Condition 5: Found node to delete and node is half node or leaf
    else:
        if T.left is None:
            T = T.right
        elif T.right is None:
            T = T.left
    return T

def findMinNode(root):
    if root.left:
        return findMinNode(root.left)
    else:
        return root


#Ascending order of elements
def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data,end=" ")
    inOrderTraversal(root.right)
    
    
#input = [15,10,20,21,8,12,7,19,11,17,14,16,18]
input = [12,5,17,3,7,13,19,1,9,14,20,8,11,18]

root = BinarySearchTree(input[0])

#Create BST
for x in input[1:]:
    insertNode(root,BinarySearchTree(x))

#Print tree
print("Inorder traversal of BST >>> ",end="")
inOrderTraversal(root)
print("")
print("####################")

#Delete leaf node
print("Deleting leaf node 1")
delete(1,root)
print("Inorder traversal of new BST >>> ",end="")
inOrderTraversal(root)
print("")
print("####################")

#Delete half node
print("Deleting half node 13")
delete(13,root)
print("Inorder traversal of new BST >>> ",end="")
inOrderTraversal(root)
print("")
print("####################")


#Delete full node
print("Deleting full node 17")
delete(17,root)
print("Inorder traversal of new BST >>> ",end="")
inOrderTraversal(root)
print("")
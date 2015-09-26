'''
Question: Given a sorted list create a BST with minimal height

Time Complexity: O(nlogn), log n for each insert
'''

class BinarySearchTree:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

#BST insert
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
    #return root

#Find BST height
def height(root):
    if (root == None) :
        return 0
    x = height(root.left)
    y = height(root.right)
    z = max(x,y) + 1
    return z

#Ascending order of elements
def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data,end=" ")
    inOrderTraversal(root.right)

#Algorithm  :idea:
#1.Find median of list, insert median
#  1.1 Go left of median
#  1.2 Go right of median
def BSTMinimalHeight(node,input,start,end):
    if (end < start):
        return None
    median = (start + end) // 2   #floor
    MedianNode = BinarySearchTree(input[median])
    insertNode(node,MedianNode)
    #go left of median
    BSTMinimalHeight(MedianNode,input,start,median-1)
    #go right of median
    BSTMinimalHeight(MedianNode,input,median+1,end)
    return MedianNode
    
    
    
input = [1,2,3,4,5]
root = BSTMinimalHeight(None,input,0,len(input)-1)

print("input >>>", input)
print("Inorder traversal of BST >>> ",end="")
inOrderTraversal(root)
print("")
print("Height =", height(root))
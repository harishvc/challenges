'''
Question: Given a Binary Search Tree (BST) and a range, count number of nodes that lie in the given range

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
            

def BSTRange(root,start,end):
    #Condition 1
    if(root is None):
        return 0
    if(root.data >= start and root.data <= end):
        return(  BSTRange(root.right,start,end) + BSTRange(root.left,start,end) + 1)
    #Condition 2
    elif (root.data < start):
        return(BSTRange(root.right,start,end))
    #Condition 3
    elif (root.data == start):
        return(BSTRange(root.right,start,end) + 1)
    #Condition 4
    elif (root.data > end):
        return(BSTRange(root.left,start,end))
    #Condition 5
    elif (root.data == end):
        return(BSTRange(root.left,start,end) + 1)
 
 
input = [12,5,17,3,7,13,19,15,9,14,20,8,11,18]
root = BinarySearchTree(input[0])
#Create BST
for x in input[1:]:
    insertNode(root,BinarySearchTree(x))

#Print tree
print("Inorder traversal of BST >>> ",end="")
inOrderTraversal(root)
print("")

start = 1
end = 10
print("#nodes in range(%d,%d) = %d" % (start,end,BSTRange(root,start,end)) )


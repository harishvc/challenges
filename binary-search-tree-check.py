'''
Question: Check if a BST is valid

Properties to check:
1. max value of left sub-tree is smaller than current node data
2. min value of right sub tree is greater than current node data
'''

class BSTNode:
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
    
def ValidBST(root):
    #Condition 1: return true if no node found
    if root == None:
        return True
    
    #Condition 2: false if the max of the left is > than root 
    elif(root.left != None and (root.left.data > root.data)):
       return False

    #Condition 3: false if the min of the right is <= than root 
    elif(root.right != None and (root.right.data < root.data)):
       return False
   
    #Condition 4: check left and right node
    else:
        return (ValidBST(root.left) and ValidBST(root.right))

#Create BST
root = BSTNode(4)
insertNode(root, BSTNode(3))
insertNode(root, BSTNode(2))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(5))
#Valid BST?
print ("BST valid?", ValidBST(root))

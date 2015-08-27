#Question: Check if a BST is valid

#Properties to check
#max value of left sub-tree is smaller than current node data
#min value of right sub tree is greater than current node data

#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter06trees/IsBST.py

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


def inorderIterative(root, result):
    if not root:
        return
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
            
def FindMin(root):
    """ return the minimum node in the current tree and its parent """
    # we use an ugly trick: the parent node is passed in as an argument
    # so that eventually when the leftmost child is reached, the 
    # call can return both the parent to the successor and the successor
    if root.left:
        return FindMin(root.left)
    else:
        return root

#Right most node that does not have a right child        
def FindMax(root):
    if root.right:
        return FindMax(root.right)
    else:
        return root
    
#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter06trees/IsBST.py
#max value of left sub-tree is smaller than current node data
#min value of right sub tree is greater than current node data
# Returns true if a binary tree is a binary search tree 
def IsBST3(root):
    if root == None:
        return True
    
    # false if the max of the left is > than root 
    elif(root.left != None and (root.left.data > root.data)):
       return False

    # false if the min of the right is <= than root 
    elif(root.right != None and (root.right.data < root.data)):
       return False

    # false if, recursively, the left or right is not a BST 
    #if(not IsBST3(root.left) or not IsBST3(root.right)): 
       #return False

    
    # passing all that, it's a BST 
    #return True
    else:
        return (IsBST3(root.left) and IsBST3(root.right))

#Create BST
root = BSTNode(4)
insertNode(root, BSTNode(3))
insertNode(root, BSTNode(2))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(5))
result = []
inorderIterative(root, result)
result = IsBST3(root)
print ("BST valid?", result)

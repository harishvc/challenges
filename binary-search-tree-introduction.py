#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter06trees/BST.py

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

def deleteNode(root, data):
	""" delete the node with the given data and return the root node of the tree """	    
	if root.data == data:
		# found the node we need to delete
		if root.right and root.left: 
			# get the successor node and its parent 
			[psucc, succ] = findMin(root.right, root)
			# splice out the successor
			# (we need the parent to do this) 
			if psucc.left == succ:
				psucc.left = succ.right
			else:
				psucc.right = succ.right					
			# reset the left and right children of the successor
			succ.left = root.left
			succ.right = root.right
			return succ                
		else:
			# "easier" case
			if root.left:
				return root.left  # promote the left subtree
			else:
				return root.right  # promote the right subtree 
	else:
		if root.data > data:  # data should be in the left subtree
			if root.left:
				root.left = deleteNode(root.left, data)
			# else the data is not in the tree 
		else:  # data should be in the right subtree
			if root.right:
				root.right = deleteNode(root.right, data)
	return root

#Left most node that does not have a left child
def findMin(root):
	""" return the minimum node in the current tree and its parent """
	# we use an ugly trick: the parent node is passed in as an argument
	# so that eventually when the leftmost child is reached, the 
	# call can return both the parent to the successor and the successor
	if root.left:
		return findMin(root.left)
	else:
		return root.data

#Right most node that does not have a right child        
def findMax(root):
    if root.right:
        return findMax(root.right)
    else:
        return root.data        

#Ascending order of elements
def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data,end="  ")
    inOrderTraversal(root.right)

def preOrderTraversal(root):
    if not root:
        return        
    print(root.data,end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)    

def postOrderTraversal(root):
    if not root:
        return        
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)    
    print(root.data,end=" ")

#Create BST
root = BSTNode(13)
insertNode(root, BSTNode(20))
insertNode(root, BSTNode(12))
insertNode(root, BSTNode(5))
insertNode(root, BSTNode(20))
insertNode(root, BSTNode(20))
#Print tree
print("Inorder traversal of BST >>> ",end="")
inOrderTraversal(root)
print("")
print("Preorder traversal of BST >>> ",end="")
preOrderTraversal(root)
print("")
print("Postorder traversal of BST >>> ",end="")
postOrderTraversal(root)
print("")

#Minimum element
print("Minimum value in BST",findMin(root))
#Maximum element
print("Maximum value in BST",findMax(root))


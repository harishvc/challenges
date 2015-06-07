#Question: Find smallestK and largestK in BST

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


#Left most node that does not have a left child
def findMin(root, parent):
	""" return the minimum node in the current tree and its parent """
	# we use an ugly trick: the parent node is passed in as an argument
	# so that eventually when the leftmost child is reached, the 
	# call can return both the parent to the successor and the successor
	if root.left:
		return findMin(root.left, root)
	else:
		return [parent, root]

#Right most node that does not have a right child        
def findMax(root, parent):
    if root.right:
        return findMax(root.right, root)
    else:
        return [parent, root]        

#Find K smallest
def inorderIterativeK(root,k):
    if not root:
        return
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node) 
            node = node.left   #all the way to the left
        else:
            if (len(stack) >= abs(k)):       #check if condition is true
                return stack.pop(k)
            else:
                node = stack.pop()
                node = node.right  #all the way to the right


#Find K greatest
#Modified inorder starting from right
def inorderIterativeRightFirstK(root,k):
    if not root:
        return
    stack = []
    node = root
    sorted = []
    counter = 0
    while stack or node:
        if node:
            stack.append(node)
            sorted.append(node)
            counter += 1 #Increment counter
            node = node.right   #all the way to the right
        else:
            if (counter >= abs(k)):
                if (len(stack) >= abs(k)):   #Handle right side of tree
                    return sorted.pop(k)
                else:
                    return sorted.pop()
            else:
                node = stack.pop()
                node = node.left  #all the way to the left
                                    

#Create BST
root = BSTNode(4)
insertNode(root, BSTNode(3))
insertNode(root, BSTNode(2))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(5))
print("Smallest element in BST >>> ",inorderIterativeK(root,-1).data)
print("2nd smallest element in BST >>> ",inorderIterativeK(root,-2).data)
print("3rd smallest element in BST >>> ",inorderIterativeK(root,-3).data)

#####TODO
print("Largest element in BST >>> ",inorderIterativeRightFirstK(root,-1).data)
print("2nd largest element in BST >>> ",inorderIterativeRightFirstK(root,-2).data)
print("3rd largest element in BST >>> ",inorderIterativeRightFirstK(root,-3).data)
print("4th largest element in BST >>> ",inorderIterativeRightFirstK(root,-4).data)
print("5th largest element in BST >>> ",inorderIterativeRightFirstK(root,-5).data)

'''
Question: Check if a binary tree is a fully balanced binary tree

Fully balanced tree is defined as a tree such that the height of the two subtrees of any node never differ by more than one.

'''
'''
Question: Check if a binary tree is symmetric. 
'''

'''Binary Tree Class and its methods'''
class BinaryTree:
    def __init__(self, data):
        self.data = data  # root node
        self.left = None  # left child
        self.right = None  # right child
    # set data
    def setData(self, data):
        self.data = data
    # get data   
    def getData(self):
        return self.data    
    # get left child of a node
    def getLeft(self):
        return self.left
    # get right child of a node
    def getRight(self):
        return self.right
    # get left child of a node
    def setLeft(self, left):
        self.left = left
    # get right child of a node
    def setRight(self, right):
        self.right = right
    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp
    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp

#Find BST height
def height(root):
    if (root is None):
        return 0
    x = height(root.left)
    y = height(root.right)
    z = max(x,y) + 1
    print("Node(%d) height=%d" % (root.data,z))
    return z

#Solution 1
#Algorithm: Check height of left sub-tree and right-subtree recursively
#Time complexity: inefficient since nodes are visited more than once
def CheckBalanced(node):
    if (node is None):
        return True
    print("comparing .... L & R", node.data)
    if (height(node.getLeft()) - height(node.getRight()) <= 1):
        #return (CheckBalanced(node.getLeft()) and CheckBalanced(node.getRight())) 
        return True
    else:
        return False

#Solution 2: Modified height to check if nodes are balanced with 3 possible return values (-1, 0 , 1)
#return -1 if unbalanced
#return 1 if balanced
#return 0 if None
def HeightBalanced(node):
    if (node is None):
        return 0
    x = HeightBalanced(node.left)
    y = HeightBalanced(node.right)
    if (x < 0 or y < 0 or abs(x-y) > 1):
        return -1
    else:
        return 1
    

import queue
def levelOrder(root, result):
    q = queue.Queue()       
    q.put(root)
    n = None
    while not q.empty():
        n = q.get()  #dequeue FIFO
        #print(n.getData())
        result.append(n.getData())
        if n.left is not None:
            #print("traversing left ..",n.left.getData())
            q.put(n.left)
        if n.right is not None:
            #print("traversing right ..",n.right.getData())
            q.put(n.right)  
                    
#Initialize Binary Tree
root = BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)
#root.getRight().getRight().insertLeft(8)
#root.getRight().getRight().getLeft().insertLeft(9)

#Traverse
result = []
levelOrder(root, result)
print("LevelOrder traversal: %s" % (result))

#Solution 1    
#print("Is the binary tree balanced? " , CheckBalanced(root))

#Solution 2
print("Is the binary tree balanced? ",end="")
if (HeightBalanced(root) != -1):
    print("True")
else:
    print("False")
         
'''
Question: Flip a binary tree. right -> left nodes
                                    <-
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


#Level order traversal and print nodes at each level    
import queue
def printBST(root):
    if root is None:
        print("EMPTY")
        return 
    result = []
    q = queue.Queue()
    seenlevel = 0
    q.put(root)
    q.put(seenlevel)
    while not q.empty():
        lnext = q.get()
        level = q.get()
        if(level != seenlevel):
            print(result)
            del result[:]
            seenlevel  = level
        result.append(lnext.data)
        if(lnext.left is not None):
            q.put(lnext.left)
            q.put(level+1)    
        if(lnext.right is not None):
            q.put(lnext.right)
            q.put(level+1)
    print(result) #IMPORTANT!!!


def flipTree(node):
    if node is None:
        return
    node.left,node.right = node.right,node.left
    flipTree(node.left)
    flipTree(node.right)

def preorder(node,result):
    if node is None:
        return
    preorder(node.left,result)
    result.append(node.data)
    preorder(node.right,result)

#Initialize Binary Tree
root = BinaryTree(4)
root.insertLeft(3)
root.insertRight(6)
root.getLeft().insertLeft(2)
root.getLeft().insertRight(5)
root.getRight().insertLeft(7)
root.getRight().insertRight(9)
print("Tree >>>")
printBST(root)
result = []
preorder(root,result)
print("Preorder >>>", result)


flipTree(root)
print("Flipped Tree >>>")
printBST(root)
del result [:]
preorder(root,result)
print("Preorder >>>", result)
#validation
assert result == [9, 6, 7, 4, 5, 3, 2], "test failed!"

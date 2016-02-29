'''
Question: Convert a sorted list into Binary Search Tree(BST)

Time Complexity: O(n)
Reference: Masters theorem
'''

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

#Notes: since the BST is created using the mid value 
# of the sorted input, the resulting BST is a balanced BST!!!
def buildBST(a,start,end):
    if (start > end):
        return
    #IMPORTANT!!!    
    mid = start + (end-start)//2
    newBST = BinarySearchTree(a[mid])
    newBST.left  = buildBST(a,start,mid-1)
    newBST.right = buildBST(a,mid+1,end)
    return newBST
    


a = [7,8,10,11,12,14,15,16,17,18,19,20,21]
newBST = buildBST(a,0,len(a)-1)
#Print tree
printBST(newBST)

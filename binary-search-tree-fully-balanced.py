'''
Question: Given ordered nodes construct a fully balanced BST.
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
            if root.left is None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insertNode(root.right, node)

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


def buildBalancedBST(nodes,start,end):
    if (start > end):
        return
    mid = start + int((end-start)/2)
    x = BSTNode(nodes[mid])
    x.left  = buildBalancedBST(nodes,start,mid-1)
    x.right = buildBalancedBST(nodes,mid+1,end)
    return x


#Step3: Build a balanced Binary Search Tree
a = [1,2,3,4,5,6]
start = 0
end = len(a)-1
root3 = buildBalancedBST(a,start,end)
printBST(root3)


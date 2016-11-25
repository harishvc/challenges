#Question: Print all paths & path sum from root to leaf

import sys
sys.path.append("./mylib")
import Tree

#Time complexity: O(n)
#Space complexity: O(n)
#Design: Iterate the binary tree level by level and store node, path and path sum in a stack
def Root2LeafPaths(root):
    nodes = []
    nodes.append(root)         #node
    nodes.append(root.data)    #path
    nodes.append(root.data)    #pathsum
    while (len(nodes) > 0):
        pathsum = nodes.pop()
        path = nodes.pop()
        next = nodes.pop()
        if(next.getRight() is not None):
            nodes.append(next.getRight())
            nodes.append(str(path) + "->" + str(next.getRight().data))
            nodes.append((pathsum + next.getRight().data))
        if(next.getLeft() is not None):    
            nodes.append(next.getLeft())
            nodes.append(str(path) + "->" + str(next.getLeft().data))
            nodes.append((pathsum + next.getLeft().data))
        if(next.getLeft() is None and next.getRight() is None):
            print("path:%s path sum:%d" % (path,pathsum))
            

#Build binary tree 
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)
root.getLeft().getLeft().insertLeft(8)
root.getLeft().getRight().insertRight(9)
root.getLeft().getRight().getRight().insertRight(10)
root.getLeft().getRight().getRight().getRight().insertRight(11)

Root2LeafPaths(root)
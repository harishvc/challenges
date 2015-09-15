'''
Question
1. Find the sum of all root to leaf paths in a binary tree.
2. Each node has a binary digit value and each root to leaf path represents a binary number. Sum all such numbers.
'''

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
                
def SumRoot2LeafPathsRecursive(node,sum):
     if(node is None):
         return 0
     sum = sum + node.data
     if(node.getLeft() is None and node.getRight() is None):
         return sum
     return SumRoot2LeafPathsRecursive(node.getLeft(),sum) + SumRoot2LeafPathsRecursive(node.getRight(),sum)
 
def SumRoot2LeafPathsRecursiveB2D(node,sum):
     if(node is None):
         return 0
     sum = sum * 2 + node.data  #convert binary to decimal
     if(node.getLeft() is None and node.getRight() is None):
         return sum
     return SumRoot2LeafPathsRecursiveB2D(node.getLeft(),sum) + SumRoot2LeafPathsRecursiveB2D(node.getRight(),sum)
 
    
#Build binary tree 
root = Tree.BinaryTree(1)
root.insertLeft(1)
root.insertRight(1)
root.getLeft().insertLeft(1)
root.getLeft().insertRight(0)
root.getRight().insertLeft(1)
root.getRight().insertRight(1)

Root2LeafPaths(root)

print("Sum of all root to leaf paths:", SumRoot2LeafPathsRecursive(root, 0))

print("Sum of all root to leaf paths (binary 2 decimal):", SumRoot2LeafPathsRecursiveB2D(root, 0))


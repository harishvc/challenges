#Question: Find all edge nodes in the binary tree

import sys
sys.path.append("./mylib")
import Tree

def printEdgeNodes(root, pType, cType):
   if root is None:
       return
   if pType == "root" or (pType == "left" and cType == "left") or (pType == "right" and cType == "right"):
        print (root.data)
   if root.left is None and root.right is None:
       print (root.data)
   if pType != cType and pType != "root":
       cType = "invalid"
   printEdgeNodes(root.left, cType, "left")


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
printEdgeNodes(root, "root", "root")

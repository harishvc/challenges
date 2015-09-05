'''
Question: Find all edge (boundary) of the binary tree

Algorithm:
1. Print all left boundary nodes from top to bottom
2. Print all leaf nodes from left to right
3. Print all right boundary nodes from bottom to top

Reference: http://stackoverflow.com/questions/30275735/to-print-the-boundary-of-binary-tree
'''

import sys
sys.path.append("./mylib")
import Tree

#Modified from http://www.careercup.com/question?id=18065671
#Time complexity: O(n)
def TreeBoundry(node,isLeft,isRight):
    #Left most node and leaf nodes
    if(isLeft or isLeaf(node)):
        print(node.data,end=' ')
    #Next left node
    if(node.getLeft() is not None): TreeBoundry(node.getLeft(), True, False)
    #Next right node
    if(node.getRight() is not None):TreeBoundry(node.getRight(), False ,True)
    #Right most node
    if(isRight and not isLeft and  not isLeaf(node)):
        print(node.data,end=' ')

def isLeaf(node):
    if (node.getLeft() is None and  node.getRight() is None):
        return True
    else:
        return False

#Tree 1
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
print("Tree 1: ", end="")
TreeBoundry(root,True,True)
print("")

#Tree 2
root2 = Tree.BinaryTree(1)
root2.insertLeft(2)
root2.insertRight(3)
root2.getLeft().insertLeft(4)
root2.getLeft().insertRight(5)
root2.getRight().insertLeft(6)
root2.getRight().insertRight(7)
root2.getLeft().getRight().insertRight(8)
print("Tree 2: ", end="")
TreeBoundry(root2,True,True)
print("")


#Tree 3
root3 = Tree.BinaryTree(1)
root3.insertLeft(2)
root3.insertRight(3)
root3.getLeft().insertLeft(4)
root3.getLeft().insertRight(5)
root3.getRight().insertLeft(6)
root3.getRight().insertRight(7)
root3.getLeft().getLeft().insertLeft(8)
root3.getLeft().getLeft().insertRight(9)
root3.getRight().getLeft().insertLeft(10)
root3.getRight().getLeft().insertRight(11)
root3.getRight().getRight().insertRight(12)
print("Tree 3: ", end="")
TreeBoundry(root3,True,True)
print("")

#Question: Print all paths & path sum from root to leaf

import sys
sys.path.append("./mylib")
import Tree

#Time complexity: O(n)
#Space complexity: O(n)
#Design: Iterate the binary tree level by level and store node, path and path sum in a stack
#solution #1
#modified pre order
def Root2LeafPaths(node,path=[],path_sum=0):
    path_sum += node.data
    path.append(node.data)
    if node.left is None and node.right is None:
        print("%s sum=%d" % (path,path_sum))
    else:
        Root2LeafPaths(node.left,path,path_sum) if node.left else None
        Root2LeafPaths(node.right,path,path_sum) if node.right else None
    path.pop()
    path_sum -= node.data

#solution #2
#modified post order
def all_path(node,path):
    path.append(node.data)
    if node.left:
        all_path(node.left,path)
    if node.right:
        all_path(node.right,path)
    if node.right is None and node.left is None:
        print(path, sum(path))
    path.pop()


'''

                         1
                       /    \ 
                      2       3
                    /   \    /  \
                  4      5  6    7
                 /        \
                8          9
                            \
                            10
                             \
                             11
'''

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

#solution #1
Root2LeafPaths(root)

#solution #2
#all_path(root,[])
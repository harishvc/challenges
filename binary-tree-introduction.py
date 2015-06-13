import sys
sys.path.append("./mylib")
import Tree

#Initialize Binary Tree
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)

#Traverse
result = []
Tree.preorderRecursive(root, result)
print("PreOrder traversal (recursive): %s" % (result))
del result[:]
Tree.inorderRecursive(root, result)
print("InOrder traversal (recursive): %s" % (result))
del result[:]
Tree.postorderRecursive(root, result)
print("PostOrder traversal (recursive): %s" % (result))
del result[:]
Tree.levelOrder(root, result)
print("LevelOrder traversal: %s" % (result))

#Question: Print all paths & path sum from root to leaf

import sys
sys.path.append("./mylib")
import Tree

#Source: http://stackoverflow.com/questions/11045399/print-every-leaf-path-of-a-tree-without-recursive
class Stack(object): 
    def __init__(self):
        self.a = []

    def push(self, b):
        self.a.append(b)

    def peek(self):
        return self.a[-1]

    def pop(self):
        return self.a.pop()

    def isEmpty(self):
        return len(self.a) == 0

    def show(self):
        return self.a
       
def RLpaths(troot):
    current = troot
    s = Stack()
    s.push(current)
    s.push(str(current.data))
    s.push(current.data)

    while not s.isEmpty():
        pathsum = s.pop()
        path = s.pop()
        current = s.pop()

        if not current.left and not current.right:
            print('path: %s, pathsum: %d' % (path, pathsum))

        if current.right:
            rightstr = path + "->" + str(current.right.data)
            rightpathsum = pathsum * 10 + current.right.data
            s.push(current.right)
            s.push(rightstr)
            s.push(rightpathsum)

        if current.left:
            leftstr = path + "->" + str(current.left.data)
            leftpathsum = pathsum * 10 + current.left.data
            s.push(current.left)
            s.push(leftstr)
            s.push(leftpathsum)
 
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
print("Printing all paths & path sum from root to leaf")
RLpaths(root)

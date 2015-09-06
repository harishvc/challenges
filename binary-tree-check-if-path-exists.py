#Question: Given path sum check if the path exists

import sys
sys.path.append("./mylib")
import Tree
        
def ValidPathSum(root,currentsum):
    global Complete
    if (root.getLeft() is None and root.getRight() is None and not Complete):
        if (currentsum == PATHSUM):
            Complete = True
    if(root.getLeft() is not None and not Complete):
        ValidPathSum(root.getLeft(),currentsum+root.getLeft().data)
    if(root.getRight() is not None and not Complete):
        ValidPathSum(root.getRight(),currentsum+root.getRight().data)
         	
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

Complete = False #GLOBAL
PATHSUM = 10     #GLOBAL
ValidPathSum(root, root.data)
print ("Is %d valid sum? %s" % (PATHSUM,Complete))
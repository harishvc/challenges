
#Implement BST iterator for next() and hasNext() using memory O(logN) and constant time

'''
OBSERVATIONS:
1. Left nodes have the smallest values, further the left node from the root (or parent node) smaller the value 
   - recurse the left side and store the nodes in a stack 
2. To build an iterator we need to keep track of the left node and left nodes of right nodes
3. Iterate the left node first and then the right node of the sub-node 
4. Since there is no reference back to the parent node, store entire node so you can traverse the left node
5. Before next() returns get ALL the left node

REFERENCE:
1. https://leetcode.com/discuss/20001/my-solutions-in-3-languages-with-stack
'''

import sys
sys.path.append("./mylib")
import BST
import BinaryTreeTraversal

#BST Iterator with operations next() and hasNext()
class BSTIterator:
    def __init__(self,root):
        self.nodes = []
        self.size  = 0
        #IMPORTANT: fill with all left nodes default
        self.fillNodes(root) 

    #store current node and nodes on the left    
    def fillNodes(self,node):
        while node:
            self.nodes.append(node)
            self.size +=1
            node = node.left

    #Time complexity: Less than O(logh), h is the depth of the sub-tree, h << n        
    def next(self):
        next_smallest_node = self.nodes.pop()
        self.size -= 1
        #IMPORTANT: check node right sub-tree
        self.fillNodes(next_smallest_node.right)
        return next_smallest_node.data

    #Time complexity:O(1)
    def hasNext(self):
        return (self.size > 0)




#Create BST
root = BST.BSTNode(4)
BST.insert(root, BST.BSTNode(3))
BST.insert(root, BST.BSTNode(6))
BST.insert(root, BST.BSTNode(2))
BST.insert(root, BST.BSTNode(5))
BST.insert(root, BST.BSTNode(7))
print("In order traversal >>")
BinaryTreeTraversal.inOrder(root)
print("")



bstI = BSTIterator(root)
while bstI.hasNext():
    print("next smallest >>>", bstI.next())



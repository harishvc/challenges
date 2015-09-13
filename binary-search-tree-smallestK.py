#Question: Find smallestK in BST

#Observation: A median is a special case of Kth smallest element

import sys
sys.path.append("./mylib")
import BST



#Solution 1:
#in-order traversal and global variable to count smallest K
#Time complexity: O(n)
#Space complexity: O(1)


#Solution 2                                    
#in-order traversal and list to store smallest K elements
#Time complexity: O(n)
#Space complexity: O(k)
def KSmallest(root,k,mylist):
    if (len(mylist) < k and root.left is not None):
        KSmallest(root.left, k, mylist)
    if (len(mylist) < k):
        mylist.append(root.data)
    if (len(mylist) < k and root.right is not None):
        KSmallest(root.right, k, mylist)

#Create BST
root = BST.BSTNode(4)
input = [3,2,1,5,6,7]
for x in input:
    BST.insertNode(root, BST.BSTNode(x))
#Smallest K
# mylist = []
# for x in range(1,len(input)+2):
#     KSmallest(root,x,mylist)
#     print("smallest element (k=%d) = %d" % (x,mylist.pop()))
#     del mylist[:]
    
    
#Solution 3
#Reference: http://stackoverflow.com/questions/2329171/find-kth-smallest-element-in-a-binary-search-tree-in-optimum-way
#Algorithm:
#Step 1:  Augment BST to store #nodes in its left subtree including current node
#Step 2:  Recursively traverse left or right subtree comparing k and #nodes in left subtree
#Time complexity: O(log n) - depth of a node
#Space complexity: O(1) 

#Modified BST class
class BSTNode:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data
        root.leftnodes = 1 #nodes on left including current node
        
#Modified BST insert that keeps track on #left nodes
def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            root.leftnodes += 1 #nodes on left including current node
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)

#Modified in-order traversal
def KSmallest2(root,k,mylist):
    if (k < root.leftnodes):
        KSmallest2(root.left, k, mylist)
    elif (k > root.leftnodes):
        KSmallest2(root.right, k-root.leftnodes, mylist)
    else:
        mylist.append(root.data)
        
#Create BST    
root2 = BSTNode(4)
input2 = [3,2,1,6,5,8,7,9,10,11]
for x in input2:
    insertNode(root2, BSTNode(x))

#Smallest K 
mylist2 = []
for x in range(1,len(input2)+2):
    KSmallest2(root2,x,mylist2)
    print("smallest(k=%d) = %d" % (x,mylist2.pop()))
    del mylist2[:]

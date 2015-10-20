'''
Question: List all the path that add up to a given value. 
Path are from parent node to child node, root and leaf can be excluded in the path
'''

import sys
sys.path.append("./mylib")
import Tree

def UpdatePathSumHash(PSH,sum,delta):
    newcount = PSH.get(sum,0) + delta
    PSH[sum] = newcount
    
path=[]
all_paths=[]
SumPathHash={} #store sum (key) and paths (value)

def diff(list1, list2):
    a = set(list1).union(set(list2))
    b = set(list1).intersection(set(list2))
    return list(a - b)
    
def SumRoot2LeafPathsRecursive(node,sum,target,PSH):
    global path,all_paths,SumPathHash
    if(node is None):
        return 0

    sum += node.data  #running sum
    path.append(node.data) #current path
    SumPathHash[sum] = list(path) 
    psum = sum - target #pathsum relative to target value
    result = PSH.get(psum,0) #get #path that add up to a pathsum
    if(result > 0): #PATH exists without root and leaf
        all_paths.append(diff(SumPathHash[psum],path))
    if (sum == target): #PATH exists from root to leaf
        all_paths.append(list(path))
        result += 1

    #Increment 1 path to running sum
    UpdatePathSumHash(PSH,sum,1)
    result += SumRoot2LeafPathsRecursive(node.getLeft(),sum,target,PSH)
    result += SumRoot2LeafPathsRecursive(node.getRight(),sum,target,PSH)
    #Decrement 1 path to running sum since path are from parent nodes to child nodes
    UpdatePathSumHash(PSH,sum,-1)
    path.pop() #remove current node 
    return result
 
     
#Build binary tree 
root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)

PSH = {} #path sum hash
target = 7 #target value
countPaths = SumRoot2LeafPathsRecursive(root,0,target,PSH)
print("#paths that sum to %d = %d" % (target,countPaths))
print("All paths =>", all_paths)
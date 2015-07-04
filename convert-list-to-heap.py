'''
Question: Given an unsorted list of length n, build max heap in linear time O(n) 
'''
#Source:https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter07priorityqueues/HeapSort.py
#Time Complexity: O(n)

def BuildMaxHeap(A):
    length = len(A) - 1
    lastParent = length // 2
    #Visit ALL parent nodes
    for i in range (lastParent, -1, -1):
        percolateDownMax(A, i, length)
        
# Modified percolateDown to skip branch already heapified
def percolateDownMax(A, ParentIndex, Size):
  MaxChildIndex = 2 * ParentIndex + 1  #child on left
  while MaxChildIndex <= Size:
    # right child exists and is value of right child larger than left child
    if (MaxChildIndex < Size) and (A[MaxChildIndex] < A[MaxChildIndex + 1]):
        MaxChildIndex += 1
    # child node has value larger than parent
    if A[MaxChildIndex] > A[ParentIndex]:
        swap(A, MaxChildIndex, ParentIndex)
        # move down to largest child
        ParentIndex = MaxChildIndex
        MaxChildIndex = 2 * ParentIndex + 1
    else:
        #parent node has value greater than child node
        #no need to percolate down - heapify on linear time!
        return  # force exit
  
def swap(A, x, y):
  temp = A[x]
  A[x] = A[y]
  A[y] = temp


A = [ 15,34,111,22,63,12,77,55,2]
print(A, "changed to heap >>> ", end="")
BuildMaxHeap(A)        
print(A)

#Print Heap
import sys
sys.path.append("./mylib")
from heapq_showtree import show_tree
show_tree(A)
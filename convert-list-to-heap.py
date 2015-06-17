'''
Question: Given an unsorted list, convert to max heap
'''

#Source:https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter07priorityqueues/HeapSort.py

def BuildMaxHeap(A):
    length = len(A) - 1
    leastParent = int(length / 2)
    for i in range (leastParent, -1, -1):
        percolateDown(A, i, length)
        
# Modified percolateDown to skip the sorted elements
def percolateDown(A, first, last):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if (largest < last) and (A[largest] < A[largest + 1]):
        largest += 1
    # right child is larger than parent
    if A[largest] > A[first]:
        swap(A, largest, first)
        # move down to largest child
        first = largest
        largest = 2 * first + 1
    else:
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
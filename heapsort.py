#Source:https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter07priorityqueues/HeapSort.py

def BuildMaxHeap(A):
    length = len(A) - 1
    leastParent = int(length / 2)
    for i in range (leastParent, -1, -1):
        percolateDown(A, i, length)

def heapSort(A):
  length = len(A) - 1
  for i in range (length, 0, -1):
    if A[0] > A[i]:
      swap(A, 0, i)
      percolateDown(A, 0, i - 1)  #i-1 (reduce the size if the heap)

        
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


A = [ 5,4,1,2,3]
BuildMaxHeap(A)        
print(A, "sorted to >>> ", end="")
heapSort(A)
print(A)

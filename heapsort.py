#Implement Heap Sort

import sys
sys.path.append("./mylib/")
import MinHeap

def buildMinHeap(a):
    myHeap = MinHeap.MinHeap()
    for i in a:
      myHeap.insertNode(i)
    return myHeap



A = [5,1,8,2,9]
print("input >>>>", A)
#Step 1: Turn list into min heap
myheap = buildMinHeap(A)
print("Min Heap  >>>")
myheap.printHeap()
#Step 2: Sort
print("Sorted values >>>")
while myheap.heapSize() > 0:
    tmp = myheap.deleteNode()
    print(tmp,end =" ")
print("")

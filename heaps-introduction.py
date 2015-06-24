#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter07priorityqueues/KthSmallestWithExtraHeap.py

import sys
sys.path.append("./mylib")
import Heap  #custome Heap Module
from heapq_showtree import show_tree

#Initialize Heap
Something = Heap.MaxHeap()
#Insert into Heap
Something.Insert(13)
Something.Insert(5)
Something.Insert(6)
Something.Insert(1)
Something.Insert(2)
Something.Insert(4)
Something.Insert(17)

#Print Heap - linear
Something.printHeap()
#Print Heap - tree
show_tree(Something.printHeap2())

#Delete node
for x in range (1,Something.size+1):
    print("Deleting node")
    Something.Delete()
    show_tree(Something.printHeap2())
    
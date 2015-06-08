#Introduction to heapq library

import heapq
input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
print ("input >>>", input)

#Min Heap (DEFAULT)
heapq.heapify(input)             
print ("input after min heap >>>", input)

#Max Heap
heapq._heapify_max(input)     
print ("input after max heap >>>", input)

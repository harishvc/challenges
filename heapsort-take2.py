#http://stackoverflow.com/questions/12749622/creating-a-heap-in-python

#Convert a list into Heap (min Heap)
def BuildHeap(A):
    length = len(A) - 1
    lastParent = length // 2
    #Visit ALL parent nodes
    for i in range (lastParent, -1, -1):
        percolateDownMin(A, i, length)
        
# Modified percolateDown
#Visit ALL child nodes of parent node BUT skip branch already heapified
def percolateDownMin(A, ParentIndex, Size):
  MinChildIndex = 2 * ParentIndex + 1  #child on left
  while MinChildIndex <= Size:
  	#Find index position of the child node with MIN value
    if (MinChildIndex < Size) and (A[MinChildIndex] > A[MinChildIndex + 1]):
        MinChildIndex += 1
    #Child node has value < than parent
    if A[MinChildIndex] < A[ParentIndex]:
        A[MinChildIndex],A[ParentIndex] = A[ParentIndex],A[MinChildIndex]
        # move down the sub-tree (IMPORTANT!!!)
        ParentIndex = MinChildIndex
        MinChildIndex = 2 * ParentIndex + 1
    else:
        #parent node has value < than child node
        #no need to percolate down
        #force exit
        return  

def percolateUpMin(input,k):
	lastParent = k//2
	for parent in range(lastParent,-1,-1):
		rightChild = parent*2 + 2
		leftChild = parent*2 + 1
		#left node and right node
		if(rightChild<= k):
			#smallest is left node
			if (input[leftChild] < input[rightChild] and input[leftChild] < input[parent]):
				input[parent],input[leftChild] = input[leftChild],input[parent]
			#smallest is right node
			elif(input[rightChild] < input[leftChild] and input[rightChild] < input[parent]):
				input[parent],input[rightChild] = input[rightChild],input[parent]
		#left node exisits and <		
		elif(leftChild <= k and input[leftChild] < input[parent]):
			input[parent],input[leftChild] = input[leftChild],input[parent]		



#Convert list to heap
A = [i for i in range(0,10)]
import random
random.shuffle(A)
print("input >>>", A)
BuildHeap(A)        
#print(A)

#Add item to heap
#A.append(0)
#print(A)
#percolateUpMin(A,len(A)-1)        
#print(A)

#Remove item from heap
#print("######################")
#A[0],A[len(A)-1] = A[len(A)-1] ,A[0]
#A.pop()
#print(A)
#percolateDownMin(A,len(A)-1)        
#print(A)

#Heap Sort
for x in range(len(A)-1,-1,-1):
	A[0],A[x] = A[x],A[0]
	percolateDownMin(A,0,x-1)
	#print(x,A)
print("Heap Sort >>>", list(reversed(A)))

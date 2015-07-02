#Heap Library
#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/ad9d11b94a6b06e32831afbcb520d07cd758d0da/src/chapter07priorityqueues/KthSmallestWithExtraHeap.py

#Max Heap Implementation
class MaxHeap:
	def __init__(self):
		self.heapList = [0]  # index position 0 = 0 (SIMPLICITY !!!!)
		self.size = 0  # Size of the heap

	def parent(self, index):
		"""
		Parent will be at math.floor(index/2). Since integer division
		simulates the floor function, we don't explicitly use it
		"""
		return index // 2
	
	def leftChild(self, index):
		if 2 * index <= self.size:
			return self.heapList[2 * index ]
		return -1
		
	def rightChild(self, index):
		if 2 * index + 1 <= self.size :
			return self.heapList[2 * index + 1]
		return -1	
	 
	# Get Minimum for MaxHeap
	def getMaxium(self):
		if self.size == 0:
			return -1
		return self.heapList[1]
	
	#Given parent node return index position of child node with max value 
	def maxChild(self, i):
		if (i * 2 + 1 > self.size):   
			#No right node. Return index position of left node
			return i * 2 #left node index
		else:
			if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
				return i * 2 + 1   #right node index
			else:
				return i * 2  #left node index
	
	#Max Heap	   
	def percolateDown(self, i):
		while (i * 2) <= self.size: #left node, since i[0] is not used
			maxChild = self.maxChild(i) #get index position of max child
			#print("checking ....", self.heapList[i], self.heapList[maxChild])
			if self.heapList[i] < self.heapList[maxChild]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[maxChild]
				self.heapList[maxChild] = tmp
			i = maxChild
	
	#Max Heap
	def percolateUp(self,i):
		while i // 2 > 0:  #Find parent , since i[0] is not used, parent node is i//2
			#print("start i=%d" % (i))
			if self.heapList[i] > self.heapList[i // 2]:
				#print("Swapping ....",self.heapList[i],self.heapList[i//2])
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2
			#print("new start i=%d" % (i))

	
	# Delete an element
	#  Delete the root (only operation supported. 
	#  Copy last element to root
	#  Delete last element 
	#  Percolate down
	def Delete(self):
	    retval = self.heapList[1]
	    self.heapList[1] = self.heapList[self.size] #starting in index 1;copy last position to first
	    self.size = self.size - 1
	    self.heapList.pop()
	    self.percolateDown(1) #pass index position of root
	    return retval
	   
	def Insert(self, k):
		self.heapList.append(k)
		self.size = self.size + 1
		#print("Inserting value=%d at index position=%d" % (k,self.size))
		self.percolateUp(self.size) #pass size of heap
		
	def printHeap(self):
		print(self.heapList[1:])
		
	def printHeap2(self):
		return(self.heapList[1:])
					
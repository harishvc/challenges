#Min Heap Implemenation

class MinHeap:
	def __init__(self):
		self.values = [-1] #starting from index=1
		self.size = 0

	def heapSize(self):
		return self.size

	def parentIndex(self,index):
		return index//2

	def leftChildIndex(self,index):
		return index*2

	def rightChildIndex(self,index):
		return index*2+1

	def minChildIndex(self,index):
		if index*2+1 > self.size: #no right child
			return index*2
		else:
			if self.values[index*2] < self.values[index*2+1]:
				return index*2
			else:
				return index*2+1

	def insertNode(self,K):
		self.values.append(K)
		self.size += 1
		self.percolateUP(self.size)

	def percolateUP(self,i):
		while i//2 > 0: #IMPORTANT: > 0 since root is at index 1
			parentIndex = self.parentIndex(i)
			if self.values[parentIndex] > self.values[i]:
				tmp  = self.values[parentIndex]
				self.values[parentIndex]  =  self.values[i]
				self.values[i] = tmp
			i = i//2 #keep going up, each node has ONE parent

	def deleteNode(self):
		tmp = self.values[1]  #IMPORTANT: start index=1
		self.values[1] = self.values[self.size]
		self.size -= 1
		self.values.pop()
		self.percolateDOWN(1) #IMPORTANT: index=1
		return tmp #IMPORTANT: return value

	def percolateDOWN(self,i):
		while i*2 <= self.size:
			minChildIndex = self.minChildIndex(i)
			if self.values[i] > self.values[minChildIndex]:
				tmp = self.values[i]
				self.values[i] = self.values[minChildIndex]
				self.values[minChildIndex] = tmp
			i = minChildIndex #IMPORTANT: ONLY visit branch with min value

	def printHeap(self):
		print(self.values[1:])

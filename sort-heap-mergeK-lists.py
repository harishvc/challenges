#Merge K sorted list of size N

'''
OBSERVATION:
1. Implement heap sort of height K
2. By keeping heap hegiht K we can reduce the complexity O(n*klog(k))

'''

import sys
class minHeap:
	def __init__(self,a,N):
		self.values = [[-1,-1]]  #starting from index=1
		self.size = 0
		self.N = N   
		self.a = a

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
			ldata,lindex,lsource = self.values[index*2]
			rdata,rindex,rsource = self.values[index*2+1]
			if ldata < rdata:
				return index*2
			else:
				return index*2+1

	def insertNode(self,dis):
		self.values.append(dis)
		self.size += 1
		self.percolateUP(self.size)

	def percolateUP(self,i):
		while i//2 > 0: #IMPORTANT: > 0 since root is at index 1
			parentIndex = self.parentIndex(i)
			#unpack values
			data,index,source = self.values[i]
			#unpack values
			pdata,pindex,psource = self.values[parentIndex]
			if pdata > data:
				tmp  = self.values[parentIndex]
				self.values[parentIndex]  =  self.values[i]
				self.values[i] = tmp
			i = i//2 #keep going up, each node has ONE parent

	def deleteNode(self):
		#step 1: unpack values at root
		data,index,source = self.values[1]  #IMPORTANT: start index=1
		#step 1: Replace root node with next value from the same list (or sys.maxsize)
		#IMPORTANT = (no insert,append)
		if index+1 < self.N:
			self.values[1] = [a[source][index+1],index+1,source]
		else:
			#All values in list processed
			self.values[1] = [sys.maxsize,-1,-1]
		#step 3: percolate down				
		self.percolateDOWN(1)	
		return data #IMPORTANT: return value

	def percolateDOWN(self,i):
		while i*2 <= self.size:
			minChildIndex = self.minChildIndex(i)
			#unpack values
			data,index,source = self.values[i]
			#unpack values
			cdata,cindex,csource = self.values[minChildIndex]
			if cdata < data:
				tmp = self.values[i]
				self.values[i] = self.values[minChildIndex]
				self.values[minChildIndex] = tmp
			i = minChildIndex #IMPORTANT: ONLY visit branch with min value

	def printHeap(self):
		print(self.values[1:])


N = 3
K = 4
a = [[3,15,17],[9,25,31],[1,8,19],[2,4,5]]

#Initialize heap
myheap = minHeap(a,N)
for i in range(len(a)):
	#pack values
	#create a list with [data,index,source]
	#INITIALIZE with first value from each list
	dis = [a[i][0],0,i]
	myheap.insertNode(dis)

count = 0
while count < N*K:
	print(myheap.deleteNode())
	count +=1

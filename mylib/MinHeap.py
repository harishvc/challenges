
#Min Implemention & Heap Sort

class MinHeap:
	def __init__(self):
		self.data = [0] # index position 0 = 0 (SIMPLICITY !!!!)
		self.size = 0

	def insert(self,data):
		self.data.append(data)
		self.size +=1 
		self.percolateUP()

	def percolateUP(self):
		current = self.size
		#IMPORTANT: current//2 > 0  since start index=1 
		while current//2 > 0:
			parent = current//2
			if self.data[current] < self.data[parent]:
				self.data[current],self.data[parent] = self.data[parent],self.data[current]
				current = parent
			else:
				#IMPORTANT: heap property is satisfied
				break

	def myprint(self):
		print(self.data)


	def delete(self):
		myreturn = self.data[1] #replace with last value
		self.data[1] = self.data[self.size]
		self.size -= 1
		self.data.pop() #remove last value
		self.percolateDOWN()
		return myreturn

	def getMinChild(self,index):
		#IMPORTANT: NO right child node
		if 2*index+1 > self.size:
			return index*2
		else:
			if self.data[index*2] < self.data[index*2+1]:
				return index*2
			else:
				return index*2+1

	def percolateDOWN(self):
		node = 1
		#IMPORTANT: node * 2 <= self.size , covers both left and right child nodes 
		while node * 2 <= self.size:
			minChildNodeIndex = self.getMinChild(node)
			if self.data[node] > self.data[minChildNodeIndex]:
				self.data[node],self.data[minChildNodeIndex] = self.data[minChildNodeIndex],self.data[node]
				node = minChildNodeIndex
			else:
				#IMPORTANT: heap property is satisfied
				break


a = [5,2,1,3,4]
h = MinHeap()
for i in a:
	h.insert(i)

print(h.delete())  #1
print(h.delete())  #2
h.insert(1)       
h.insert(2)
print(h.delete())  #1 
print(h.delete())  #2



















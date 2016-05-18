'''
Given a queue return max value at any given time in constant time

Example:
Input          Max
[1]            1
[1,5]          5 
[1,5,4]        5
[5,4]          5
[4]            4

NOTES: 
Why use double ended queue to store max value?
1. order matters
2. when new value is greater than value at head of queue all values are popped!
3. when new value is in between the existing values in the max queue all
   values less (on the right) need to be removed - double ended queue is ideal!
'''
import queue
import collections
class MyQueue:
	def __init__(self):
		self.q = queue.Queue()
		self.max = collections.deque()
		self.size = 0 #size of max queue

	def put(self,value):
		self.q.put(value)
		#update max
		self.updatemaxQueue(value)

	def get(self):
		tmp = self.q.get()
		if self.max[0] == tmp:
			self.max.popleft()
			self.size -=1
		return tmp

	def getMax(self):
		return self.max[0]

	def updatemaxQueue(self,newvalue):
		#case 1: max queue is emtpy
		if self.size == 0:
			self.max.append(newvalue)
			self.size  = 1
		#case2: newvalue greater than first value in max queue
		#pop all value in max queue
		elif newvalue >= self.max[0]:
			while self.size > 0:
				self.max.pop()
				self.size -= 1
			self.max.append(newvalue)
			self.size  = 1			
		#case3: newvalue is less than last value in max queue
		#add new value to max queue
		elif newvalue <= self.max[self.size-1]:
			self.max.append(newvalue)
			self.size  += 1
		#case4: new value is in between values in max queue
		else:
			while self.max[self.size] < newvalue:
				self.max.pop()
				self.size -= 1
			self.max.append(newvalue)
			self.size  += 1

q = MyQueue()
q.put(1)
print(q.getMax())
q.put(5)
print(q.getMax())
q.put(4)
print(q.getMax())
q.get()
print(q.getMax())
q.get()
print(q.getMax())

#Implement queue using linked lists
#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter05queues/QueuesWithLinkedLists.py

# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self, data=None, next=None):
		self.data = data
		self.last = None
		self.next = next
	# method for setting the data field of the node    
	def setData(self, data):
		self.data = data
	# method for getting the data field of the node   
	def getData(self):
		return self.data
	# method for setting the next field of the node
	def setNext(self, next):
		self.next = next
	# method for getting the next field of the node    
	def getNext(self):
		return self.next
	# method for setting the last field of the node
	def setLast(self, last):
		self.last = last
	# method for getting the last field of the node    
	def getLast(self):
		return self.last	
	# returns true if the node points to another node
	def hasNext(self):
		return self.next != None


class Queue(object):
	def __init__(self, data=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enQueue(self, data):
		self.lastNode = self.front
		self.front = Node(data, self.front)
		if self.lastNode:
			self.lastNode.setLast(self.front)
		if self.rear is None:
			self.rear = self.front
		self.size += 1

	def queueRear(self):
		if self.rear is None:
			print ("Sorry, the queue is empty!")
			raise IndexError
		return self.rear.getData()

	def queueFront(self):
		if self.front is None:
			print ("Sorry, the queue is empty!")
			raise IndexError
		return self.front.getData()

	def deQueue(self):
		if self.rear is None:
			print ("Sorry, the queue is empty!")
			raise IndexError
		result = self.rear.getData()
		self.rear = self.rear.last
		self.size -= 1
		return result

	def size(self):
		return self.size
	
que = Queue()
que.enQueue("first")
print ("Front: " + que.queueFront())
print ("Rear: " + que.queueRear())
que.enQueue("second")
print ("Front: " + que.queueFront())
print ("Rear: " + que.queueRear())
que.enQueue("third")
print ("Front: " + que.queueFront())
print ("Rear: " + que.queueRear())
print ("Dequeuing: " + que.deQueue())
print ("Front: " + que.queueFront())
print ("Rear: " + que.queueRear())
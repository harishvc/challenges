'''
Question:
Implement a queue using a linked list
'''

class LinkedList:
	def __init__(self,data):
		self.data = data
		self.next = None

class Queue:
	def __init__(self):
		#IMPORTANT - reference to the head of the linked list
		self.head = None

	#Add new node to the tail of the linked list (queue)
	def enqueue(self,data):
		node = LinkedList(data)
		if self.head:
			current = self.head
			while(current.next is not None):
				current = current.next
			current.next = node
		else:
			self.head = node
	
	def dequeue(self):
		#case 1: one more node after
		if self.head and self.head.next:
			node = self.head
			self.head = self.head.next
			node.next = None
			#print("###", self.head.data)
			return node.data
		#case 2: last node	
		elif self.head:
			tmp = self.head
			self.head = None
			return tmp.data
		#case 3: queue empty!
		else:
			print("Error: queue empty")
			return None, None

	def PrintLinkedList(self):
		list = self.head
		while list is not None:
			if list.next is not None:
				print(list.data,end=" -> ")
			else:
				print(list.data,end="\n")
			list = list.next


#create queue using linked list
q = Queue()
for i in range(1,4):
	q.enqueue(i)
print("input >>> " , end="")
q.PrintLinkedList()
print("$>dequeue 5 >>> " , end="")
q.enqueue(5)
q.PrintLinkedList()
print("$>enqueue ")
print(q.dequeue())
print("$>enqueue ")
print(q.dequeue())
print("input >>> " , end="")
q.PrintLinkedList()


'''
Question:
Implement a max queue using a linked list
'''

'''
NOTES
input              max
1                  1
1,2                2
1,2,5              5
--
5                  5
3                  5,3
5,3,3              5,3,3

1. max values are in descending order!
2. dequeue all values less than new value 
'''

def MaxQueueAdd(head,data):
	newnode = LinkedList(data)
	if head is None:
		head = newnode
	else:
		#IMPORTANT: dequeue all less values than the new value
		node = head
		while node:
			if newnode.data > node.data:
				node.data = newnode.data
				#delete(node.next)
				node.next = None
				break
			node = node.next
	return head

def MaxQueueRemove(head,data):
	if head.data == data:
		tmp = head
		head = head.next
		tmp.next = None
		return head

class LinkedList:
	def __init__(self,data):
		self.data = data
		self.next = None

class Queue:
	def __init__(self):
		self.head = None
		self.qmax = None

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
		#Max queue:
		self.qmax = MaxQueueAdd(self.qmax,data)


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
		#Max queue
		self.qmax = MaxQueueRemove(self.qmax,data)

	def getMax(self):
		return self.qmax.data

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
for i in range(1,6):
	q.enqueue(i)
print("input >>> " , end="")
q.PrintLinkedList()
print("max=",q.getMax())
print("$>enqueue 2 >>> " , end="")
q.enqueue(2)
q.PrintLinkedList()
print("max=",q.getMax())
print("$>denqueue ")
print(q.dequeue())
print("max=",q.getMax())
print("$>enqueue ")
print(q.dequeue())
print("max=",q.getMax())
print("input >>> " , end="")
q.PrintLinkedList()


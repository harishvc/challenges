#Insert a node in a sorted circular linked list

class LinkedList:
	def __init__(self,data):
		self.data = data
		self.next = None

	def insert(self,node):
		current = self
		while(current.next is not None):
			current = current.next
		current.next = node

def PrintLinkedList(list):
	while list is not None:
		if list.next is not None:
			print(list.data,end=" -> ")
		else:
			print(list.data,end="\n")
		list = list.next


#insert a node in a sorted circular link list
#solution 1
def insertCLL(head,newnode):
	current = head
	#edge case: linked list empty!
	if head is None:
		head = newnode
		newnode.next = head
		return head
	while True:
		if newnode.data < current.data:
			#case 1: insert at head
			newnode.next = current
			#find the last node pointing back to head!
			while current.next is not head:
				current = current.next
			current.next = newnode
			return newnode
		elif newnode.data >= current.data and newnode.data <= current.next.data:
			#case 2: insert somewhere in the middle
			newnode.next = current.next
			current.next = newnode
			return head
		elif newnode.data >= current.data and current.next == head:
			#case 3: insert at end
			newnode.next = current.next
			current.next = newnode
			return head
		#case 4: keep iterating until one of the conditions is fulfilled
		current = current.next
	return head #maybe new head!!!

#solution 2: modified solution #1
def insertCLL2(head,newnode):
	current = head
	changeHead = False
	#edge case: linked list empty!
	if head is None:
		head = newnode
		newnode.next = head
		return head
	while True:
		if newnode.data < current.data and not changeHead:
			#case 1 (part 1): insert at head
			newnode.next = current
			changeHead = True
			#find the last node pointing back to head!
			#while current.next is not head:
			#	current = current.next
			#current.next = newnode
			#return newnode
		elif newnode.data >= current.data and newnode.data <= current.next.data:
			#case 2: insert somewhere in the middle
			newnode.next = current.next
			current.next = newnode
			return head
		elif newnode.data >= current.data and current.next == head:
			#case 3: insert at end
			newnode.next = current.next
			current.next = newnode
			return head
		elif current.next == head and changeHead:
			#case 1 (part 2): change last node to point to new head
			current.next = newnode
			return newnode
		#case 4: keep iterating until one of the conditions is fulfilled
		current = current.next
	return head #maybe new head!!!



#create circular list
head = LinkedList(1)
for i in range(2,10):
	tmp = LinkedList(i)
	head.insert(tmp)
#create loop at value 
tmp.next = head

tmp = LinkedList(0)
head = insertCLL2(head,tmp)
#PrintLinkedList(head)
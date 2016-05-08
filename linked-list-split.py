'''
Question:
Split a linked list into two list with odd and even values. 
Retain the order of value and solve with no additional space.
'''

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


def add2List(reference,node):
	#IMPORTANT: keep copy of head node
	head = reference
	if reference:
		while reference.next:
			reference = reference.next
		reference.next = node
		#IMPORTANT: update next
		reference.next.next = None
		return head #send head node
	else:
		reference = node
		#IMPORTANT: update next
		reference.next = None
		return reference #send head node

#split node by odd or even value
def splitLL(node):
	odd = None
	even = None
	while node:
		current = node
		#IMPORTANT: Get next node to process!!!
		node = node.next
		if current.data%2 ==0:
			tmp = even
			#IMPORTANT: Get reference to head node
			even = add2List(tmp,current)
		else:
			tmp = odd
			#IMPORTANT: Get reference to head node
			odd = add2List(tmp,current)
	return odd,even

#create linked list
head = LinkedList(1)
for i in range(2,10):
	tmp = LinkedList(i)
	head.insert(tmp)
PrintLinkedList(head)
odd,even = splitLL(head)
PrintLinkedList(odd)
PrintLinkedList(even)
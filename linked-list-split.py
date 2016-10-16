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


def splitLL(node):
    oddHead = None
    evenHead = None
    odd = None
    even = None
    while node:
        #IMPORTANT: get next
        tmp = node.next 
        if node.data%2 == 0:  #even
            if evenHead is None:
                evenHead = node
                even = node
            else:
                even.next = node
                even = node
        else: #odd
            if oddHead is None:
                oddHead = node
                odd = node
            else:
                odd.next = node
                odd = node
        #IMPORTANT: end each node        
        node.next = None
        #IMPORTANT: next node
        node = tmp
    return oddHead,evenHead

#create linked list
head = LinkedList(1)
for i in range(2,10):
	tmp = LinkedList(i)
	head.insert(tmp)
PrintLinkedList(head)
odd,even = splitLL(head)
PrintLinkedList(odd)
PrintLinkedList(even)

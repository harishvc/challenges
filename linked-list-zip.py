#Zip a linked list
#1->2->3->4>5->6 = 1->6->2->5->3->4 

#NOTES
#1. Find length
#2. Reverse second half
#3. Zip now!

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

#find last and mid
def MiddleEnd(headNode):
	slow = headNode
	fast = headNode
	#step1: find middle and end
	while fast.next is not None:
		slow = slow.next
		if fast.next.next is not None:
			fast = fast.next.next
		else:
			fast = fast.next
	return slow,fast


def ReverseLinkedListIterative(node):
	prev=None
	while node is not None:
		tmp = node
		node = node.next
		tmp.next = prev
		prev = tmp
	return prev


def zipLinkedList(headNode):
	#step 1: get mid and last
	mid,last =MiddleEnd(headNode)		
	#step2: reverse second half
	mid.next = ReverseLinkedListIterative(mid.next)
	#step3: alternate values between first half and second half
	start = headNode
	#IMPORTANT: mid node becomes the last node!!!!
	while mid.next is not None:
		#remove last node 
		last = mid.next 
		#re-arrange mid node `next`
		if last.next is not None:
			mid.next = last.next
		else:
			mid.next = None
		#pointer to the second node	
		start2 = start.next
		start.next = last
		last.next = start2
		start = start2
	return headNode 

#create
head = LinkedList(1)
#insert
head.insert(LinkedList(2))
head.insert(LinkedList(3))
head.insert(LinkedList(4))
head.insert(LinkedList(5))
head.insert(LinkedList(6))
print("Input >>> ",end="")
PrintLinkedList(head)
#
head = zipLinkedList(head)
print("zipped result >>> ",end="")
PrintLinkedList(head)


#Find the node where cycle starts

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


def isLinkedListLoop(head):
	slow = head
	fast = head
	cycleLength = 0
	while (fast and fast.next):
		slow = slow.next
		fast = fast.next.next
		#find the node where slow pointer and fast (x2) pointer meet
		if fast == slow:
			#node where cycle starts 
			#1. move the slow pointer to the head
			#2. move the slow  and fast pointer one node at a time until they meet
			slow = head
			while(slow != fast):
				slow = slow.next
				fast = fast.next
			return slow.data


#create circular list
myhash = {}
head = LinkedList(1)
for i in range(2,10):
	tmp = LinkedList(i)
	myhash[i] = tmp
	head.insert(tmp)
#start loop at value 3
myhash[9].next = myhash[3]

#Find node where cycle starts
print("Node where cycle starts=%d" % (isLinkedListLoop(head)))

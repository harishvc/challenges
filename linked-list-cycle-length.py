#Find the length of the cycle

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
		#check for cycle
		if fast == slow:
			#LENGTH OF CYCLE
			#Anchor one pointer and move other pointer until both pointers are at the same node
			slow = slow.next
			cycleLength = 1
			while (slow != fast):
				slow = slow.next
				cycleLength +=1
				#print("at=", slow.data, " cycle length=", cycleLength)
			return cycleLength
	#return cycleLength


#create circular list
myhash = {}
head = LinkedList(1)
for i in range(2,10):
	tmp = LinkedList(i)
	myhash[i] = tmp
	head.insert(tmp)
#start loop at value 3
myhash[9].next = myhash[3]

#Check is a linked list has a cycle
print("Length of cycle=", isLinkedListLoop(head))

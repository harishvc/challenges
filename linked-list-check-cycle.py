#Check if a given linked list has a cycle

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
	while (fast and fast.next):
		slow = slow.next
		fast = fast.next.next
                #same node?
		if fast == slow:
			return True
	return False



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
print("Does this linked list have a cycle?", isLinkedListLoop(head))

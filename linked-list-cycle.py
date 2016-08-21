#Detect length and start node for cycle

'''
Length of cycle: 
	1. Anchor one pointer and move other pointer until both pointers are at the same node

Start of cycle: 
    1. Move one pointer to the head
	2. Move both pointers one node at a time until they meet		
'''

def cycleLengthStart(node):
	fast = node
	slow = node
	cycleLength = 0
	cycleStart = None
	#IMPORTANT: store pointer to head
	head = node
	while node and node.next:
		fast = fast.next.next
		slow = slow.next
		#cycle!
		if fast == slow:
			#Find length of cycle
			#Anchor one pointer and move other pointer until both 
			#pointers are at the same node
			slow = slow.next
			cycleLength +=1
			while slow != fast:
				slow = slow.next
				cycleLength +=1
			#Find start of cycle
			#move one pointer to the head
			#move both pointers one node at a time until they meet
			slow =  head
			while slow != fast:
				slow = slow.next
				fast = fast.next
			break
	return cycleLength,slow.data	



import sys
sys.path.append("./mylib/")
import LinkedListLibrary

class LLNode:
        def __init__(self,data):
                self.data = data
                self.next = None

#create circular list
myhash = {}
head = LLNode(1)
for i in range(2,6):
	tmp = LLNode(i)
	myhash[i] = tmp
	LinkedListLibrary.Insert2End(head,tmp)
#start loop at value 2
myhash[5].next = myhash[2]



cycleLength,startNode = cycleLengthStart(head)
print("Cycle Length=%d & Cycle start node=%d" % (cycleLength,startNode))


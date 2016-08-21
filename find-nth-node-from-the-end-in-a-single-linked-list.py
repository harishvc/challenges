#Question: Given a linked list. Find the Nth node from the end

'''
ALGORITHM:
1. Maintain two pointers (fast and slow) and initialize them to head
2. Keep the distance between both pointers == N
3. When fast reaches the end, slow will have the nth element from the end

REFERENCE:
1. http://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
'''

import sys
sys.path.append("./mylib/")
import LinkedListLibrary

class LLNode:
	def __init__(self,data):
		self.data = data
		self.next = None


def lastN(node,N):
	fast = node
	slow = node
	fastIndex = 1 #first node
	slowIndex = 1 #first node
	while fast:
		fast = fast.next
		fastIndex +=1
		if fastIndex - slowIndex > N:
			slow = slow.next
			slowIndex +=1
			#difference in index between fast and slow is N
			assert fastIndex-slowIndex == N, "logic error"
	return slow.data


head = LLNode(1)
for i in range(2,6):
	newNode = LLNode(i)
	LinkedListLibrary.Insert2End(head,newNode)

print("input >>>>")
LinkedListLibrary.PrintLinkedList(head)
for N in range(1,6):
	print("Last K (K=%d) = %d" % (N,lastN(head,N)))

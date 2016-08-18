#Question: Find the middle element in a linked list in one pass

'''
OBSERVATION:
1. If there are even #nodes then there would be two middle nodes. We need the second middle.
2. By checking node.next we know there is a valid next node (can make 1 hop)
    - 2.1 Then node.next.next will either return True or False without error!
    - 2.2 Simple logic
3. By checking node we need to check if there is a node.next node and node.next.next
    - 3.1 More checking, logic is more complex    

ALGORITHM:
1. Two pointers fast and slow
2. Initialize fast and slow to the head of the link list
3. Fast pointer hops by 2 nodes and slow pointer hops by 1 node
'''

import sys
sys.path.append("./mylib/")
import LinkedListLibrary

class LLNode:
	def __init__(self,data):
		self.data = data
		self.next = None

def FindMiddle(node):
	slow = node
	fast = node
	#until valid next node 
	while fast.next:
		#2 jump?
		if fast.next.next:
			fast = fast.next.next #reaches end
			slow = slow.next      #reaches middle
		#1 jump - find second middle if #nodes is even
		else:
			fast = fast.next  #reaches end
			slow = slow.next  #reaches middle
	return slow.data


head = LLNode(1)
for i in range(2,7):
	newNode = LLNode(i)
	LinkedListLibrary.Insert2End(head,newNode)



LinkedListLibrary.PrintLinkedList(head)
print("Middle Node = ", FindMiddle(head))


#Delete node from link list

import sys
sys.path.append("../mylib/")
import LinkedListLibrary

class LLNode:
	def __init__(self,data):
		self.data = data
		self.next = None


#Solution 1
def deleteNode1(node,target):
	prev = None
	keepGoing = True
	head = node
	while node and keepGoing:
		if node == target:
			keepGoing = False
			if node == head:
				head = node.next
			else:
				prev.next = node.next
		else:
			prev = node
			node = node.next
	return head

#Solution 2:
#https://medium.com/@bartobri/applying-the-linus-tarvolds-good-taste-coding-requirement-99749f37684a#.ne8bqover
#Not working for end node
def deleteNode(node,target):
	head = node
	while node != target:
		node = node.next
	node = target.next
	if head != target:
		return head
	else:
		return node


head1 = LLNode(1)
head2 = head1
for i in range(2,6):
	newNode = LLNode(i)
	if i == 3:
		head2 = newNode
	LinkedListLibrary.Insert2End(head1,newNode)       

LinkedListLibrary.PrintLinkedList(head1)

print("node to delete >>>", head2.data)

head2 = deleteNode(head1,head2)
LinkedListLibrary.PrintLinkedList(head2)

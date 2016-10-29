
#Delete node from link list

#Inspiration
#https://medium.com/@bartobri/applying-the-linus-tarvolds-good-taste-coding-requirement-99749f37684a#.ne8bqover

import sys
sys.path.append("../mylib/")
import LinkedListLibrary

class LLNode:
	def __init__(self,data):
		self.data = data
		self.next = None


#Solution 1: return head node
#Assumption: target node is always there!
def deleteNode(node,target):
	prev = None
	headNode = node #keep track of the head node
	while node != target:
		prev = node
		node = node.next
	if prev:
		prev.next = node.next
	else:
		#Head node since prev is None!
		headNode = node.next
	return headNode

#Solution 2: No return
#Assumption: target node is always there!
def deleteNode2(node,target):
	prev = None
	while node != target:
		prev = node
		node = node.next
	if prev:                         #not head node
		prev.next = node.next
	elif node.next:                  #head node with next node
		assert prev is None, "logic error"
		tmp = node.next              #reference to next node
		node.data = node.next.data   #deep copy next node
		node.next = node.next.next   #deep copy next node
		tmp.next = None              #remove references to next node
	else: 
		node = None                  #head node ONLY

head1 = LLNode(1)
head2 = head1
for i in range(2,6):
	newNode = LLNode(i)
	if i == 3:
		head2 = newNode
	LinkedListLibrary.Insert2End(head1,newNode)       
LinkedListLibrary.PrintLinkedList(head1)


print("node to delete >>>", head2.data)
deleteNode2(head1,head2)
LinkedListLibrary.PrintLinkedList(head1)

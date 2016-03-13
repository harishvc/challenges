'''
Double Linked List introduction
'''
class LLNode:
  def __init__(self,data):
    self.val = data # contains the data
    self.next = None # contains the reference to the next node
    self.prev = None

#Print Linked List
def PrintLinkedList (node):
	a = []
	while node is not None:
		print(node.val,end=" ")
		if (node.prev is None):
			a.append(node.prev)
		else:
			a.append(node.prev.val)
		node = node.next
	print("")
	print("Linked List (prev values) >>>",a)

#Add to end of linked list
def Insert2End(currentNode,newNode):
    #Traverse linked list until end
    while(currentNode.next is not None):
        currentNode = currentNode.next
    currentNode.next = newNode
    newNode.prev = currentNode #back to previous

a = [1,2,3]
head = LLNode(a[0])
for x in range(1,len(a)):
    Insert2End(head,LLNode(a[x]))

print("Linked List:", end="")
PrintLinkedList(head)

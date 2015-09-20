'''
Reverse linked list recursively
'''

class Node:
  def __init__(self,data):
    self.data = data # contains the data
    self.nextNode = None # contains the reference to the next node

#Print Linked List
def PrintLinkedList (node):
    while node is not None:
        print(node.data,end=" ")
        node = node.nextNode
    print("")
    
#Add to end of linked list
def Insert2End(currentNode,newNode):
    #Traverse linked list until end
    while(currentNode.nextNode is not None):
        currentNode = currentNode.nextNode
    currentNode.nextNode = newNode
    

def ReverseRecursive(next, previous):
    if (next is None):
        return previous
    #pass next node and previous node
    head = ReverseRecursive(next.nextNode,next)
    next.nextNode = previous
    return head

def ReverseIterative(node):
    prev = None
    while (node):
        tmp = node
        node = node.nextNode
        tmp.nextNode = prev
        prev = tmp
    return prev
    
    
#Initialize the Linked List
inputs = [1,2,3,4,5]
head = Node(inputs[0])
for x in range(1,len(inputs)):
    currentNode = head
    Insert2End(currentNode,Node(inputs[x]))

#Print Linked List 
print("Linked List:")
PrintLinkedList(head)

head=ReverseRecursive(head, None)
print("Reversed Linked List (recursive):")
PrintLinkedList(head)


head=ReverseIterative(head)
print("Reversed Linked List (iterative):")
PrintLinkedList(head)

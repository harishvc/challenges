'''
Linked List Introduction: Initialize, Insert, Delete & Print
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

def DeleteNode(headNode,data):
    n = headNode
    #Scenario 1: head node
    if (n.data == data):
        return(n.nextNode)
    #Scenario 2: 
    while(n.nextNode is not None):
        if (n.nextNode.data == data):
            n.nextNode = n.nextNode.nextNode
            return(headNode)    
        else:
            n = n.nextNode
    #Scenario 3: Not found
    print(data," Not found!")
    return headNode
    
#Initialize the Linked List
inputs = [1,2,3,4,5]
head = Node(inputs[0])
for x in range(1,len(inputs)):
    currentNode = head
    Insert2End(currentNode,Node(inputs[x]))

#Print Linked List
print("Linked List (insert to end):")
PrintLinkedList(head)

#Delete from Linked List
remove = 3
head = DeleteNode(head, remove)
print("Linked List (after deleting %d):" %(remove))
PrintLinkedList(head)

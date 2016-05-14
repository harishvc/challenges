'''
Remove duplicate values & retain order of existing values
'''

class LinkedListNode:
  def __init__(self,data):
    self.val = data # contains the data
    self.next = None # contains the reference to the next node

#Print Linked List
def PrintLinkedList (node):
    while node is not None:
        print(node.val,end=" ")
        node = node.next
    print("")
    
#Add to end of linked list
def Insert2End(currentNode,newNode):
    #Traverse linked list until end
    while(currentNode.next is not None):
        currentNode = currentNode.next
    currentNode.next = newNode

def optimalList(headNode):
    seen = set()
    start = headNode
    behind = headNode #one step behind to handle case #3
    while start is not None:
        #case 1: new value
        if (start.val not in seen):
            seen.add(start.val)
            behind = start
            start = start.next
        #case 2: seen before and value not at end
        elif (start.next is not None):
            start.val = start.next.val
            start.next = start.next.next  #IMPORTANT!
        #case 3: seen before and value at end
        else:
            behind.next=None
            start=None #IMPORTANT!

a = [3,4,3,2,6,1,2,6]
headNode = LinkedListNode(a[0])
for x in range(1,len(a)):
    Insert2End(headNode,LinkedListNode(a[x]))
print("input >>> ", end="")
PrintLinkedList(headNode)
optimalList(headNode)
print("unique values >>> ", end="")
PrintLinkedList(headNode)

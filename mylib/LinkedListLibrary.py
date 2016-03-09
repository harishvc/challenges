'''
Linked List Libraries

class Node:
  def __init__(self,data):
    self.val = data # contains the data
    self.next = None # contains the reference to the next node

'''

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

#Find mid node, last node and their index positions
def findMidLast(headNode):
    start = headNode
    slow  = headNode
    fast  = headNode
    midIndex = 1
    lastIndex = 1
    #edge case: 1 node
    if(headNode.next is None):
        return(headNode,1,headNode,1)
    #edge case: 2 node
    if(headNode.next.next is None):
        return(headNode,1,headNode.next,2)
    while(fast.next is not None):
        slow = slow.next
        midIndex += 1
        if (fast.next.next is not None):
            fast = fast.next.next
            lastIndex += 2
        else:
            fast = fast.next
            lastIndex += 1
    return (slow,midIndex,fast,lastIndex)


#Reverse linked list
def reverseLinkedList(next,previous=None):
    if (next is None):
        return previous
    #pass next node and previous node
    head = reverseLinkedList(next.next,next)
    next.next = previous
    return head

#Split a linked list given start and size
def splitLinkedList(headNode,size):
    if (size == 0):
        return Node(None)
    if (size == 1):
        return Node(headNode.val)
    count = 0
    newNode = Node(headNode.val)
    headNode = headNode.next
    count += 1
    while (count < size):
        Insert2End(newNode,Node(headNode.val))
        headNode = headNode.next
        count += 1
    return newNode


#Merge two linked list into one
def mergeLinkedList(t1,t2):
    newNode = Node(t1.val)
    t1 = t1.next
    Insert2End(newNode,Node(t2.val))
    t2 = t2.next
    while(t1 is not None and t2 is not None):
        Insert2End(newNode,Node(t1.val))
        t1 = t1.next
        Insert2End(newNode,Node(t2.val))
        t2 = t2.next
    while(t1 is not None):
        Insert2End(newNode,Node(t1.val))
        t1 = t1.next
    return newNode

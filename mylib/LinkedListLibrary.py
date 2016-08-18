'''
Linked List Libraries

class LLNode:
  def __init__(self,data):
    self.data = data
    self.next = None

'''

#Print Linked List
def PrintLinkedList(list):
	while list is not None:
		if list.next is not None:
			print(list.data,end=" -> ")
		else:
			print(list.data,end="\n")
		list = list.next

#Add to end of linked list
def Insert2End(currentNode,newNode):
    #Traverse linked list until end
    while(currentNode.next is not None):
        currentNode = currentNode.next
    currentNode.next = newNode

#Deep copy a list
def deepCopy(current,new):
    newNodeHead = None
    while(current is not None):
        if (new is None):
            new = Node(current.val)
            newNodeHead = new
        else:
            new.next = Node(current.val)
            new = new.next
        current = current.next
    return newNodeHead

#Delete node
def delete(headNode,value):
        currentNode = headNode
        lastNode = None #reference to last node
        while currentNode is not None and currentNode.data != value:
            lastNode = currentNode
            currentNode = currentNode.next
        #case 1: value not found
        if (currentNode is None):
            return headNode
        #case 2: head node
        elif(lastNode is None):
            headNode = currentNode.next
            currentNode.next = None #remove reference
            return headNode
        #case 3: last node
        elif(currentNode.next is None):
            lastNode.next = None #remove reference
            return headNode
        #case 4: some where between head and tail
        else:
            lastNode.next = currentNode.next
            currentNode.next = None #remove reference
            return headNode


#Find mid node, last node
#slow pointers -> one hop
#fast pointer -> two hops
#when fast pointer reaches end, slow pointer is in the middle
#Time complexity O(n)
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

#Find max value
def findMax(node):
    maxNode = LinkedListNode(None)
    while node is not None:
        print("comparing ,,,,", maxNode.val,node.val)
        if maxNode.val is None:
            maxNode = node
        elif (node.val > maxNode.val):
                maxNode = node
        node = node.next
    return maxNode


#pop first node from linked list
def popFirst(headNode):
    tmp = headNode.next
    headNode.next = None
    return tmp


#Remove duplicate values, retain order of existing values
#input >>>  3 4 3 2 6 1 2 6 
#output >>> 3 4 2 6 1
def optimalList(headNode):
    seen = set()
    start = headNode
    behind = headNode #one step behind to handle case #3
    while start is not None:
        #case 1: new value
        if (start.data not in seen):
            seen.add(start.data)
            behind = start
            start = start.next
        #case 2: seen before and value not at end
        elif (start.next is not None):
            start.data = start.next.data
            start.next = start.next.next  #IMPORTANT!
        #case 3: seen before and value at end
        else:
            behind.next=None
            start=None #IMPORTANT!

'''
Question: Find the middle element in a linked list in one pass
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

#slow pointers -> one hop
#fast pointer -> two hops
#when fast pointer reaches end, slow pointer is in the middle
#Time complexity O(n/2)
def FindMiddle(n):
        slow = n
        fast = n
        while(fast is not None):
            #print(slow.data,fast.data)
            slow = n
            if (fast.nextNode is not None and fast.nextNode.nextNode is not None):
                fast = fast.nextNode.nextNode
            elif(fast.nextNode is not None):
                fast = fast.nextNode
            else:
                fast = None
            n = n.nextNode
        return slow.data


#Initialize the Linked List
inputs = [1,2,3,4,5,6,7]
head = Node(inputs[0])
for x in range(1,len(inputs)):
    Insert2End(head,Node(inputs[x]))

print("Linked List:", end="")
PrintLinkedList(head)
print("Middle value =",FindMiddle(head))
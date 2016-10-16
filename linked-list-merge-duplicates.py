#Return a linked list that contains the intersection of two linked lists

class Node:
  def __init__(self,data):
    self.data = data # contains the data
    self.next = None # contains the reference to the next node

#Print Linked List
def PrintLinkedList (node):
    while node is not None:
        print(node.data,end=" ")
        node = node.next
    print("")
    
#Add to end of linked list
def Insert2End(currentNode,newNode):
    #Traverse linked list until end
    while(currentNode.next is not None):
        currentNode = currentNode.next
    currentNode.next = newNode

'''
Assumtions:
 1. Linked list are sorted with numbers
 2. Linked list are almost the same length
 3. Values can be modified
 4. New linked list created from one of the two linked lists
 5. Remove references to old link list (garbage collection)
'''
def MergeDuplicates(nodeA,nodeB):
    #nodeA will hold the result
    resultHead = None
    result =  None
    while nodeA and nodeB:
        if nodeA.data == nodeB.data:  #match
            tmp = nodeA  #nodeA will hold the result 
            nodeA = nodeA.next
            nodeB = nodeB.next
            if resultHead is None:
                resultHead = tmp
                result = tmp
                result.next = None
            else:
                result.next = tmp
                result = tmp
                result.next = None
        elif nodeA.data > nodeB.data:
            nodeB = nodeB.next
        else:
            nodeA = nodeA.next
    return resultHead


#Initialize the Linked List
inputs = [1,3,7,11]
head = Node(inputs[0])
for x in range(1,len(inputs)):
    currentNode = head
    Insert2End(currentNode,Node(inputs[x]))


inputs2 = [3,9,10,11]
head2 = Node(inputs2[0])
for x in range(1,len(inputs2)):
    currentNode = head2
    Insert2End(currentNode,Node(inputs2[x]))


print("input 1 >>")
PrintLinkedList(head)

print("input 2 >>")
PrintLinkedList(head2)

headMerged = MergeDuplicates(head,head2)
print("union >>")
PrintLinkedList(headMerged)


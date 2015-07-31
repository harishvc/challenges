#Question: Reverse a Linked List

class Node:
  def __init__(self,data):
    self.data = data # contains the data
    self.nextNode = None # contains the reference to the next node

#Initialize
def InitializeLinkedList(input):
    MyList = Node(input[0])
    current = MyList
    for i in range(1,len(input)):
        new_node = Node(input[i])
        current.nextNode = new_node
        current = new_node 
    return MyList

#Print Linked List
def PrintLinkedList (node):
    while node is not None:
        print(node.data,end=" ")
        node = node.nextNode

#Reverse Linked List
#http://linearspacetime.blogspot.com/2012/05/reverse-linked-list-without-using.html
def ReverseLinkedList(node):
    zero = node;
    one = zero.nextNode
    two = one.nextNode
    zero.nextNode = None
    while (one is not None):
        #Reverse the direction
        one.nextNode = zero
        # Move the pointers
        zero = one
        one = two
        if (two is not None):
            two = two.nextNode
    return zero


#Initialize the Linked List
inputs = ["ABCCBA", "123456", "122", "1221"]
for input in inputs:
    #Initialize
    MyList = InitializeLinkedList(input)
    PrintLinkedList(MyList)
    print (">>>>> ", end="")
    PrintLinkedList(ReverseLinkedList(MyList))
    print(" ")
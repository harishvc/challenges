#Question: Check if a Linked List is a Palindrome

'''
Reference: http://www.careercup.com/question?id=13489670
Algorithm:

Step 1. Find the middle element of the linked list - This can be done in linear time by moving two pointers; one at 1x speed and the other at 2x speed. 
The pointer moving at 1x points to the middle when thepointer moving at 2x hits the end. 

Step 2: Reverse the second part of the linked list (from middle to end) using recursion - This can be done in linear time. 
Refer to linearspacetime.blogspot.com/#!/2012/05/reverse-singly-linked-list.html 

Step 3: Use two pointers; one from the original start node and the other from the start of now reversed second part of the list. 
Move those pointers to their next nodes and compare. If they are equal till they hit the middle portion of the list, 
the linked list contains a palindrome. 
'''

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

def FindMiddleLinkedList(MyList):
    middle = MyList
    end = MyList
    while end is not None and end.nextNode is not None:
        if (end.nextNode.nextNode is not None):
            end = end.nextNode.nextNode
            middle = middle.nextNode
        else:
            end = end.nextNode
            middle = middle.nextNode  #setting up for step 2
    return(middle)
    
#Compare two linked lists
def CompareTwoLinkedLists(string1, string2):
    while (string1 is not None and string2 is not None):
        if (string1.data == string2.data):
            string1 = string1.nextNode
            string2 = string2.nextNode
        else:
            return("not palindrome")
    return("palindrome")


#Initialize the Linked List
inputs = ["ABCCBA", "123456", "122", "1221"]
for input in inputs:
    #Initialize
    MyList = InitializeLinkedList(input)
    PrintLinkedList(MyList)

    #Step1: Find middle of linked list
    string1 = MyList
    middle = FindMiddleLinkedList(MyList)

    #Step 2:
    string2 = ReverseLinkedList(middle)
    #PrintLinkedList(string2)    

    #Step 3:
    print(">>>> " , CompareTwoLinkedLists(string1, string2))

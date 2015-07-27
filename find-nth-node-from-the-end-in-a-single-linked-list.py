#Question: Given a linked list. Find the nth node from the end.

#Reference:http://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
#Algorithm:
#"Maintain two pointers – reference pointer and main pointer. Initialize both reference and main pointers to head. 
# First move reference pointer to n nodes from head. Now move both pointers one by one until reference pointer reaches end. 
# Now main pointer will point to nth node from the end. Return main pointer."
#
#1. Two pointers (reference,main) initialized to start
#2. Iterate (i) the list
#    - when i=N , reference = i
#       - continue to move reference and main for each iteration 
#       - when reference reaches the end, main will have the nth element from the end
        
#Solution
class Node:
  def __init__(self):
    self.data = None # contains the data
    self.nextNode = None # contains the reference to the next node
                    
#Print linked list
def PrintLinkedList (node):
    while node is not None:
        print(node.data,end=" ")
        node = node.nextNode

#Find Last N node
def FindLastN(MyList,N):
    r = MyList  #reference 
    m = MyList  #main
    i = 1
    move = False
    while r is not None:
        r = r.nextNode
        if(move):
            m = m.nextNode
        if(i == N): #Handle array starting at position 0
            move = True
        i += 1
    return m.data


#Create a linked list
MyList = Node()
MyList.data = 1
N = 3    #location from end

#Initialize a linked list with 9 elements
current = MyList
for i in range(2,11):
  new_node = Node()
  new_node.data = i
  current.nextNode = new_node
  current = new_node  

print("Input ... ", end=" ")
PrintLinkedList(MyList)
print("")
print(N , "element from end of input ===>", FindLastN(MyList,N))

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
def findLastN(head,N):
	fast = head
	slow = head
	count = 0
	#IMPORTANT: Iterator end is fast.next
	while fast.nextNode is not None:
		fast = fast.nextNode
		count +=1
		#IMPORTANT: >=, spacing N
		if count >= N:
			slow = slow.nextNode
			#print("count=%d slow=%d fast=%d" % (count,slow.data,fast.data))
	return slow.data


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
print(N , "element from end of input ===>", findLastN(MyList,N))

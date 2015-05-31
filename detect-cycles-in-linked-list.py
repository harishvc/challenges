#Question: Given a linked list detect if it contains a cycle. If so find the cycle length and the first node when the cycle begins

from random import randint

class Node:
  def __init__(self):
    self.data = None # contains the data
    self.nextNode = None # contains the reference to the next node
    
#Print node #, node data, next node data    
def PrintLinkedList (head):
    current = head
    endList = False
    cnt = 0
    hashMap = {}  #handle cycles
    while (endList == False):
        cnt += 1
        #Next node data
        if (not current.nextNode):
            nnd = None
        else:
            nnd = current.nextNode.data
        #Print node #, node data, next node data    
        print (cnt, current.data, nnd)
        if (current.nextNode != None and (not hashMap.get(current.nextNode)) ):
            current = current.nextNode
            hashMap[current] = current.data #store visited node
        else:
            endList = True
           
#Solution 1                        
#http://pythonfiddle.com/check-linked-list-cycle/                        
#Time & Space complexity: O(n), where n is # of nodes
def detectCycle(head):   
  toReturn = None
  foundCycle = False
  current = head
  hashMap = {}
  cnt = 0
  while current.nextNode and not foundCycle:
    cnt += 1  
    if not hashMap.get(current):  
      hashMap[current] = cnt   #store node address and location as hash
      current = current.nextNode  
    else:
      foundCycle = True
      toReturn = "Yes. Node %d cycles to node %d" % (cnt-1, hashMap[current]) 
  return toReturn
    
#Solution 2
#http://jelices.blogspot.com/2014/05/leetcode-python-linked-list-cycle.html
#Time Complexity: O(n) where n is # of nodes, Space complexity: O(1)
def is_circular(head):
    slow = head
    fast = head
    cnt = 0
    while fast != None and fast.nextNode != None:
            fast = fast.nextNode.nextNode
            slow = slow.nextNode
            cnt += 1   #cycle length!
            if fast == slow:
                #Where does the cycle start
                #Reference: http://nghiaho.com/?p=2063
                slow = head  #set slow to head node and start iterating nodes
                CSN = 1  #cycle start node
                while fast != slow: 
                    fast = fast.nextNode
                    slow = slow.nextNode
                    CSN += 1
                return "Yes. Cycle length = %d. First node of cycle = %d" % (cnt,CSN) 
    return False

# create a linked list without a cycle    
nonCycle = Node()
nonCycle.data = randint(1,26)
current = nonCycle
for i in range(2,10):
  new_node = Node()
  new_node.data = randint(1,26)
  current.nextNode = new_node
  current = new_node  

# create a linked list with a cycle    
cycle = Node()
cycle.data = randint(1,26)
current = cycle
four = None  #cycle
for i in range(2,10):
  new_node = Node()
  new_node.data = randint(1,26)
  current.nextNode = new_node
  current = new_node
  if i == 4: four = new_node#implement cycle
  if i == 9: new_node.nextNode = four        #node 9 points to node 4

    
#PrintLinkedList(nonCycle)            
print ("1. Found cycle? ", detectCycle(nonCycle))
print ("2. Found cycle? ", is_circular(nonCycle))

#PrintLinkedList(cycle)
print ("3. Found cycle? ", detectCycle(cycle))
print ("4. Found cycle? ", is_circular(cycle))

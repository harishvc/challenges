'''
Design and implement Least Used Cache (LRU)
REFERENCE:
http://mcicpc.cs.atu.edu/archives/2012/mcpc2012/lru/lru.html
'''

'''
Implement Least Recentry Used Cache (LRU)
CONSTRAINTS:
1. get and set values on constant time
2. evict (open up space) in < O(n)
DESIGN:
1. Hash can provide constant time for set() and get()
2. Listing of key-value of based on least recently used needs to be stored in a different data structure
   2.1. A linked list can be used to store this information. Head node can point to linked list nodes listed by access time
3. When a key already present get's set again, it needs to move to the head of the linked list
   3.1  Using a double linked list will help achieve the desired time complexity since we don't need to traverse
        the linked list to find the prior node
   3.2 A double linked list can also achieve desired time complexity while removing LRU key value pair
4. Each node in the link list will contain
   4.1 data, prev node, next node, reference to the key in the dictionary
   4.2 reference to the key in the dictionary is critical to remove keys when their values are removed from the linked list
ALGORITHM:
1. set(key,value):
   - Create DLL node with key, value
   - Move DLL node to head (most recently used)
   - Store reference to DLL node in the hash
2. get(key)
   - Get DLL node from hash
   - Move DLL node to head (most recently used)
   - return value from DLL node
3. evict() - remove the least used node, called internally by set()
   - remove DLL node
   - update size
   - remove hash key   
'''
class DLL:
	def __init__(self,key,data):
		self.data = data
		self.next = None
		self.prev = None
		self.key = key  #reference to hash key

class LRU:
	def __init__(self,capacity):
		self.keys = {}  #hash of keys and values
		self.capacity = capacity
		self.size = 0
		self.head = None #pointer to the first DLL (MRU)

	def set(self,key,value):
		#TODO: Check if key already exists
		#step 1: create DLL
		node = DLL(key,value)
		#step 2: match hash key with DLL (value)
		self.keys[key] = node
		#step 3: move DLL to the head
		if (self.size == 0): #first node
			self.head = node
		else:
			self.insertHead(node)
		self.size += 1

	def get(self,key):
		#step 1: move node containing the key to the head
		node = self.keys[key]
		#case 1: node has prev and next
		if node.prev and node.next:
			node.prev.next = node.next
			node.next.prev = node.prev
			node.prev=None
			node.next=None
			self.insertHead(node)
		#case 2: node is at the end		
		elif node.next is None:
			t = node.prev
			t.next = None
			node.prev = None
			self.insertHead(node)
		#case 3: node at top  - nothing to do!
		return node.data
	
	def insertHead(self,node):
		t = self.head
		self.head = node
		node.next = t
		t.prev = node

	def evict(self):
		node = self.head
		#IMPORTANT: Find node before last node
		while node.next.next:
			node = node.next
		tmp= node.next
		#delete DLL and reference
		del self.keys[tmp.key] #remove hash key
		node.next = None #update node before last node
		self.size -= 1 #reduce size

	def size(self):
		return self.size

	def print(self):
		node = self.head
		while node:
			print(node.data,end=" ")
			node = node.next
		print("")

myLRU = LRU(5)
myLRU.set(1,1)
myLRU.set(2,2)
myLRU.set(3,3)
print(">LRU Size:", myLRU.size)
print(">LRU Values >>",end="")
myLRU.print()
print(">get ", myLRU.get(2))
print(">LRU Values >>",end="")
myLRU.print()
print(">Evict")
myLRU.evict()
print(">LRU size:", myLRU.size)
print(">LRU Values >>",end="")
myLRU.print()

#Implement a function that inserts, deletes and getrandom in O(1)

'''
Source: https://leetcode.com/problems/insert-delete-getrandom-o1/

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 1 is the only number in the set, getRandom always return 1.
randomSet.getRandom();
'''

'''
NOTES/OBSERVATION

Operation       key_to_index (dictionary)             index_to_key (list)    
insert(A)       A->0                                  [0]=A 
insert(B)       A->0,B->1                             [0]=A,[1]=B
insert(C)       A->0,B->1,C->2                        [0]=A,[1]=B,[2]=C
remove(B)       A->0,C->1                             [0]=A,[1]=C
remove(C)       A->0                                  [0]=A 

Limitation:
1. only works if KEYS are unique
'''



class randomSet():
	def __init__(self):
		self.key_to_index = {} #store key and mapping index in index_to_key
		self.index_to_key = [] #store key in each index (random generator)
		self.index_to_key_size = 0
		self.random_start = 0 

	def insert(self,key):
		if key in self.key_to_index.keys():
			return False  #key already there!
		else:
			#new key
			self.key_to_index[key] = self.index_to_key_size
			self.index_to_key.insert(self.index_to_key_size,key) 
			self.index_to_key_size += 1
			return True

	def remove(self,key):
		if key not in self.key_to_index.keys():
			return False #key does not exits
		else:
			index_position = self.key_to_index[key]  
			last_key = self.index_to_key.pop() 
			self.index_to_key_size -= 1
			#IMPORTANT: Handle remove the last key!!!     
			if index_position != self.index_to_key_size:
				self.index_to_key[index_position] = last_key
				self.key_to_index[last_key] = index_position
			else:
				assert last_key == key, "logic error"
			#IMPORTANT: Delete key
			del self.key_to_index[key]
			return True

	def getRandom(self):
		#start over
		if self.random_start >= self.index_to_key_size:
			self.random_start = (self.random_start)%self.index_to_key_size
		myreturn = self.index_to_key[self.random_start]
		self.random_start +=1
		return myreturn

randomSet = randomSet()
print("Insert 1, insert=%s random=%s" % (randomSet.insert(1), randomSet.getRandom()))
print("Insert 2, insert=%s random=%s" % (randomSet.insert(2), randomSet.getRandom()))
print("Insert 3, insert=%s random=%s" % (randomSet.insert(3), randomSet.getRandom()))
print("Remove 3, status=%s" % (randomSet.remove(3)))
print("Remove 3, status=%s" % (randomSet.remove(3)))
print("Random #=%d" % (randomSet.getRandom()))
print("Remove 2, status=%s" % (randomSet.remove(2)))
print("Random #=%d" % (randomSet.getRandom()))


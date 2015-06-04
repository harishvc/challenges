#Question:Design and implement Least Used Cache (LRU)
#Excellent explanation
#http://mcicpc.cs.atu.edu/archives/2012/mcpc2012/lru/lru.html

import collections
#Source:http://www.kunxi.org/blog/2014/05/lru-cache-in-python/
#Solution 1: 
# Advantages: Constant time for storage and time , simplicity
# Disadvantages: Emphasis on timestamp. So there may be a situation where keys access frequently at the start but not actively latter will be removed
class LRUCache1:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

#     def get(self, key):
#         try:
#             value = self.cache.pop(key)
#             self.cache[key] = value
#             return value
#         except KeyError:
#             return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)  #Always pop
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)  #Remove element added first, similar to queue
        self.cache[key] = value  #Always insert, ordered dictionary keeps track of the order
                
    def print(self,state):
        print("%s ---> " % (state) ,end="")
        for key in (self.cache):
            print (key,end=" ")
        print ("")        


#Solution: 2
#Disadvantages: Two dictionaries, time to find the entry with the least timestamp
class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0        #timestamp
        self.cache = {}    #dictionary to store key, value  
        self.lru = {}      #dictionary to sore  key, timestamp

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])  #find key with minimum timestamp in dictionary!
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm   #timestamp
        self.tm += 1  #increment timestamp

    def print(self,state):
        print("%s ---> " % (state) ,end="")
        for key in (self.cache):
            print (key,end=" ")
        print ("")        

input = 'ABC!D!BE!DEF!'
        
start1 = LRUCache1(3)
print ("Solution 1")
for i,x in enumerate(list(input)):
    if (x == "!"):
        start1.print(input[0:i])
    else:
        start1.set(x,1)      

start2 = LRUCache2(3)
print ("Solution 2")
for i,x in enumerate(list(input)):
    if (x == "!"):
        start2.print(input[0:i])
    else:
        start2.set(x,1)      



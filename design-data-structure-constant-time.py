'''
Question: Design a data structure that provides insert, remove, contains and get random operations in O(1) time

Reference: 
1. http://stackoverflow.com/questions/196017/unique-non-repeating-random-numbers-in-o1

Follow up questions:
1. unique values - dictionary keys collision
2. delete - last inserted value or user can provide any value?
3. random - can deleted values get returned back?
'''

import random

class Awesome(object):
    def __init__(self,data):
        self.hash = {}  #dictionary for insert,delete,lookup (constant time)
        self.size = 0   #count 
        self.list = []  #list for generating a random value
        self.list.insert(self.size,data) #insert value at a specific position
        self.hash[data] = self.size     #store index position as value in hash
        self.size += 1
        
    def insert(self,data):
        self.list.insert(self.size,data) #insert value at a specific position
        self.hash[data] = self.size       #store index position as value in hash
        self.size += 1                     #size is +1

    
    def remove(self,data):
        index_location = self.hash[data]    #find index position in the list
        last_index = self.Asize()-1         #since we are using index 0
        tmp = self.list[index_location]     #last value in list
        self.list[index_location] = self.list[last_index] #copy value in last index
        self.list[last_index] = tmp #copy value to be deleted to the last index
        self.hash[self.list[index_location]] = index_location #update index position
        del self.hash[data]
        self.size -= 1 #reduce size of list
        
    def contains(self,data):
        return(data in self.hash)
    
    def random(self):
        print("random seed .......", random.randrange(self.size))
        return self.list[random.randrange(self.size)]

    def Asize(self):
        return self.size
    
    def Aprint(self):
        print("HASH >>> ",end=" ")
        for keys in self.hash:
            print("%d:%d" % (keys,self.hash[keys]),end=" ")
        print(" LIST >>> ", self.list)
        
        
x = Awesome(5)

#Insert
print("Insert 5")
print("New data structure & size ")
x.Aprint()  
print("size:",x.Asize())  
print("###########") 

x.insert(10)
print("Insert 10")
print("New data structure & size ")
x.Aprint()  
print("size:", x.Asize())   
print("###########") 

x.insert(15)
print("Insert 15")
print("New data structure & size ")
x.Aprint()
print("size:", x.Asize())   
print("###########") 

#Contains
print("Is 10 contained? ", x.contains(10))
print("Is 20 contained? ", x.contains(20))

#Delete
print("removing 10 ...")
x.remove(10)
print("New data structure & size ")
x.Aprint()  #Aprint does not work!!!
print("size:", x.Asize())


#Random
print("Random value:", x.random())   


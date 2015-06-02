#Question: Implement a queue using two stacks
#Observation:
#Two stacks chained together will return the elements in the same order
#Algorithm:
# 1. Two stacks s1 & s2
# 2. Enqueue: push to s1
# 3. Dequeue: if s2 not empty pop from s2  
#              if s2 empty copy all elements from s1 to s2 and then pop


#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter05queues/QueueWithStacks.py
# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Queue(object):
    def __init__(self):
        self.S1 = []
        self.S2 = []
     
    def enqueue(self, data):
        print("inserting data... %d" % (data))
        self.S1.append(data)
    
    def dequeue(self):
        if not self.S2:
            while self.S1:
                self.S2.append(self.S1.pop())
        return self.S2.pop() 
	    
q = Queue()
for i in range(5):
    q.enqueue(i)
for i in range(5):
    print("returning data ...", q.dequeue()) 


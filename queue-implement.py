#Implement queue using lists (arrays)

class Queue(object):

    def __init__(self):
        self.myqueue = []
        self.size = 0
           
    def isEmpty(self):
        return self.size <= 0

    def add(self, item):
            self.myqueue.append(item)
            self.size +=1

    def remove(self):
        if self.size <= 0:
            print('Queue Underflow!')
            return -1
        else:
            self.size -=1
            return self.myqueue.pop(0)
            
    def peek(self):
        if self.size <= 0:
            print('Queue Underflow!')
            return -1
        else:
            return self.myqueue[0]
            
    def mysize(self):
        return self.size
       

input = [1,2,3,4,5]
demoQueue = Queue()
for i in input:
    demoQueue.add(i)
    print("Add: ", i, " Queue size: ", demoQueue.mysize())
print("~~~")    
for i in range(0,demoQueue.mysize()):
    print("Remove:  ", demoQueue.remove(), " Queue size: ", demoQueue.mysize())

'''
Stack: 
1. Stack uses LIFO (Last in First Out) ordering
2. Constant time to add and remove elements since no internal shifting around
3. Does not offer constant time to access elements at position i unlike list/array
4. Operations in constant time
   push() 
   pop()
   peek()
   isEmpty()
   size()  
'''
#Stack Implementation using list/array
class Stack(object):

    def __init__(self):
        self.mystack = []
        self.size = 0
        
    def isEmpty(self):
        return self.size <= 0

    def push(self, item):
            self.mystack.append(item)
            self.size +=1

    def pop(self):
        if self.size <= 0:
            print('Stack Underflow!')
            return -1
        else:
            self.size -=1
            return self.mystack.pop()
            
    def peek(self):
        if self.size <= 0:
            print('Stack Underflow!')
            return -1
        else:
            return self.mystack[-1]
            
    def mysize(self):
        return self.size
     

input = [1,5,3,4,2]
demoStack = Stack()
for i in input:
    demoStack.push(i)
    print("Push: ", i, " Stack size: ", demoStack.mysize())
    
for i in range(0,demoStack.mysize()):
    print("Pop: ", demoStack.pop(), " Stack size: ", demoStack.mysize())

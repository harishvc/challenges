#Stack implementation using list

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
     

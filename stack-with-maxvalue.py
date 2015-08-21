'''
Question: Implement a stack with getMax() function that returns back the max value and operates in O(1) time

Observation:
1. Max value changes happen during push or pop
2. Values can be stored in a Max heap and root of the max heap contains the max value. 
   Inserting a new max value has time complexity of 0(log n) and space complexity is O(n) 
3. Max value could be stored in another stack and updated during push and pop. Time complexity is O(1) and space complexity is O(n)

Output:
Push:  1  Stack size:  1  Max Value:  1
Push:  2  Stack size:  2  Max Value:  2
Push:  4  Stack size:  3  Max Value:  4
Push:  3  Stack size:  4  Max Value:  4
Push:  5  Stack size:  5  Max Value:  5
####
Pop:   5  Stack size:  4  Max Value:  4
Pop:   3  Stack size:  3  Max Value:  4
Pop:   4  Stack size:  2  Max Value:  2
Pop:   2  Stack size:  1  Max Value:  1
'''

class Stack(object):

    def __init__(self):
        self.mystack = []
        self.size = 0
        self.maxstack = [] #list for storing max value
           
    def isEmpty(self):
        return self.size <= 0

    def push(self, item):
            self.mystack.append(item)
            self.size +=1
            #Store max value in the max stack
            if (self.size == 1):
                self.maxstack.append(item)
            elif (item > self.getMax()):
                self.maxstack.append(item)
            else:
                self.maxstack.append(self.getMax())

    def pop(self):
        if self.size <= 0:
            print('Stack Underflow!')
            return -1
        else:
            self.size -=1
            tmp = self.maxstack.pop()
            return self.mystack.pop()
            
    def peek(self):
        if self.size <= 0:
            print('Stack Underflow!')
            return -1
        else:
            return self.mystack[-1]
            
    def mysize(self):
        return self.size
     
    
    def getMax(self):
        if self.size <= 0:
            print('max stack empty - Stack Underflow!')
            return -1
        else:
            return self.maxstack[-1]

input = [1,2,4,3,5]
demoStack = Stack()
for i in input:
    demoStack.push(i)
    print("Push: ", i, " Stack size: ", demoStack.mysize(), " Max Value: ", demoStack.getMax())
print("####")    
for i in range(0,demoStack.mysize()-1):
    print("Pop:  ", demoStack.pop(), " Stack size: ", demoStack.mysize(), " Max Value: ", demoStack.getMax())

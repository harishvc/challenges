#Implement stack using dynamic array
#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter04stacks/StackWithDynamicArrays.py

class Stack(object):
	def __init__(self, limit=10):
		self.stk = limit * [None]
		self.limit = limit	

	def isEmpty(self):
		return len(self.stk) <= 0

	def push(self, item):
		if len(self.stk) >= self.limit:
			self.resize() #RESIZE!!!!
		self.stk.append(item)
		print ('Stack after Push', self.stk)

	def pop(self):
		if len(self.stk) <= 0:
			print ('Stack Underflow!')
			return 0
		else:
			return self.stk.pop()
			
	def peek(self):
		if len(self.stk) <= 0:
			print ('Stack Underflow!')
			return 0
		else:
			return self.stk[-1]
			
	def size(self):
		return len(self.stk)

	def resize(self):
		newStk = list(self.stk)
		self.limit = 2 * self.limit 
		self.stk = newStk
		
our_stack = Stack(5)
our_stack.push("1")
our_stack.push("21")
our_stack.push("14")
our_stack.push("11")
our_stack.push("31")
our_stack.push("14")
our_stack.push("15")
our_stack.push("19")
our_stack.push("3")
our_stack.push("99")
our_stack.push("9")
print (our_stack.peek())
print (our_stack.pop())
print (our_stack.peek())
print (our_stack.pop())
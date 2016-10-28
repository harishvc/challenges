#Expression evaluator that handles + , * and single digits
#http://www.geeksforgeeks.org/expression-evaluation/

# 1 + 4 * 6 = 25
# 1 + 4 * 6 + 9  + 6 * 1 = 34

'''
Logic: 
1. Hold on the value(s) seen so far
2. operator determines what to do next
   - + , push last seen value in stack, reset multiple flag
   - * , set mutiply flag
   - digit
        - if multiply flag set then multiply with value(s) seen so far 
        - else (no multiple flag), hold on to the digit
3. pop all the values from stack and add to holding digit
'''

def expressionEvaluator(a):
	mysum = 0
	mystack = []
	multiplyFlag = False
	for c in a:
		if c == "+":
			multiplyFlag = False  #end of multiple
			mystack.append(mysum)
			mysum = 0 #reset mysum
		elif c == "*":
			multiplyFlag = True
		elif multiplyFlag:
			mysum = mysum * int(c) #keep going
		else:
			mysum = int(c) #append to stack

	#sum all the values in stack + mysum		
	while mystack:
		mysum += mystack.pop()

	return mysum	

a = ["1+4*6+9" , "1+5*2*3*4+5+1"]
for a2 in a:
	print("%s >>> %d" % (a2,expressionEvaluator(a2)))

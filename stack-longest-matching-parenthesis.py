'''
Find the length of the longest valid parenthesis sequence in a string, in O(n) time

#http://stackoverflow.com/questions/25952326/find-the-length-of-the-longest-valid-parenthesis-sequence-in-a-string-in-on-t/35954710#35954710
'''

'''
ALGORITHM:
1. Add ( to (imaginary) stack and keep track of stack size
2. When you see ) either you have a match or no match
   a. if stack size > 0 (match), pop from stack, increment current max length by 2
   b. if stack size <= 0 (no match), check current max length with result and reset current max length
'''
def longestMatchingParenthesis(a,size):
	current = 0
	currentMaxlength = 0
	result = 0
	mystack = []
	mystacksize = 0
	while (current < size):
		if (a[current] == "("):
			#mystack.append(a[current])
			mystacksize += 1
		else:
			#case 1: matching right
			if (mystacksize > 0):
				#mystack.pop()
				mystacksize -= 1
				currentMaxlength +=  2
			#case 2: no match!
			else:
				if (currentMaxlength > result):
					result = currentMaxlength
				currentMaxlength = 0 #IMPORTANT!!!
		current += 1
	return max(result,currentMaxlength)


a = ["()()()", "", "((((", "(((()", "(((())("]
for x in a:
	print(x, "=",longestMatchingParenthesis(x,len(x)))
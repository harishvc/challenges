#Find the length of the longest valid parenthesis sequence in a string, in O(n) time

'''
REFERENCES:
1. http://stackoverflow.com/questions/25952326/find-the-length-of-the-longest-valid-parenthesis-sequence-in-a-string-in-on-t/35954710#35954710
2. http://www.geeksforgeeks.org/length-of-the-longest-valid-substring/
'''


def longestMatchingParenthesis(a):
	pstack = []        #index position of left parenthesis
	pstack.append(-1)  #default value; handles ) without ( and when match adds up to 2!
	stack_size = 1 
	result = 0
	for i in range(0,len(a)):
		if a[i] == '(':
			pstack.append(i) #Append current index
			stack_size += 1
		else:    # handle )
			#IMPORTANT: pop the first value, since stack size >= 1
			pstack.pop()
			stack_size -= 1
			#determine length of longest match!
			if stack_size > 0:
				#difference of current index - index at top of the stack (yet to be matched)
				result = max(result, i - pstack[-1])
			else:
				#stack size == 0, append current index
				pstack.append(i)
				stack_size += 1 
	return result

a = ["()()()", "", "((((", "(((()", "(((())(", "()(()" ,"()(())"]
for x in a:
	print("%s = %s" % (x,longestMatchingParenthesis(x)))

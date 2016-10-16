#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

#Reference: 
#1. https://leetcode.com/problems/valid-parentheses/
#2. http://blog.gainlo.co/index.php/2016/09/30/uber-interview-question-delimiter-matching/

#Assumtion
#1. Input ONLY contains '(', ')', '{', '}', '[' and ']'

#Time & Space complexity: O(n)
def valid(a):
	match = {'(':')' , '{':'}' , '[':']'}
	mystack = []
	size = 0
	for i in a:
		if i in ["(" , "{", "["]:
			mystack.append(i)
			size += 1
		else:
			if size == 0: return False 
			p = mystack.pop()
			if i != match[p]: return False
			size -= 1
	return True if size == 0 else False


a = ["()" ,"()[]{}" ,"(]" , "([)]", "(((("]
for a2 in a:
	print("%s = %s" % (a2,valid(a2)))


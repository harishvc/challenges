#Check if a number is a happy number

'''
SOURCE: https://leetcode.com/problems/happy-number/

A happy number is a number defined by the following process: Starting with any 
positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0 + 0 = 1
'''


def splitNumber(n):
	d = 10
	mysum = 0
	while n > 0:
		r = n%d   #get reminder
		n = n//d  #get quotient
		mysum += r**2
	#Next step?
	if mysum == 1:
		return True
	elif mysum < 9:  #exit condition
		return False
	else:
		#print("checking ....", mysum)
		return splitNumber(mysum)

n1 = [19,29]
for n in n1:
	print("%d Happy Number? %s" % (n,splitNumber(n)))

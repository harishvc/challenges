#Given a list of integers and two target values find the shortest distance between the two target values

'''
NOTES:
1. Use two pointers, one for each target value
2. Iterate through the list
   2.1 When both the target values are found, calculate distance, 
   2.2 Move the pointer with LOW index value
'''

import sys
def shortestDistance(a,target1,target2):
	size = len(a)
	findNext = True
	itarget1 = 0
	itarget2 = 0
	result = sys.maxsize #default 
	while findNext:
		while itarget1 < size and a[itarget1] != target1:
			itarget1 +=1
		while itarget2 < size and a[itarget2] != target2:
			itarget2 +=1
		#IMPORTANT: or
		if itarget1 == size or itarget2 == size:
			findNext = False
		else:
			#print("match ....", abs(itarget1-itarget2))
			result = min(result, abs(itarget1-itarget2))
			#IMPORTANT: Which pointer to move next?
			#move ponter with low index
			if itarget1 < itarget2:
				itarget1 +=1
			else:
				itarget2 +=1
	return result	

a = [0,4,3,2,4,5,6,7,9]
num1 = 4
num2 = 7
print("input >>>", a)
print("ShortestDistance(%d,%d)=%d" % (num1,num2,shortestDistance(a,num1,num2)))

#Can you fix an almost sorted list with **one swap** (such that the result is sorted)?  
# [1,2,4,3]  = True
# [3,1,2,4]  = False
# [3,2,1,4]  = True

'''
OBSERVATION:
Solution 1:
The list can be sorted and then we can find value(s) that don't meet condition.

Solution 2: Can we do better than nlogn
1. Since list is sorted. each value is  greater than value before and less than value after
2. If a value does not meet condition #1 it is a candidate for swap
3. SPECIAL CASE where there can be 3 values to swap but 2nd and 3rd have to be next to each other!   
'''

def isSorted(a):
	count = len(a)
	for i in range(count):
		if i == 0 and a[i] > a[i+1]:
			return False
		elif i > 0 and i == count +1 and a[i] < a[i-1]:
			return False
		elif (i > 0  and i< count-1) and (a[i] < a[i-1] or a[i] > a[i+1]):
			return False
	return True

def oneSwapFix(a):
	swapCount = 0
	swapindex = [None] * 3
	count = len(a)
	for i in range(count):
		if i == 0 and a[i] > a[i+1]:
			swapindex[swapCount] = i
			swapCount +=1
		elif i > 0 and i == count-1 and a[i] < a[i-1]:
			swapindex[swapCount] = i
			swapCount +=1
		elif (i > 0  and i< count-1) and (a[i] < a[i-1] or a[i] > a[i+1]):
			swapindex[swapCount] = i
			swapCount +=1
		#Handle special case	
		if swapCount == 3 and i == swapindex[1]+1:
			swapCount = 2
			swapindex[1] = i #update
	#Can the list be fixed?
	if swapCount > 2:
		return False
	elif swapCount == 1:
		return False
	elif swapCount == 0:
		return True
	else:
		a[swapindex[0]],a[swapindex[1]] = a[swapindex[1]],a[swapindex[0]]
		return isSorted(a)

a = [3,2,1,4]
print("input >>> %s" %(a))
print("one swap fix? %s" %(oneSwapFix(a)))



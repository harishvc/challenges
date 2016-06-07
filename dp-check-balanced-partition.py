#Can the given list be partitioned into two sub-lists with equal sum (balanced partition)?
#Retain order. Input is integers (positive and negative) and values may be repeated  

'''
NOTES:
1. If sum of values is odd, the list can't be split into two sub-list with equal sum
2. If values are not sorted, you need to iterate the entire list
3. If values are positive, negative and repeating , you need to iterate the entire list
4. If order of values need to retained, no sorting!
'''

#Reference
#http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
def CheckBalancedPartition(a):
	#Find sum
	total = 0
	size = 0
	for x in a:
		total += x
		size += 1
	#Target value for balanced partition	
	target = total //2

	#Check sum
	if total%2 !=0: #sum is odd! 
		return False
	else:
		return CheckBalancedPartition2(a,size,target)

def CheckBalancedPartition2(a,size,target):
	if target == 0:
		return True
	if size == 0 and target != 0:
		return False
	#include last value or exclude last value	
	return CheckBalancedPartition2(a,size-1,target) or CheckBalancedPartition2(a,size-1,target-a[size-1]) 


print("Can be divided into two subsets of equal sum?")
myinput = [[3,1,5,9,12],[3,1,5,9,10],[3,1,3,9,12],[4,1,-5,6,-11,3]]
for a in myinput:
	print("%s >>  %s" % (a,CheckBalancedPartition(a)))

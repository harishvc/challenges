'''
Given a list of sorted values find the value that occurs the most (50%)
(AKA most popular value, majority element)

1. [1, 2, 3, 3, 3, 3, 10] = 3
2. [1, 1, 2, 4, 4, 4, 6, 6] = 4

http://www.geeksforgeeks.org/check-for-majority-element-in-a-sorted-array/

OBSERVATION: :notes:
1. If a value occurs more than 50% of the time then it needs to be in the middle of the list
2. Apply Binary Search concept to find the first and last occurance of the value in the middle of the list
3. if  (last occurance - first occurance) + 1 > 50% input  result is True 
'''
def findFirstOccurance(a,left,right,target):
	if (right >= left):
		mid = left + (right-left)//2
		if (mid == right):
			assert a[mid] == target
			return mid
		elif(a[mid] >= target):
			#go left
			return findFirstOccurance(a,left,mid,target)
		else:
			#go right
			return findFirstOccurance(a,mid+1,right,target)			

def findLastOccurance(a,left,right,target):
	if (right >= left):
		mid = left + (right-left)//2
		if ((mid == right and a[mid] == target)or(a[mid] == target and a[mid+1] > target)):
			return mid
		elif(a[mid] <= target):
			#go right
			return findLastOccurance(a,mid+1,right,target)
		else:
			#go left
			return findLastOccurance(a,left,mid,target)



#Time complexity O(log n)
#Apply Binary Search concept to find the first 
#and last occurance of value at the middle of the list 
def PopularValue(a):
	mid = len(a)//2
	startIndex = findFirstOccurance(a,0,mid-1,a[mid])
	endIndex = findLastOccurance(a,mid+1,len(a)-1,a[mid])
	if (endIndex-startIndex+1 >= mid):
		return a[mid]
	else:
		return "None"

myinput = [[1, 2, 3, 3, 3, 3, 3, 3, 4, 5]]
for a in myinput:
	print("input >>> %s popular value=%s" % (a,PopularValue(a)))

'''
Given a sorted list and a value, find the first and last occurance of the value

Reference
http://www.studyalgorithms.com/array/find-the-index-of-last-occurrence-of-an-element-in-a-sorted-array/
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


'''
Observation: For a value to be the last occurance (of a value), 
the next right value must be larger
'''
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


a = [1, 2, 2, 3, 3, 3, 4]
find = 3
print("first occurance=",findFirstOccurance(a,0,len(a)-1,find))
print("last occurance=",findLastOccurance(a,0,len(a)-1,find))


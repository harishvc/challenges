#Given a sorted list and a value, find the first and last occurance of the value

'''
OBSERVATION:
BST search algorithm can be modified to handle duplicate values
 1. first occurance is greater than the value before (a[i] > a[i-1])
 2. last occurance is less than the value after (a[i] < a[i+1])
'''

#Time complexity: O(log n)
#Space complexity: O(1)
def findFirstOccurance(a,start,end,target):
	mid = start + (end-start)//2
	if a[mid] == target:
		#case 1: first occurance is at index position 0
		if mid-1 < 0:
			return mid
		#case 2: first occurance > value in last index
		elif a[mid] > a[mid-1]:
			return mid
		#case 3: go left to find first occurance
		else:
			return findFirstOccurance(a,start,mid-1,target)
	#go right
	elif a[mid] < target:
		return findFirstOccurance(a,mid+1,end,target)
	#go left
	else:
		assert a[mid] > target, "error"
		return findFirstOccurance(a,start,mid-1,target)

def findLastOccurance(a,start,end,maxsize,target):
	mid = start + (end-start)//2
	if a[mid] == target:
		#case 1: last occurance is at index position maxsize (end)
		if mid-1 < maxsize:
			return mid
		#case 2: last occurance < value in last index
		elif a[mid] < a[mid+1]:
			return mid
		#case 3: go right to find last occurance
		else:
			return findLastOccurance(a,mid+1,end,target,maxsize)
	#go right
	elif a[mid] < target:
		return findLastOccurance(a,mid+1,end,target,maxsize)
	#go left
	else:
		assert a[mid] > target, "error"
		return findLastOccurance(a,start,mid-1,target,maxsize)


a = [1, 3, 3, 3, 3, 4, 4]
target = 3
print("input >>> %s target=%d" % (a,target))
print("index position of first occurance=",findFirstOccurance(a,0,len(a)-1,target))
print("last occurance=",findLastOccurance(a,0,len(a)-1,target,len(a)))

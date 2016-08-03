#Given random numbers. Find length of Longest Increasing Subsequence (LIS) and the sequence.

# REFERENCE:
# 1. https://github.com/mission-peace/interview/blob/master/src/com/interview/array/LongestIncreasingSubSequenceOlogNMethod.java
# 2. https://www.youtube.com/watch?v=S9oUiVYEq7E
#
# NOTES:
# 1. Keep track of index positions with value low ... high
# 2. Algorithm: New value can have 3 possibilities: low, high or in between
#     - High:  increment maxLength and add to table, add to result
#     - Low (lowest):  new T[0] 
#     - In between: Find the next highest value greater than new value

#Time Complexity: O(nlogn)
#Space Complexity: O(n)

DEBUG = False
def LIS(a):
	global DEBUG
	#end index of LIS
	endIndex = [0]*len(a)
	#start index of LIS
	startIndex = [-1]*len(a)
	#length of LIS
	lis = 0 
	endIndex[0] = 0
	for i in range(1,len(a)):
		if DEBUG: print("i=%s a[i]=%d endIndex=%s startIndex=%s lis=%d" % (i,a[i],endIndex,startIndex,lis))
		#case 1: new value is largest
		if a[i] > a[endIndex[lis]]:
			lis +=1
			endIndex[lis] = i
			startIndex[i] = endIndex[lis -1]
		#case 2: new value is smallest
		elif a[i] < a[endIndex[0]]:
			endIndex[0] = i
		#case 3: new value in between
		else:
			nextLargestIndex = findNextLargest(a,i,a[i],endIndex)
			endIndex[nextLargestIndex] = i
			startIndex[i] = endIndex[nextLargestIndex-1]
		if DEBUG: print("i=%s a[i]=%d endIndex=%s startIndex=%s lis=%d\n" % (i,a[i],endIndex,startIndex,lis))
	return (startIndex,endIndex,lis)


#Modified Binary Search to find the next value greater than target O(logn)
def findNextLargest(a,end,target,endIndex):
	global DEBUG
	start = 0
	while start <= end:
		mid = start + (end-start)//2
		if a[endIndex[mid]] < target and a[endIndex[mid+1]] > target:
			if DEBUG: print("new index ...", mid+1)
			return mid+1
		elif a[endIndex[mid]] > target:
			#go left
			end = mid-1
		else:
			#go right
			start = mid+1
	return -1 #error

#start from the end index to -1
def findLISSequence(a,startIndex,endIndex,lis):
	end = endIndex[lis]
	result = []
	#Keep going LEFT to generate the sequence
	while end != -1:
		result.append(a[end])
		#go left
		end = startIndex[end]
	#IMPORTANT:Reverse the sequence
	return result[::-1]



a= [10, 22, 9, 33, 21, 50, 41, 60]
startIndex,endIndex,lis = LIS(a)
print("input >> ",a)
#IMPORTANT: lis+1
print("LIS length=",lis+1)
print("LIS=",findLISSequence(a,startIndex,endIndex,lis))

#Find min in the rotated sorted list

a = [1,2,3,4,5]
ra = [3,4,5,1,2] #rotated right 3 times!

#Solution 1: O(n)
#min in a rotated sorted list
def minRSL(a):
	first = 0
	second = 1
	while(a[first] < a[second]):
		print(a[first] < a[second])
		first = second
		second +=1
	return a[second]


#Solution 2: O(log n)
'''
OBSERVATION:
1. Minimum value is the only value with higher values on left and right
2. Apply BST principles to find min value

REFERENCE:
http://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
'''
def minValue(a,start,end):
	#condition 1: list sorted
	if (a[start] < a[end]):
		return a[start]
	#condition 2: one value 
	if(start == end):
		return a[start]
	mid = start + (end-start)//2
	#condition 3: mid index is min value!
	if (a[mid] < a[mid-1] and a[mid] < a[mid+1]):
		assert a[mid] < a[end], print("Error")
		return a[mid]
	#compare value at middle with end (not start) since 
	#middle value is floor so, middle value can be equal to start in some case (2 values)	
	if a[mid] > a[end]: #first half sorted
		#condition 4: min value in second half
		return minValue(a,mid+1,end)
	else:
		#condition 5: min value in first half 	
		return minValue(a,start,mid-1)


#Solution 3: O(log n)
#Credit:
#Inspired by https://www.interviewcake.com/question/python/find-rotation-point
def find_rotation_point(ginput):
	#assertion #1: value at index 0 is always > value at rotation point
	guess = 0
	#
	start = 0
	end = len(ginput) - 1
	while start <  end:
		mid = start + (end-start)//2
		if ginput[mid] >=  ginput[guess]:
			#go right
			start = mid
		else:
			#go left
			end=mid
		if start+1 == end:
			#assertion #2: 
			  #start point at the end of sorted list
			  #end points at the start of sorted list
			return end

a = [[2,3,4,5,6,7,8,1],[5,6,1,2,3,4],[4,5,6,7,0,1,2],[0,1,2,3,4,5,6,7],[2,1],[1,2],[3,2,1]]
for ra in a:
	print(ra , " >>> " , minValue(ra,0,len(ra)-1))
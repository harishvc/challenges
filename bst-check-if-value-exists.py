#Given a sorted list find if a value exists

'''
NOTES:
1. Apply divide and conquer technique to find a value in the first half or second half
2. Reduce the size (of seach) by half each time
3. Idea behind Binary Search!
'''

#Time complexity: O(logn)
def findTarget(a,start,end,target):
	while start <= end:
		mid = start + (end-start)//2
		if a[mid] == target:
			return True
		elif a[mid] > target:
			end = mid -1
		else:
			start = mid + 1
	return False


a = [1,2,3,4,5]
target = [-5,1,15]
for t in target:
	#IMPORTANT: start=0; end = len-1
	print("Is %d in %s ? %s" % (t,a,findTarget(a,0,len(a)-1,t)))


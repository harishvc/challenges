#Find the missing number in an increasing sequence (1 ...N)

'''
OBSERVATION
1. Input is an increasing sequence starting at 1  and ending at N
2. Value at index
   0 = 1
   1 = 2
   2 = 3
   ..
   ..
   5 = 6  (if N == 6)
3. if value at index Z != Z+1  then the missing sequence is on the left of Z including Z
4. if value at index Z == Z+1  then the missing sequence is on the  right of Z excluding Z   
'''


#Time complexity: O(logn)
def findMissing(a,start,end,size):
    #case 1: Exit condition
	if start == end:
		return start + 1
	mid = start + (end-start)//2
	#case 2: missing number at start
	if mid == 0 and a[mid] != mid + 1:
		return 1
	#case 3:  missing number at end
	elif mid == size -1 and a[mid] != mid +1:
		return mid + 1
	#case 4: missing number on the LEFT including middle
	elif a[mid] != mid + 1:
		#go left!
		return findMissing(a,start,mid,size)
	#case 5: missing number on the RIGHT	
	else:
		#go right
		return findMissing(a,mid+1,end,size)


a = [[1,2,3,4,6,7,8],[1,2,3,5],[2,3]]
for a2 in a:
	print("%s >>> %d" % (a2,findMissing(a2,0,len(a2)-1,len(a2))))
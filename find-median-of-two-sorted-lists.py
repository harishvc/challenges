#Find median in two sorted list

'''
Notes:
1. For any value N to be median there should be x values  < N and y values  > N
2. Let's go with x values < N 
3. There are two sets a, b  
    - a = [a1,a2,a3]      #size 3
    - b = [b1,b2,b3,b4]   #size 4
    - total size = 7
    - value at index a[2] is median if there are 3 values less than a[2]
       - there are already two values in a (a[0] & a[1])
       - if b[0] < a[2] and b[1] > a[2] then we got the median!
'''

#Time Complexity: O(log n) + O(log m)  where n and m are # values in input
#Soluton can be further optimized by making "a" as the input with less values
def findMedianWrapper(a,asize,b,bsize,valuesBelow):
	median = None
	for index in range(asize,-1,-1):
		#is value at index median?		
		targetIndex = (valuesBelow - index) -1
		#print("checking ,,,,," ,a[index])
		if targetIndex < 0:
			#print("next small value")
			continue
		elif b[targetIndex] < a[index] and a[index] < b[targetIndex+1]:
			#print("found median")
			median = a[index]
			break
		elif b[targetIndex] < a[index]:
			#print("next small value")
			continue
		else:
			#median not in this list
			#print("median not in this list")
			break
	return median

def findMedian(a,b):
	asize = len(a)
	bsize = len(b)
	valuesBelow = (asize + bsize)//2
	median = None
	if (asize + bsize)%2 == 1 : #odd
		median = findMedianWrapper(a,asize-1,b,bsize-1,valuesBelow)
		if median is None:
			median = findMedianWrapper(b,bsize-1,a,asize-1,valuesBelow)
		return median
	#TODO
	#else: #even

a = [3,5,9]
b = [1,12,18,21]

print("a >>%s b>>%s median=%d" % (a,b,findMedian(a,b)))

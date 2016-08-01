#Quick Sort

1. Quick sort uses divide and conquer
2. Quick sort first selects a pivot value to split the list. 
3. There are many ways to select the pivot value - first , last, random
4. Index position of the pivot value is commonly called the split point
5. Split point is used to divide the list for subsequent calls to the quick sort

NOTES:
1. Divide and conquer
2. Inplace algorithm 
3. NO need for extra memory
4. NOT STABLE - does not retain the order of same values
5. When list size becomes 16-20, quick sort becomes insertion sort
6. DEFAULT system sort
7. Time complexity:
   - Each of the n items needs to check against the pivot value - O(n)
   - There are log n divisions after the split point is found
   - average: O(nlogn)
   - worst case:  O(n^2)
'''

def quicksort(a,start,end):
	if start < end:
		pivotIndex = partition(a,start,end)
		quicksort(a,start,pivotIndex)
		quicksort(a,pivotIndex+1,end)

#Handle duplicates
def partition(a,start,end):
	pivotValue = a[start]  #select first value to be pivot
	left = start + 1
	right = end
	done = False
	while not done:
		 while left <=right and a[left] < pivotValue:
		 		left +=1
		 while right >=left and a[right] >= pivotValue:
		 		right -=1
		 #still more values to visit		
		 if left < right:
		 	a[left],a[right] = a[right],a[left]
		 #no more values left to visit
		 else:
		 	done = True

	#IMPORTANT: 
	#a[start] is the pivot value
	#a[right] partitions the list into into 2 parts
	#values on the left of a[right] are <= 
	#values on the right of a[right] are >	 	
	a[start],a[right] = a[right],a[start]
	return right #index position


import random
a= [1,4,3,4,4,4,4,5]
random.shuffle(a)
print("input >>>", a)
quicksort(a,0,len(a)-1)
print("sorted input>>>",a)

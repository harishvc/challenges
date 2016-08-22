#Quick sort

'''
NOTES:
1. Recursive
2. NOT stable  (duplicates retain their relative order)
3. Time Complexity: Best: O(n), Average: O(nlogn), Worst: O(n^2)
4. Average time complexity is O(n log n) since the pivot splits the input into
   two sub-list of idential length until length ==1
5. Choosing the pivot is critical (pivot is the largest or smallest), that leads 
   to worst cast time complexity of O(n^2)
6. Performance highly depends upon selection of the pivot (key)   

'''

def quicksort(a,start,end):
	#IMPORTANT: exit condition
	if start < end:
		pivotIndex = partition(a,start,end)
		quicksort(a,start,pivotIndex-1)
		quicksort(a,pivotIndex+1,end)

#Handle duplicates
def partition(a,start,end):
	pivotValue = a[start]  #select first value to be pivot
	left = start + 1
	right = end
	end = False
	while not end:
		 while left <=right and a[left] < pivotValue:
		 		left +=1
		 #a[right] >= pivotValue , handle duplicates		
		 while right >=left and a[right] >= pivotValue:
		 		right -=1
		 #check if there are values to swap?		
		 if left < right:
		 	a[left],a[right] = a[right],a[left]
		 #no values to swap;reached end!
		 else:
		 	end = True

	#IMPORTANT: 
	#a[start] is the pivot value
	#a[right] partitions the list into into 2 parts
	#values on the left < a[right] 
	#values on the right >= a[right]	 	
	a[start],a[right] = a[right],a[start]
	return right #index position


import random
a= [1,4,3,4,4,4,4,5]
random.shuffle(a)
print("input >>>", a)

quicksort(a,0,len(a)-1)
print("sorted input>>>",a)
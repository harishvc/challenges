#Quick sort

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
	end = False
	while not end:
		 while left <=right and a[left] < pivotValue:
		 		left +=1
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
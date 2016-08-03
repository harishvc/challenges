#Insertion Sort

'''
NOTES:
1. Insertion sort is simple (no recursion)
2. For small lists, insertion is generally faster than a comparably implemented quicksort or mergesort
3. In-place sort & STABLE
4. Insertion sort maintains a sorted sub-list
5. Each new value is inserted inside a sorted sublist
6. Shift operation requires approximately a third of the processing work of an exchange since only one assignment is performed
7. Time complexity: O(nlogn) - consistent, NO assumptions are made here!!!
8. Space complexity: Best: O(n), Average O(n^2)

ALGORITHM OBESERVATION:
1. Values are sorted from left to right
2. At iteration i, all values from 0 ... i+1 are sorted
3. Inner while loop will not get executed if i+1 > i (already sorted)
4. Insertion sort makes less comparisons if list is sorted!
'''

def insertionSort(a):
	#IMPORTANT: exclude last value; since we are checking i & i+1
	end = len(a) -1 
	#go right!
	for right in range(0,end):	
		left = right
		#go left!
		#IMPORTANT: If values from a[0] ... a[i+1] are sorted, this loop will NOT execute
		while left >= 0 and a[left] > a[left+1]:
			a[left],a[left+1] = a[left+1],a[left]
			left -= 1


import random
alist = [5,4,3,2,1,1,3,2,1]
random.shuffle(alist)
print("input >>>", alist)
insertionSort(alist)
print("insertion sort:",alist)

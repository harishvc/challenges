#Insertion Sort

''''
ALGORITHM:
1. Iterate through the items in the list 
2. If the value is greater than the next
    a. shift values
    b. go back and shift values 
The sub-list is sorted at the end of each pass!!!

NOTES:
1. Insertion sort is simple (no recursion)
2. For small lists, insertion is generally faster than a comparably implemented quicksort or mergesort
3. In-place sort
4. Insertion sort maintains a sorted sub-list
5. Each new value is inserted inside a sorted sublist
6. Shift operation requires approximately a third of the processing work of an exchange since only one assignment is performed
7. Time complexity: O(nlogn) - consistent, NO assumptions are made here!!!
8. Space complexity: Best: O(n), Average O(n^2)


REFERENCE:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
'''


import random
def insertionSort(input):
	inputLength = len(input)-1  #ignore last value
	for i in range(inputLength):
		while i >= 0 and i< inputLength and input[i] > input[i+1]:
			input[i+1],input[i] = input[i],input[i+1]
			i -=1
		#sorted sub-list	
		#print(">>>", input)

alist = [54,26,93,17,77,31,44,55,20]
random.shuffle(alist)
print("input >>>", alist)
insertionSort(alist)
print("insertion sort:",alist)

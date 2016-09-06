#Merge Sort

'''
ALGORITHM:
1. Comparison based
2. Divide and conquer algorithm 
3. Merge sort recursively splits a list in half and merges the results

NOTES:
1. STABLE - can be modified to retain order of same values
2. NOT in place sorting
3. EXTRA space is needed to hold two halves.
4. Requiring additional space is a critical factor if the list is large
5. Time complexity: O(nlogn) - consistent
6. Space complexity: O(n)

TODO: Remove slice operation to guarantee O(nlogn) time complexity
'''

import random
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        lefthalflength = len(lefthalf)
        righthalflength = len(righthalf)
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < lefthalflength and j < righthalflength:
	    #IMPORTANT: < works but <= makes merge sort stable! 
            if lefthalf[i] <= righthalf[j]:   
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < lefthalflength:
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < righthalflength:
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

alist = [54,26,93,17,77,31,44,55,20]
random.shuffle(alist)
print("input >>>", alist)
mergeSort(alist)
print("merge sort >>>", alist)
assert alist == [17, 20, 26, 31, 44, 54, 55, 77, 93], "Merge Sort error!"

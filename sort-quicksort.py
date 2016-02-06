#Quick Sort

'''
ALGORITHM:
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

#http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
import random

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first] #first value is pivot, many value to select pivot!
   leftmark = first+1
   rightmark = last
   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
       	   alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]

   alist[first],alist[rightmark] = alist[rightmark],alist[first]        
   return rightmark


alist = [54,26,93,17,77,31,44,55,20]
random.shuffle(alist)
print("input >>>", alist)
quickSort(alist)
print("quick sort >>>", alist)
assert alist == [17, 20, 26, 31, 44, 54, 55, 77, 93], "Quick sort error!"
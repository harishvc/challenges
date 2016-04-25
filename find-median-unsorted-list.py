#Find median in an unsorted list

'''
NOTES:

Modification of Quick Sort Algorithm to find the Kth smallest value (median)

1. We partition into 2 partitons (greater than the pivot, and lesser than the pivot)
2. Since we are looking for the Kth smallest we continue the partition when K is []
3. Time complexity: 
   a. Average = n + 1/2 n + 1/4 n + 1/8 n + ..... < 2 n ~ n = O(n)
      - Sensitive to the pivot that is chosen
      http://stackoverflow.com/questions/5945193/average-runtime-of-quickselect
   b. Worst case: O(n^2) if bad pivots are choosen

REFERENCES:
1. http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
2. http://stackoverflow.com/questions/14659637/python-based-quickselect-implementation-resulting-in-error
'''

import random
def quick_select(A, k):
    #pivot value is random
    pivot = random.choice(A)

    A1 = [] #values < pivot
    A2 = [] #values > pivot

    for i in A:
        if i < pivot:
            A1.append(i)
        elif i > pivot:
            A2.append(i)
        else:
            pass  # ignore Pivot value!

    #case 1: median is in A1
    if k <= len(A1):
        return quick_select(A1, k)
    #case 2: median is in A2
    elif k > len(A) - len(A2):
        return quick_select(A2, k - (len(A) - len(A2)))
    #case 3: median found
    else:
        return pivot
	
a = [6,4,2,9,1]
mid = len(a)//2 +1
print("input=%s median=%d" % (a,quick_select(a,mid)))




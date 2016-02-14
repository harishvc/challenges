#Quick Select

'''
Modification of Quick Sort Algorithm to find the Kth smallest value 

NOTES:
1. We partition into 2 partitons (greater than the pivot, and lesser than the pivot)
2. Since we are looking for the Kth smallest we continue the partition when K is
3. Time complexity: 
   a. Average = n + 1/2 n + 1/4 n + 1/8 n + ..... < 2 n ~ n = O(n)
      - Sensitive to the pivot that is chosen
      http://stackoverflow.com/questions/5945193/average-runtime-of-quickselect
   b. Worst case: O(n^2) if bad pivots are choosen

REFERENCES:
1. http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
2. http://stackoverflow.com/questions/14659637/python-based-quickselect-implementation-resulting-in-error
3. http://blog.teamleadnet.com/2012/07/quick-select-algorithm-find-kth-element.html

'''

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

    #K is in the pile of small elements
    if k <= len(A1):
        return quick_select(A1, k)
    #K is in the pile of large elements
    elif k > len(A) - len(A2):
        return quick_select(A2, k - (len(A) - len(A2)))
    #K found
    else:
        return pivot
	
input = [14, 4, 0, 9, 11, 19, 13]
import random
random.shuffle(input)
print(input)
k = 3
a = quick_select(input,k)
print("3rd Smallest value=",a)




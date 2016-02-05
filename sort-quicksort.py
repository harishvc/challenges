#Quick Sort

#source:https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter10sorting/QuickSort.py
#Notes
# 1. Example of divide and conquer
# 2. Picks an element in the array to be a pivot
# 3. Average O(n* log n)
# 4. Worse case O(n^2)
 
import random
#low and high are index position of list elements
#pivot is a value
def QuickSort(A, low, high):
    if low < high:
        pivot = Partition(A, low, high)
        QuickSort(A, low, pivot - 1)
        QuickSort(A, pivot + 1, high)
 
def Partition(A, low, high) :
    pivot = low + random.randrange(high - low + 1)
    swap(A, pivot, high)
    for i in range(low, high):
        if A[i] <= A[high]:
            swap(A, i, low)
            low += 1
    swap(A, low, high)
    return low
 
def swap(A, x, y):
    A[x],A[y] = A[y],A[x]

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
random.shuffle(A)
print("Input >>", A)
QuickSort(A, 0, len(A) - 1)
print("Quick Sort: ", A)
assert A ==  [127, 220, 246, 277, 321, 454, 534, 565, 933], "ERROR"
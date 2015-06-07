#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter10sorting/MergeSort.py
#Notes:
# 1. Divide and conquer
# 2. No assumptions made here
# 3. worst, best and average = O(n*logn)
# 4. Widely used 
def MergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        MergeSort(lefthalf)  #recursive call
        MergeSort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i = i + 1
            else:
                A[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            A[k] = righthalf[j]
            j = j + 1
            k = k + 1

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
MergeSort(A)
print("Merge Sort: ", A)


#source:https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter10sorting/QuickSort.py
#Notes
# 1. Example of divide and conquer
# 2. Picks an element in the array to be a pivot
# 3. Average O(n* log n)
# 4. Worse case O(n^2)
 
import random
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
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
QuickSort(A, 0, len(A) - 1)
print("Quick Sort: ", A)
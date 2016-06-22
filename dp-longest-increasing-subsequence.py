#Given a list of random numbers. Find length of Longest Increasing Subsequence (LIS) and the sequence.

'''
Subsequence is a generalization of substring. Order of values in retained 
however one of values missing.

OBSERVATION:
1. Longest Increasing Subsequence (LIS) will have values sorted!
2. We can keep track of values we have seen (since we don't know the upcoming values)
3. LIS at each position can be stored in a list
4. LIS at each position will depend on the NEXT smallest value + 1  
    - Self Balancing BST can be seached and new value inserted
'''

#Solution 1: Run two loops
#http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
#Time complexity: O(n^2)


#Solution 2: Use Dynamic Programming to take advantage 
#of information gathered/analyzed so far by using additional storage
#
# REFERENCE:
# https://github.com/mission-peace/interview/blob/master/src/com/interview/array/LongestIncreasingSubSequenceOlogNMethod.java
#
# NOTES:
# 1. Keep track of index positions with value low ... high
# 2. Data Structure:
#   T = Temporary LIS calculated so far (sorted from low to high)
#   R = Result, backtrack to get values
#   maxLength = max length calculated so far
# 3. Algorithm: New value can have 3 possibilities: low, high or in between
#     - High:  increment maxLength and add to T
#     - Low (lowest):  new T[0] 
#     - In between: Find the next highest value greater than new value
#       and replace this value with the new value


#Time Complexity: O(nlogn)
#Space Complexity: O(n)
def LIS(a):
    T = [0]*len(a)   #LIS at each index
    R = [-1]*len(a)
    maxLength = 0
    T[0] = 0
    for i in range(1,len(a)):
        #case 1: new value is the largest
        if a[i] > a[T[maxLength]]:
            maxLength += 1  #increment ONLY when new value is greater
            T[maxLength]= i
            R[T[maxLength]] = T[maxLength-1]; #store index to backtrack
        #case 2: new value is the smallest
        elif a[i] < a[T[0]]:
            T[0] = i
        #case 3: new value in between small and large
        else:
            index = findNextLargest(a,T,maxLength,a[i])
            T[index] = i
            R[T[index]] = T[index-1];
    return(T,R,maxLength)


#Modified Binary Search to find the next value greater than target O(nlogn)
def findNextLargest(a,T,end,target):
    start = 0
    #IMPORTANT: start <= end , since there is one value!!!
    while start <= end:
        mid = start + (end-start)//2
        if a[T[mid]] < target and a[T[mid+1]] > target:
            return mid+1
        elif a[T[mid]] < target :
            #go right
            start = mid+1
        else:
            #go left
            end = mid-1
    return -1 #ERROR

def findLISvalues(a,T,R,maxLength):
    start = T[maxLength]
    result = []
    while start != -1:
        result.append(a[start])
        start = R[start]
    #IMPORTANT:Reverse
    return result[::-1]

a= [3,4,-1,5,8,2,3,12,7,9,10]
T,R,maxLength = LIS(a)
result = findLISvalues(a,T,R,maxLength)
print("Input >>>", a)
print("Max LIS Length=", maxLength+1)
print("LIS = ", result  )



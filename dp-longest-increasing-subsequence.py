#Given a list of random numbers. Find length of Longest Increasing Subsequence (LIS).

'''
Subsequence is a generalization of substring. Order of values in retained 
however one of values missing.

OBSERVATION:
1. Longest Increasing Subsequence (LIS) will have values sorted!
2. We can keep track of values we have seen (since we don't know the upcoming values)
3. LIS at each position can be stored in a list
4. LIS at each position will depend on the NEXT smallest value + 1  
    - Self Balancing BST can be seached and new value inserted

REFERENCE:
1. http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
2. https://allaboutalgorithms.wordpress.com/2011/10/21/longest-increasing-subsequence/
'''

#http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
#Time complexity: O(n^2)
def lis(arr):
    n = len(arr)
 
    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n
 
    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
        	#Important: new value is greater and new subsequence is greater!
        	#negative values will fail the second condition
        	#Improve time complexity using BST
        	#Using a self-balancing BST like AVL insert and search is gaurantee to log N
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
 
    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0
 
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum , lis[i])
 
    print(lis)
    return maximum

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
#arr = [-1, 4, 5 ,-3, -2, 7, -11, 8, -2]
print("Length of lis is", lis(arr))    
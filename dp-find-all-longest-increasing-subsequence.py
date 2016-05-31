#Given a list of random numbers. Find all increasing subsequences

#REFERENCE:
#http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

'''
ALGORITHM:
1. If A[i] is smallest among all end candidates of active lists, 
   we will start new active list of length 1.

2. If A[i] is largest among all end candidates of active lists, 
   we will clone the largest active list, and extend it by A[i].

3. If A[i] is in between, we will find a list with largest end element 
   that is smaller than A[i]. Clone and extend this list by A[i]. 
   We will discard all other lists of same length as that of this modified list.
'''


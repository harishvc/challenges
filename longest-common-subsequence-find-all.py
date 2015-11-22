#Question: Given two sequences find all the the Longest Common Subsequence (LCS)

'''
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
So a string of length n has 2^n different possible subsequences.

References
1. http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/ 
2. Tushar Roy - https://www.youtube.com/watch?v=NnD96abizww
3. Tushar Roy - https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/LongestCommonSubsequence.java
4. WSLabs     - https://www.youtube.com/watch?v=RUckZMzqUcw
5. Lec 15 | MIT 6.046J - https://www.youtube.com/watch?v=V5hZoJ6uK-s
'''

#Print two dimensional matrix        
def PrintMatrix(Table):
    for row in range(0,len(Table)):
        for col in range(0,len(Table[row])):
            print("%d" % (Table[row][col]),end=" ")
        print("")

#Time Complexity: O(mn), Space Complexity: O(mn)
#Bottom-up (Dynamic Programming)
#Start with the lowest values of the input and keep building the solutions for higher values
def LCS(X, Y):
    m = len(X) #rows
    n = len(Y) #cols
    # An (m+1) times (n+1) matrix
    C = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    #PrintMatrix(C)
    #print(m,n,C[m][n])
    return C

#Traverse the two dimensional matrix to find all LCS
def backTrackAll(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([""])
    #letters match!
    elif X[i-1] == Y[j-1]:
        return set([Z + X[i-1] for Z in backTrackAll(C, X, Y, i-1, j-1)])
    else:
        R = set()
        #left
        if C[i][j-1] >= C[i-1][j]:
            R.update(backTrackAll(C, X, Y, i, j-1))
        #up
        if C[i-1][j] >= C[i][j-1]:
            R.update(backTrackAll(C, X, Y, i-1, j))
        return R
    
X = "ABCBDAB"
Y = "BDCABA"
m = len(X)
n = len(Y)
C = LCS(X, Y)
print("Input strings => %s  %s" % (X,Y))
print("All LCSs: %s" % backTrackAll(C, X, Y, m, n))
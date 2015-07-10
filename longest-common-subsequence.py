#Question: Given two sequences, find the length of longest subsequence present in both of them

'''
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
So a string of length n has 2^n different possible subsequences.

Reference: http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/ 
'''

#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter19dynamicprogramming/LongestCommonSubsequenceWithDP.py
#Time Complexity: O(mn), Space Complexity: O(mn)
def LCS(X, Y):
    Table = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]
    
    #Step 1: 
    # a. Build a matrix by iterating X & Y
    # b. if X[i] = Y[j] then increment else get max value of row-1 or col-1
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                #print("Match .... %s at i=%d j=%d" % (x,i,j))
                Table[i + 1][j + 1] = Table[i][j] + 1
            else:
                Table[i + 1][j + 1] = max(Table[i + 1][j], Table[i][j + 1])
    
    
    #Print Matrix 
    #for row in range(0,len(Table)):
        #for col in range(0,len(Table[row])):
            #print("%d" % (Table[row][col]),end=" ")
        #print("")
    
    #Step 2:
    # a. check if the value at location in matrix is eaual to row-1 or col-1
    # b. if not equal then letters match, add to result!
    # c. else ie equal to row than row-1 or col-1
    result = ""
    x, y = len(X), len(Y)
    while x != 0 and y != 0:
        if Table[x][y] == Table[x - 1][y]:
            x -= 1
        elif Table[x][y] == Table[x][y - 1]:
            y -= 1
        else:
            assert X[x - 1] == Y[y - 1]
            #print("Substring match .... %s at position A[%d] = B[%d]" %(X[x - 1],x-1,y-1))
            result = X[x - 1] + result
            x -= 1
            y -= 1
    return result

A= "AGGTAB"
B = "GXTXAYB"
print ("string1=%s \nstring2=%s \nlongest common substring=%s" % (A, B, LCS(A,B)))    

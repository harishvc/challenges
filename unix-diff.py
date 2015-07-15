#Question: Implement Unix diff

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

#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter19dynamicprogramming/LongestCommonSubsequenceWithDP.py

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
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C
    
def printDiff(C, X, Y, i, j):
    if i > 0 and j > 0 and X[i-1] == Y[j-1]:
        printDiff(C, X, Y, i-1, j-1)
        print("  " + X[i-1])
    else:
        if j > 0 and (i == 0 or C[i][j-1] >= C[i-1][j]):
            printDiff(C, X, Y, i, j-1)
            print("+ " + Y[j-1])
        elif i > 0 and (j == 0 or C[i][j-1] < C[i-1][j]):
            printDiff(C, X, Y, i-1, j)
            print("- " + X[i-1])
            
X = [
    "This part of the document has stayed",
    "the same from version to version.",
    "",
    "This paragraph contains text that is",
    "outdated - it will be deprecated '''and'''",
    "deleted '''in''' the near future.",
    "",
    "It is important to spell check this",
    "dokument. On the other hand, a misspelled",
    "word isn't the end of the world.",
]
Y = [
    "This is an important notice! It should",
    "therefore be located at the beginning of",
    "this document!",
    "",
    "This part of the document has stayed",
    "the same from version to version.",
    "",
    "It is important to spell check this",
    "document. On the other hand, a misspelled",
    "word isn't the end of the world. This",
    "paragraph contains important new",
    "additions to this document.",
]

C = LCS(X, Y)
printDiff(C, X, Y, len(X), len(Y))
#Question: Given two sequences find the longest common substring

'''
References
1. http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/ 
2. Tushar Roy - https://www.youtube.com/watch?v=BysNXJHzCEs&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=26
3. Tushar Roy - https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/LongestCommonSubstring.java
4. Lec 15 | MIT 6.046J - https://www.youtube.com/watch?v=V5hZoJ6uK-s
5. WikiBooks - https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python3
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
    m = len(X)
    n = len(Y)
    longest, x_longest = 0, 0
    # An (m+1) times (n+1) matrix
    C = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                C[i][j] = C[i-1][j-1] + 1
                if C[i][j] > longest:
                    longest = C[i][j]
                    x_longest = i  
            else:
                C[i][j] = 0
    #PrintMatrix(C)
    return X[x_longest - longest: x_longest]

    
X = "ABCDAF"
Y = "ZBCDAF"
m = len(X)
n = len(Y)
C = LCS(X, Y)
print("Input strings => %s  %s" % (X,Y))
print("Longest common substring => %s" % (C))
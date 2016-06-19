#Question: Given two sequences find the longest common substring

'''
References
1. http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/ 
2. Tushar Roy - https://www.youtube.com/watch?v=BysNXJHzCEs&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=26
3. Tushar Roy - https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/LongestCommonSubstring.java
4. Lec 15 | MIT 6.046J - https://www.youtube.com/watch?v=V5hZoJ6uK-s
5. WikiBooks - https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python3

OBSERVATION:
1. Characters have to be continuous for substring
2. if continuous characters match we increment 
   length of max substring else ignore (since we are only calculating max length)
3. Max substring can end at any location (not necessarily at the end) so need to track it! 
'''

#Space complexity: O(n) 
#Time complexity: O(mn)
def LongestSubstring(m,n):
    msize = len(m)
    nsize = len(n)
    row1 = [0] * nsize #col size
    row2 = [0] * nsize #col size
    maxsize = 0
    for i in range(0,msize):
        for j in range(0,nsize):
            if n[j] == m[i]:
                row2.append(row1[j-1] + 1)
                #maxsize = row2[j] if row2[j] > maxsize else maxsize
                if row2[j] > maxsize: maxsize = row2[j] 
            else:
                #doesn't matter for substring since characters have to be continuous
                row2.append(0)
        #IMPORTANT: switch rows
        row1,row2 = row2,row1
        #IMPORTANT: empty the second list; size=0
        del row2[:]  #row2.clear()
    #IMPORTANT: since rows get switched use row1
    return maxsize

    
X = "ABCDAF"
Y = "ZBCDAF"
print("Input strings => %s  %s" % (X,Y))
print("Length of longest common substring => %s" % (LongestSubstring(Y,X)))



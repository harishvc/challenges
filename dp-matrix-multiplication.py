#Given a sequence of matrices. Find the most efficient way to multiply these matrices together

'''
NOTES & OBSERVATIONS
1. Matrix multiplication is associative. 
2. Result is same however the #computation steps will be different
3. size & possibilities
   m0m1 = m0m1  #size=2 , 1 possibility
   m0m1m2 = MIN(m0(m1m2), (m0m1)m2) #size=3 , 2 possibilities
   m0m1m2m3 = MIN(m0(m1m2m3), (m0m1m2)m3, (m0m1)*(m2m3))  #size=4 , 3 possibilities

REFERENCE
1. http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
2. https://www.youtube.com/watch?v=vgLJZMUfnsU
'''

import sys
#recursion
def solution1(a,i,j):
	if i == j:
		return 0
	#http://stackoverflow.com/questions/13795758/what-is-sys-maxint-in-python-3	
	#sys.maxint constant was removed, since there is no longer a limit to the value of integers in Python3
	#sys.maxsize can be used as an integer value larger than any practical list or string index.
	minA = sys.maxsize
	for k in range(i,j):
		count = solution1(a,i,k) + solution1(a,k+1,j) + a[i-1]*a[k]*a[j]
		#print("i=%d k=%d j=%d count=%d" % (i,k,j,count))
		if count < minA:
			minA = count
	return minA


#http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
#Time complexity: O(n^3)
#Space complexity: O(n^2)
#dynamic programming
def solution2(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
 
    #Cost for size=1 is zero
    for i in range(1, n):
        m[i][i] = 0
 
    #Find the cost for size = 2 ....n
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = sys.maxsize
            for k in range(i, j): 
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n-1]


a  = [5,7,2,8]
print("input >>> %s minium cost=%d" % (a,solution2(a,len(a))))


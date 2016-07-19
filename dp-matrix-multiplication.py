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
def solution1(a,start,end):
	if start == end:
		return 0
	#http://stackoverflow.com/questions/13795758/what-is-sys-maxint-in-python-3	
	#sys.maxint constant was removed, since there is no longer a limit to the value of integers in Python3
	#sys.maxsize can be used as an integer value larger than any practical list or string index.
	minA = sys.maxsize
    #OBESERVATION
    #For loop computes cost with different combinations
    #Recursion reduce the matrix size to a smaller value
	for k in range(start,end):
		count = solution1(a,start,k) + solution1(a,k+1,end) + a[start-1]*a[k]*a[end]
		if count < minA:
			minA = count
	return minA


#http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
#http://web.eecs.utk.edu/~leparker/Courses/CS581-spring14/Lectures/5-Jan-23-Matrix-Chain-Mult-no-answers.pdf
#Time complexity: O(n^3)
#Space complexity: O(n^2)
#dynamic programming
import sys
sys.path.append("../mylib")
import doless

def solution2(p, n):
    m = [[sys.maxsize for x in range(n)] for x in range(n)]
 
    #Cost for size=1 is zero
    for i in range(1, n):
        m[i][i] = 0
 
    #Find the cost for size = 2 ....n-1
    for L in range(2, n):
        #Keep moving the start index
        #IMPORTANT: start=1 ... n-L+1 
        for start in range(1, n-L+1):
            #end = L indexes away from start
            end = start+L-1
            for k in range(start, end): 
                #Find the smallest cost for ixj
                q = m[start][k] + m[k+1][end] + p[start-1]*p[k]*p[end]
                if q < m[start][end]:
                    m[start][end] = q

    #doless.PrintMatrix(m)

    #minimum operations for n values in row=1 col=n-1
    return m[1][n-1]


a  = [5,7,2,8]

#IMPORTANT: start=1 end=len(a)-1
#print("input >>> %s minium cost=%d" % (a,solution1(a,1,len(a)-1)))

print("input >>> %s minimum cost=%d" % (a,solution2(a,len(a))))

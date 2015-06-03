#Source: http://www.ardendertat.com/2012/01/26/programming-interview-questions-27-squareroot-of-a-number/

#Question: Find the squareroot of a given number rounded down to the nearest integer, without using the sqrt function. For example, squareroot of a number between [9, 15] should return 3, and [16, 24] should be 4

#Observation: The squareroot of a (non-negative) number N always lies between 0 and N/2. The straightforward way to solve this problem would be to check every number k between 0 and N/2, until the square of k becomes greater than or rqual to N. If k^2 becomes equal to N, then we return k. Otherwise, we return k-1 because we’re rounding down. - See more at: http://www.ardendertat.com/2012/01/26/programming-interview-questions-27-squareroot-of-a-number/#sthash.JWKdzaiX.dpuf

#Solution:
def sqrt1(num): 
    if num < 0: raise ValueError 
    if num ==1: return 1 
    for k in range(1+int(num/2)): 
        if k**2==num: 
            return k 
        elif k**2>num: 
            return k-1 
    return k 

input = [2,4,5,6,7,8,9,10]
for x in input:
    print("%d^0.5=%d" % (x,sqrt1(x)))
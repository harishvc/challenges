#Question: How many trailing zeros are in n! (n factorial)
#Answer:
#1. Observation:
#   1.1 Each multiplication with 10 creates one trailing zero 
#   1.2 What is the prime number combination that generates 10?  5x2 
#   1.3 Find the number of 2 and 5 combinations to find trailing zeros. Since there are 
#       more factor 2 than factor 5 count factor 5
#       5! = 2^3 *  3 * 5  , leading zero = 1
#       10! = 2^8 * 3^4 * 5^2 * 7,  leading zero = 2
#   1.4 Numbers like 25, 125, etc have more than one 5 - handle this!
#2. Algorithm:
#    First divide n by 5 and remove all single 5s, 
#    then divide by 25 to remove extra 5s and so on. 
#3. Complexity:
#   3.1 O(n/5) ~ O(n)
#4. Test Cases & Proof:    
# 5!=120 , #trailing zeros= 1
# 10!=3,628,800  , #trailing zeros= 2
#5. Reference:
#http://www.purplemath.com/modules/factzero.htm
#http://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
#6. Code: Python 3.4.3

#Source: http://stackoverflow.com/questions/1174505/counting-trailing-zeros-of-numbers-resulted-from-factorial
def countFives(n):
    fives = 0    
    m = 5  
    while m <= n: 
        fives = fives + int (n/m)
        m = m*5  #handle extra 5's in 25, 125
    return fives

#Iterative
def IFactorial(n):
    result = 1
    for x in range (1,n+1):
        result *= x
    return result

I = [10,15,20,25,30,35,40,45]
for x in I:
    print ("%d!=%s  , #trailing zeros= %s" % (x, "{:,}".format(IFactorial(x)),countFives(x)))

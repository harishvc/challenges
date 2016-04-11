#Number of perfect squares between two given numbers

'''
Reference
http://www.geeksforgeeks.org/find-number-perfect-squares-two-given-numbers/

We take floor of sqrt(b) because we need to consider numbers before b.

We take ceil of sqrt(a) because we need to consider numbers after a.
'''


import math
def CountSquares(a,b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)
 
# Driver Code
a = 8
b = 24
print("squares between %d and %d = %d " % (a,b,int(CountSquares(a,b))))

'''
Write an efficient program to unset the right most bit and count number of 1s in binary representation of an integer

REFERENCE:
http://www.geeksforgeeks.org/count-set-bits-in-an-integer/

NOTES: Brian Kernighan’s Algorithm
1. Subtraction of 1 from a number toggles all the bits (from right to left) till the 
rightmost set bit (including the righmost set bit)
2. So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset 
the righmost set bit. If we do n & (n-1) in a loop and count the no of times loop executes 
we get the set bit count.
3. Beauty of the this solution is number of times it loops is equal to 
the number of set bits in a given integer.
'''


#Count the number of ones in a number
def CountBinaryOnes(n):
	count = 0
	while(n):
		count += 1
		n &= n-1
		#print(n)
	return count

values = [3,4,5]
count = 0
for n in values:
	count = CountBinaryOnes(n)
	print("input=%s 1s=%d" %(n,count))

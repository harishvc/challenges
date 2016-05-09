
'''
Given a string and pattern with 1's and 0's find the minimum # of turn needed to make sure the pattern does not appear in the string.

Example:
input   = 00101 101 100 101
pattern = 101
#occurances of pattern = 3
#turns = 3
'''

def flip(a,pattern):
	turns = 0
	asize =len(a)
	psize = len(pattern)
	for i in range(psize-1,asize):
		#substring matches pattern
		if a[i+1-psize:i+1] == pattern:
				turns += 1
	return turns

a = "00101101100101"
pattern="101"
print("input >>>", a, " length=",len(a))
print("# of flips=",flip(a,pattern))


'''
Given a string and pattern with 1's and 0's find the minimum # of turn needed to make sure the pattern does not appear in the string.

Example:
input   = 00101 101 100 101
pattern = 101
#occurances of pattern = 3
#turns = 3

NOTES:
1. Observe the pattern
   - Are there pattern inside the pattern?
   - How long is the pattern?
   - Is the pattern pre-determined or run-time?
2. Information about the pattern will determine if we need to go back and check again when there is match
'''

def turns(a,pattern):
	turns = 0
	asize =len(a)
	psize = len(pattern)
	for i in range(psize-1,asize):
		#substring matches pattern
		if a[i+1-psize:i+1] == pattern:
				turns += 1
	return turns

a = "00101101100101"
#pattern has no sub-patterns, so just keep going forward
pattern="101"
print("input >>>", a, " length=",len(a))
print("# of turns=",turns(a,pattern))

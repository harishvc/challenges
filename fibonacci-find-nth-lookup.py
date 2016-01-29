#Question: Find the nth Fibonacci number
'''
The Fibonacci Sequence is the series of numbers:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34 , ....
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3

References:
1. https://www.mathsisfun.com/numbers/fibonacci-sequence.html
2. http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibseries.html
'''
#Solution using lookup to save time
#Time complexity: O(n), Space complexity: O(n)

lookup = {}
def CheckLookup(n):
	if n in lookup.keys():
		#print("Found ..." , n)
		return True
	else:
		return False

def fib(n):
	n1 = None
	n2 = None
	if (n <= 2):
		lookup[n] = 1
		return 1
	#n-1	
	if(CheckLookup(n-1) is False):
		n1 = fib(n-1)
		lookup[n-1] = n1
	else:
		n1 = lookup[n-1]

	#n-2
	if(CheckLookup(n-2) is False):
		n2 = fib(n-2)
		lookup[n-2] = n2
	else:
		n2 = lookup[n-2]

	lookup[n] = n1 + n2
	return n1 + n2

for n in range(1,11):
	print("f(%d)=%d" % (n,fib(n)))


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
#Question: Find the nth Fibonacci number
def FibonacciIterative(n):
    sum = 0
    n0 = 0
    n1 = 1
    if (n < 2):
        return n
    else:
        for i in range(1,n):
            sum = n0 + n1
            n0 = n1
            n1 = sum
        return sum    

def FibonacciRecursive(n):
    if (n < 2):
        return n
    else:
        return (FibonacciRecursive(n-1) + FibonacciRecursive(n-2))

for x in range(0,5):
    print("%d = %d" % (x,FibonacciIterative(x)))

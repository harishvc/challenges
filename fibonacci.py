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

#Question: Find the Fibonacci sequence
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1) #recursive call

#Range: 0-10
start = 0  #start
end =  10   #end
print("range for Fibonacci series:", range(start, end))
print("Fibonacci series:", list(map(fib, range(start,end+1))))

#Range: 6-10
start = 6  #start
end =  10   #end
print("range for Fibonacci series:", range(start, end))
print("Fibonacci series:", list(map(fib, range(start,end+1))))

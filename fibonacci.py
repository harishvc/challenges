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
#Question: Find the Fibonacci series for a given range
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1) #recursive call
start = 0  #start
end =  10   #end
print("range for fibonacci series:", range(start, end))
print("fibonacci series:", list(map(fib, range(start,end+1))))
start = 6  #start
end =  10   #end
print("range for fibonacci series:", range(start, end))
print("fibonacci series:", list(map(fib, range(start,end+1))))

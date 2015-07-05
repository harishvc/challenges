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

#Question:Find odd numbers in the Fibonacci series
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = list(filter(lambda x: x % 2 , fib))
print("odd numbers in fibonacci series:", result)


#Question: Find even numbers in the Fibonacci series
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = list(filter(lambda x: x % 2 == 0 , fib))
print("even numbers in fibonacci series:", result)

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

#Solution 1: Iterative
#Time complexity: O(n), Space complexity: O(1)
def FibonacciIterative(n):
    a,b = 0,1
    for i in range(n):
        a, b = b, a+b
    return a    

    
#Solution 2: Recursive
#Time complexity: O(n), Space complexity: O(n), recursive calls need a stack size of n
def FibonacciRecursive(n):
    if (n < 2):
        return n
    else:
        return (FibonacciRecursive(n-1) + FibonacciRecursive(n-2))


#Solution 3: Bottom-up (Dynamic Programming)
#Start with the lowest values of the input and keep building the solutions for higher values
#Time complexity: O(n), Space complexity: O(n)
def FibonacciBottomUp(n):
    fibTable = [0,1]  #store values in a list
    for i in range(2,n+1): #range 2 .... n+1 since values for 0,1 are already in list
        fibTable.append(fibTable[i-1]+fibTable[i-2])  #append values to list so lookup is in constant time
        #if (i+1 == n+1):
            #print("sending ....", fibTable)
    return fibTable[n]    


#Solution 4: Top-down (Dynamic Programming)
#Preserve recursive calls and use the values if they are already computed
#Memoization (Caching): Store values computed, check if already computed before computing
#Time complexity: O(n), Space complexity: O(n)
fibTable = {1:1,2:1}  #store values in a global list
def FibonacciTopDown(n):
    if (n <= 2):
        #print ("***found value for n=",n)
        return 1
    if n in fibTable:
        #print ("***found value for n=",n)
        return fibTable[n]  #return value stored from global dictionary
    else:
        fibTable[n] = FibonacciTopDown(n-1) + FibonacciTopDown(n-2)  #add to global dictionary 
        #print ("++++ adding n=",n)
        return fibTable[n]

#Solution 5: Observartion based on bottom-up approach
# f(n) = f(n-1) + f(n-2)
# So we need to last two values to calculate the next
#Time complexity: O(n), Space complexity: O(1)
def FibonacciSimple(n):
    a,b = 0,1
    for i in range (n):
        a, b = b, a+b
    return a


for x in range(0,9):
    print("%d = %d" % (x,FibonacciIterative(x)))
y = 9
print("%d = %d" % (y,FibonacciBottomUp(y)))
y=  10
print("%d = %d" % (y,FibonacciTopDown(y)))

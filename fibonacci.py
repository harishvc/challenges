#Question1: Find the fibonacci series between a given range
start = 1  #start
end =  10   #end
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1) #recursive call
print "range for fibonacci series:", range(start, end)
print "fibonacci series:", map(fib, range(start,end+1))


#Question 2: Find odd numbers in the fibonacci series
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2 , fib)
print "odd numbers in fibonacci series:", result


#Question 3: Find even numbers in the fibonacci series
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2 == 0 , fib)
print "even numbers in fibonacci series:", result

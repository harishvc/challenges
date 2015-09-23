#lambda argument_list: expression 
#1.The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments. 
#2. You can assign the function to a variable to give it a name. 
#3. No return statement, contains the expression to be returned

#References
#http://www.python-course.eu/python3_lambda.php
#http://www.bogotobogo.com/python/python_functions_lambda.php
#https://developers.google.com/edu/python/sorting
#http://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/


#Question: Add two numbers using Lambda
sum = lambda x, y : x + y
print(sum(3,4)) #7

#Question: Find square of all even numbers from 0,10
def square(x):
    return x*x

#Solution 1
result = []
for x in range(0,10,2):
    result.append(square(x))
print(result)

#Solution 2: Using map
#The map() function applies a function 
# to every member of an iterable and returns the result.
result2 = map(square, range(0,10,2))
print(list(result2)) #python 3

#Solution 3: Using lambda
result3 = lambda x: x*x
print([result3(i) for i in range(0,10,2)])

#Solution 4: Using map and lambda
result4 = map(lambda x: x*x, range(0,10,2))
print(list(result4))


#Question: Find odd numbers in the Fibonacci series
fib = [0,1,1,2,3,5,8,13,21,34,55]
result5 = list(filter(lambda x: x % 2 , fib))
print("odd numbers in Fibonacci series:", result5)


#Question: Sort the list based on length of the string in the list
people = ['Harish', 'Jon', 'fooo']
print(sorted(people,key=len)) #['Jon', 'fooo', 'Harish']

#Question: Reverse sort list with numeric values
lucky = ['22', '11', '31']
lucky.sort(key=lambda x: int(x),reverse=True)
print(lucky) #['31', '22', '11']

#Question: Sort list of list by lucky number
people2 = [
    ['Harish', 'Chakravarthy', 22],  #first name, last name, lucky number
    ['Jon', 'Doe', 27],
    ['Foo', 'Bar', 18],
]
print(sorted(people2,key=lambda people_item: people_item[2],reverse=False))


#Question: Sort list of dictionaries with labels by lucky
people3 = [
    {'FirstName':'Harish','LastName':'Chakravarthy','Lucky':22},
    {'FirstName':'Jon', 'LastName':'Doe', 'Lucky':27},
    {'FirstName':'Foo', 'LastName':'Bar', 'Lucky':18},
]
print(sorted(people3,key=lambda people_item: people_item['Lucky'],reverse=False))

#Question: Sort dictionary by key, value. Find min and max value
people4 = {'zeek':4,
          'thomas':1,
          'bob':10,
          'ryan':7}
#sort by key
for key in sorted(people4):
    print("%s: %s" % (key, people4[key]))
#sort by value in descending order
print(sorted(people4.items(), key=lambda x: x[1],reverse=True)) #list of tuples
print("min = ", min(people4.items(), key=lambda x: x[1]))    
print("max = ", max(people4.items(), key=lambda x: x[1]))    
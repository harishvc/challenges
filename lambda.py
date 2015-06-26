#lambda argument_list: expression 
#1.The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments. 
#2. You can assign the function to a variable to give it a name. 
#3. No return statement, contains the expression to be returned

#References
#http://www.python-course.eu/python3_lambda.php
#http://www.bogotobogo.com/python/python_functions_lambda.php
#https://developers.google.com/edu/python/sorting
#http://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/


#Question 1: Add two numbers
sum = lambda x, y : x + y
print(sum(3,4)) #7

#Question: Find exponential of a number
L = [lambda x: x ** 2,lambda x: x ** 3,lambda x: x ** 4]
for f in L:
    print(f(3)) #9 27 81


#Question 2: Sort the list based on length of the string in the list
people = ['Harish', 'Jon', 'fooo']
print(sorted(people,key=len)) #['Jon', 'fooo', 'Harish']

#Question: Reverse sort list with numeric values
lucky = ['22', '11', '31']
lucky.sort(key=lambda x: int(x),reverse=True)
print(lucky) #['31', '22', '11']

#Question 3: Sort list of list by lucky number
people2 = [
    ['Harish', 'Chakravarthy', 22],  #first name, last name, lucky number
    ['Jon', 'Doe', 27],
    ['Foo', 'Bar', 18],
]
print(sorted(people2,key=lambda people_item: people_item[2],reverse=False))


#Question 4: Sort list of dictionaries with labels by lucky
people3 = [
    {'FirstName':'Harish','LastName':'Chakravarthy','Lucky':22},
    {'FirstName':'Jon', 'LastName':'Doe', 'Lucky':27},
    {'FirstName':'Foo', 'LastName':'Bar', 'Lucky':18},
]
print(sorted(people3,key=lambda people_item: people_item['Lucky'],reverse=False))

#Question 5: Sort dictionary by key, value. Find min and max value
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
####
lucky = ['22', '11', '31']
print(lucky)
lucky.sort(reverse=True)
print("sorted in reverse ...")
print(lucky)
print("~~~~~~~~~")

####
xyz = ['abcd','abcdef', 'abc']
print(xyz)
xyz.sort(key=len,reverse=True)
print("sorted in reverse string length ...")
print(xyz)
print("~~~~~~~~~")

#####List of lists
people2 = [
    ['Harish', 'Chakravarthy', 22],  #first name, last name, lucky number
    ['Jon', 'Doe', 27],
    ['Foo', 'Bar', 18],
]
print(people2)
people2.sort(key=lambda x: x[2],reverse=True)
print ("sorted by lucky number in reverse")
print(people2)
print("~~~~~~~~~")

####List of dictionaries
people3 = [
    {'FirstName':'Harish','LastName':'Chakravarthy','Lucky':22},
    {'FirstName':'Jon', 'LastName':'Doe', 'Lucky':27},
    {'FirstName':'Foo', 'LastName':'Bar', 'Lucky':18},
]
print(people3)
people3.sort(key=lambda x: x['LastName'],reverse=True)
print ("sorted by last name in reverse")
print(people3)


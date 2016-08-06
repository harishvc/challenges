###QUICK INTRO  
#Declare, initialize, update, delete
#
#Immutable - Cannot change value once created
#Strings - Immutable

#LIST - Mutable (inexpensive operation to make changes)
a = []
a = [1]
print(a.index(1)) #0 , print index position of element 1
a.append(2)
a.pop()         #2
a.append(1)
a.append(2)
a.append(3)
a.append(2)
a.remove(2) #1,2,3  remove first occurance
#
a.insert(3,0)   #insert at position 3 or append 
del a[:]        #remove all values in a list 
x in a          #check if x is in a, average time complexity O(n)
#
#
#QUEUE
import queue
q = queue.Queue()
q.put(1)  #Add elements to queue
q.put(2)
print(q.get()) #Get elements
print(q.empty()) #Check if queue is empty
#
#
#DEQUE - Double ended queue, add and remove from both ends
import collections
dq = collections.deque()
dq.append(1)
dq.append(2)
dq.extendleft([0])  #add elements to left
print(dq)           #deque([0, 1, 2])
print(len(dq))      #3
dq.pop()            #2
dq.popleft()        #0     
#
#
#SET - MUTABLE
#SET PROPERTIES: 
# 1. unique values
# 2. no gaurantee on the order of values
# 3. can't refer values by index 
a = set()
#1. ADD
a.add(99)
a.add(20)
a.add(30)
a.add(42)
a.add(56)
print(a)
#
#2. REMOVE VALUE THAT EXIST
a.remove(42)
print(a)
#
#3. REMOVE VALUE THAT MAY NOT EXIST
a.discard(7777)
print(a)
#
#4. REMOVE SOME RANDOM VALUE
z = a.pop()
print(a,z)
#
#5. LENGTH
print(len(a))
#
#6. ITERATE OVER
for i in a:
	print(i)
#
#7. Check if a value exists
if 30 in a:
	print("Found!")
#
#8. DELETE ALL VALUES IN A SET
a.clear()
print(a)   #set()	
# 
#


#DICTIONARY INTRO - MUTABLE
a = {}               #initialize
a[1] = 1             #assign
a[2] = 2
print(a[2])          #2
del a[3]             #delete key 3    
z = a.get(3,None)    #find key else initialize
                     #IMPORTANT: get DOES NOT add key to dict
print(z)             #None
print(len(a))        #2 , # of keys in dictionary
print(list(a.keys()))   #ALL keys as list
print(list(a.values())) #ALL values as list
if key in a.keys():     #Check if key exists
    print("key exists")
if value in a.values():  #Check if value exists
    print("value exists")
#
#
#create key automatically and initialize if not present, and return value
a = {}
a.setdefault('a',1) #insert key 'a' with value 1 if key 'a' does not exisit and returns the value 1
a.setdefault('b',2) #returns 2
a.setdefault('b',5) #returns 2 , since key 'b' already exists
print(a)            #{'a': 1, 'b': 2}
#
#DEFAULTDICT
import collections
d = collections.defaultdict(int) #values are of type int;handles non existant keys
d['abcd'] += 1  #handles non existant keys
d['abcd'] += 1
print(d['abcd']) #2
#
z = collections.defaultdict(list) #values are of type list; dict of list
z['a'].append('hello')
z['a'].append('world')
print(z['a']) #['hello', 'world']
#
s = collections.defaultdict(set) #values are of type set; dict of set
s['a'].add('world')
s['a'].add('hello')
print(s['a']) #{'hello', 'world'} order is NOT retained!
    
#SPRINTF
a = "Hello %s" % ("Harish")
print(a)  #Hello Harish

#FOR LOOP
a = "Harish"
for i in a:
    print(i,end=",")  #H,a,r,i,s,h,
#
a = [11,12,13,14,15]
for i in a:
    print(i,end=",")  #11,12,13,14,15,
#
a = "Harish"
for i,v in enumerate(a):
    print(i,v)  # 0, H   1,a
#    
for i in range(5):
    print(i)         #0 1 2 3 4
#    
for i in range(0,5,2): #increment by 2
    print(i)         #0 2 4
#
for i in range(5,0,-2): #decrement by 2
    print(i)        #5,3,1

for i in range(0,5)[::-1]:
    print(i)        #4,3,2,1,0

#convert string to list
a = input()      #1,2,3,4,5
print(type(a),a)
b = list(map(int,a.split(",")))
print(type(b),b)  #[1,2,3,4,5]


#Find max value in dictionary
d= {'a':2,'b':5,'c':3}
print(d)
print("Key with max value =", max(d, key=d.get))
print("~~~")

###Sorted by Key
d = {"ZHarish": 22, "Joe": 115, "Moe": 52}
print("Sorted by key ...")
for key in sorted(d):
    print("%s: %s" % (key, d[key]))
    
###Sorted by value
print("Sorted by value ...")
for key in sorted(d, key=d.get, reverse=False):
    print("%s: %s" % (key, d[key]))


###Use list comprehension to initialize list
#[<expression> for <element> in <sequence> if <conditional>]
#Initialize x with all even numbers between 1 ... 11
x = [i for i in range(11) if i%2 == 0]
print(x) #[0, 2, 4, 6, 8, 10]

###Tuple
#immutable (along with strings)  - value can't be changed after created!
#take less space in bytes
#used for structure
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
#days[1] += "xxx"  #Error
for x in days:
    print(x)

###List
#mutable   
days2 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days2[1] = "xxx"
for x in days2:
    print(x)    


###Read from file
#with keyword is used when working with unmanaged resources (like file streams). 
# It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown
#with open("python-intro2111.py") as f:
#        data = f.read()
        #do something with data
#        print(data)
        
xyz = "old stuff"            
def test(x):
    x[0] = 10
    print("xxxxxxxxxx")
    global xyz 
    xyz = "new stuff"
    return x
x= [5]
print(x)
print(xyz)
test(x)
print(x)  #Value changes since list is mutable - "pass by objects"
print(xyz)

###Print each character in a string
test="Hello"
for x in test:
    print(x)
    

#Initialize matrix with random values
def Initialize(matrix):
    from random import randint
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[row])):
            matrix[row][col] = randint(1,26)

#Print Matrix
def PrintMatrix(matrix): 
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[row])):
            print("%d" % (matrix[row][col]),end=" ")
        print("")
    

# Creates nxm matrix
n = 5 #rows
m = 3 #cols
matrix = [[0 for x in range(n)] for x in range(m)]

print("~~~~~~")
Initialize(matrix)
print ("%dx%d matrix >>>" % (m,n))
PrintMatrix(matrix)
    

#DATA STRUCTURES: QUICK INTRO  

#Immutable - Cannot change value once created

#Strings - Immutable
#Print each character in a string
test="Hello"
for x in test:
    print(x)

test = "Hello    World"
a = test.split() #SPLIT with no arguments uses ONE or MANY spaces as delimiter
print(a)  #Hello, World


#####LIST - Mutable (inexpensive operation to make changes)
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
del a[0:1]      #remove value 0
x in a          #check if x is in a, average time complexity O(n)
#LIST SPLIT
x = [1, 2, 3, 4]
print(x[3])        #index position 3, 4th element
print(x[-1])       #last index
print(x[-3])       #3rd index from the end
print(x[1:3])      #elements in index 1 & 2
print(x[:2])       #elements in index 0 & 1
print(x[1:])       #elements in index 1 to end of list
print(x[-2:4])     #elements in between 2nd index from the end and 3rd index from start
print(x[::2])      #every other element is skipped
print(x[:-2])      #elements in index 0,1
print(x[-2:])      #elements in index 2,3
print(x[::-1])     #reverse
print(x[-1:0:-1])  #elements in index position 3 (last, -1) and index position 1 going left

#Tuple
#immutable (along with strings)  - value can't be changed after created!
#take less space in bytes
#used for structure
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
#days[1] += "xxx"  #Error
for x in days:
    print(x)



#QUEUE
import queue
q = queue.Queue()
q.put(1)  #Add elements to queue
q.put(2)
print(q.get()) #Get elements
print(q.empty()) #Check if queue is empty


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
    

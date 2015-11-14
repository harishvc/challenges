#swap without using temporary space
#check performance? 
#import dis  #Bytecode Disassembler
a,b = 1,2
print(a,b) # 1 2
a,b = b,a
print(a,b) #2 1

#https://docs.python.org/3.4/tutorial/datastructures.html#more-on-lists
a = [66.25, 333, 333, 1, 1234.5]
b = [77,55]
a[0] = 9999
#Count number of times 333 occurs
print("333 occurs:%d times" % (a.count(333)))
#Index in the list for first occurrence of  333 
if 333 in a:
    print("333 occurs at position:%d" % (a.index(333)))
#Count number of times 45 occurs
print("45 occurs:%d times" % (a.count(45)))
#Add element to the end of the list
a.append(99)
#Add element at start of the list
a.insert(0,1)
#Print all elements in the list
print("List after insert and append:", a)
#Remove first occurrence element with value 333
a.remove(333)
#Print all elements in the list
print("List after removing first occurrence of value 333:", a)
#Remove and returns element at index = 3)
a.pop(3)
#Print all elements in the list
print("List after removing element in position 3:", a)
#del statement is similar to pop except no return and used to slice (range)
del a[4:5]
print("List after removing element in position 4 and 5:", a)
#Sort array - ascending order
a.sort()
print("Sorted list:",a)
#reverse array - decending order
a.reverse()
print("Reverse sorted list:",a)
#extend list with element from another list
a.extend(b)
print("List after extending b:", a)
#Create an array with 20K elements and sort it reverse
#l = range(20000)
#l = sorted(l, reverse=True)

print("### STACK ###")
#STACK -  last-in, first-out;easy to use a list as a stack;combination of append() and pop()
stack = [1,2,3]
stack.append(4) 
stack.append(5) 
print("List after append 4,5:", stack)
stack.pop()
print("List after pop:", stack)


print("### QUEUE ###")
#QUEUE -  first-in, first-out;lists are not efficient for this purpose because all of the other elements have to be shifted by one
queue = []
queue.append(6)
queue.append(7)
queue.append(8)
print("List after append 6,7,8:", queue)
queue.pop(0)
print("List after pop first position", queue)

print("List Comprehensions")
#List comprehensions provide a concise way to create lists
#A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
powers = [2**n for n in range(10)]
print (powers)
vec = [-4, -2, 0, 2, 4]
vec2 = [x for x in vec if x >= 0]
print ("vec = ", vec)
print ("vec2 = ", vec2)
vec3 = [[1,2,3], [4,5,6], [7,8,9],[9,6,4]]
print ("vec3 = ", vec3)
vec4 = [num for elem in vec3 for num in elem]
print ("vec4 = ", vec4)

print("Matrix")
#3x4 = 3 lists of length 4
matrix1 = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
matrix2 = [[row[i] for row in matrix1] for i in range(4)]
print("3x4 matrix:", matrix1)
print("4x3 matrix:", matrix2)

print("Tuples")
#A tuple consists of a number of values separated by commas, usually contain an heterogeneous sequence of elements accessed via unpacking or indexing
tuple = 12345, 54321, 'hello!'
t1,t2,t3 = tuple
print("Tuple tuple=",tuple)
print("t1=%d,t2=%d,t3=%s" % (t1,t2,t3))


print("Set")
#A set is an unordered collection with no duplicate elements
#NO DUPLICATE ITEMS
s1 = set("Hello World!")
s2 = set("Hello Python!")
#{'a', 'b','z','a'}
#print("Hello World in set:",s1)
print ("s1 = ",s1)
print ("s2 = ",s2)
print ("Characters only in s1, s1-s2 = ",s1-s2)
print ("characters in both s1 & s2, s1 & s2 = ",s1&s2)
print ("Characters in s1 or s2 but not both, s1 ^ s2", s1 ^ s2)
print ("Characters in s1 or s2, s1 | s2 = ",s1|s2)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
s3 = set(basket)
print ("basket:", basket)
print ("basket set:", s3)



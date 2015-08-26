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
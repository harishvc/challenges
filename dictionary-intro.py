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

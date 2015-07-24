#Question: Find pairs in an integer array whose sum is equal to a given value

#Time complexity: O(n)
#Space complexity: O(n)

input = [5,7,8,2,3,0]
mydict = {}
MAX = 10

print("input >>>", input)
print("Listing pairs that add up to ", MAX)

#Store array elements in a dictionary - constant access time
for i in range(len(input)):
    mydict[input[i]] = i

#Iterate array to find if key exists for MAX-array element
for i in range(len(input)):
    #print(i, " comparing .....", input[i], MAX-input[i])
    if( MAX-input[i] in mydict and  mydict[MAX-input[i]] != i):
        print ("[%d,%d]" % (input[i],MAX-input[i]))
'''
Question: Find the min value of two unsorted lists
'''

a = [6,3,4,8]
b = [9,4,10,3]

#Step 1: Iterate through both the list and find the intersection
#c = [val for val in a if val in b]
#simple generator!
c = [x for x in a and b]

#Step 2: Iterate through the intersection to find the min
min = c[0]
for x in range(1,len(c)):
    if c[x] < min:
        min = c[x]
print(a , b)        
print("min = ", min)

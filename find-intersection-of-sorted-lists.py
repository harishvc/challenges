'''
Question: Find the intersection of two sorted list

Time complexity: O (minimum(i,j)), when i is len of a, j is len of b

Output:

list 1 >>> [1, 3, 4, 7, 9]
list 2 >>> [2, 3, 5, 6, 7]
common elements >>> 
3
7
'''

a = [1,3,4,7,9]   
b = [2,3,5,6,7]    
print("list 1 >>>",  a)
print("list 2 >>>",  b)
i = 0
j = 0
print ("common elements >>> ")
while (i < len(a) and j < len(b)):
  if (a[i] == b[j]):
        print(a[i])
        i += 1
        j += 1
  elif (a[i] > b[j]):
        j += 1
  else:
      i+= 1


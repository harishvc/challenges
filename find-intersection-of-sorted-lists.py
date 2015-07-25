#Question: Find the intersection of two sorted arrays

#Time complexity: O (minimum(i,j)), when i is len of a, j is len of b

a = [1,3,4,7,9]   
b = [2,3,5,6,7]    
i = 0
j = 0
while (i < len(a) and j < len(b)):
  if (a[i] == b[j]):
        print(a[i])
        i += 1
        j += 1
  elif (a[i] > b[j]):
        j += 1
  else:
      i+= 1


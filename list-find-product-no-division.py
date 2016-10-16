#Given a list of numbers, return a list of products of **all other numbers** (no division) in O(n) time

'''
Reference
http://stackoverflow.com/questions/2680548/given-an-array-of-numbers-return-array-of-products-of-all-other-numbers-no-div

NOTES 
The trick is to construct a list (for 4 elements)
[              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2],  ]
[ a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1,  ]
'''


#Find products without division
#Time complexity: O(n)
def findPWD(a):
   size = len(a)
   result = [1]*size
   psf = a[0] #product so far
   #go left to right
   for i in range(1,size):
      result[i] = psf
      psf *= a[i]
   psf = a[-1] #reset product so far with last value
   #go right to left
   for i in range(size-2, -1,-1):
      result[i] *= psf
      psf *= a[i]
   return result

a = [4,2,6]
print(a, "  >>>> ", findPWD(a))


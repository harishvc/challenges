#Radix sort

'''
ALGORITHM:
1. The idea of Radix Sort is to do digit by digit sort starting from 
   least significant digit to most significant digit. 
2. Radix sort uses counting sort as a subroutine to sort.
3. Radix sort creates a bucket for each digit
4. For decimal values, the number of buckets is 10
5. Values are continuously sorted by significant digits all the way up 
   to the most significant digit

NOTES:
Time complexity: 
 - Best Case/Average Case/Worst Case = O(kn)
 - k=length of the longest number, n=size of the input array
 - Lower bound for Comparison based sorting algorithm is nlogn - can't do better!
 - If k < log N, radix is a GOOD FIT!
 - If k is greater than log(n) then an nlog(n) algorithm would be a better fit

REFERENCES:
1. http://www.geeksforgeeks.org/radix-sort/
2. http://www.geekviewpoint.com/python/sorting/radixsort
'''

#Source: http://www.geekviewpoint.com/python/sorting/radixsort
import random
def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for  i in aList:
      tmp = i / placement
      buckets[int(tmp % RADIX)].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX


alist = [170, 45, 75, 90, 802, 24, 2, 66]
random.shuffle(alist)
print("input >>>", alist)
radixsort(alist)
print("Radix sort >>>", alist)
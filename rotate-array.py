#Reference: http://programmingpraxis.com/2010/10/12/rotate-an-array/

#Question: Rotate single dimension array

#Source:http://stackoverflow.com/questions/17350330/python-array-rotation
def rotate(l, y=1):
   if len(l) == 0:
      return l
   y = -y % len(l)     # flip rotation direction
   return l[y:] + l[:y]

print ("[1,2,3,4,5] rotated by 0 ===> ", rotate([1,2,3,4,5],0))
print ("[1,2,3,4,5] rotated by 2 ===> ", rotate([1,2,3,4,5],2))
print ("[1,2,3,4,5] rotated by -2 ===> ", rotate([1,2,3,4,5],-2))
print ("[1,2,3,4,5] rotated by 7 ===> ", rotate([1,2,3,4,5],7))
print ("abcdefghijk rotated by 4 ===> ", rotate('abcdefghijk',4))

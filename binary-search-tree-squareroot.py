#Find the square root of an integer without using square root function 

'''
REFERENCE:
http://www.geeksforgeeks.org/square-root-of-an-integer/

OBSERVATION:
1. if x is sqrt of y then x^2 = y

ALGORITHM:
1. Apply Binary Search on range on rumbers from 1 .... n (input)
2. Find mid point, go left or right
'''


def sqrt(a):
	start = 1
	end = a
	while True:
		mid =  (end+start)//2  #IMPORTANT!!!
		tmp = mid*mid
		#print("start=%d, end=%d, mid=%d" % (start,end,mid))
		if tmp == a:
			return mid
		#go left	
		elif tmp > a:
			end = mid-1
		#go right
		else:
			start = mid + 1

a = 100
print("square root of %d = %d" % (a,sqrt(a)))
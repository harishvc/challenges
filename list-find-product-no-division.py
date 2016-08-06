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
def findPWD(a):
	size = len(a)
	#result list initialized to 1
	result = [1] * size
	#go forward
	tmp = 1
	for i in range(0,size):
		#IMPORTANT replace with tmp, since no prior value
		result[i] = tmp
		tmp = a[i]*tmp  #take value to next index
	#go backward
	tmp = 1
	for i in range(size-1,-1,-1):
		#IMPORTANT * tmp since values are already there
		result[i] *= tmp 
		tmp = tmp*a[i]   #take value to previous index
	return result


a = [4,2,6]
print(a, "  >>>> ", findPWD(a))


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
def FPWD(a):
	products = [0]*len(a)
	tmp = 1
	for i in range(len(a)):
		products[i] = tmp
		tmp = tmp * a[i]
	tmp = 1
	for i in range(len(a)-1,-1,-1):
		products[i] = products[i] * tmp
		tmp =  tmp * a[i]
	return products 


a = [4,2,3]
print(a, "  >>>> ", FPWD(a))
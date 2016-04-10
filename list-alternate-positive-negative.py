
#Given a list containing postive and negative values print values
#alternatively (postive and negative or vise versa) while retaining 
#order and contant space

def alternateValues(a):
	size = len(a)
	for current in range(0,size-1,2): #increment by 2
		i  = current+1
		if a[current] > 0:
			#find next negative
			while i < size and a[i] > 0:
				i += 1
		else:
			#find next positive
			while i < size and a[i] < 0:
				i += 1
		#next two values are alternating
		if (i < size):
			a[current+1],a[i] = a[i],a[current+1]

a = [-2,3,-4,9,-1,-7,1,5]
print("input >>> ", a)
alternateValues(a)
print("result >>> ", a)






















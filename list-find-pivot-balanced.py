#Find the PIVOT value that splits the list into balanced partitions
# input=[5,4,6,10,7,25] pivot =7


'''
OBSERVATION
1. a + b + c +  d = total
2. a + b = d  if c is the pivot
3. from 1 & 2:  
   a + b + c + a + b = total
   c = total - 2(a+b)
'''
def findPivot(a):
	#step 1: find sum of the list
	total = 0
	for i in a:
		total += i

	#step 2: iterate the list to find PIVOT
	currentsum = a[0]
	for i in range(1,len(a)):
		if a[i] == total - (2*currentsum):
			print("pivot =", a[i])
		else:
			currentsum += a[i]

a = [5,4,6,10,7,5,20]
print("input >>> %s" % (a))
findPivot(a)


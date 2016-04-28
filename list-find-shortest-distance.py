#Given a list of integers and two target values find the shortest distance between the two target values

'''
NOTES:
1. Use two pointers, one for each target value
2. Iterate through the list
   2.1 When both the target values are found, calculate distance, 
   2.2 Move the pointer with LOW index value
'''
def ShortestDistance(a,num1,num2):
	count = len(a)
	l = 0
	r = 0
	result = None
	while True:
		#num1 first index position
		while l < count and a[l] != num1:
			l += 1
		#num2 first index position:
		while r < count and a[r] != num2:
			r += 1
		#result
		if (l < count and r < count):
			if result is None:
				result = abs(l-r)
			elif abs(l-r) < result:
				result = abs(l-r)
			#determine while pointer moves next
			if (l < r):
				l+=1
			else:
				r+=1
		else:
			assert l == count or r == count, "Error"
			break
	return result


a = [0,4,3,2,4,5,6,7]
num1 = 4
num2 = 7
print("input >>>", a)
print("ShortestDistance(%d,%d)=%d" % (num1,num2,ShortestDistance(a,num1,num2)))


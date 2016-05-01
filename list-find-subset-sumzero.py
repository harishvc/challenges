#Given a list with postive, negative and repeated values find a continuous subarray of sum zero


#Solution 1: O(n^2)
def sumZero1(a):
	size = len(a)
	sum = 0
	result = None
	for i in range(0,size):
		if a[i] == 0:
			result = a[i]
			break
		sum = a[i]
		for j in range(i+1,size):
			sum += a[j]
			if(sum ==0):
				result = a[i:j+1]
				break

	if result is not None:
		return result
	else:
		return
'''
Solution 2: time and space: O(n)
1. store `sum` and index position in a hash
2. if you have already calculated the sum, you have a result
3. PROOF
   >> a1 + a2 = sum
   >> a1 + a2 + a3 + a4 + a5 = sum
   >> a3 + a4 + a5 = 0
'''
def sumZero2(a):
	size = len(a)
	sum = {}
	count = 0
	result = None
	for i in range(0,len(a)):
		if a[i] == 0:
			result = a[i]
			break
		count += a[i]
		if count in sum.keys():
			result = a[sum[count]+1: i+1]
			break
		else:
			sum[count] = i
	if (result is None):
		return
	else:
		return result


a = [5,1,2,-9,7,4]
print(a, " >>> ", sumZero2(a))

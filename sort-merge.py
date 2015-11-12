'''
Question: Given two sorted lists merge them.
'''

#Source: http://stackoverflow.com/questions/2488889/how-can-i-merge-two-lists-and-sort-them-working-in-linear-time
#Solution 1: Build result array in descending order
def merge1(l, r):
	result = []
	while l and r:
		if l[-1] > r[-1]:
			result.append(l.pop())
		else:
			result.append(r.pop())
	result+=(l+r)[::-1]
	result.reverse()
	return result
 
 
'''
Solution 2: Build result array in ascending order
Time complexity: O(n) where n is the length of the shorter list 
                 provided the length of the list is know.
Space complexity: O(m+n)
'''
def merge2(a1,a2,l1,l2):
	i = 0
	j = 0
	result = []
	while (l1 > i and l2 > j):
		if (a1[i] == a2[j]):
			#Same
			result.append(a1[i])
			result.append(a2[j])
			i +=1
			j +=1
		elif (a1[i] > a2[j]):
			#next small value from a2
			result.append(a2[j])
			j += 1
		else:
			#next small value from a1
			result.append(a1[i])
			i += 1
	#traverse rest of the list
	if (l1 <= i):
		#append all elements from a2
		result.extend(a2[j:])	
	if (l2 <= j):
		#append all elements from a1
		result.extend(a1[i:])
	return result 
		

a1 = [1,2,6,70,90]
a2 = [1,3,5,9]
print("Input ==>",a1,a2) 
result = []
result = merge2(a1,a2,len(a1),len(a2))
print("Merged sorted output ===>", result)

'''
Given a list of unsorted values find the value that occurs the most 
(AKA most popular value, majority element)

1. [2,2,2,3,3] = 2
2. [2,3,3,2,2,2] = 2
'''

#solution1: Time & Space complexity O(n)
#Iterate the list and count # occurances of a value

#solution 2: Time complexity O(n)
#Moore's voting algorithm
'''
Basic idea of the algorithm is if we cancel out each occurrence of an element 'e'
with all the other elements that are different from 'e' then 'e' will exist 
till end if it is a majority element.


Limitation:
1. Input should have a value that occurs the most (no validation)
2. Majority element occurs more than 50% of the time
'''

def PopularValue(a):
	popular = None
	count = 0
	for value in a:
		if count == 0:
			popular = value
			count = 1
		elif value == popular:
			count += 1
		elif value != popular:
			count -=1
	return popular

myinput = [[2,2,2,3,3],[2,3,3,2,2,2]]
for a in myinput:
	print("%s popular value=%d" % (a,PopularValue(a)))

#Largest Sum Contiguous Subarray


'''
Kadane Algorithm:

Iterate values
    - find sum so far
    - if sum so far > max sum, update max sum
    - else sum so far is NEGATIVE, reset to 0

Limitation:
 - Only works if there are +ve and -ve values

Reference:
1. http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
'''
def maxContiguousSum1(a):
	sum_so_far =0
	max_sum = 0
	for i in range(0,len(a)):
		sum_so_far += a[i]
		if sum_so_far > 0:
			max_sum = max(max_sum,sum_so_far)
		else:
			assert sum_so_far < 0 , "Logic error"
			#IMPORTANT: reset sum_so_far
			sum_so_far = 0
	return max_sum


#Handle list of all negative values
#Check if values are negative and return the smallest negative value!
import sys
def maxContiguousSum(a):
	sum_so_far =0
	max_sum = 0
	hasAllNegativeValues = True
	nmax_sum = sys.maxsize
	for i in range(0,len(a)):
		if a[i] < 0 and hasAllNegativeValues:
			if a[i] < nmax_sum:
				nmax_sum = a[i]
		else:
			hasAllNegativeValues  = False #+ve value found!
			sum_so_far += a[i]
			if sum_so_far > 0:
				max_sum = max(max_sum,sum_so_far)
			else:
				sum_so_far = 0
	if hasAllNegativeValues:
		return nmax_sum
	else:
		return max_sum		




a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("input >>> %s , max contiguous sum=%d" % (a,maxContiguousSum(a)))

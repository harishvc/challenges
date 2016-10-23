#Largest Sum Contiguous Subarray

'''
Kadane Algorithm:
  - keep track of sum_so_far  (max of sum_so_far + new_value or new_value)
  - keep track of max_sum
  - working with all -ve values
    - Logic above works if there are +ve and -ve values
    - If all input values are -ve return the smallest negative value!

Reference:
1. http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
2. http://www.programcreek.com/2013/02/leetcode-maximum-subarray-java/
'''

#Handle input with  
#  - +ve & -ve values
#  - all negative values
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
			sum_so_far = max(a[i], sum_so_far+a[i])
			max_sum = max(max_sum,sum_so_far)
	if hasAllNegativeValues:
		return nmax_sum
	else:
		return max_sum		




a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("input >>> %s , max contiguous sum=%d" % (a,maxContiguousSum(a)))

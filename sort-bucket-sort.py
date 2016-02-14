#Bucket Sort (or Bin sort)

'''
ALGORITHM:
1. Find range: maxValue, size of input
2. Find #buckets based on size of inputL
3. Hash algoritm to drop values in buckets 
4. Iterate through input, insert value inside appropriate bucket
5. Sort value in each bucket
6. Iterate all the buckets to generate sorted list

NOTES:
1. Distribute elements of the input into a number of buckets. 
2. Each bucket is then sorted individually using a different sorting algorithm
3. Need maxValue value (limitation)
4. Hash algorithm impacts performance!
5. Works well on a well distributed data set  WITHOUT repetition!!!
6. NOT a comparison sort (but can be modified to use comparison)
7. Time complexity: O(n + k), n=#values, k=#buckets

REFERENCE:
http://pages.cs.wisc.edu/~siff/CS367/Notes/sorting.html
'''

import random
import math
def bucketSort(input):
	#Find maxValue, size and buckets count
	maxValue = None
	minValue = None
	size = 0
	for x in input:
		size += 1
		if maxValue is None or maxValue < x:
			maxValue = x
		if minValue is None or minValue > x:
			minValue = x
	rangeValue = maxValue - minValue
	bucketSize = int((rangeValue + size)/size)
	bucketsCount = int((maxValue-minValue)/size) + 1
	#print("size=%d, maxValue=%d, rangeValue=%d, bucketSize=%d, #buckets=%s" % (size,maxValue,rangeValue,bucketSize,bucketsCount))
	buckets = [list() for _ in range(bucketsCount)]
	
	#Insert values into buckets
	for x in input:
		location = myhash(x,minValue,bucketsCount)
		buckets[location].append(x)

	#Sort each bucket using insertion sort
	for bucket in buckets:
		insertionSort(bucket)

	#Iterate the buckets to generate the sorted list
	count = 0
	for bucket in buckets:
		for value in bucket:
			input[count] = value
			count += 1

def myhash(value,minValue,bucketSize):
	location = int((value-minValue)/bucketSize) 
	#print(value,"=",location)
	return location


def insertionSort(input):
	inputLength = len(input)-1  #ignore last value
	for i in range(inputLength):
		while i >= 0 and i< inputLength and input[i] > input[i+1]:
			input[i+1],input[i] = input[i],input[i+1]
			i -=1

alist = [54,26,93,17,77,31,44,55,20]
random.shuffle(alist)
print("input >>>", alist)
bucketSort(alist)
print("bucket sort:",alist)
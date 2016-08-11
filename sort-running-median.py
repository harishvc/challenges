#Median in a stream of integers (running median)
#http://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/

'''
5  > 5
5, 15 > 10
5, 15, 1 > 5
5, 15, 1, 3 > 4
'''

#Modified insertion sort
#go left: if the new value at index left is < val at index left-1
def insertionSort(a,left):
	while left > 0 and a[left] < a[left-1]:
		a[left],a[left-1] = a[left-1],a[left]
		left -= 1

def findMedian(a,size):
	q = size//2   #find quotient
	if size%2 == 1: #odd
		return a[q]
	else: #even
		return (a[q] + a[q-1])/2

a = [5,15,1,3]
for i in range(0,len(a)):
	insertionSort(a,i)
	m = findMedian(a,i+1)
	print(a[0:i+1], ">>>>", m)

'''
Question: Find median of two sorted arrays

References:
1. Find median in odd and even #arrays
https://www.mathsisfun.com/median.html

2. Algorithm for finding median of two sorted arrays
http://www.geeksforgeeks.org/median-of-two-sorted-arrays/

Algorithm:
1) Calculate the medians m1 and m2 of the input arrays ar1[] 
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)
3) If m1 is greater than m2, then median is present in one 
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one    
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays 
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get 
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
'''

#Modified mean to return mean and next index position in the list
def median(a):
    length = len(a)
    if (length % 2 != 0):  #odd since mod is > 0
        return (a[(length+1)//2 - 1],length//2)  #floor
    else: #even
        t1 = a[(length//2) - 1]
        t2 = a[length//2]
        t3 = (t1 + t2)/2  #could be a decimal
        return (t3,length//2)

def FindMedian2List(a,b,m1,n1,m2,n2):
    #condition 1
    if (m1 == m2):
        return m1    
    #condition 2
    elif (len(a) == 2 and len(b) == 2):
        return ((max(a[0],b[0]) + min(a[1],b[1]))/2)
    #condition 3
    elif(m1 > m2):
        ta = a[:n1+1]
        tb = b[n2:]
        tam1,tan1 = median(ta)
        tbm2,tbn2 = median(tb)
        return(FindMedian2List(ta,tb,tam1,tan1,tbm2,tbn2))
    #condition 4
    else: #m1< m2
        ta = a[n1:]
        tb = b[:n2+1]
        tam1,tan1 = median(ta)
        tbm2,tbn2 = median(tb)
        return(FindMedian2List(ta,tb,tam1,tan1,tbm2,tbn2))

a = [1, 12, 15, 26, 38]
b = [2, 13, 17, 30, 45]
m1,n1 = median(a)
m2,n2 = median(b)
print("input 1 >>> ",a)
print("input 2 >>> ",b)
print("median = ", FindMedian2List(a,b,m1,n1,m2,n2))


######
#Solution 2
'''
NOTES: :notes: :rocket:
1. A given value is median if there are X values greater and Y values lesser
2. In a sorted list `a` of size 7 where index positions are 0 1 2 3 4 5 6 
   value at index position 3 (7//2+1) is median if a[3]>a[2] and a[3]<a[4]
3. In a sorted list `a` of size 3 and sorted list `b` of size 4 value at
   index position a[2] is median if a[2] > b[0] and a[2] < b[1]
'''

def findMedian(a,asize,b,bsize,countBelow):
	start = asize//2
	count = 0
	while (start >=0 and start <= asize):
		count = asize-start  
		remaining = countBelow - count
		#print("checking %d remaining=%d" % (a[start],remaining))
		#case 1:
		if (remaining == 0 and a[start] > b[bsize]):
			return a[start]
		#case 2:
		elif a[start] > b[bsize-remaining] and a[start] < b[bsize-remaining+1]:
			return a[start]
		#case 3:
		elif a[start] <  b[bsize-remaining] and a[start] <  b[bsize-remaining+1]:
			start +=1
		#case 4:
		else:
			start -= 1
	#case 5: No median
	#print("No Median")
	return None

def findMedianWrapper(a,asize,b,bsize,countBelow):
	#check list a
	median = findMedian(a,asize,b,bsize,countBelow)
	if median is not None:
		return median
	else:
		#median in list b
		return findMedian(b,bsize,a,asize,countBelow)
#test 1
a = [1,3,5]
b = [2,6,8,10]
#test 2
#a= [1,2,3]
#b= [5,6,7,8]
acount = len(a)
bcount = len(b)
#Question: How to handle even count?
medianIndex = (acount+bcount)//2 + 1
# values below the median
countBelow = acount+bcount - medianIndex
print("input >>> %s%s \nmedian >>> %d" % (a,b,findMedianWrapper(a,acount-1,b,bcount-1,countBelow)))

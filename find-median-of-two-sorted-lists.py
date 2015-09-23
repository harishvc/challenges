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
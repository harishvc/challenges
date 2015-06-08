#Question: Given a million points (x, y), give an O(n) solution to find the 100 points closest to (0, 0).

#Source: http://programmingpraxis.com/2012/11/27/amazon-interview-question/
from math import sqrt, ceil
 
def norm(point):
    return sqrt(point[0]**2 + point[1]**2)
 
def k_smallest(k, a, f):
    n, medians = len(a), []
    # solve the particular cases
    if k == n: return a[:]
    if n <= 5: return sorted(a, key=f)[:k]
    # split the list in n/5 buckets and compute their medians
    for i in range( int(ceil(n / 5.)) ):
        start, end = 5*i, min(5*(i + 1), n)
        b = sorted(a[start:end], key=f)
        medians.append(b[(end - start) // 2])
    # find the median of the medians using recursivity with k=n/2
    splitElm = max(k_smallest(n // 2, medians, f))
    # split the list in 2 sub-lists picking splitElm as a pivot 
    a1 = [e for e in a if f(e) < f(splitElm)]
    a2 = [e for e in a if f(e) >= f(splitElm)]
    # use again the recursivity on one of the sub-lists to solve the problem
    if k <= len(a1):
        return k_smallest(k, a1, f)
    else:
        return a1 + k_smallest(k - len(a1), a2, f)
 
print("3 -->", k_smallest(3, [(0, 0), (1, 7), (2, 2), (3, 2), (1, 4), (3, 0)], norm))
print("7 -->", k_smallest(7, [(0, 0), (1, 7), (2, 2), (3, 2), (1, 4), (3, 0)], norm))


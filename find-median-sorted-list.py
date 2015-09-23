'''
Question: Given sorted list find median
'''

def median(a):
    length = len(a)
    if (length % 2 != 0):  #odd since mod is > 0
        return a[(length+1)//2 - 1] #find floor
    else: #even
        t1 = a[(length//2) - 1]
        t2 = a[length//2]
        t3 = (t1 + t2)/2  #could be a decimal
        return t3

a = [1, 12, 15, 26]
b = [2, 13, 17, 30, 45]
                                
print("Input >>> ", a, ", median=", median(a))
print("Input >>> ", b, ", median=", median(b))


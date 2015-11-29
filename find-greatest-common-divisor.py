'''
Find the greatest common divisior of two positive integers

Logic:
Keep subtracting the difference of two numbers and the smallest 
of the two numbers until numbers are same.

Example:
300, 210 = 30    
300 - 210 = 90
90 - 210  = 120
90 - 120  = 30
30 - 90   = 60
60 - 30   = 30
30 - 30   = 0
'''

def GCD(x,y):
    if (x == y):
        return x
    if x < y:
        small = x
    else:
        small = y
    #print(abs(x-y),small)
    return(GCD(abs(x-y),small))

input = [[3,9], [24,30], [300,210], [1,5]]
for x in input:    
    print("GCD for %d & %d = %d" % (x[0],x[1],GCD (x[0],x[1])))



#Multiply two numbers without using * and / with minimal operations

'''
NOTES:
35 * 7 
7 * 35
3*35 + 3*35 + 35 
2*35 +35  +2*35 +35 + 35
1*35+ 35         1*35+35
'''

#Time complexity: O(log s), s is the smallest
def mysort(a,b):
	if a < b:
		return(a,b)
	else:
		return(b,a)

def NewMultiply(a,b):
	sum = 0
	a,b = mysort(a,b)
	if a == 1:
		#print("%dx%d=%d" % (a,b,b))
		return b
	else:
		reminder = 0
		if a%2 == 1:    #check is a is odd or even
			reminder = b		
		a = a >> 1  #right shift, divide by 2
		sum = NewMultiply(a,b)
		return sum + sum + reminder

a = 16
b = 7
print("%dx%d=%d" % (a,b,NewMultiply(a,b)))

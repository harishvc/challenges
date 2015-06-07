#Question: Find factorial of n

#Time Complexity: O(n^2)

#Iterative
def IFactorial(n):
	result = 1
	for x in range (1,n+1):
		result *= x
	return result

#Recursive
def RFactorial(n):
	return 1 if (n < 1) else n * RFactorial(n-1)
	
print("### Find factorial ###")
while True:
	try:
		x = int(input("Enter number: ")) 
		break
	except:
		print ("Invalid number, please try again")

#Solution 1: Iterative
print ("%d!=%s" % (x,"{:,}".format(IFactorial(x))))

#Solution 2: Recursive
print ("%d!=%s" % (x,"{:,}".format(RFactorial(x))))

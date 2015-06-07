#Question: Write a program to calculate x^n
#Answer:
#1. Observation:
#   1.1 exponent is a positive integer           
#2. Algorithm:
#   2.1: Dividing & conquering using the least significant bit in the exponent and using a iterative function will improve efficiency
#3. Complexity
#   3.1: O(n/2) where n is the exponent
#4. Test cases:
#    4.1 2^15
#5. Proof:
#    5.1: 2^15=32,768    
#6. Code:
def IPower(x,n):
    result = 1
    for i in range(n):
        result *= x
    return result

while True:
    try:
        x = int(raw_input("Enter base: "))
        n = int(raw_input("Enter exponent: ")) 
        break
    except:
        print "Invalid input, please try again"

t = IPower(x,n/2) #Divide and conquer
result = t * t if (n % 2 == 0) else x*t*t #least significant bit in the exponent 
print ("%d^%d=%s" % (x,n,"{:,}".format(result)))

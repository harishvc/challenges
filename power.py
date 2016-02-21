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

#Solution 1
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

#Solution 2
#Shifting bits
#http://stackoverflow.com/questions/2198138/calculating-powers-e-g-211-quickly?lq=1
def intpow(base, exp):
        if exp == 0:
                return 1
        elif exp == 1:
                return base
        elif (exp & 1) != 0:
                print("%d*intpow(%d*%d,%d//2)" %(base,base,base,exp))
                return base * intpow(base * base, exp // 2)
        else:
                print("intpow(%d*%d,%d//2)" %(base,base,exp))
                return intpow(base * base, exp // 2)

base = float(2)
exp = 13
negative=False
if(exp < 0):
        negative = True
        exp = abs(exp)
result = intpow(base,exp)
if(negative):
        print(1/result)
else:
        print(result)

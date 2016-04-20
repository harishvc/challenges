#Introduction to bitwise operations

a = 25
b = 12

#http://www.tutorialspoint.com/python/bitwise_operators_example.htm
#Convert decimal to binary
print("%d in binary = %s" % (a,bin(a)[2:]))
#Convert binary to decimal
print("11001 in decimal = %d" % (int('11001',2)))
#AND
print("a=%d,b=%d,a&b=%d" % (a,b,a&b))
#OR
print("a=%d,b=%d,a|b=%d" % (a,b,a|b))
#EOR
print("a=%d,b=%d,a^b=%d" % (a,b,a^b))
#COMPLEMENT
print("a=%d,~a=%d" % (a,~a))
# x << y  Left Shift
# Shift x by y bits to the left. Same as x*2**y
#Examples: 4<<2=16  5<<2=20
print("a=%d,a2<<2=%d" % (a,a<<2))
# x >> y Right Shift
# Shift x by y bits to the right. Samw as x//2**y
#Examples: 5>>2=1 3>>2=0 7>>2=1
print("a=%d,a>>2=%d" % (a,a>>2))

#set bit N of variable x to 0
#https://stackoverflow.com/questions/10571822/how-to-remove-the-leftmost-bit-and-add-bit-in-its-rightmost-bit/
x &= ~(1 << N)

#set bit N of variable x to 1
#https://stackoverflow.com/questions/10571822/how-to-remove-the-leftmost-bit-and-add-bit-in-its-rightmost-bit/
x |= 1 << N

#http://www.quora.com/How-would-you-add-two-integers-using-bit-manipulation
#http://en.wikipedia.org/wiki/Kogge%E2%80%93Stone_adder
def add(a, b):
    p, g, i = a ^ b, a & b, 1
    while True:
        if (g << 1) >> i == 0:
            return a ^ b ^ (g << 1)
        if ((p | g) << 2) >> i == ~0:
            return a ^ b ^ ((p | g) << 1)
        p, g, i = p & (p << i), (p & (g << i)) | g, i << 1
        
print ("1+2 =", add(1,2))
print ("1-2 =", add(1,-2))
print ("-4+2 =", add(-4,2))
print ("100+200 =", add(100,200))        


#http://www.geeksforgeeks.org/subtract-two-numbers-without-using-arithmetic-operators/
def subtract(x,y):
    while (y != 0):
        borrow = ~x & y
        x = x ^ y
        y = borrow << 1
    return x

print ("5-3=",subtract(5,3))
print ("29-13=",subtract(29,13))

#2s complement
#https://delightlylinux.wordpress.com/2014/10/13/binary-lesson-12-ones-complement-and-twos-complement/

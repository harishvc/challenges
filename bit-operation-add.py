#Question: Add two integers using bit manipulation


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

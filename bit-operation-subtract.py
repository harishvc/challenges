#Question: Subtract integers using bit operation

#http://www.geeksforgeeks.org/subtract-two-numbers-without-using-arithmetic-operators/
def subtract(x,y):
    while (y != 0):
        borrow = ~x & y
        x = x ^ y
        y = borrow << 1
    return x

print("5-3=%d" % (subtract(5,3)))
print("29-13=%d" % (subtract(29,13))) #higher,lower


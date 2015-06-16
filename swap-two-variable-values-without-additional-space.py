'''
Question: Swap two variable values without using additional space

Solution: Use XOR

Reference:
http://betterexplained.com/articles/swap-two-variables-using-xor/
'''

x = 5
y = 9
print("x=%d,y=%d changed to " % (x,y),end="")
x = x ^ y
y = x ^ y
x = x ^ y
print("x=%d,y=%d" % (x,y))


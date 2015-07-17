#Question: Find sum of all even numbers for a given range

def numformat(value):
    return "{:,}".format(value)

from functools import reduce
start = 0
end   = 101
interval = 2
result = numformat(reduce(lambda x,y:x+y,range(start,end,interval)))       
print("Sum of even numbers from %d to %d = %s" % (start+1,end-1,result))

'''
Write a function that given an integer returns a formatted number string. 

Questions:
1. Integers?
2. Negative integers?

Test cases:
1234 = "1,234"
123456789  =  "123,456,789"
'''

#Python library
#Solution 1:
import locale
locale.setlocale(locale.LC_ALL, 'en_US')
print(1234567, " =" , locale.format("%d", 123456789 , grouping=True))

#Python library
#Solution 2:
tmp = "{:,}".format(123456789)
print(123456, " =",tmp)

#Programmatic iterative solution
#Solution 3: Inefficient use of strings
def solution3(inputlist):
    #inputlist = str(input)
    count = 0
    output = ""
    for x in range(len(inputlist)-1,-1,-1):
        tmp = inputlist[x]
        if (count >= 3):
            output = tmp + "," + output 
            count = 0
        else:
            output = tmp  + output  
        count += 1
    return output

#Solution 4  :thumpsup:
#Programmatic recursive solution
#Source: http://code.activestate.com/recipes/498181-add-thousands-separator-commas-to-formatted-number/
def splitthousands(s, sep=','):  
    if len(s) <= 3: 
        return s  
    return (splitthousands(s[:-3], sep) + sep + s[-3:])

input = [123 ,1234 , 123456789, 1234567]
for x in input:
    #print(x,"=",solution3(x))
    print(x,"=",splitthousands(str(x)))


#Benchmarking
#Reference: http://www.peterbe.com/plog/thousands-commafy-large-numbers
from time import time
for f in (solution3,splitthousands):
    t0 = time()
    for i in range(1000000):
        f(str(i))
    t1 = time()
    print(f.__name__, t1 - t0, 'seconds')

# Write a function that given an integer returns a formatted number string. 
# Test cases:
# 1234 = "1,234"
# 123456789  =  "123,456,789"

#Solution 1: Inefficient use of strings
def format(input):
    inputlist = str(input)
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

input = [123 ,1234 , 123456789, 1234567]
for x in input:
    print(x,"=",format(x))
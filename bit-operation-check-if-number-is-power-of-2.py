#Question: Given a number n, check whether the number is a power of 2

#Observation: if (n & n-1 == 0) then the number is a power of 2

#Solution
input = [8,16,24,25,30,100]
for n in input:
    if (n & n-1 == 0):
        print(n,True)
    else:
        print(n,False)



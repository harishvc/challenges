#Question: Given a number n, multiple the number by power of 2 k

#Observation: n << k  

#Solution:
#2*2^2=8
#3*2^3=24
#4*2^4=64
#5*2^5=160

#Code
input = [2,3,4,5]
k = 2
for n in input:
    print("%d*2^%d=%d" % (n,k,n<<k))
    k += 1

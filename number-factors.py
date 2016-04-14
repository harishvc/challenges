'''
Question: Write all possible numbers which multiply to a give number
Example: 12 = 12*1, 2*6, 2*2*3,3*4 . Don’t include 4*2 (duplicate)
'''

#lookup to check for duplicates and insert only new ones
def lookup(result,new):
    for a in result:
        if new  == a:
            #duplicate
            return
    result.append(new)

def findFactors(num,result,prefix):
    for i in range(1,int(num/2)+1):
        #remainder == 0
        if(num%i == 0):
            tmp = prefix + [i,num//i]
            #sort to avoid duplicates
            tmp.sort()
            #lookup to check for duplicates and insert only new ones
            lookup(result,tmp)
            #further break down
            if (i != 1):
                findFactors(i,result,prefix +[num//i])
                findFactors(num//i,result,prefix + [i])

num = 12
result = []
prefix = []
findFactors(num,result,prefix)
print(num, " = ", result)


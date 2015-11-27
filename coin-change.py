'''
Find total #ways to reach a total using given denominations
'''


def MyLength(self):
    return len(self)


denominations = [1,2,3,4,5]
def Combinations(total,result,prefix):
    global denominations
    for i in range(len(denominations)):
        if (denominations[i] <= total):
            #multiples
            if ( total % denominations[i] == 0):
                newcombination = [prefix + [denominations[i] for x in range(int(total/denominations[i]))]]
                if newcombination not in result:
                    result += newcombination
            else:
                #find combinations
                new_total = total - denominations[i]
                tmp = prefix +[denominations[i]]
                result = Combinations(new_total,result,tmp)
    #del prefix[:]
    return result

total = 5
result = []
Combinations(total,result,[])
print("Total=%d denominations=%s" % (total,denominations))
print("# combinations",len(result))
print("All possible combinations >>>",result)
result.sort(key=MyLength)
print("Most optimal solution:",result[0])



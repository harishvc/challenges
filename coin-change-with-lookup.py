'''
Question: Given denominations and a total, find total #ways to reach a total using given denominations. 

Solution:
Inspired by the Python solution from @leif posted at http://stackoverflow.com/questions/1106929/find-all-combinations-of-coins-when-given-some-dollar-value
New solution created with lookup
'''


def MyLength(self):
    return len(self)

def LocalLookup(mapping,key,value):
    value.sort() #IMPORTANT! , resolves [2,3][3,2]
    if(key in mapping.keys()):
        if value not in mapping[key]:
            mapping[key].append(value)
    else:
        #new
        mapping[key] = [value]  #[] don't unpack
        
def Combinations(total,prefix,result,mapping):
    for i in range(len(denominations)):
        if (denominations[i] <= total):
            #multiple
            if total % denominations[i]  == 0:
                tmp1 = [denominations[i] for x in range(0,int(total/denominations[i]))]
                #Add to lookup
                LocalLookup(mapping,total,tmp1)
                tmp2 = prefix + tmp1
                tmp2.sort() #IMPORTANT! , resolves [2,3][3,2]
                if tmp2 not in result:
                    result.append(tmp2)
            #combinations
            else:
                new_total = total - denominations[i]    
                new_prefix = prefix + [denominations[i]] #send prefix as list
                #Add to lookup
                if (len(new_prefix) > 1):
                    LocalLookup(mapping,sum(new_prefix),new_prefix)
                #Check lookup before recursion
                if (new_total in mapping.keys()):
                    tmp3 = mapping[new_total]
                    for i in range(len(tmp3)):
                        tmp4 = new_prefix + tmp3[i]
                        result.append(tmp4)
                else:
                    result = Combinations(new_total,new_prefix,result,mapping)
        else:
            return result
    return result

denominations = [1,2,3,4,5]
total = 5
result = []
mapping = {}
Combinations(total,[],result,mapping)
print("Total=%d denominations=%s" % (total,denominations))
print("# combinations",len(result))
print("All possible combinations >>>",result)
result.sort(key=MyLength)
print("Most optimal solution:",result[0])

#Print map
#for key in mapping:
#    print(key, ">>>", mapping[key])

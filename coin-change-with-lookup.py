'''
Find total #ways to reach a total using given denominations with lookup

TODO:
1. Handle [2,3], [3,2]
2. Calculate [1,1]

'''

denominations = [1,2,3,4]

def MyLength(self):
    return len(self)


def Lookup(map,key,values):
    if(key in map.keys()):
        t1 = map[key]
        if values not in t1:    
            t1.append(values)
            map[key] = t1
        #else:
            #print("ignoring .....", values)
    else:
        map[key] = [values]


def Combinations(total,prefix,result,map):
    global denominations
    for i in range(len(denominations)):
        if (denominations[i] <= total):
            #multiples
            if ( total % denominations[i] == 0):
                t1 = [denominations[i] for x in range(int(total/denominations[i]))]
                Lookup(map,total,t1)
                if(len(prefix) > 0):
                    t2 = [prefix[-1]] + t1
                    Lookup(map,sum(t2),t2)
                newcombination = prefix + t1
                Lookup(map,sum(newcombination), newcombination)
                if newcombination not in result:
                    result += [newcombination]
            else:
                #find combinations
                new_total = total - denominations[i]
                new_prefix = prefix +[denominations[i]]
                if(len(new_prefix) > 0):
                    Lookup(map,sum(new_prefix), new_prefix)
                if new_total in map.keys():
                    for i in range(len(map[new_total])):
                        result.append(new_prefix + map[new_total][i])
                else:    
                    #missing 2 >> [1,1]
                    result = Combinations(new_total,new_prefix,result,map)
    return result

total = 5
result = []
map = {}
Combinations(total,[],result,map)
print("Total=%d denominations=%s" % (total,denominations))
print("# combinations",len(result))
print("All possible combinations >>>",result)
result.sort(key=MyLength)
print("Most optimal solution:",result[0])

#Print map
#for key in map:
#    print(key, ">>>", map[key])

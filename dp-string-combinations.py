#Find all string combinations

'''
NOTES:
1. In combinations order does not matter. Example: lottery ticket 
2. Combinations can have strings of different length including empty one!
3. Combination can be considered as a COMPLETE GRAPH TRAVERSAL problem without visiting any node twice

input = abc (n=3)
- formula = n!/(n-r)! * r! 
- part a: when length = 1 (r=1 and n = 3). #combinations = 3
- part b: when length = 2 (r=2 and n = 3). #combinations = 3
- part c: when length = 3 (r=3 and n = 3). #combinations = 1
- part d: empty set []
- total combinations = 3 + 3 + 1 + 1 = 8

'''




def pre_processing(linput):
    #step 1: find unique characters and count
    #c_dict = { 'A' : 2,
    #            'B' : 1,
    #            'C' : 1 }
    c_dict = {} 
    for key in linput:
        if key in c_dict:
            c_dict[key] += 1
        else:
            c_dict[key] = 1

    #step2: Sort unique characters and create two list - unique characters and count
    #characters = ['A','B','C']
    #character_count = [2,1,1]
    characters = []
    character_count = []
    for key in sorted(c_dict):
        characters.append(key)
        character_count.append(c_dict[key])

    return characters,character_count 


def find_combinations(characters,character_count,level,path,unique_combinations):
    #new combinations!
    #print(path[0:level])
    t = path[0:level]  
    t.sort()
    t2 = "".join(t)
    #add to set - retain only unique values
    unique_combinations.add(t2)

    for i in range(0,len(characters)):
        #check count
        if character_count[i] == 0:
            continue
        else:
            path[level] = characters[i]
            character_count[i] = character_count[i] - 1
            level = level + 1
            find_combinations(characters, character_count, level, path,unique_combinations)
            level = level - 1
            character_count[i] = character_count[i] + 1


linput = ['B','A','C']
characters, character_count = pre_processing(linput)
result = [0 for i in range(len(linput))]
unique_combinations = set()
print ("Combinations of %s" % ("".join(linput)))
find_combinations(characters,character_count,0,result,unique_combinations)
print(unique_combinations)
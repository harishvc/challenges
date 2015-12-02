'''
Flatten a JSON like object representation

example: {a:1, b:2, c:{d:3,e:4}} flattens to {a:1,b:2,c.d:3,c.e:4}
'''

def flattenHash(input,prefix,result):
    #print("Start ...", input,prefix,result)
    kvpairs = []
    prefix_entry = prefix #Important!!!
    #Store key value pair in list
    #Since there is no guarantee of the order in which keys are stored in hash
    for key in input:
        kvpairs.append([key,input[key]])
    #Iterate through the list and process each value
    for i in range(len(kvpairs)):
        #Check type before processing
        if(type(kvpairs[i][1]) != type(dict()) or  len(str(kvpairs[i][1])) == 1):
            #Best case scenario, nothing to parse
            result.append(prefix_entry + kvpairs[i][0] + ":" + str(kvpairs[i][1]))
        else:
            prefix += kvpairs[i][0] + "."
            result = flattenHash(kvpairs[i][1],prefix,result)
    return result


input= [ {"a":1, "b":2, "c":{"d":3,"e":4}}, 
         {"a":1, "b":2, "c":{"d":3}}, 
         {"a":1, "b":2, "c":{"d":3,"e":{"f":{"g":[1,2,3]}}}}, 
         {"a":1, "b":2, "c":{"d":[1,2,3]}}] 


for i in range(len(input)):
    result = []
    flattenHash(input[i],"",result)
    print(input[i], ">>>>", result)

'''
Check if two given strings are Isomorphic.

Two strings str1 and str2 are called Isomorphic if 
  1. There is a one to one mapping possible for every character of str1 to every character of str2
  2. All occurrences of every character in ‘str1′ map to same character in ‘str2′

Example:
  1. "egg", "add"     = true
  2. "foo", "bar"     = false
  3. "paper", "title" = true
  
http://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/
http://www.programcreek.com/2014/05/leetcode-isomorphic-strings-java/
'''

def CheckIsomorphic(input1,input2):
    l1 = len(input1)
    l2 = len(input2)
    
    #Check length of strings
    if (l1 != l2):
        return False 
    
    map = {}  #character mapping - string1 => string2
    visited = [] #set of visited characters in string2
    
    for i in range(l1):
        #New character in string1
        if (input1[i] not in map.keys()):
            #New character in string2
            if (input2[i] not in visited):
                map[input1[i]] = input2[i]
                visited.append(input2[i])
            else:
                return False
        #Check mapping oF character in string1     
        elif (map[input1[i]] != input2[i]):
            return False
    return True    

input = [["aab","xxy"],["aab","xyz"]]
for x in input:
    print("%s & %s Isomorphic? %s" % (x[0],x[1],CheckIsomorphic(x[0],x[1])))

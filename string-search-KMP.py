#Search for a pattern in text

#Solution 1:
#Brut force: Time Complexity: O(n * m) 
# n = # characters in text , m = #characters in pattern
def findPattern(text,pattern):
    for t in range(0,len(text)):
        t2 = t
        for p in range(0,len(pattern)):
            if text[t2] == pattern[p]:
                t2 +=1
                if  p == len(pattern) -1:
                    print("match at index ...", t)
                    break
            else:
                break


#Solution 2: KMP
'''
Implement KMP (Knuth Morris Pratt) algorithm to search a pattern in a long string

Time Complexity: O(m+n) 

References:
http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
http://code.activestate.com/recipes/117214-knuth-morris-pratt-string-matching/
https://www.quora.com/What-is-the-best-resource-to-learn-KMP-Algorithm
http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
'''

'''
Partial Match Table (length of the longest proper prefix that matches a proper suffix)
The length of the longest proper prefix in the (sub)pattern that matches a proper suffix in the same (sub)pattern
pattern = snape , longest proper prefix = s,sn,sna, snap
pattern = snape , longest proper suffix = nape,ape,pe,e

1. Idea behind the Partial Match Table is to identify an index position > 0  in the pattern such that
  if current character in the text and current character in the pattern don't match, so we don't have to start over!

2. Partial Match Table ONLY adds value of the pattern contains duplicate characters. If characters are UNIQUE, then
the values will be 0 - start from beginning if there is no match
'''


#O(m) - m is the length of the pattern
def MaxShift(pattern):
    size = len(pattern)
    maxShift = [0]*size
    j = 0
    i = 1
    while i < size:
        if (pattern[i] == pattern[j]):
            #IMPORTANT: Increment
            maxShift[i] = j + 1
            j += 1
            i += 1
        elif(j != 0):
            #IMPORTANT: move back j
            j = maxShift[j-1]
        else:
            assert j == 0, "logic error"
            #j == 0
            i += 1    
    #print(maxShift)        
    return maxShift

#0(n) - n is the length of the text document
def KMP(text,pattern):
    maxShift = MaxShift(pattern)
    p = 0 #index for pattern
    t = 0 #index for text
    while t < len(text):
        #CHARACTER MATCH
        if(pattern[p] == text[t]):
            p +=1
            t +=1
            #ENTIRE PATTERN MATCH!!!
            if(p >= len(pattern)):
                yield t-p
                #IMPORTANT: 
                # 1. p is NOT reset to 0
                # 2. This logic handles recurring occurances
                # 3. Example: text = GGCACACATG, pattern = CAC apprears twice 
                p = maxShift[p-1] #shift pattern index
        elif p != 0:
            #IMPORTANT: Get shift position based on last character 
            # so we don't start from index positon == 0 if there is a proper prefix in the pattern 
            p = maxShift[p-1]
        else:
            #first index in pattern does not match, read next character from text document
            t +=1


text = "GGCACACATG"
pattern = "CACA"

print("input >>>", text)
print("pattern >>>", pattern)
result = KMP(text,pattern)
for x in result:
    print("pattern found at start position >>>", x)


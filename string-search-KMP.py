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
'''
def MaxShift(pattern):
    size = len(pattern)
    maxShift = [0]*size
    maxLength = 0
    currentIndex = 1
    while (currentIndex < size):
        #print(currentIndex,maxLength)
        if (pattern[currentIndex] == pattern[maxLength]):
            maxLength += 1
            maxShift[currentIndex] = maxLength
            currentIndex += 1
        elif(maxLength != 0):
            #IMPORTANT: New maxLength
            maxLength = maxShift[maxLength-1]
        else:
            maxShift[currentIndex] = 0
            assert maxLength ==0, "Error"
            currentIndex +=1
    return maxShift


def KMP(text,pattern):
    maxShift = MaxShift(pattern)
    p = 0 #index for pattern
    t = 0 #index for text
    for c in text:
        #print("comparing,,,,", pattern[p],c)
        if(pattern[p] == c):
            p +=1
            t +=1
            if(p == len(pattern)):
                yield t-p
                p = maxShift[p-1] #shift pattern index
        elif p != 0:
            #maxShift[0] .... maxShift[p-1] with match!
            p = maxShift[p-1]
            t += 1
        elif p == 0:
            t += 1

text = "hello 123 world 123"
pattern = "123"
#text = "ABABDABACDABABCABAB"
#pattern = "ABABCABAB"
print("input >>>", text)
print("pattern >>>", pattern)
result = KMP(text,pattern)
for x in result:
    print("pattern found at start position >>>", x)

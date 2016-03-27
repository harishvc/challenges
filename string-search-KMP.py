'''
Implement KMP (Knuth Morris Pratt) algorithm to search a pattern in a long string

Time Complexity: O(m+n) 

Reference:
http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
http://code.activestate.com/recipes/117214-knuth-morris-pratt-string-matching/
https://www.quora.com/What-is-the-best-resource-to-learn-KMP-Algorithm
'''


'''
Partial Match Table (length of the longest proper prefix that matches a proper suffix)
The length of the longest proper prefix in the (sub)pattern that matches a proper suffix in the same (sub)pattern
pattern = snape , longest proper prefix = s,sn,sna, snap
pattern = snape , longest proper suffix = nape,ape,pe,e
'''
def buildJumpBackList(pattern,size):
    jumpBack = [1] * ( size + 1) #pre-allocated list
    shift = 1
    for p in range(size):
        while shift <= p and pattern[p] != pattern[p-shift]:
            shift += jumpBack[p-shift]
        jumpBack[p+1] = shift
    return jumpBack

def KMP(text,pattern):
    size = len(pattern)
    jumpBack = buildJumpBackList(pattern,size)
    MatchStartPos = 0  #index postion of pattern match
    matchLen = 0
    for c in text:
        while matchLen == size or  (matchLen >= 0 and pattern[matchLen] != c):
            MatchStartPos += jumpBack[matchLen] #incremented match start position
            matchLen -= jumpBack[matchLen]      #decrement match length
        matchLen += 1
        if matchLen == size:
            yield MatchStartPos #multiple pattern matches

text = "hello 123 world 123"
pattern = "123"
print("input >>>", text)
print("pattern >>>", pattern)
result = KMP(text,pattern)
for x in result:
    print("pattern found at start position >>>", x)

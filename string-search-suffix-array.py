'''
Implement Suffix Array to search a pattern in a text

Notes :notes:
1. Using Suffix Array to search a pattern is ideal for search 
   a text (input) again and again with different patterns
2. Since the suffix are created for the text (input). 
   There is one-time overhead!
'''

#http://stackoverflow.com/questions/27600004/find-one-occurence-of-substring-using-suffix-array
#Binary Search to find one occurance
def bisect_left(a, x, text, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if text[a[mid]:] < x: 
        	lo = mid+1
        else: 
        	hi = mid
    if not text[a[lo]:].startswith(x): 
        # i suppose text[a[lo]:a[lo]+len(x)] == x could be a faster check
        raise IndexError('not found')
    return a[lo]


text = "banana"
suffix = [text[i:] for i in range(len(text))]
#print(suffix)
Sortedsuffix = sorted([text[i:] for i in range(len(text))])
#print(Sortedsuffix)
SuffixArray = [ suffix.index(Sortedsuffix[i]) for i in range(len(text))]
#print(SuffixArray)

pattern = "nan"
print("text >>>", text)
print("pattern >>>", pattern)
print("pattern found at index >>>", bisect_left(SuffixArray,pattern,text))

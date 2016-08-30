#Implement Suffix Array to search a pattern in a text

'''
Notes :notes:
1. PREPROCESS: Suffix Array to search a pattern is ideal for search 
   a text (input) again and again with different patterns
2. Run a binary search on the suffix array
'''


'''
Since we have a sorted array of all suffixes, Binary Search can be used to search for the
first occurance

Reference:
http://stackoverflow.com/questions/27600004/find-one-occurence-of-substring-using-suffix-array
'''

def bisect_left(a, x, text, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    #Binary search
    while lo < hi:
        mid = (lo+hi)//2
        #Python string comparion
        if text[a[mid]:]  == x:
            return a[mid]
        #first character of text < first character of x
        elif text[a[mid]:] < x: 
        	lo = mid+1
        else: 
        	hi = mid
    if not text[a[lo]:].startswith(x): 
        # i suppose text[a[lo]:a[lo]+len(x)] == x could be a faster check
        raise IndexError('not found')
    #lo has index of first match
    return a[lo]

#Generate a suffix array
#Time complexity: O(n^2logn), since two strings of length n are compared
#Step 1: Get all suffix
text = "banana"
suffix = [text[i:] for i in range(len(text))]
#print(suffix)

#Step 2: Sort all suffix in a-z order
#Time complexity: O(n^2logn), since two strings of length n are compared
#Ukkonen's suffix tree can create a suffix array and is much more sophisticated
Sortedsuffix = sorted([text[i:] for i in range(len(text))])
#print(Sortedsuffix)

#Step 3: Suffix array with sorted suffix mapped to index in suffix
#Reference: http://www.geeksforgeeks.org/suffix-array-set-1-introduction/
SuffixArray = [ suffix.index(ss) for ss in Sortedsuffix]
#print(SuffixArray)

pattern = "nan"
print("text >>>", text)
print("pattern >>>", pattern)
print("pattern found at index >>>", bisect_left(SuffixArray,pattern,text))

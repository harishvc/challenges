#Find the longest palindromic substring 

'''
NOTES:
References: 
1. http://difusal.blogspot.com/2014/08/manachers-algorithm-longest-palindromic.html
2. http://articles.leetcode.com/longest-palindromic-substring-part-ii/

Manacher’s Algorithm
Take advantage of the palindrome’s symmetric property and avoid some of the unnecessary computations.
1. Create a new string (T) by adding # on the left and right side of each character in the string  
    - new string (T) length is odd
2. Consider each character in T to be center of a palindrome. How long is the palindrome? store in new list P
3. Using the maximum value of list P the longest palindromic substring can be constructed!
'''

#Pre-processing
def pad(a,mypad):
	result = mypad
	for x in a:
		result += x + mypad
	return result

'''
Whenever a palindrome centered at i expands past the right bound of the palindrome 
centered at C (in other words, if it expands past R), C is assigned the value of i 
and R is updated according to the content of P[i] and i itself.
'''
#Time & Space complexity: O(n)
def ManacherAlgorithm(a,mypad):
	#step 1: pre-processing
	T=pad(a,mypad)
	#step 2: create list to store max length of palindrome at each index position
	p = [0]*len(T)
	C,R = 0,0
	maxCenterIndex = 1
	for i in range(1,len(T)-1):
		ii = 2 * C - i
        #optimization!!!
		p[i] = min(R - i, p[ii]) if (R > i)  else 0
		#expand the palindrome
		while (i+1+p[i] < len(T) and i-1-p[i] >=0 and T[i + 1 + p[i]] == T[i - 1 - p[i]]):
			p[i] += 1
		#adjust center if i + p[i] > R	
		if (i + p[i] > R):
			C = i
			R = i + p[i]
    	#Keep track of the index with max value
		if p[i] > p[maxCenterIndex]:
			maxCenterIndex = i

	return T[maxCenterIndex-p[maxCenterIndex]:maxCenterIndex+p[maxCenterIndex]].replace(mypad,"")


a ="abaccddccefe"
#a ="cfceg"
mypad="#"
print(a, " >>>> ", ManacherAlgorithm(a,mypad))

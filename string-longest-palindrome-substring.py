#Find the longest palindromic substring 

'''
Manacher’s Algorithm:
1. Take advantage of the palindrome’s symmetric property and avoid some of the unnecessary computations
    - Create a new string (T) by adding # on the left and right side of each character in the string  
    - new string (T) length is odd
2. Consider each character in T to be center of a palindrome and expand. Find new center (C), end of palindrome (R) & maxLength at each index
3. If current index (i) < R, see if we can take advantage of already claculated value
4. Iterate maxLength and find the length of palindrome and reconstruct the characters

References: 
1. https://www.youtube.com/watch?v=nbTSfrEfo6M&spfreload=5
'''

#Pre-processing
def pad(a,mypad):
	result = mypad
	for x in a:
		result += x + mypad
	#start $ end @ for code simplicity (Line 55)	
	return "$"+result+"@"


'''
Whenever a palindrome centered at i expands past the right bound of the palindrome 
centered at C (in other words, if it expands past R), C is assigned the value of i 
and R is updated according to the content of P[i] and i itself.
'''



#Time & Space complexity: O(n)
def ManacherAlgorithm(a,mypad):	
	#
	#Preprocessing
	T=pad(a,mypad)
	maxLength = [0]*len(T)
	#center index of longest palindrome calculated so far
	C = 0
	#right index of palindrome calculated so far	
	R = 0
	
	#
	#Find the length of the longest palindrome that each index
	for i in range(1,len(T)-1):
		#Step 1: Take advantage of the work do so far
		# i < R, we can already seen T[i]
		if i < R:
			#IMPORTANT: length of mirror 
			mirror = 2*C - i
			#IMPORTANT: min length of palindrome at index i
			maxLength[i] = min(maxLength[mirror],R-i)
		#Step 2: Expand with i as the center of both sides
		#T has start $ end @  - while loop will break, no need to check both ends	 
		while T[i + (maxLength[i]+ 1)] == T[i - (maxLength[i]+1)]:
			maxLength[i] +=1
		#Step 3: Find new C and R
		if (maxLength[i] + i > R):
			C = i
			R = maxLength[i] +i

	#Find the longest length (from the center)
	#Construct the left and right of the palindrome 
	center = 0
	length = 0
	for i in range(len(maxLength)):
		if maxLength[i] > length:
			length = maxLength[i]
			center = i
	start = T[center-length:center]
	end = T[center:center+length]
	t = start+end
	#replace mypad		
	return t.replace(mypad,"")


a ="abaccddccefeG"
mypad="#"
print("input >>>", a)
print("Longest Palindrome >>> ", ManacherAlgorithm(a,mypad))

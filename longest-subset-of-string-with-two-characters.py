#Longest substring with at the most 2 unique characters

'''
NOTES
1. Since we are looking for 2 unique characters, there are 4 MAIN conditions to handle
2. startIndex = starting index of new substring
3. changeIndex = index position where the next character is different than the current character
4. When you see the third uniqiue character change values of startIndex and changeIndex
   - startIndex = changeIndex + 1
   - changeIndex = currentIndex - 1
'''

def LS2(a):
	print("input >>>", a)
	startIndex = 0  #start of new substring
	changeIndex = 0 #index position where the next character is different than the current character
	longestSubstring = None
	longestSubstringlength = 0
	seenCount  = 0 #count of characters seen
	seen = set() #characters seen so far
	for currentIndex in range(0,len(a)):
		#condition 1: first unique character
		if currentIndex == 0:
			seen.add(a[currentIndex])
			seenCount = 1
			startIndex = 0
		#condition 2: second unique character
		elif a[currentIndex] != a[currentIndex-1] and seenCount == 1:
			seen.add(a[currentIndex])
			seenCount = 2
			changeIndex = currentIndex-1
		#condition 3: first followed by second or second followed by first
		elif a[currentIndex] != a[currentIndex-1] and a[currentIndex] in seen and a[currentIndex-1] in seen:
			changeIndex = currentIndex-1
		#condition 4: third unique character
		elif a[currentIndex] != a[currentIndex-1]:
			assert a[currentIndex] not in seen and seenCount == 2, print("Error")
			if currentIndex - startIndex > longestSubstringlength:
				longestSubstringlength = currentIndex - startIndex
				longestSubstring = a[startIndex:currentIndex]
			seen.remove(a[changeIndex])
			seen.add(a[currentIndex])
			#optimization! - not starting over again
			startIndex = changeIndex + 1
			changeIndex = currentIndex - 1
	#condition 5: input has only two characters repeating!
	if (seenCount == 2 and longestSubstringlength == 0):
		return(a)
	#condition 6: input has only 1 character repeating!					
	elif(seenCount == 1):
		return
	else:
		return(longestSubstring)

a = "aabaaabbccccd"
print(a, " >>> ", LS2(a))

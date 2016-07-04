#Given a string and limit provide line breaks based on even distribution of empty spaces
#AKA Best arrangement to provide even distribution of empty spaces
#Text justification

'''
NOTES:
Even distribution factor (Badness factor or Cost factor): Square of empty spaces in every line. 
Example: 3 empty space on one line gets penalized as 9 (3^2)

1. Greedy Solution
   - Insert each word until size <= maxlength
   - Does not gaurantee even distribution of empty space
2. Optimal DP Solution
   - You have words1, words2, word3 to print.
   - Print word2 with word1 if word1 word2 distribution factor < word2 word3  
   - Check for each word!

REFERENCE:
1. http://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/
2. https://www.youtube.com/watch?v=RORuwHiblPc

'''

#Solution 1: Greedy
'''
1. Insert word to output if the new length <= maxlength. Continue until end of input
2. This solution is simple. If there is a penalty for empty space in each output line
   for this given input there will be a penalty on each line (except #2) 
'''
def solution1(a,maxlength):
	count = 0
	output = []
	for word in a.split(" "):
		wsize = len(word)
		if wsize <= maxlength-count:
			if count == 0 :
				output.append(word)
			else:
				output.append(" " + word)
				count +=1
			count += wsize
		else:
			myprint(output,count,maxlength)
			count = 0
			#Empty list but keep initialization intact!!
			del output [::]
			output.append(word)
			count = wsize
	#Important
	#Print any remaining input
	if count > 0:
		myprint(output,count,maxlength)

def myprint(output,count,maxlength):
	t = "".join(output)
	print("%s\t\tsize=%d space=%d" % (t,count,maxlength-count))

##################

import sys
def printResult(words,result):
	seen = None
	for i in range(len(words)):
		end = result[i]
		if seen is None or seen != end:
			print(" ".join(words[i:end]))
			seen = end


#Time & Space Complexity: 0(n^2)
def solution2(a,maxlength):
	#step 1: split the string into words (space delimited)
	words = a.split(" ")

	#Step 2: Fill Cost Table determined by #empty space in each line
	table = [[sys.maxsize]*len(words) for i in range(len(words))]
	for i in range(len(words)):
		size = len(words[i])
		table[i][i] = (maxlength-len(words[i]))**2 #each word <= maxlength
		for j in range(i+1,len(words)):
			#Important: Add spacing
			size += len(words[j]) + 1
			if size <=maxlength:
				table[i][j] = (maxlength-size)**2
			else:
				#kill inner loop
				break
	#print(table)

	#step 3: Find minimum cost & result
	mincost = [0]*len(words)
	result = [0]*len(words)
	#start from the end of the cost table!
	#IMPORTANT: wcount - 1
	wcount = len(words)-1
	#step 4: Find optimal #words to print on the same line
	for i in range(wcount,-1,-1):
		#default values
		mincost[i] = table[i][wcount] #default cost
		result[i] = wcount +1 #add 1  #default end index
		#Can we do better with space?
		#step 5: move the cols to the left 
		for j in range(wcount,i,-1):
			#IMPORTANT:
			#Check if the default cost can be reduced 
			#by comparing with the cost computed earlier with the NEXT word
			#and word BEFORE
			# i value does NOT change, j values reduces till < i  	
			if mincost[i] > mincost[j] + table[i][j-1]:
				mincost[i] = mincost[j] + table[i][j-1] #new cost
				result[i] = j #new end index
	print("Minimum Cost=%d" % (mincost[0]))
	print("\nString with even spacing >>>")
	printResult(words,result)


a =  "Harish V.C likes to code"
maxlength = 10
solution2(a,maxlength)

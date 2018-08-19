#Find all permutations of a string in sorted (lexicographic) order - should handle duplicate values.

'''
NOTES:
1. Combinations where order matters is a Permutation. Example: lock combination  
2. Permutation result has same length are original string (no empty string and strings of different length)
3. Permutation can be considered as a COMPLETE GRAPH TRAVERSAL problem without visiting any node twice

Problem #1: How many permutations are there in  `ABCD`  
  - 4 unique characters. 4!
Problem #2: How many permutations are there in   `ABAD`  
  - 4 characters, `A` repeats 2 times 
  - 4!/2! = 4x3 = 12
Problem #3: How many permutations are there in   `ABADBB`  
  - 6 characters, `A` repeats 2 times, `B` repeats 3 times 
  - 6!/(2! * 3!) = 60
'''


'''
Reference: Tushar Roy - Coding Made Simple
String Permutation Algorithm 
1. https://www.youtube.com/watch?reload=9&v=nYFd7VHKyWQ
2. https://github.com/mission-peace/interview/blob/master/python/recursion/stringpermutation.py
'''

def pre_processing(linput):
	#step 1: find unique characters and count
	#c_dict = { 'A' : 2,
	#			'B' : 1,
	#			'C' : 1 }
	c_dict = {} 
	for key in linput:
		if key in c_dict:
			c_dict[key] += 1
		else:
			c_dict[key] = 1

	#step2: Sort unique characters and create two list - unique characters and count
	#characters = ['A','B','C']
	#character_count = [2,1,1]
	characters = []
	character_count = []
	#sorting 
	for key in sorted(c_dict):
		characters.append(key)
		character_count.append(c_dict[key])

	return characters,character_count 

def find_permutations(characters,character_count,level,path):
	#reached end!
	if level == len(path):
		print("".join(path))
		return
	for i in range(0,len(characters)):
		#check count
		if character_count[i] == 0:
			continue
		else:
			#insert new character in current level
			path[level] = characters[i]
			#reduce # occurance of current character
			character_count[i] = character_count[i] - 1
			#increase level
			level = level + 1
			find_permutations(characters, character_count, level, path)
			#decrease level
			level = level - 1
			#increase #occurance
			character_count[i] = character_count[i] + 1


linput = ['B','A','C','A']
print("Sorted permutations of %s >>> " % ("".join(linput)))
characters, character_count = pre_processing(linput)
result = [0 for i in range(len(linput))]
find_permutations(characters,character_count,0,result)

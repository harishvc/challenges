'''
Question: Find the longest subset of a given string with two unique characters.
'''

'''
Notes: :notes:
1. Store unique characters
2. Change = keep track of the index position where characters change
3. Start  = start of the new substring

input = aabaaabbccccd
substrings with 2 unique characters are
1. aabaaabb
2. bbcccc
'''

def LongestSubstring(input):
    seen = []
    start = 0
    change = 0
    max_length = 0
    max_substring = ""
    last_seen = input[0]
    for i in range(len(input)):
        #Seen 
        if (input[i] in seen):
            if(i> 0 and input[i] != input[i-1]):
                change = i
        #New character (1st or 2nd)
        elif(input[i] not in seen and len(seen) < 2):
            seen.append(input[i])
            if(i> 0 and input[i] != input[i-1]):
                change = i #index position of last change
        else:
            tmp = input[start:i]  #substring
            tmp2 = len(tmp) 
            #max length of substring
            if(tmp2 > max_length):
                max_length = tmp2
                max_substring = tmp
            #Update seen characters
            del seen[:]
            seen.append(change)
            seen.append(input[i])
            #update start pointer
            start = change
            #update change pointer
            change = i
    return(max_substring,max_length)


input = "aabaaabbccccd"
print("input >>>", input)
a,b = LongestSubstring(input)
print ("Longest 2 characters subset>>", a)        
#Question: Reverse all words in a sentance
#Complexity: O(n) where n is the lenght of the sentance

#Answer

#Source: http://stackoverflow.com/questions/18686860/reverse-a-string-in-python-without-using-reversed-or-1
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

sentances = ['Alice likes Bob']


#Solution 1: Using list comprehension    
for n in sentances:
    print (n,"===>",end=" ")
    print (''.join([x for r in reverse(n).split(" ") for x in reverse(r) + " " ]))
    
#Solution 2: Function call (more space efficient than solution 1)   
for n in sentances: 
    print (n, "===>",end=" ")
    for x in reverse(n).split(" "):
        print(reverse(x),end=" ") 
print(" ")


#Solution 3: Convert string to list and then reverse
def reverse(a,start,end):
	while start < end:
		a[start],a[end] = a[end],a[start]
		start += 1
		end -= 1
	return a

#Reference: https://www.interviewcake.com/question/python/reverse-words
#Time & Space complexity: O(n)
def reverseSentance(a):
	#step 1: convert string to list since string is immutable :notes:
	na = list(a)  #new a
	size = len(na) -1
	#step 2: reverse entire list
	na = reverse(na,0,size)
	#step 3: reverse each word (when space is encountered)
	start = 0
	for i in range(0,size+1):
		if na[i] == " ":
			reverse(na,start,i-1)
			start = i + 1
		elif i == size:  #last word
			reverse(na,start,i)
	return "".join(na) #convert list back to string

a= "Alice likes Bob"
print(a, "===>", reverseSentance(a))

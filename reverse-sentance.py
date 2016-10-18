#Question: Reverse all words in a sentance

#Helper function that reverses all the characters between a start and end index (inclusive)
def reverse(a,start,end):
	while start < end:
		a[start], a[end] = a[end], a[start]
		start += 1
		end -= 1

#Time complexity: O(n)
#Space Complexity: O(1)
def reverseSentance(a):
	#step 1: reverse the entire string
	reverse(a,0,len(a)-1)

	#step 2: reverse each word in the string
	start_index = 0
	end_index = 0
	for i in range(0,len(a)):
		if a[i] == " ":  #nd of word!
			end_index = i-1 #leave the space
			reverse(a,start_index,end_index)
			start_index = i+1 #next character!
	#IMPORTANT: Handle last word!
	reverse(a,start_index,len(a)-1)


a= ['A','l','i','c','e'," ",'l','i','k','e','s'," ",'B','o','b']
print(a)
reverseSentance(a)
print(a)

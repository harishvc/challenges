#Given a number find the next largest Palindrome

'''
References:
1. https://www.quora.com/What-is-the-best-algorithm-for-finding-the-next-smallest-palindrome-of-a-given-number
2. http://stackoverflow.com/questions/36439810/how-to-find-the-middle-value-of-an-integer-without-converting-it-to-a-string-usi
'''

def nextPalindrome(num):
	a = str(num) #convert to string!!!
	size = len(a)
	#condition 1: single digit
	if (num < 9):
		return num + 1
	#condition 2: two digits 10 - 99
	elif(num  < 99):
		return num + 11-(num%11)
	#conditions 3-6
	elif (size%2 == 0):
		#even
		mid = size//2 -1
		#condition 3: even, reversed digits > current digits at end
		if a[0:mid+1][::-1] > a[mid+1:]:
			return a[0:mid+1]+a[0:mid+1][::-1]
		#condition 4: even, reversed digits < current digits at end
		else:
			front = str(int(a[0:mid+1]) + 1)
			back = front[0:mid+1][::-1]
			return(front+back)
	else:
		#odd
		mid = size//2
		#condition 5: odd, reversed digits > current digits at end
		if a[0:mid][::-1] > a[mid+1:]:
			return a[0:mid]+a[mid]+a[0:mid][::-1]
		#condition 6: odd, reversed digits < current digits at end	
		else:
			front = str(int(a[0:mid+1]) + 1)
			back = front[0:mid][::-1]
			return(front+back)


myinput = [6,23,1204,1291,12345,12309,12921,808]
for a in myinput:
	print(a , " >>> ", nextPalindrome(a))


#Question: Test if a string is a Palindrome. Ignore all non-alphanumeric characters.  
#Source: Section 7.3, Elements of Programming Interviews

#Answer:

#Solution 1
#Limitations: 
# 1. Does not handle non-alphanumeric characters
# 2. Not efficient since entire string is reversed for comparison
#n = "racecaR"
#if n.lower() == n.lower()[::-1]:
#    print (n, " is ", "palindrome")
#else:
#    print (n, " is ", "not palindrome")
    
#Solution 2
#Time Complexity: O(n) where n is the number of characters in the string
def CheckPalindrome(n):
    i = 0
    j = len(n) - 1
    while (i < j):
        #Skip non-alpha characters
        while ( (n[i].isalpha() == False) and i<j):   
            i = i + 1
        #Skip non-alpha characters
        while ( (n[j].isalpha() == False) and i<j):
            j = j - 1            
        if (n[i].lower() != n[j].lower()):
            return "not palindrome"
        i = i + 1
        j = j - 1
    return "palindrome" 

words = ['A man, a plan, a canal, Panama', 'Able was I,ere I saw Elba!','Ray a Ray']
for n in words:
    print (n, " is ", CheckPalindrome(n))

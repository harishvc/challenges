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

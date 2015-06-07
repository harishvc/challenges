#Question:
#Complexity: O(4^n n). There are no more than 4 recursive call (letter z has 4), n is input length

#Answer
#Source: http://pythonfiddle.com/phone-number-mnemonic/
numberMap = [ '', 
              '', 
              ['A','B','C'],
              ['D','E','F'],
              ['G','H','I'],
              ['J','K','L'],
              ['M','N','O'],
              ['P','Q','R', 'S'],
              ['T','U','V'],
              ['W','X','Y','Z']]


def generateSequences(numberSequence, string):  
  num = int(numberSequence[0])  
  chars = numberMap[num] 
  for char in chars:
        
    if len(numberSequence) == 1:
      print (string + char)
    
    else: 
      generateSequences(numberSequence[1:], string+char)
  
  
#seq = '227'
seq = '7729'
generateSequences(seq, '')

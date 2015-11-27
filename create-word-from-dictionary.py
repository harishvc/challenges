'''
Can you create the given word from the given dictionary.
Dictionary holds one or two length characters and the sequence of the characters match the input string.

Example:
 
input = [abcde]
 
dictionary = ['e','a','bc','de']
result = True
 
dictionary = ['a','ab','bc', 'de']
result = True
 
dictionary = ['e','ab','de']
result = True
'''

def ValidPatternWrapper():
    def ValidPattern(input):
        nonlocal dictionary
        #print(dictionary)
        if(len(input) == 0):
            return True
        count = 0
        if(input[0] in dictionary):
            count = 1
        elif (input[0:2] in dictionary):
            count = 2
        if(count > 0):
            return(ValidPattern(input[count:]))
        else:
            return False

    input = 'abcde'
    dictionarylist = [['e','a','bc','de'],
                  ['a','ab','bc', 'de'],
                  ['e','ab','de']
                  ]
    print("input >>> ", input)
    for i,dictionary in enumerate(dictionarylist):
        print("dictionary=%s valid pattern? %s" %(dictionary,ValidPattern(input)))

ValidPatternWrapper()

        
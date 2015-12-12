'''
Given a word and a dictionary. Find all possible words can you make that are found in the dictionary?

input = appletablet
dictionary = [app,let,apple,t,applet]
'''

input = "appletablet"
dictionary = ["app","let","apple","t","applet"]
result = []
for r in range(1,len(input)):
    a = [input[i:i+r] for i in range(0, len(input), r)]
    #print(a)
    for w in range(len(a)):
        if(a[w] in dictionary and a[w] not in result):
            #print(a[w])
            result.append(a[w])
print("input >>>", input)
print("dictionary >>>", dictionary)
print("valid permutations >>>", result)

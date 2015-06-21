#Question:Given a dictionary and two words find path from one word to another such that all intermediate words are also in the dictionary. At each time only one character can change.
#Source: http://www.ardendertat.com/2011/10/17/programming-interview-questions-8-transform-word/

import collections
import string

def constructGraph(dictionary):
    graph=collections.defaultdict(list)
    letters=string.ascii_letters #a-zA-Z
    #print(letters)
    for word in dictionary:
        for i in range(len(word)):
            remove=word[:i]+word[i+1:] #new word = characters from left and right
            if remove in dictionary:   #new word exists in directory 
                graph[word].append(remove) #store new word and transformation
            #change 1 character
            for char in letters:
                change=word[:i]+char+word[i+1:] #new word = character from left + A-Z + character from right
                if change in dictionary and change!=word:
                    graph[word].append(change)
        #add 1 character to the word
        for i in range(len(word)+1):
            for char in letters:
                add=word[:i]+char+word[i:]
                if add in dictionary:
                    graph[word].append(add)
    #print graph
    #for k in graph:
    #   print("%s=%s" % (k,graph[k]))                
    return graph

def transformWord(graph, start, goal): 
    paths=collections.deque([ [start] ]) 
    #print("path =%s length=%d" % (paths,len(paths)))
    extended=set() 
    #Breadth First Search
    #count = 0 
    while len(paths)!=0:
        #count += 1 
        currentPath=paths.popleft() 
        currentWord=currentPath[-1]
        #print("currentpath=%s , currentword=%s" % (currentPath,currentWord)) 
        if currentWord==goal: 
            #print("found match in %s iterations" % (count))
            return currentPath 
        elif currentWord in extended: 
            #already extended this word 
            continue   
        
        extended.add(currentWord) 
        transforms=graph[currentWord] 
        for word in transforms: 
            if word not in currentPath: 
                #avoid loops 
                #print("adding to path >>>", currentPath[:]+[word])
                paths.append(currentPath[:]+[word])
                #print("new paths >>>", paths)
                #print("~~~~~~~~~")
        #print(paths)
           
    #no transformation 
    return [] 




dictionary=['cat','bat','bet','bed','at','ad','ed']
graph = constructGraph(dictionary)
print(transformWord(graph, 'cat','bed'))

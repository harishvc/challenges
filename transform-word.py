#Question:Given a dictionary and two words find path from one word to another such that all intermediate words are also in the dictionary. At each time only one character can change.


#Source: http://www.ardendertat.com/2011/10/17/programming-interview-questions-8-transform-word/

import collections
import string

def constructGraph(dictionary):
    graph=collections.defaultdict(list)
    letters=string.ascii_letters
    for word in dictionary:
        for i in range(len(word)):
            #remove 1 character 
            remove=word[:i]+word[i+1:] 
            if remove in dictionary: 
                graph[word].append(remove)
            #change 1 character
            for char in letters:
                change=word[:i]+char+word[i+1:]
                if change in dictionary and change!=word:
                    graph[word].append(change)
        #add 1 character
        for i in range(len(word)+1):
            for char in letters:
                add=word[:i]+char+word[i:]
                if add in dictionary:
                    graph[word].append(add)
    return graph

def transformWord(graph, start, goal): 
    paths=collections.deque([ [start] ]) 
    extended=set() 
    #Breadth First Search 
    while len(paths)!=0: 
        currentPath=paths.popleft() 
        currentWord=currentPath[-1] 
        if currentWord==goal: 
            return currentPath 
        elif currentWord in extended: 
            #already extended this word 
            continue   
        
        extended.add(currentWord) 
        transforms=graph[currentWord] 
        for word in transforms: 
            if word not in currentPath: 
                #avoid loops 
                paths.append(currentPath[:]+[word])
        #print(paths)
           
    #no transformation 
    return [] 

dictionary=['cat','bat','bet','bed','at','ad','ed']
graph = constructGraph(dictionary)
print(transformWord(graph, 'cat','bed'))

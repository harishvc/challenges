'''
Question:Given a source word, target word and dictionary, transform the source word to target
by changing/adding/removing 1 character at a time, while all intermediate words being valid 
words in the dictionary. Return the transformation chain which has the smallest number of intermediate words.

#Modified from http://www.ardendertat.com/2011/10/17/programming-interview-questions-8-transform-word/

'''

import collections
import string
import queue

#Time Complexity: O(nm^2). n = length of start word, m=length of word in dictionary - Pre-processing 
def Transformations(dictionary):
    graph=collections.defaultdict(list)  #dictionary of list
    letters=string.ascii_letters #a-zA-Z
    #print(letters)
    for word in dictionary:
        for i in range(len(word)):
            #Remove 1 characater
            remove=word[:i]+word[i+1:] #new word = characters from left and right
            if remove in dictionary:   #new word exists in directory 
                graph[word].append(remove) #store new word and transformation
            #Change 1 character
            for char in letters:
                change=word[:i]+char+word[i+1:] #new word = character from left + A-Z + character from right
                if change in dictionary and change!=word:
                    graph[word].append(change)
            #Add 1 character to the word
            for char in letters:
                add=word[:i]+char+word[i:]
                if add in dictionary and change != word:
                    graph[word].append(add)
    #print graph
    #for k in graph:
    #   print("%s=%s" % (k,graph[k]))                
    return graph

#Breadth first traversal
def Traverse(graph, start, end):
    result = {} #store result paths and length
    paths=queue.Queue()
    paths.put([start])
    seen=set()  #Keep track of seen words
    while not paths.empty():
        currentPath=paths.get()
        currentWord=currentPath[-1]
        if currentWord==end: 
            print ("Found new path >>> ", currentPath,len(currentPath))
            result[len(currentPath)] = currentPath #store 
        elif currentWord in seen: #already processed this word
            continue           
        seen.add(currentWord) 
        transforms=graph[currentWord] 
        for word in transforms: 
            if word not in currentPath: 
                paths.put(currentPath[:]+ [word])  #create a new list and add it to paths           
    return result



dictionary=['cat','bat','bet','bed','bobcat', 'at','ad','ed']
graph = Transformations(dictionary)
start = 'cat'
end = 'ed'
print("Find all possible paths to transform '%s'  to '%s' " % (start,end))
allpaths = Traverse(graph,start,end)
print ("Shortest path")
print(min(allpaths.items(), key=lambda x: x[0]))
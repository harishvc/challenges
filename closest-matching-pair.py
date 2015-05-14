#Source: Section 13.8 ,Elements of Programming Interviews: The Insiders' Guide, ISBN 1479274836

#Question: Let S be an array of strings. Write a function which finds a closest pair of equal entries.
#S = ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "result"]
#2nd and 3rd occurrence of 'no' is the closet pair

S = ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "result"]

        
def MatchingClosetPair(S):        
    Seen = {}        #store words seen before; key=word,value=#occurances:last_position ; Seen = { 'and': '2:12', 'All': '1:1', 'for': '1:7', 'no': '4:13' ...}
    occurance = 1    #default #occurrence
    Result = []      #store closet pair information
    for Cindex in range(len(S)):        #loop over the array
        if Seen.has_key(S[Cindex]):     #Have we already seen the word? 
            Loccurance, Lindex = Seen[S[Cindex]].split(":")
            spacing = Cindex - int(Lindex)
            occurance = int(Loccurance) + 1
            #print "found .....  %s >>> occurrence #:%d  at position: %d last position:%s spacing:%d" % (S[Cindex],occurrence,Cindex + 1,Lindex,spacing)
            if not Result:  #Handle empty array - first time
                Result = [spacing, S[Cindex], int(Loccurance), occurance]
            elif (spacing < Result[0]):  #insert only if spacing is less than prior recorded value
                Result = [spacing, S[Cindex], int(Loccurance), occurance]
        Seen[S[Cindex]] = str(occurance)+":"+str(Cindex+1)   #Add word to Seen with occurrence and last position
    return Result


result = MatchingClosetPair(S)
if not result:
    print "no closet matching pair"
else:
    print S
    print "Occurrence ", result[2], "and ", result[3] , " of ", result[1], " is the closest pair"
    
#Notes & Observations
#1.Time Complexity: O(n) , constant amount of work for each word in the array, n is number of words
#2.Space Complexity: O(d) , d is unique words in a give array    
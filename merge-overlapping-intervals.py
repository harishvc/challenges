'''
Given a list of intervals merge overlapping intervals
Example: [1,3][4,6][2,9]   ===> [1,9]
'''
    
def MergeInterval(input):
    
    #Step 1: Sort the time interval by start time and end time
    #input = sorted(input,key=lambda x:(x[0],x[1]))
    input.sort(key=lambda x:(x[0],x[1]))
    #print("sorted input .....", input)
    
    #Step2: Iterate through the sorted list
    #Initialize with first entry
    result = [[input[0][0],input[0][1]]]
    end = input[0][1] 
    for x in range(1,len(input)):
        #New start is less than or equal to end
        if (input[x][0] <= end):
            #New end is larger than end 
            if (input[x][1] > result[-1][1]):
                result[-1][1] = input[x][1] #Merge!
                end = input[x][1]  #new end
        #New start is greater than last seen end
        else:
            result.append([input[x][0],input[x][1]]) #new time interval
            end = input[x][1]  #new end
    return result


input = [[1,3],[4,6],[10,15],[1,2],[2,9]]
print(input, "merged interval ->>>", MergeInterval(input))
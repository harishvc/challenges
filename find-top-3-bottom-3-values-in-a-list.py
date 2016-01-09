'''
Question: Find top 3 and bottom 2 values from the list in O(n)
'''


input = [20,5,6,100,3]

t1,t2,t3,it1,it2,it3,b1,b2,ib1,ib2 = None,None,None,None,None,None,None,None,None,None
for i,x in enumerate(input):
    ############
    #BOTTOM 1,2
    if(b2 is None):
        b2 = x
        ib2 = i
    #smallest
    elif(x < b2 and b1 is None):
        #shuffle
        ib1 = i
        b1 = x
    #new smallest    
    elif(x < b1):
        ib2 = ib1
        b2 = b1
        ib1 = i
        b1 = x
    #next smallest    
    elif(x > b1 and x < b2):
        b2 = x
        ib2 = i
    #########
    #TOP 1,2,3
    #Scenario 1: t3 is None
    if(t3 is None):
        t3 = x
        it3 = i
    #Scenario 2: x > t3 
    #shuffle back   
    elif(x > t3):
        it1 = it2
        t1 = t2
        it2 = it3
        t2 = t3
        it3 = i
        t3 = x
    #Scenario 3: x < t3
    #check t2 and t1
    elif (x < t3):
        #t2?
        if (t2 is None):
            t2 = x
            it2 = i
        #shuffle back    
        elif(x > t2):
            it1 = it2
            t1 = t2
            it2 = i
            t2 = x
        elif(x < t2 and t1 is None):
            t3 = x
            it3 = i
        elif(x > t1):
            it1 = i
            t1 = x
 
print(input)
print("Top 3 values >>> ", t1,t2,t3 , "and their index positions =", it1,it2,it3)
print("Bottom 2 values >>> ", b1,b2, "and their index positions =", ib1,ib2)
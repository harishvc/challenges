'''
Design a rate limiting web service that allows 100 requests/second from an IP address
'''

import time

#return time now in milliseconds
def timeNow():
    millis = int(round(time.time() * 1000))
    return millis
 
'''
Solution 1: 
1. Use hash to store : 
   a. KEY = IP 
   b. VALUES:
    - timestamp of first request at the start of the window
    - timestamp of last request received
    - #requests
2. WHen a new request comes in
    a. Scenario 1: New IP
    b. Scenario 2: Existing IP, within time period and within limit
    c. Scenario 3: Existing IP, within time period and more than limit
    d. Scenario 4: Existing IP, more than time period
''' 
def ProcessRequest(IP,table,period,limit):
    if IP in table.keys():
        #existing
        window = timeNow() - table[IP][0]
        #print("checking ,,,,,", IP, table[IP][0],table[IP][1],table[IP][2])
        if( window > period):
            #Scenario 4: reset
            table[IP][0] = timeNow()
            table[IP][1] = timeNow()
            table[IP][2] = 1
            return True
        elif (window < period and table[IP][2] < limit):
            #Scenario 2 
            table[IP][2] += 1
            table[IP][1] = timeNow()
            return True
        else:
            #Scenario 3 
            return False
    else:
        #new request
        #Scenario 1
        table[IP] = [timeNow(),timeNow(),1]
        return True

table = {}
period = 1000 #in milliseconds
limit  = 10 
IP = "12345"
for x in range(1,15):
    print(x, " Status ?", ProcessRequest(IP,table,period,limit))

#for key in table:
#    print(key," >>> ", table[key])


'''
Solution 2: 

1. Use a double ended queue (Deque) for each KEY , capacity = limit
2. Store all request  in the queue
3. If queue is filled then check the timstamp of the last entry
    a. if timestamp less than period, return false
    b. if timestamp greater than period, pop from queue, add to queue
4. Greatest benefit from this design is keeping track of 
   historic information about requests and only removing them from queue as needed
'''
          
'''
Given a string for a text message and character limit. Break the message 
without breaking the words and include message count.

Example: 
Input => "Hi there! You are awesome. Have a great day"
Limit => 20
Output =>
Hi there! You are  (1/3)
awesome. Have a  (2/3)
great day.  (3/3)
'''

def GenerateMessage(input,limit):
    count = 0
    output = ""
    words = input.split()
    message = []
    for i in range(len(words)):
        #print("processing .....>>>>", words[i])
        word_length = len(words[i]) + 1  #add space
        if ((word_length + count) < limit):
            output += words[i] + " "
            count += word_length
        else:
            message.append(output)
            output = words[i] + " "
            count = word_length 
    #Last word!
    if(len(output)>0):
        message.append(output)
     
    return message   

def SendText(message):
    size = len(message)
    for i in range(size):
        print("%s (%d/%d)" % (message[i],i+1,size))

        
input = "Hi there! You are awesome. Have a great day."
limit = 20
SendText(GenerateMessage(input,limit))      
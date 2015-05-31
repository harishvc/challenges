#Given n appointments, find all conflicting appointments
#Input: appointments = [[1,5],[3,7],[2,6],[10,15],[5,6],[4,100]]
#Output
#[3,7] conflicts with [1,5]
#[2,6] conflicts with [1,5]
#[4,100] conflicts with [1,5]
#[2,6] conflicts with [3,7]
#[5,6] conflicts with [3,7]
#[4,100] conflicts with [3,7]
#[5,6] conflicts with [2,6]
#[4,100] conflicts with [2,6]
#[4,100] conflicts with [10,15]
#[4,100] conflicts with [5,6]

#Observations:
# 1. appointments have start and end
# 2. end is greater than start
# 3. conflict happens when there is another appointment  
# 4. start time conflict: when start time is between an existing appointment
# 5. end time conflict: when end time is between an existing appointment
# 6. No conflict with start time then there is no conflict with end time
#Algorithm:
# 1. Iterate through the array and check if there is conflict with current and next appointment
# 2. Next appointment is either before current appointment or after current appointment for no conflict
#Complexity:
# Time complexity: O(n^2)
# Space complexity: O(1)

#Code
appointments = [ [[1,5],[3,7],[2,6],[10,15],[5,6],[4,100]] , [[3,7],[2,6],[10,15],[5,6],[4,100]] ]
for input in appointments:
    print("finding conflicts for ", input)
    for index,appointment in enumerate(input):
        start,end = appointment  #current appointment
        for next_appointment_index in range (index+1,len(input)):
            cond1 = False
            cond2 = False
            start_next_appointment,end_next_appointment = input[next_appointment_index]
            #Check if next appointment is before current appointment  
            if (start >= end_next_appointment):   
                cond1 = True 
            #Check if the next appointment is after current appointment
            if  (end <= start_next_appointment):   
                cond2 = True
            if (cond1 == False and cond2==False):      
                print("[%d,%d] conflicts with [%d,%d]" % (start_next_appointment,end_next_appointment,start,end))
       
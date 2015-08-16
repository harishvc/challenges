'''

Question: Count inversions in an array

Reference: 
1. http://www.geeksforgeeks.org/counting-inversions/


'''

#Code modified from http://stackoverflow.com/questions/23484711/merge-sort-algorithm-counting-inversions

#global
count = 0
inversions = []

def sort_list(unsortedlist):

    m = len(unsortedlist)

    A_list = unsortedlist[:int(m/2)]
    B_list = unsortedlist[int(m/2):]

    if len(A_list) > 1: # if the list is longer thn 2 items, break it up
        A_list = sort_list(A_list)

    if len(B_list) > 1: # breaking and sorting second part
        B_list = sort_list(B_list)

    return merge_sort(A_list,B_list) # merge the smaller lists to return either a-list/b_list or full_list        


def merge_sort(a_list,b_list):

    initiallist = a_list + b_list
    final_list = []
    i = 0
    j = 0
    global count
    global inversions
    while len(final_list) < (len(initiallist)):

        if len(a_list) != 0 and len(b_list) != 0:
            if  a_list[i] < b_list[j]:
                final_list.append(a_list.pop(i))
            #inversion
            elif a_list[i] > b_list[j]:
                for z in a_list:
                    tmp = [z,b_list[j]]
                    inversions.append(tmp)
                final_list.append(b_list.pop(j))
                count += len(a_list)
            elif a_list[i] == b_list[j]:
                final_list.append(a_list[i])
                final_list.append(b_list[j])


        elif len(b_list) == 0 :
            final_list+=a_list


        elif len(a_list) == 0 :
            final_list+=b_list

    #print("sorted output >>>", final_list)
    return (final_list)



input = [2, 4, 1, 3, 5]
print("input >>> ", input)
sort_list(input)
print("#inversions: %d , inversion list: %s" % (count,inversions))

'''
Question: Compute all possible string combinations that can be made my placing spaces (zero or one) between them.
Example: ABC -> A BC,AB C,ABC, A B C
'''
#source: http://stackoverflow.com/questions/16478793/how-do-i-generate-all-possible-combinations-of-a-string-with-spaces-between-the
from itertools import combinations
def gen_spaces(data):
    return_value = []
    size = len(data)-1
    #data_as_list = list(data)
    for num_spaces in range(size):
        for comb in combinations(range(size), num_spaces+1):
            data_as_list = list(data)
            for i in comb:
                data_as_list[i] +=' '
            return_value.append(''.join(data_as_list))
    return return_value,len(return_value)
 
input= "abc"
result,count = gen_spaces(input)
print("%s input has %d combinations" % (input,count))
print(result)
    

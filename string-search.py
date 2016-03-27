'''
Given a long string seperated by space, find how many occurances of another small string
'''

input  = "fsfsf test te st aadadadaddd test"
search = "test"

#
import re
print("#occurance=%d" % (len(re.findall(search,input))))
print("#start & end positions = %s" % ([[m.start(),m.end()] for m in re.finditer(search,input)]))

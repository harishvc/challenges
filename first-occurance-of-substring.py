#First occurrence of a substring

import re

input="Hello World!"

#Solution 1: find()
print("ll found at index",input.find("ll"))

#Solution 2: Regular expressions
for m in re.finditer(r"ll", input):
    print ('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

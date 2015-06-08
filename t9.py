#Question: Implement T9


#Source: http://stackoverflow.com/questions/12074963/t9-system-to-numpad

from collections import Counter
import re
import itertools 

all_words=Counter()
n2l={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
with open('/usr/share/dict/words','r') as di:  # UNIX 250k unique word list 
     all_words.update({line.strip() for line in di if len(line) < 6}) 

# with open('holmes.txt','r') as fin:   # http://www.gutenberg.org/ebooks/1661.txt.utf-8
#     for line in fin:
#          all_words.update([word.lower() for word in re.findall(r'\b\w+\b',line)])

def combos(*nums):
    t=[n2l[i] for i in nums]
    return tuple(''.join(t) for t in itertools.product(*(t)))

def t9(*nums):
    combo=combos(*nums)
    c1=combos(nums[0])
    first_cut=(word for word in all_words if word.startswith(c1))
    return (word for word in first_cut if word.startswith(combo))

def try_it(*nums):
    s=set(t9(*nums))
    n=10
    print('({}) produces {:,} words. Top {}:'.format(','.join(str(i) for i in nums),
            len(s),min(n,len(s))))
    for i, word in enumerate(
          [w for w in sorted(all_words,key=all_words.get, reverse=True) if w in s],1):
        if i<=n:
            print ('\t{:2}:  "{}" -- weighted {}'.format(i, word, all_words[word]))

    print()        

# try_it(2)
# try_it(2,3)
# try_it(2,3,4)
# try_it(2,3,3,4)
try_it(6,6,8,3)   
#try_it(2,3,3,4,5) 

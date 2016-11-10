'''
Question:
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.

Source:
1. https://leetcode.com/problems/all-oone-data-structure/
2. https://discuss.leetcode.com/topic/63683/0ms-all-in-o-1-with-detailed-explantation
'''


'''
NOTES:

1. Maintain two dictionaries
    - keys_to_occurrencess   #keep track of key and #occurance 
    - occurances_to_keys   #dictionary of set

2. For input "AABC"
   keys_to_occurrencess         occurances_to_keys
   A -> 2                     1 -> {'B', 'C'}
   B -> 1                     2 -> {'A'}
   C -> 1

3. increment
    - update #occurances in keys_to_occurrencess
    - update occurances_to_keys 
           - remove key from current set (where key=#occurance , del key if set is empty)
           - add key to new set (where key=#occurance+1 , create key if not present)

4. decrement
    - decrement #occurances in keys_to_occurrencess , delete key is #occurance == 0
    - update occurances_to_keys 
           - remove key from current set (where key=#occurance , del key if set is empty)
           - if #occurance-1 > 0:
               - add key to new set (where key=#occurance-1 , create key if not present)
'''

class AllOne(object):

    def __init__(self):
        self.keys_to_occurrences = {}   #dic of int
        self.occurrences_to_keys = {}   #dic of set


    def addOccurrences(self,key,occurrences_count):
        if occurrences_count in self.occurrences_to_keys.keys():
            self.occurrences_to_keys[occurrences_count].remove(key)
            #empty set? remove key
            if len(self.occurrences_to_keys[occurrences_count]) == 0:
                del self.occurrences_to_keys[occurrences_count]
        if occurrences_count+1 in self.occurrences_to_keys.keys():
            self.occurrences_to_keys[occurrences_count+1].add(key)
        else:
            self.occurrences_to_keys[occurrences_count+1] = set()
            self.occurrences_to_keys[occurrences_count+1].add(key)

    def inc(self, key):
        if key not in self.keys_to_occurrences.keys():
            self.keys_to_occurrences[key] = 0
        self.addOccurrences(key,self.keys_to_occurrences[key])
        self.keys_to_occurrences[key] +=1
    
    def removeOccurrences(self,key,occurrences_count):
        self.occurrences_to_keys[occurrences_count].remove(key)
        #empty set? remove key
        if len(self.occurrences_to_keys[occurrences_count]) == 0:
            del self.occurrences_to_keys[occurrences_count]
        if occurrences_count-1 > 0 and occurrences_count-1 in self.occurrences_to_keys.keys():
            self.occurrences_to_keys[occurrences_count-1].add(key)
        elif occurrences_count-1 > 0:
            self.occurrences_to_keys[occurrences_count-1] = set()
            self.occurrences_to_keys[occurrences_count-1].add(key)

    def dec(self, key):
        self.removeOccurrences(key,self.keys_to_occurrences[key])
        #remove key if #occurances == 0
        if self.keys_to_occurrences[key] == 1:
            del self.keys_to_occurrences[key]
        else:
            self.keys_to_occurrences[key] -=1
         

    def getMaxKey(self):
        if len(self.occurrences_to_keys) > 0:
            max_value = max(self.occurrences_to_keys)
            return next(iter(self.occurrences_to_keys[max_value]))
        else:
            return None


    def getMinKey(self):
        if len(self.occurrences_to_keys) > 0:
            min_value = min(self.occurrences_to_keys)
            return next(iter(self.occurrences_to_keys[min_value]))
        else:
            return None


a = AllOne()
a.inc('A')
print("insert A  , max = %s min=%s" % (a.getMaxKey(),a.getMinKey()))
a.inc('A')
print("insert A  , max = %s min=%s" % (a.getMaxKey(),a.getMinKey()))
a.inc('B')
print("insert B  , max = %s min=%s" % (a.getMaxKey(),a.getMinKey()))
a.dec('B')
print("delete B  , max = %s min=%s" % (a.getMaxKey(),a.getMinKey()))
a.dec('A')
print("delete A  , max = %s min=%s" % (a.getMaxKey(),a.getMinKey()))
a.dec('A')
print("delete A  , max = %s min=%s" % (a.getMaxKey(),a.getMinKey()))

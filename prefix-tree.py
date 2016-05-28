#Implement Prefix tree (Trie)  with insert, search, startsWith and delete methods
#Input is lowercase letters a-z

#TODO: Implement delete method
'''
1. Trie is an efficient information retrieval data structure. 
2. Using trie, search complexities can be brought to optimal limit (seach string (key) length).
3. Every node of trie consists of multiple branches 
4. Each branch represents a possible character of keys 
5. Last node of every key as leaf node
'''


#http://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
from collections import defaultdict

class Trie:
    def __init__(self):
        self.root = defaultdict()

    #Space complexity: O(ALPHABET_SIZE * key_length * N)
    #ALPHABET_SIZE  = # unique characters in the input
    #key_length = length of each key
    #N = #of keys    
    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {}) #handle keys already existing!
        #end of current word
        current.setdefault("_end")

    #Time complexity: O(m)
    # m = #of characters in the search string
    def search(self, word):
        current = self.root
        for letter in word:
            #print("letter=%s current=%s" % (letter,current))
            #case 1: current is smaller than word
            if letter not in current:
                return False
            current = current[letter]
        #case 2: exact match
        if "_end" in current:
            return True
        #case 3: word is smaller than current
        return False

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True

    def print(self):
        for key in self.root:
            print("key=%s value=%s" % (key,self.root[key]))


test = Trie()
a = ["helloworld", "helloa", "hellob", "ilikeapple"]
for i in a:
    print("Inserting ...", i)
    test.insert(i)

test.print()

print("search(hello) ?" , test.search('hello'))
print("search(ilikeapple) ?", test.search('ilikeapple'))
print("searchwith(hello) ?", test.startsWith('hello'))

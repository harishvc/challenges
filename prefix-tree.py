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
#from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.root = {} #store Trie as dict of dict

    #Space complexity: O(ALPHABET_SIZE * key_length * N)
    #ALPHABET_SIZE  = # unique characters in the input
    #key_length = length of each key
    #N = #of keys    
    def insert(self, word):
        current = self.root
        for letter in word:
            #IMPORTANT: 
            #dict of dict
            #setdefault handles NO key, returns value
            #current = current.setdefault ... returns value!
            current = current.setdefault(letter, {}) 
        #end of current word
        current.setdefault("_end")

    #Time complexity: O(m)
    # m = #of characters in the search string
    def search(self,target):
        current = self.root
        for c in target:
            #Check if key is present
            if c in current.keys():
                current = current[c]
            else:
                #word not there!
                return False
        #check if the word ends!        
        if "_end" in current:
            return True
        return False

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True

    #Assumption: word exists in Tie    
    def delete(self,target):
        self.delete2(self.root,target,0)


    def delete2(self,current,target,index):
        #reached end of word since word ends with _end
        if len(target) == index+1:
            #print(">>> deleting ", target[index], current[target[index]])
            del current[target[index]]["_end"]
            #print(">> new trie ", target[index], current[target[index]])
        else:
            ctmp = current
            r = self.delete2(current[target[index]],target,index+1)            
            ctmp = r
            return ctmp

    def Tprint(self):
        for key in self.root:
            print("key=%s value=%s" % (key,self.root[key]))


test = TrieNode()
a = ["helloworld", "helloa", "hellob", "ilikeapple"]

for i in a:
    print("Inserting ...", i)
    test.insert(i)


print("search(hello) ?" , test.search('hello'))
print("search(ilikeapple) ?", test.search('ilikeapple'))
print("searchwith(hello) ?", test.startsWith('hello'))
print("deleting helloa")
test.delete('helloa')
print("search(hellob) ?", test.search('hellob'))



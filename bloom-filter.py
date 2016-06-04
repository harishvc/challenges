#Implement Bloom Filter

'''
REFERENCE:
http://www.maxburstein.com/blog/creating-a-simple-bloom-filter/

What is a Bloom Filter?
Bloom filters are super efficient data structures that allow us to tell if 
an object is most likely in a data set or not by checking a few bits. 
Bloom filters return some false positives but no false negatives

Examples:
1. Chrome uses Bloom filter to store malicious URL
2. Cassandra uses Bloom filters to save IO when performing a key lookup

How does it work?
1. A Bloom filter is essentially a huge bit array. 
2. Bloom filters work by hashing an object several times.
3. Each time an object is hashed the corresponding hash value in 
   the bit array is then marked as 1  - save space!
4. 2 variables: size of bit array and number of times to run the hash function


Benefits & Limitations:
1. To reduce false positive rate we'll need to determine the size of data set
2. According to WolframAlpha a bloom filter with 1.1 million bits and 
   7 hash functions has about a 0.5% chance of a false positive.
'''

from bitarray import bitarray
import mmh3

class BloomFilter:
	def __init__(self,size,hashcount):
		self.hashcount = hashcount
		self.size = size
		self.lookuplist = bitarray(size) #create bit array
		self.lookuplist.setall(0)  #initialize

	def add(self, string):
		for seed in range(self.hashcount):
			result = mmh3.hash(string, seed) % self.size
			#print(result)
			self.lookuplist[result] = 1

	def lookup(self, string):
		for seed in range(self.hashcount):
			result = mmh3.hash(string, seed) % self.size
			if self.lookuplist[result] == 0:
				return "No"
		return "Maybe"

	def print(self):
		print(self.lookuplist)		

bf = BloomFilter(50, 7)
lines = open("bloom-filter-words.txt").read().splitlines()
for line in lines:
    bf.add(line)

#bf.print()

print("test ?",  bf.lookup("test"))
print("world ?", bf.lookup("world"))

'''
$>cat bloom-filter-words.txt
hello
world
'''
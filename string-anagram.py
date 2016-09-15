#Given a sequence of words, print all anagrams together

#Reference
https://github.com/harishvc/challenges

#OBSERVATION
1. Sort each word
2. Create a prefix tree using characters in each word
3. End each word with the index position in the input
4. Traverse the prefix tree and find anagram words

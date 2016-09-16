#Sort a string of printable characters (BUCKET SORT)

'''
1. 256 ASCII characters. This includes standard ASCII characters (0-127) and 
   Extended ASCII characters(128-255).
2. 95 printable characters in ASCII characters in range 0 - 127
3. ord('a')  converts a character to corresponding ASCII value (int)
4. chr(40) converts int to character
'''
def bucketsort(a):
    buckets = [0] * 128 
    for c in a:
        buckets[ord(c)] += 1 #convert to ASCII (int)
    for i in range(0,len(buckets)):
        for c in range(0,buckets[i]):
                print(chr(i), end="")  #convert back to character
    print("")    


input="XBXCRA"
print("input >>>",input)
print("bucket sort >>>")
bucketsort(input)

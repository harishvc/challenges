'''
Question: Given an input string and pattern find the minimum window in the input string that
will contain all the characters in the pattern.
'''

#Modified from: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/ad9d11b94a6b06e32831afbcb520d07cd758d0da/src/chapter15stringalgorithms/MinWindowSubstr.py
def minWindowSubstr(inputStr, pattern):
    if inputStr == '' or pattern == '': return ''
    last_seen = {}
    #start = 0; end = len(inputStr) - 1
    pattern_as_char = set(pattern)
    window = ""
    # find such a substring ended at i-th character.
    for i, ch in enumerate(inputStr):
        if ch not in pattern_as_char: continue
        last_seen[ch] = i
        if len(last_seen) == len(pattern):
            # all chars have been seen
            first = min(last_seen.values())  # **We can use a priority queue, O(logn)
            last = max(last_seen.values())
            window = inputStr[first:last+1]
            return window
    return window

input ="XFDOYEZODEYXNZD"
pattern = "XYZF"
print("input=%s pattern=%s  match=%s" % (input,pattern, minWindowSubstr(input, pattern)))

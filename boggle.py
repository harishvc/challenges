#Question: How to find list of possible words from a letter matrix [Boggle]
#Source:http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver#746345

class TrieNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = [None] * 26
        self.isWord = False
        if parent is not None:
            parent.children[ord(value) - 97] = self

def MakeTrie(dictfile):
    dict = open(dictfile)
    root = TrieNode(None, '')
    for word in dict:
        curNode = root
        for letter in word.lower():
            if 97 <= ord(letter) < 123:
                nextNode = curNode.children[ord(letter) - 97]
                if nextNode is None:
                    nextNode = TrieNode(curNode, letter)
                curNode = nextNode
        curNode.isWord = True
    return root

def BoggleWords(grid, dict):
    rows = len(grid)
    cols = len(grid[0])
    queue = []
    words = []
    for y in range(cols):
        for x in range(rows):
            c = grid[y][x]
            node = dict.children[ord(c) - 97]
            if node is not None:
                queue.append((x, y, c, node))
    while queue:
        x, y, s, node = queue[0]
        del queue[0]
        for dx, dy in ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < cols and 0 <= y2 < rows:
                s2 = s + grid[y2][x2]
                node2 = node.children[ord(grid[y2][x2]) - 97]
                if node2 is not None:
                    if node2.isWord:
                        words.append(s2)
                    queue.append((x2, y2, s2, node2))

    return words

d = MakeTrie('/usr/share/dict/words')
print(BoggleWords(['fxie','amlo','ewbx','astu'], d))

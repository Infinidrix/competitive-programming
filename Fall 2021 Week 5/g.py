from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 3)

def play(trie):
    if len(trie) == 0:
        return False
    
    for val in trie.values():
        if not play(val):
            return True
    return False

def lost(trie):
    if len(trie) == 0:
        return True
    for val in trie.values():
        if not lost(val):
            return True
    return False

n, k = list(map(int, input().split()))

trie = {}

for i in range(n):
    word = input()
    curr = trie
    for j in range(len(word)):
        letter = word[j]
        if letter not in curr:
            curr[letter] = {}
        curr = curr[letter]
# print(trie)

canwin = play(trie)
canLose = lost(trie)
# print(canwin, canLose)
if (canwin and canLose) or (canwin and k % 2 == 1):
    print("First")
else:
    print("Second")